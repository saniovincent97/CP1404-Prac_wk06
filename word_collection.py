numbers = {}
sentence = "this is a collection of words of nice words this is a fun thing it is"
sentence_split = sentence.split(" ")
for word in sentence_split:
    if word in numbers:
        numbers[word] += 1
    else:
        numbers[word] = 1
for sentence_split, numbers in numbers.items():
    print("{} : {}".format(sentence_split, numbers))