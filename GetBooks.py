from fileinput import filename
import gutenbergpy.textget

def getBook(id, fileName):
    book = gutenbergpy.textget.get_text_by_id(id)
    clean_book = gutenbergpy.textget.strip_headers(book)
    clean_book = str(clean_book)
    f = open(f'{fileName}.txt','x')
    f.write(clean_book)
    f.close()




bookID = '2701'
bookFileName = 'mobydick'

if __name__ == '__main__':
    getBook(bookID,bookFileName)