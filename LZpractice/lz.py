#import

#variables
dictionary = dict()
length = 0
i = 0

#Functions
def main():
    init()
    assignDictionary()

def init():
    f = open("sample.txt", "r")
    data = f.read()
    f.close()
    print(data) #Debug
    length = len(data)
    print(length) #Debug

def assignDictionary():
    print("assign")
    for i in range(length):
        print(i)
        if data[i] in dictionary.items():
            print("DEBUG")


main()