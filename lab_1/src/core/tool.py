from typing import Any
from abc import ABC, abstractmethod

class Tool(ABC):
    def __init__(self, description:str):
        self.__description = description

    @property
    def description(self)->str:
        return self.__description

    @description.setter
    def description(self, description:str)->None:
        self.__description = description
    
    @abstractmethod
    def perform_task(self, *args:Any, **kwargs:Any):
        pass