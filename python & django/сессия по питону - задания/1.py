import requests
import re

def stars_translate(x): #x - общее количество слов во всех документах

    result = x / (8032 * 60) #получаем отношение "звездочка/строка", с помощью которого будем строить гистограмму
    return result


def solution():

    session = requests.session()
    sum_of_words = 0
    years = {} #здесь будем хранить все годы создания документов (ключ - год, значение - кол-во слов)

    for i in range(1, 8032):
        text = session.get('https://www.rfc-editor.org/rfc/rfc' + str(i) + '.txt').text
        sum_of_words += re.split('; |, |\*|\n', text).count()
        #далее что-то вроде years[год] = кол-во слов
    
    stars =stars_translate(sum_of_words) #само отношение звездочки к словам

    #после прохода строим гистограмму
    for i, j in years.items(): #j - кол-во слов для данного года 
        print(i + ':' + '*' * (stars * j))

solution()
