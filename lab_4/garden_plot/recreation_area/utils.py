from abc import ABC, abstractmethod

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class BaseManager(models.Manager, ABC):
    @abstractmethod
    def get_obj(self):
       pass

    def delete_obj(self):
        if self.get():
            self.get().delete()