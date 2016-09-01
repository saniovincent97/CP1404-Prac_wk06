word_count = {}
input_string = input("Please enter a sentence")
input_string = input_string.split(" ")
for word in input_string:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)