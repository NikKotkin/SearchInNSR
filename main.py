# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Имена функций, переменных и атрибутов должны следовать формату lowercase_underscore (нижний регистр букв,
#  разделение слов символами подчеркивания) .
# Имена защищенных атрибутов экземпляра должны следовать _leading_underscore (один символ подчеркивания в начале).
# Имена закрытых атрибутов экземпляра должны следовать формату __leading_underscore (два символа подчеркивания в начале).
# Имена классов и исключений должны следовать формату CapitalizeWord (каждое слово начинается с прописной буквы).
# Константы уровня модуля должны записываться в формате ALL_CAPS (все буквы прописные, в качестве разделителя
#  используется символ подчеркивания).
# В определениях методов экземпляров классов в качестве имени первого параметра следует всегда указывать self (это имя
#  ссылается на текущий объект).
# В определениях методов классов в качестве имени первого параметра следует всегда указывать cls (это имя ссылается на
#  текущий класс).
#
# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('Поиск в NSR')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Чтобы напечатать все строки, которые содержат заданное слово в данном текстовом файле, закодированном в utf-8 кодировке:

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ import print_function
import io
import os
import re
import datetime
import glob
import config  # конфиги мои config.tokenTelegramm
import pathlib
import click

# time.strptime(строка [, формат]) - разбор строки, представляющей время в соответствии с форматом.
# Возвращаемое значение struct_time. Формат по умолчанию: "%a %b %d %H:%M:%S %Y".
#


# находит все пути, совпадающие с заданным шаблоном в соответствии с правилами, используемыми оболочкой Unix.
# Обрабатываются символы "*" (произвольное количество символов), "?" (один символ), и диапазоны символов с помощью []


# https://habr.com/ru/post/513966/ логгинг тема прикольнаф на потом
# !VANONCED 03/03/2021
# !DATE 11/10/2013 сделать отсечки для доков после 01/01/2020
# отсечь только нулевую редакцию
#       !NODOC

# Допустимы только следующие ключи:
#  -srv:<server> - адрес сервера или его IP адрес, обязателен
#  -port:<port> - порт сервера, обязателен
#  -l:<sender login> - логин отправителя в арчи, обязателен.
#  -p:<sender password> - пароль отправителя, обязателен.
#  -r:<recepient login> - Логин получателя в арчи.
#  -s:<subject> - тема письма, необязательна
#  -b:<body> - тело сообщения. Обязательно должно быть или -b или -bf
#  -bf:<file with body> - имя файла из которого читать тело письма. Обязательно должно быть или -b или -bf

# os.system(
#         ExeFromArchi + f' -srv:192.168.1.5 -port:32100 -l:PIPEOUT -p:PIPEOUT -r:lu -s:"Тема" -b:"{path}"')
# alcuSendArchieMail.exe -srv:192.168.1.5 -port:32100 -l:lu -p:111 -r:lu -s:"Тема" -b:Ошибки
# b: и без пробела текст письма либо bf: и имя файла из которого  тест письма придет
#  конец кода НСК


# word = u'!VANONCED'



patternForSearchANONCED = r'(^!VANONCED)\s(\d\d\/\d\d\/\d{4})\s'
patternForSearchTOPIC = r'(^!TOPIC) (\d+)'
pathToNsrFile = 'Z:/- python -/SearchInNSR/test/'  #сделать аргументом
currentDate = datetime.datetime.today()
limitDeltaDate = 3

# fullPathToArchiMailFile = "Z:\- python -\SearchInNSR\mailForArchi.txt"
fullPathToArchiMailFile = "mailForArchi.txt"  #пишем в текущий каталог

@click.command()
@click.argument('path_to_nsr_file_catalog_from_CLI')
# имя аргумента, переданное click, должно совпадать с именем аргумента в объявлении функции.
# В нашем случае значение аргумента командной строки location будет передано функции main в качестве аргумента location.
def main(path_to_nsr_file_catalog_from_CLI):

# Y:\DLT_NSR\NSR\9000191.nsr
# Z:\- python -\SearchInNSR\test\400289325.nsr

# with open(path + topic + '.nsr', 'r', encoding='cp866') as fl: #utf-8

