import sys
import time
sys.setrecursionlimit(15000)
f = open("BEE.txt", "r")
text = f.read()
words = text.split()
user_input = int(input("Word speed:"))
speed = float(60 / user_input)


def main():
    global words, user_input, speed
    for i in range(len(words)):
        time.sleep(speed)
        print(words[i-1])


main()
