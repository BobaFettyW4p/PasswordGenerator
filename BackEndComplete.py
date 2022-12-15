from fileinput import filename
import random,string,gutenbergpy.textget, sys

def get_book(id):
    book = gutenbergpy.textget.get_text_by_id(id)
    return book

def clean_book(book):
    lower,final = [],[]
    clean_book = gutenbergpy.textget.strip_headers(book)
    clean_book = clean_book.decode()
    split = clean_book.split()
    for word in split:
        lower.append()

if __name__ == '__main__':
    id = sys.argv
    book = get_book(id) 
    clean_book(book)
