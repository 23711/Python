import random
import os


def getFileInfoInArray(url):
    with open(url, "r",encoding="utf-8") as f:
        words = [word.replace("\n","") for word in f]
        word = random.choice(words)
    return word

def hidWord(word):
    hidden = "".join(word)
    return hidden

def askUser():
    try:
        answer = input("Write one letter: ")
        if len(answer) > 1 or len(answer) == 0:
            raise ValueError("Write just one letter pleas!")
        if answer.isnumeric():
            raise ValueError("I can't accept  a number =(, try again pleas")
        return answer
    except ValueError as ve:
        print(ve)

def run():
    word = getFileInfoInArray("./archivos/words.txt")
    arrayWord = [" _ " for i in word]
    wordHid = hidWord(arrayWord)
    timeAsking = 0 
    # print(arrayWord)
    while word != wordHid :
        # os.system("clear")
        print(wordHid)
        wordOfUser = askUser()
        for i in range(0,len(word)):
            if word[i] == wordOfUser:
                arrayWord[i] = word[i]
                wordHid = "".join(arrayWord)
            else: 
                if timeAsking == 0:
                    print('''
                        0
                    ''')
                    timeAsking = timeAsking + 1
                if timeAsking == 1:
                    print('''
                        0
                        |
                    ''')
                    timeAsking = timeAsking + 1
    print("you win!")








if __name__ == "__main__":
    run()