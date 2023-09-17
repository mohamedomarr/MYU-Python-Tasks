'''
Task 1: Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in the x,y range
'''
def odd_even_lists(x, y):
    odd = []
    even = []
    for i in range(x, y+1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("Odd numbers:", odd)
    print("Even numbers:", even)
    print("-"*30)

'''
Task 2: Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can be divided on x,y
'''
def divisible_numbers(x, y):
    numbers = []
    for i in range(1, 101):
        if i % x == 0 and i % y == 0:
            numbers.append(i)
    print(numbers)
    print("-"*30)

'''
Task 3: Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
'''
def multiplication_table(x, y):
    for i in range(1, y+1):
        result = x * i
        print(f"{x} x {i} = {result}")

    print("-"*30)

'''
Task 4: Create a function that takes a sentence and prints the sentence without duplicated words
'''
def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    print(' '.join(unique_words))
    print("-"*30)

'''
Task 5: Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)
'''
def word_count(sentence):
    words = sentence.split()
    count = len(words)
    print(count)
    print("-"*30)

'''
Task 6: Create a function that takes a sentence and word and remove the word from the sentence
'''
def remove_word(sentence, word):
    words = sentence.split()
    new_sentence = []
    for w in words:
        if w != word:
            new_sentence.append(w)
    print(' '.join(new_sentence))
    print("-"*30)

'''
Task 7: Create a function takes a sentence and a word and prints how many time the word used in the sentence
'''
def word_occurrence(sentence, word):
    words = sentence.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(count)
    print("-"*30)

'''
Task 8: Create a function that takes x,y and prints all the number that can be divide by y from x to 100
'''
def divisible_by_y(x, y):
    numbers = []
    for i in range(x, 101):
        if i % y == 0:
            numbers.append(i)
    print(numbers)
    print("-"*30)

# Test the functions
print("Task 1:")
odd_even_lists(1, 10)
print("Task 2:")
divisible_numbers(3, 5)
print("Task 3:")
multiplication_table(5, 10)
print("Task 4:")
remove_duplicates("hello world hello mohamed")
print("Task 5:")
word_count("hello world hello mohamed")
print("Task 6:")
remove_word("hello world hello mohamed", "hello")
print("Task 7:")
word_occurrence("hello world hello mohamed", "hello")
print("Task 8:")
divisible_by_y(50, 5)