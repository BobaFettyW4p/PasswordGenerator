import random, string

def import_book(fileName):
    f = open(fileName, 'r')
    file = f.read()
    return file

def generate_password(book,passwordLength):
    finalPassword = ''
    alphabet = string.ascii_lowercase
    alphabetList = list(alphabet)
    numbers = [*range(1,100)]
    symbols = ['!','@','#','$','%','^','&','*','?']
    split = book.split()

    while len(finalPassword) < (passwordLength - 3):
        candidate = random.choice(split)
        print(f'candidate is {candidate}')
        validCandidate = True
        for letter in candidate:
            if letter not in alphabetList:
                validCandidate = False
                break
        if validCandidate:
            finalPassword+=f'{candidate.capitalize()}'
    finalPassword+=f'{random.choice(numbers)}{random.choice(symbols)}'
    return finalPassword

if __name__ == '__main__':
    usablePassword = []
    passwordLength = input('How many characters long does your password need to be?')
    passwordLength = int(passwordLength)
    bookLocation = input('What file are we pulling the password from?')
    bookText = import_book(bookLocation)
    while len(usablePassword) < 3:
        generatedPassword = generate_password(bookText,passwordLength)
        usablePassword.append(generatedPassword)
    print(usablePassword)

