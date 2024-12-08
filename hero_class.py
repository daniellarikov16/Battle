from time import sleep
from random import randint
class Hero():
    def __init__ (self, name, health, armor, power, weapon):
        self.name = name
        self.health = int(health)
        self.armor = int(armor)
        self.power = int(power)
        self.weapon = weapon
    def info (self):
        print('Встречайте ->', self.name)
        print('Показатель здоровья -', self.health, )
        print('Показатель защиты -', self.armor, )
        print('Показатель силы -', self.power, )
        print('Оружие -', self.weapon, '\n')
    def strike(self,enemy):
        attack = randint(self.power-5,self.power+5)
        print('-> УДАР!!!', self.name, 'атакует', enemy.name, ' с силой ', str(attack), 'используя', self.weapon, '\n')
        enemy.armor -= attack
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
            print('Удар', self.name, 'раскумарил',enemy.name, 'на', attack, '\n', 'Текущее здоровье', enemy.health, '\n')
    def draka (self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <=0:
                print(enemy.name, 'чилит в пабе','\n')
                break
            sleep (3)
            enemy.strike(self)
            if enemy.health <=0:
                print(self.name, 'чилит в пабе','\n')
                break
            sleep (3)