# filesListNsrFromPath = glob.glob('Z:\\- python -\\SearchInNSR\\test\\*.nsr')  #pathToNsrFile
# filesCatalogNsrFromPath = glob.glob(pathToNsrFile+'\*.nsr')  #pathToNsrFile path_to_nsr_file_catalog_from_CLI
    filesCatalogNsrFromPath = glob.glob(path_to_nsr_file_catalog_from_CLI+'\*.nsr')

    result4mailForArchiTxtFile = list()

    for fileNsr in filesCatalogNsrFromPath:
        try:
            print('Взят в работу ', fileNsr)  # выводим имя файла с которым работаем
            with io.open(fileNsr, encoding='cp866') as NsrFile:
                # перебираем строки в файле из каталога
                for lineFromNsrFile in NsrFile:

                    # найдем номер топика
                    matchTOPIC = re.search(patternForSearchTOPIC, lineFromNsrFile)
                    if matchTOPIC:
                        # print(matchTOPIC[2])
                        numberTOPIC = matchTOPIC[2]

                    # найдем дату анонсед
                    matchANONCED = re.search(patternForSearchANONCED, lineFromNsrFile)
                    if matchANONCED:
                        # print('Дата анонса =', match[2])
                        anoncedDate = datetime.datetime.strptime(matchANONCED[2], "%d/%m/%Y")  # Y это с веком
                        # numberTOPIC = (matchTOPIC[2])

                        # deltaAnoncedCurrentDate = abs(currentDate-anoncedDate)#абсолютное отклонение
                        deltaAnoncedCurrentDate = anoncedDate - currentDate  # отклонение в днях
                        if deltaAnoncedCurrentDate.days > limitDeltaDate:  # сравнивать можно только одинаковые  размерности day дал нам целое число
                            # if anoncedDate > currentDate and deltaAnoncedCurrentDate.days > limitDeltaDate:  # сравнивать можно только одинаковые  размерности day дал нам целое число
                            print(' > Выход  за границы ->  Файл =', fileNsr, 'Дата анонса =', anoncedDate,
                                  'Дата текущая =', currentDate, 'Разница =',
                                  deltaAnoncedCurrentDate, 'Лимит =', limitDeltaDate, 'Номер топика = ', numberTOPIC)

                            # преобразуем втекстовые и выводим в список для последующей записи в лог
                            result4mailForArchiTxtFile.append(
                                ' > Выход  за границы ->  Файл = ' + fileNsr + ' Дата анонса = ' + str(
                                    anoncedDate) + ' Дата текущая = ' + str(
                                    currentDate) + ' Разница (дней часов секунд) = ' + str(
                                    deltaAnoncedCurrentDate) + ' Лимит (дней)= ' + str(
                                    limitDeltaDate) + ' Номер топика = ' + str(numberTOPIC))
                            # print('> Выход  за границы ->  Файл =', fileNsr, 'Дата анонса =', anoncedDate, 'Дата текущая =', currentDate, 'Разница =',
                            #   deltaAnoncedCurrentDate, 'Лимит =', limitDeltaDate', file=mailForArchiTxtFile)
                            # print по-умолчанию выводит с переводом строки

                            # print(deltaAnoncedCurrentDate.days)  # дни


                    else:
                        continue


        except:
            print('error ex')
            continue
    # print('End of list NSR - files & Date From It')


# lines = ["first", "second", "third"]
# with open(r"D:\test.txt", "w") as file:
#     for  line in lines:
#         file.write(line + '\n')

# lines = ["first", "second", "third"]
# with open(r"D:\test.txt", "w") as file:
#     file.writelines("%s\n" % line for line in lines)

    # вынести отправку в отдельный модуль
    with open(fullPathToArchiMailFile, 'w') as mailForArchiTxtFile:
        # print (result4mailForArchiTxtFile)

        for row in result4mailForArchiTxtFile:
            # mailForArchiTxtFile.write(''.join(row)+'\n')
            mailForArchiTxtFile.write(row + '\n')

        #    mailForArchiTxtFile.writelines(result4mailForArchiTxtFile)
        #    print('Проверка', file=mailForArchiTxtFile)  # print по-умолчанию выводит с переводом строки
        mailForArchiTxtFile.close()  # закрываем дескриптор файла

        # os.system(spammerExeFromArchi + f' -srv:192.168.1.5 -port:32100 -l:lu -p:111 -r:lu -s:"Выход даты VANONCED за допустимые пределы" -bf:"Z:\- python -\SearchInNSR\mailForArchi.txt"')
        os.system(
            config.spammerExeFromArchi + f' -srv:192.168.1.5 -port:32100 -l:lu -p:111 -r:lu -s:"Выход даты VANONCED за допустимые пределы" -bf:"' + fullPathToArchiMailFile + '"')
        # -bf:"{path}\\mail.txt"'

