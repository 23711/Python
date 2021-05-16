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
    ask = 0
    arrayWord = ["_ " for i in word]
    wordHid = hidWord(arrayWord)
    print(wordHid)
    while ask <= len(arrayWord):
        wordOfUser = askUser()
        for letter in word:
            if letter == wordOfUser:
                ask = ask + 1
                for i in range(0,len(word) + 1):
                    # arrayWord[i] = letter









if __name__ == "__main__":
    run()