import gutenbergpy.textget

def get_book(id):
    book = gutenbergpy.textget.get_text_by_id(id)
    return book

def clean_book(book):
    lower = []
    final = []
    clean_book = gutenbergpy.textget.strip_headers(book)
    clean_book = clean_book.decode()
    split = clean_book.split()
    for word in split:
        lower.append(word.lower())
    for word in lower:
        if word not in final:
            final.append(word)
    final = ' '.join(final)
    return final

def export_book(finalBook, fileName):
    f = open(f'{fileName}.txt','x')
    f.write(finalBook)
    f.close()

if __name__ == '__main__':
    id = 2701
    fileName = 'mobydick'
    raw_book = get_book(id)
    cleaned_book = clean_book(raw_book)
    export_book(cleaned_book, fileName)

    