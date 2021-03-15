from dataclasses import dataclass
from random import randint


@dataclass
class User:
    _id: int = randint(1, 100)
    name: str = 'Какое_то_имя'
