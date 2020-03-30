import re
import string
translator = str.maketrans('', '', string.punctuation)  # noktalama işaretlerini siler.
def inputData():
    data = input("Arama yapılacak datayı giriniz: ")
    file = open('metin_dosyasi.txt', 'w', encoding="utf-8")
    file.write(data)
    file = open('metin_dosyasi.txt', 'r', encoding="utf-8")
    word_list = []
    for line in file:  # kelimeleri listeye döker.
        words = line.split(" ")
        for word in words:
            word_list.append(word)

    for w in range(len(word_list)):  # \n 'leri siler.
        word_list[w] = re.sub('\n', '', word_list[w])


    for w in range(len(word_list)):
        word_list[w] = word_list[w].translate(translator)
        word_list[w] = word_list[w].lower()
    file.close()
    return word_list
def inputSearch():
    search = input("Bulmak istediğiniz kelimeyi giriniz: ")
    search_file = open('search_file.txt','w',encoding="utf-8")
    search_file.write(search)
    search_list = []
    search_file = open('search_file.txt','r',encoding="utf-8")
    for line in search_file:  # kelimeleri listeye döker.
        words = line.split(" ")
        for word in words:
            search_list.append(word)
    for w in range(len(search_list)):
        search_list[w] = search_list[w].translate(translator)
        search_list[w] = search_list[w].lower()
    search_file.close()
    return search_list

def isThere(text,data_list):

    index = 0
    i = 0

    for t in data_list:
        i += 1
        temp = i
        j = 0

        if t == text[j]:

            j += 1
            while(j != len(text)):
                if(text[j] == data_list[i]):
                    if((j+1) == len(text)):
                        index += 1
                        i += 1
                        j += 1
                    else:

                        i += 1
                        j += 1


                else:
                    i = temp
                    break
            else:
                if(j == 1):
                    index += 1
                i = temp

    return index
search = inputSearch()
data = inputData()
print(str(search),"Kelimesi ",isThere(search,data),"kere tekrar etmektedir.")
