# Find the most common word in file

file_name_1 = input('Enter File: ')
if len(file_name_1) < 1: file_name_1 = 'clown.txt'
handle_1 = open(file_name_1)

dictionary_1 = dict()
for line in handle_1:
    line = line.rstrip()
    # print(line)
    words_1 = line.split()
    # print(words_1)
    for word in words_1:
        # print('**', word, dictionary_1.get(word, -99))

        # old_count = dictionary_1.get(word, 0)
        # print(word, 'old', old_count)
        # new_count = old_count + 1yhgvhui
        # dictionary_1[w] = new_count
        # print(word, 'new', new_count)

        # # print(word)
        # if word in dictionary_1:
        #     dictionary_1[word] += 1
        #     # print('**EXISTING**')
        # else:
        #     dictionary_1[word] = 1
        #     # print('**NEW**')
        # print(word, dictionary_1[word])

        # the following is a one line version of the previous 5 lines
        # idiom: retrieve/create/update counter
        dictionary_1[word] = dictionary_1.get(word, 0) + 1
        # print(word, 'new', dictionary_1[word])

# print(dictionary_1)

# Now find the most common word
largest = -1
the_word = None
for k, v in dictionary_1.items():
    # print(k, v)
    if v > largest:
        largest = v
        the_word = k  # capture/remember the word that was largest

# print('Done', the_word, largest)
print(the_word, largest)
