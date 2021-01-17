#2
f = open('файл.txt', "r")
content = f.read()
print(f'Содержимое файла: \n {content}')

f = open('файл.txt', 'r')
content = f.readlines()
print(f'Количество строк в файле - {len(content)}')

f = open('файл.txt', 'r')
content = f.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1}-ой строки {len(content[i])}')

f = open('файл.txt', 'r')
content = f.readline()
content = content.split()
content2 = f.readline()
content2 = content2.split()
content3 = f.readline()
content3 = content3.split()
print(f'Количество слов первой стороки - {len(content)} \nКоличество слов второй стороки - {len(content2)} \nКоличество слов третьей стороки - {len(content3)}')

f.close()
