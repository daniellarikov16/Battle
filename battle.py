from hero_class import Hero
from time import sleep
knight = Hero('Санечка', 30, 20, 50, 'Шампур Армянский')


dragon = Hero('Дракошка', 100, 0, 30, 'Шаверма Питерская')

print('Сочинские шашлычные громит делетант из Питера...')
print('Появляется защитник улиц:')
knight.info()
sleep(3)

varvar = Hero('Глебосина', 10, 10, 10, 'Понты')
print('На его пути, что бы понтануться перед столичными девочками появляется', varvar.name)
sleep(3)
if input('Не дать себя опустить: да/нет') == 'да':
    print('\n', 'ПОНЕСЛОСЬ МАХАЛОВО!','\n')
    sleep(3)
    knight.draka(varvar)
    if knight.health > 0:
        knight.armor *=1.5
        knight.health *=1.5
        print('Смелый поступок закалил', knight.name, '\n')
        print('Его здоровье - ', knight.health)
        print('Его броня - ', knight.armor)
print('Вот и питерский балбес...')
sleep(3)
dragon.info()
knight.draka(dragon)
