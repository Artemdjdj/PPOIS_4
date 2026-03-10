import random
import time

import pygame
from src.settings.settings import SCREEN_WIDTH, SITTING_CHICKEN, HEIGHT_FLYING_CHICKEN, BASE_WIDTH_OF_SITTING_CHICKEN, \
    SCREEN_HEIGHT, SPEED_THIRD_LAYER, LEFT_FLYING_CHICKEN, \
    RIGHT_FLYING_CHICKEN, MIN_CHICKEN_SPEED, MAX_CHICKEN_SPEED, DEFAULT_SPEED_WORLD, MIN_VERTICAL_CHICKEN_SPEED, \
    MAX_VERTICAL_CHICKEN_SPEED, CHICKEN_DEAD_IMAGE, ALPHA, CHICKEN_SHOOT, RIGHT_FLYING_CHICKEN_HORIZONTAL, \
    LEFT_FLYING_CHICKEN_HORIZONTAL, \
    SCORE_HORIZONTAL_CHICKEN, SCORE_FLYING_CHICKEN, SCORE_BIG_CHICKEN, LEFT_RUNNING_CHICKEN_IMAGE_1, \
    RIGHT_RUNNING_CHICKEN_IMAGE_1, LEFT_RUNNING_CHICKEN_IMAGE_2, \
    RIGHT_RUNNING_CHICKEN_IMAGE_2, SPEED_ANIMATION_RUNNING_CHICKEN, RIGHT_FLYING_CHICKEN_2, LEFT_FLYING_CHICKEN_2, \
    RIGHT_FLYING_CHICKEN_HORIZONTAL_2, LEFT_FLYING_CHICKEN_HORIZONTAL_2
from src.objects.base_sprite import BaseSprite
from src.utils.image_formatter import ImageFormatter


class BaseChicken(BaseSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int, layer_speed: float, score:int) -> None:
        super().__init__(image, x, y, score)
        self.layer_speed = layer_speed
        self.shoot_time = 0
        self.mask = pygame.mask.from_surface(self.image)

        self._dead_image = ImageFormatter.scale_image(pygame.image.load(CHICKEN_DEAD_IMAGE).convert_alpha(),
                                                      self.image.get_width())
        self._alpha = ALPHA
        self._is_fading = False

    def draw(self, screen: pygame.Surface, scroll_position: float) -> None:
        screen_x = self.rect.x - scroll_position * self.layer_speed
        if self._is_fading:
            screen.blit(self._dead_image, (screen_x, self.rect.y))
        else:
            screen.blit(self.image, (screen_x, self.rect.y))

    def update(self, dt: float=0.0) -> None:
        pass

    def shoot(self) -> None:
        self.shoot_time = time.time()
        super().shoot()

    def animate(self) -> None:
        if self._is_killed and not self._is_fading:
            self._is_fading = True
            self._dead_image.set_alpha(self._alpha)

        if self._is_fading:
            self._alpha = max(0, self._alpha - 4)
            self._dead_image.set_alpha(self._alpha)

            if self._alpha <= 0:
                self.kill()

    def play(self, volume) ->None:
        self._player.set_sound(CHICKEN_SHOOT)
        super().play(volume)


class SittingChicken(BaseChicken):
    def __init__(self, x: int, y: int, layer_speed: float):
        image = pygame.image.load(SITTING_CHICKEN).convert_alpha()
        score = SCORE_BIG_CHICKEN
        super().__init__(image, x, y, layer_speed, score)

class MoveChicken(BaseChicken):
    def __init__(self,image, x: int, y: int, layer_speed:float, velocity: float, direction: str, score:int):
        self._direction = direction
        self._velocity = velocity
        self._float_x = float(x)
        self.animation_period = time.time()
        self.image_1 = None
        self.image_2 = None
        super().__init__(image, x, y, layer_speed, score)

    def change_state(self) -> None:
        if self.image_1 is not None:
            current_time = time.time()
            if current_time - self.animation_period > SPEED_ANIMATION_RUNNING_CHICKEN:
                if self.image == self.image_1:
                    self.image = self.image_2
                else:
                    self.image = self.image_1
                self.animation_period = current_time

    def update(self, dt:float=0.0) -> None:
        if not self._is_killed:
            self.change_state()
            if self._direction == "left":
                self._float_x -= self._velocity * dt
            else:
                self._float_x += self._velocity * dt

            self.rect.x = int(self._float_x)