if __name__ == "__main__":
    main()


# ---------------------------------------------
# with io.open('Z:/- python -/SearchInNSR/test/'+'400289325.nsr', encoding='cp866') as NsrFile:
#     for lineFromNsrFile in NsrFile:
#         # match = re.search('(^!TOPIC) (\d+)',line)
#         match = re.search(patternForSearch, lineFromNsrFile)
#
#         if match:
#             print('Дата анонса =',match[2])
#             anoncedDate = datetime.datetime.strptime(match[2], "%d/%m/%Y")#Y это с веком
#             deltaAnoncedCurrentDate = anoncedDate-currentDate
#             print('Дата анонса =', anoncedDate, 'Дата текущая =',currentDate, 'Разница =',deltaAnoncedCurrentDate )
#
#
# #
# try:
#     value = my_dict["a"]
# except KeyError:
#     print("A KeyError occurred!")
# else:
#     print("No error occurred!")
# finally:
#     print("The finally statement ran!")


# print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
# print(f'Группа букв >{match[1]}< с позиции {match.start(1)} до {match.end(1)}')
# print(f'Группа цифр >{match[2]}< с позиции {match.start(2)} до {match.end(2)}')
###
# -> Найдена подстрока >   Опять45   < с позиции 3 до 16
# -> Группа букв >Опять< с позиции 6 до 11
# -> Группа цифр >45< с позиции 11 до 13


# данный метод закрывает входной файл (with-инструкция), не рассчитывая на особенности
# уборки мусора в реализации интерпретатора или возникновения исключений (ошибок)
# считывание файла идёт построчно без загрузки всего файла в память
# поддерживаются произвольные Юникодные символы (можно другую кодировку использовать
# в io.open() вызове -- она никак не связана с кодировкой исходного кода)
# дин и тот же код работает как на Питоне 2 так и на Питоне 3.

# сцылка по регуляркам https://habr.com/ru/post/349860/
# \d\d/\d\d/\d{4}	Даты в формате ДД/ММ/ГГГГ (и прочие куски, на них похожие, например, 98/76/5432)

# Документация и ссылки
# Оригинальная документация: https://docs.python.org/3/library/re.html;
# Очень подробный и обстоятельный материал: https://www.regular-expressions.info/;
# Разные сложные трюки и тонкости с примерами: http://www.rexegg.com/;
# Он-лайн отладка регулярок https://regex101.com (не забудьте поставить галочку Python в разделе FLAVOR слева);
# Он-лайн визуализация регулярок https://www.debuggex.com/ (не забудьте выбрать Python);
# Могущественный текстовый редактор Sublime text 3, в котором очень удобный поиск по регуляркам;

