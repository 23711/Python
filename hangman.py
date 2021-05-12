import random
import os


def getFileInfoInArray(url):
    with open(url, "r",encoding="utf-8") as f:
        words = [word.replace("\n","") for word in f]
    return words

def randomWord(list):
    word = random.choice(list)
    

def run():
    getFileInfoInArray("./archivos/words.txt")



if __name__ == "__main__":
    run()