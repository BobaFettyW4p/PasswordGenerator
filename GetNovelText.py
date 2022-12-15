from __main__ import BOOK_ID
import gutenbergpy.textget, sys, string

def get_book(BOOK_ID):
    book = gutenbergpy.textget.get_text_by_id(BOOK_ID)
    return book

def clean_book(book):
    final_book = []
    clean_book = gutenbergpy.textget.strip_headers(book)
    clean_book = clean_book.decode()
    split = clean_book.split()
    final_book = [x.lower() for x in split if x not in final_book]
    return final_book

def main(BOOK_ID):
    book = get_book(BOOK_ID)
    final_book = clean_book(book)
    print(final_book)

main(BOOK_ID)

