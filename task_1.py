import random
array = {"Hello": "Здравствуй", "Bуe": "Пока", "Lesson": "Урок"}
value_arr = list(array.values())
while True:
    rnd_value = value_arr[int(random.random() * 3)]
    print(rnd_value)
    input_value = input("Ведите перевод на английском: ")
    if array.get(input_value) == rnd_value:
        print("Перевод указан верно\n\n\n\n\n")
    else:
        print("Перевод указан не верно\n\n\n\n\n")
    if input_value == 'quit':
        exit(0)
    if input_value == 'show':
        print(array)