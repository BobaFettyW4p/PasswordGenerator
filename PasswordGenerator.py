import random


def pull_words(length):
    samples = ['Tetrarchy','Pontifex','Coliseum','Boudicca','Centurion','Augustus','Gracchus','Gaius']
    final_string='' 
    while len(final_string) < length-3:
        final_string=f'{final_string}{random.choice(samples)}'
    return final_string

def create_password(words):
    numbers = [*range(1,100,1)]
    symbols = ['!','@','#','$','%','^','&','*','?']
    password = f'{words}{random.choice(numbers)}{random.choice(symbols)}'
    return password




if __name__ == '__main__':
    password_length = input('How many charactesr do your passwords need to be? ')
    password_length = int(password_length)
    password_candidates = []
    while len(password_candidates) < 3:
        string = pull_words(password_length)
        password = create_password(string)
        password_candidates.append(password)

    print(f'Potential passwords:')
    for password in password_candidates:
        print(password)
    