class FlyingChicken(MoveChicken):
    def __init__(self, x: int, y: int, layer_speed: float, velocity: float, direction: str,
                 y_min: int, y_max: int):
        self._float_y = float(y)
        self._y_min = y_min
        self._y_max = y_max
        self._target_y = float(y)
        self._vertical_speed = 0.0
        self._time_until_next_move = random.uniform(2.0, 4.0)

        image_path_1 = LEFT_FLYING_CHICKEN if direction == "left" else RIGHT_FLYING_CHICKEN
        image_path_2 = LEFT_FLYING_CHICKEN_2 if direction == "left" else RIGHT_FLYING_CHICKEN_2
        image_1 = pygame.image.load(image_path_1).convert_alpha()
        image_2 = pygame.image.load(image_path_2).convert_alpha()
        super().__init__(image_1, x, y, layer_speed,velocity, direction, SCORE_FLYING_CHICKEN)
        self.image_1 = image_1
        self.image_2 = image_2

    def _pick_new_target_y(self) -> None:
        self._target_y = float(random.randint(self._y_min, self._y_max))
        self._vertical_speed = self._velocity * random.uniform(MIN_VERTICAL_CHICKEN_SPEED, MAX_VERTICAL_CHICKEN_SPEED)

    def update(self, dt: float=0.0) -> None:
        super().update(dt)
        if not self._is_killed:
            self._time_until_next_move -= dt
            if self._time_until_next_move <= 0:
                self._pick_new_target_y()
                self._time_until_next_move = random.uniform(2.0, 4.0)

            diff = self._target_y - self._float_y
            if abs(diff) > 1.0:
                move = self._vertical_speed * dt
                if diff > 0:
                    self._float_y += move
                else:
                    self._float_y -= move
            else:
                self._float_y = self._target_y

            self.rect.x = int(self._float_x)
            self.rect.y = int(self._float_y)

class HorizontalFlyingChicken(MoveChicken):
    def __init__(self, x: int, y: int, layer_speed:float, velocity: float, direction: str):
        image_path_1 = LEFT_FLYING_CHICKEN_HORIZONTAL if direction == "left" else RIGHT_FLYING_CHICKEN_HORIZONTAL
        image_path_2 = LEFT_FLYING_CHICKEN_HORIZONTAL_2 if direction == "left" else RIGHT_FLYING_CHICKEN_HORIZONTAL_2
        image_1 = pygame.image.load(image_path_1).convert_alpha()
        image_2 = pygame.image.load(image_path_2).convert_alpha()
        super().__init__(image_1, x, y, layer_speed, velocity, direction, SCORE_HORIZONTAL_CHICKEN)
        self.image_1 = image_1
        self.image_2 = image_2


class HorizontalRunningChicken(MoveChicken):
    def __init__(self, x: int, y: int, layer_speed:float, velocity: float, direction: str):
        image_path_1 = LEFT_RUNNING_CHICKEN_IMAGE_1 if direction == "left" else RIGHT_RUNNING_CHICKEN_IMAGE_1
        image_path_2 = LEFT_RUNNING_CHICKEN_IMAGE_2 if direction == "left" else RIGHT_RUNNING_CHICKEN_IMAGE_2
        image_1 = pygame.image.load(image_path_1).convert_alpha()
        image_2 = pygame.image.load(image_path_2).convert_alpha()
        super().__init__(image_1, x, y, layer_speed, velocity, direction, SCORE_HORIZONTAL_CHICKEN)
        self.image_1 = image_1
        self.image_2 = image_2


