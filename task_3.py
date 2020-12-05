from datetime import *
from time import *
    
year = int(input("Введите год рождение: "))
mounth = int(input("Введите месяц рождение: "))
day = int(input("Введите день рождение: "))

currentDate = time()
birth = datetime(year, mounth, day, 12, 12, 12)

print("Столько секунд вы живете: "currentDate - birth.timestamp())