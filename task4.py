words = input("введите слова ")
words_list = []
count = 1

for i in range(words.count(' ') + 1):
    word = words.split()
    
    if len(str(word)) <= 10:
        print(f'{count} {word [i]}')
        num += 1

    else:
        print(f'{count} {word [i] [0:10]}')
        count += 1