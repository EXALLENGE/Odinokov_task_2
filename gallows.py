from random import randint as randi

words = ['Capital', 'Country', 'City', 'District', 'Region']
a = 0
b = len(words) - 1
rand = randi(a, b)
shadow = ''
word_for_game = words[rand] # слово по рандомному индексу

for _ in word_for_game: # форматируем слово в ****
    shadow += '*'

print(words[rand], shadow)
while True:
    print('Guess a letter:', end='')
    prospective_letter = str(input()) # вводим предполагаемую букву
    up_prosp_letter = prospective_letter.upper()

    where_is_letter = [] # список с индексами мест, на которых находится данная буква
    i = 0
    number_of_mistake = 0
    if prospective_letter in word_for_game:
        print('Hit!')
        for _ in word_for_game:
            if _ == prospective_letter:
                where_is_letter.append(i)
            i += 1
        for _ in where_is_letter:
            shadow = shadow[:_] + prospective_letter + shadow[_+1:]
        print('The word:', shadow)

    elif up_prosp_letter in word_for_game:
        print('Hit!')
        for _ in word_for_game:
            if _ == up_prosp_letter:
                where_is_letter.append(i)
            i += 1
        for _ in where_is_letter:
            shadow = shadow[:_] + up_prosp_letter + shadow[_+1:]
        print('The word:', shadow)

    else:
        number_of_mistake += 1
        print('Missed, mistake ', number_of_mistake, 'out of 5')
        if number_of_mistake == 5:
            print('You lost!')
            break
    if '*' not in shadow:
        print('You won!')
        break


