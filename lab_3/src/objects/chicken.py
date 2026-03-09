import random
import pygame
from src.settings.settings import SCREEN_WIDTH, SITTING_CHICKEN, HEIGHT_FLYING_CHICKEN, SCALE_IMAGE_THIRD_POWER, \
    SCALE_IMAGE_SECOND_POWER, BASE_WIDTH_OF_SITTING_CHICKEN, SCREEN_HEIGHT, SPEED_THIRD_LAYER, LEFT_FLYING_CHICKEN, \
    RIGHT_FLYING_CHICKEN, MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED, DEFAULT_SPEED_WORLD, MIN_VERTICAL_CHICKEN_SPEED, \
    MAX_VERTICAL_CHICKEN_SPEED
from src.objects.base_sprite import BaseSprite
from src.utils.image_formatter import ImageFormatter


class BaseChicken(BaseSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int, layer_speed: float) -> None:
        super().__init__(image, x, y)
        self.layer_speed = layer_speed
        self.mask = pygame.mask.from_surface(self.image)

    # def get_collision_rect(self) -> pygame.Rect:
    #     margin_x = int(self.rect.width * 0.20)
    #     margin_y = int(self.rect.height * 0.20)
    #     return self.rect.inflate(-margin_x * 2, -margin_y * 2)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))

    def update(self, dt:float) -> None:
        pass


class SittingChicken(BaseChicken):
    def __init__(self, x: int, y: int, layer_speed: float):
        scale = self._get_size(layer_speed)
        width = int(BASE_WIDTH_OF_SITTING_CHICKEN * scale)
        image = ImageFormatter.scale_image(
            pygame.image.load(SITTING_CHICKEN).convert_alpha(),
            width
        )
        super().__init__(image, x, y, layer_speed)

    @staticmethod
    def _get_size(layer_speed: float) -> float:
        if layer_speed == SPEED_THIRD_LAYER:
            return SCALE_IMAGE_THIRD_POWER
        return SCALE_IMAGE_SECOND_POWER

class FlyingChicken(BaseChicken):
    def __init__(self, x: int, y: int, layer_speed: float, velocity: float, direction: str,
                 y_min:int, y_max:int):
        self._direction = direction
        self._velocity = velocity
        self._float_x = float(x)
        self._float_y = float(y)

        self._y_min = y_min
        self._y_max = y_max
        self._target_y = float(y)
        self._vertical_speed = 0.0
        self._time_until_next_move = random.uniform(2.0, 4.0)

        image_path = LEFT_FLYING_CHICKEN if direction == "left" else RIGHT_FLYING_CHICKEN
        image = pygame.image.load(image_path).convert_alpha()
        super().__init__(image, x, y, layer_speed)

    def _pick_new_target_y(self) -> None:
        self._target_y = float(random.randint(self._y_min, self._y_max))
        self._vertical_speed = self._velocity * random.uniform(MIN_VERTICAL_CHICKEN_SPEED, MAX_VERTICAL_CHICKEN_SPEED)

    def update(self, dt: float) -> None:
        if self._direction == "left":
            self._float_x -= self._velocity * dt
        else:
            self._float_x += self._velocity * dt

        self._time_until_next_move -= dt
        if self._time_until_next_move <= 0:
            self._pick_new_target_y()
            self._time_until_next_move = random.uniform(2.0, 4.0)

        diff = self._target_y - self._float_y
        if abs(diff) > 1.0:
            move = self._vertical_speed * dt
            if diff >0:
                self._float_y += move
            else:
                self._float_y -= move
        else:
            self._float_y = self._target_y

        self.rect.x = int(self._float_x)
        self.rect.y = int(self._float_y)

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        screen.blit(self.image, (screen_x, self.rect.y))

