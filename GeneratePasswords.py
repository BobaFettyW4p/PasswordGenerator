import random, sys, GetNovelText

BOOK_ID = int(sys.argv[1])

def main(BOOK_ID):
    dictionary = GetNovelText.main(BOOK_ID)
    print(dictionary)

if __name__ == '__main__':
    main(BOOK_ID)
