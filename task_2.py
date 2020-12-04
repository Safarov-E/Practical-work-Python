import shutil
while True:
    value = input("Введиет кмоанду \"read\" или \"copy\":" )
    if value == 'read':
        pathView = input("Напишите путь к файлу, содержимое которого Вы хотите посмотреть: ")
        fileText = open(pathView, 'r')
        print(fileText.read())
        fileText.close()
    elif value == 'copy':
        pathView = input("Напишите путь к файлу, который Вы хотите скопировать: ")
        shutil.copyfile(pathView, 'Путь с именем файла')