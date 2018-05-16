#Q1
def Q1_1(word):
    new_word = ""
    for w in word:
        new_word = w+new_word
    return(new_word)

Q1_1("junyiacademy")



def Q1_2(sentence):
    new_sentence = ""
    sentence_list = sentence.split(" ")
    for word in sentence_list:
        new_sentence += Q1_1(word) + " "
    return(new_sentence)



Q1_2("Hello my name is Kevin")


#Q2
def Q2(number):
    num_list = []
    for n in range(number):
        if ((n+1)%3 ==0 or (n+1)%5 ==0) and not (n+1)%15==0:
            pass
        else:
            num_list.append(n+1)
            
    return(num_list.__len__())


Q2(15)

#Q3
'''一定要選標籤為混合的袋子，因為標籤絕對錯，混和袋裡面一定只有可能是鉛筆或原子筆。
若混和袋裡面是鉛筆，便可確認標籤為原子筆的袋子內一定是混和(因為排除標籤的原子筆和全為鉛筆選項)，
最後推出標籤為鉛筆的袋子只有可能是原子筆。
反之，若混和袋裡面是原子筆，便可確認標籤為鉛筆的袋子內一定是混和(因為排除標籤的鉛筆和全為原子筆選項)，
最後推出標籤為原子筆的袋子只有可能是鉛筆。'''

#Q4
'''810是三人各多付30元之後的錢，實際該付的是750而已，810-60 = 750,此時的60才是服務生案扛的，
那如果今天沒有特價，實際要價900的話，810+90 = 900，每個人則要從一個人付270到一個人付300
一人多付了30元，30*3 = 90，故題目中得出來的870並沒有意義，不能這麼算。'''





