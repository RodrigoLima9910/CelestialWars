import math

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # 🔹 Configuração do voo oscilante
        self.base_y = position[1]  # posição inicial Y
        self.time = 0              # contador de tempo
        self.amplitude = 20        # altura da oscilação
        self.speed_wave = 0.05     # velocidade da oscilação

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        self.time += 1
        offset = self.amplitude * math.sin(self.time * self.speed_wave)
        self.rect.centery = self.base_y + offset

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))