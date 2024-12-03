import pygame
import math

class Basic():                                            # Главный класс игровых обьектов
    def __init__(self):                                   #

        self.name  = "NaN"                                # Имя обьекта

        self.DEBUG     = False                            # Режим отладки
        self.messDebug = "[DEBUGE]"                       # Сообщение дебага
        self.messEr    = "[ERROR]"                        # Сообщение ошибки
        self.messWar   = "[WARNING]"                      # Сообщение предупреждения

        self.layer     = 0                                # Слой сортировки

        self.position = Vector2(0, 0)                     # Координаты по умолчанию
        self.size     = Vector2(64, 64)

    def Log(self, message):
        if self.DEBUG: message = self.DEBUG + " " + message
        print(message)

    def Error(self, code, message):
        print(f'{self.messEr} {code} in {self.name}: {message}')

    def Warning(self, message):
        print(f'{self.messWar} in {self.name}: {message}')


class Vector2():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} y:{self.y}"
        
    def __repr__(self):
        return f"Vector2({str(self)})"
    
    def __add__(self, value): #+
        return Vector2(self.x + value.x, self.y + value.y)
        
    def __mul__(self, value): #*
        return Vector2(self.x * value.x, self.y * value.y)
        
    def __neg__(self): #-Vector2
        return Vector2(-self.x,-self.y)
        
    def __sub__(self, value, /): #-
        return Vector2(self.x - value.x, self.y - value.y)
        
    def __truediv__(self, value):
        return Vector2(self.x // value.x, self.y // value.y)
    
    def distance(self, vector):
        return math.sqrt((vector.x - self.x)**2 + (vector.y - self.y) ** 2)
    
    @property
    def right(self):
        return Vector2(1, 0)
    @property
    def left(self):
        return Vector2(-1, 0)
    @property
    def up(self):
        return Vector2(0, 1)
    @property
    def down(self):
        return Vector2(0, -1)
    @property
    def zero(self):
        return Vector2(0, 0)
    
    @property
    def xy(self):
        return (self.x, self.y)