# # 16866965 это из discard_last_changes.py - новосиб
# import os, sys, sysnsrc, colorama, re, datetime
#
# pipeout = r'D:\utils\pipeout2\PipeOut2.exe'
#
#
# def exportdocument(path, topic):
#     os.system(f'{pipeout} /Server:192.168.0.230 /User:PIPEOUT:PIPEOUT /W:D"{topic}" /H:DER /DD /P:"{path}"')
#
#
# if __name__ == '__main__':
#     colorama.init()
#     sysnsrc.title(os.path.split(sys.argv[0])[1], 'Скрипт выполняет откат редакций')
#     print(sys.argv)
#     path = os.getcwd()
#     if len(sys.argv) < 3:
#         sysnsrc.printparam('Параметры запуска', '[ТОПИК] [КОЛИЧЕСТВО ОТКАТОВ] [ДИРЕКТОРИЯ НАЗНАЧЕНИЯ - ОПЦИОНАЛЬНО]')
#         exit(1)
#     elif len(sys.argv) == 4:
#         path = sys.argv[3]
#         if path[-1] != '\\':
#             path += '\\'
#         if not os.path.exists(path):
#             os.makedirs(path)
#
#
#     topic = sys.argv[1]
#     sysnsrc.printparam('Основной топик:', topic)
#     revertcount = int(sys.argv[2])
#     sysnsrc.printparam('Количество откатов:', revertcount)
#     sysnsrc.printparam('путь:', path)
#     # folder = datetime.datetime.today().strftime('%Y-%m-%d %H %M %S')
#     # path = path + folder + '\\' + topic + '\\'
#     exportdocument(path, topic)
#     os.system(f'nsplit {path} 0')
#
#     oldtopic = topic
#     olddoc = []
#     header = []
#     deletelist = ['!STYLE P 0 73 0\n;TOPICS FOR DELETE\n']
#
#     with open(path + topic + '.nsr', 'r', encoding='cp866') as fl:
#         cyrdoc = fl.readlines()
#
#     insertinheader = True
#     params = {}
#     cyrblock = ''
#     # выцепим заголовок
#     for i in range(len(cyrdoc)):
#         if cyrdoc[i].strip() == '':
#             continue
#         elif cyrdoc[i][0] != '!':
#             continue
#         elif cyrdoc[i].find('!VERLINK') > -1 or cyrdoc[i].find('!CHDATE') > -1 or cyrdoc[i].find('!ACTIVE') > -1:
#             continue
#         elif cyrdoc[i].find('!STYLE') > -1:
#             insertinheader = False
#         if insertinheader:
#             header.append(cyrdoc[i])
#         else:
#             rsm = re.search('^!(BLOCK|SUB) (\d+)', cyrdoc[i])
#             if rsm:
#                 cyrblock = rsm[2]
#             rsm = re.search('^!(TYPE|KIND|CLASS)', cyrdoc[i])
#             if rsm:
#                 if not cyrblock in params.keys():
#                     params[cyrblock] = []
#                 params[cyrblock].append(cyrdoc[i])
#     with open(path + 'params.txt', 'w', encoding='cp866') as fl:
#         fl.write(str(params))
#     # выцепим верлинки
#     while revertcount > 0:
#         revertcount -= 1
#         with open(path + oldtopic + '.nsr', 'r', encoding='cp866') as fl:
#             olddoc = fl.readlines()
#         verlink = re.search('^!VERLINK (\d+)', ''.join(olddoc), re.MULTILINE)
#         if not verlink:
#             break
#         else:
#             oldtopic = verlink[1]
#             print('oldtopic', oldtopic)
#             deletelist.append(';' + verlink[1] + '\n')
#     print('Найден топик редакции для отката:', oldtopic, len(olddoc), topic)
#
#     # считаем последнюю верную редакцию
#     with open(path + oldtopic + '.nsr', 'r', encoding='cp866') as fl:
#         olddoc = fl.readlines()
#     # выцепим правильный верлинк
#     tryverlink = 0
#     for i in range(len(olddoc)):
#         v = re.search('^!(VERLINK|ACTIVE|CHDATE) (\d+)', olddoc[i])
#         if v:
#             if v[1] == 'VERLINK':
#                 tryverlink = v[1]
#             header.append(olddoc[i])
#         olddoc[i] = re.sub('(\x04)(' + oldtopic + ')([\x04|\.])', '\g<1>' + topic + '\g<3>', olddoc[i])
#         olddoc[i] = re.sub('(!TOPIC\s+)(' + oldtopic + ')(\s*)', '\g<1>' + topic + '\g<3>', olddoc[i])
#     # выкосим
#     while True:
#         if olddoc[0].find('!STYLE') == -1:
#             olddoc.pop(0)
#         else:
#             break
#     # добавим заголовки
#     olddoc = header + deletelist + olddoc
#
#     # растиражируем команды
#     for i in range(len(olddoc) - 1, -1, -1):
#         rsm = re.search('^!(BLOCK|SUB)\s+(\d+)', olddoc[i])
#         if rsm and rsm[2] in params.keys():
#             print(params[rsm[2]])
#             olddoc.insert(i + 1, ''.join(params[rsm[2]]))
#     os.system(f'ren "{path}*.nsr" *.bak')
#     with open(path + 'import.nsr', 'w', encoding='cp866') as fl:
#         fl.writelines(olddoc)
#     print('save nsr')
#     with open(path + 'deletelist.txt', 'w', encoding='cp866') as fl:
#         fl.writelines(deletelist)
#     print('save deletelist')
#     # for i in range(len(basedoc)-1,-1, -1):
