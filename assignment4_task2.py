a = input('Enter text to write to the file: ')
with open('output.txt', 'r+') as file:
    writing = file.write(a)
    print('Data successfully written to output.txt.')
b = input('Enter additional text to append: ')
with open('output.txt', 'a') as file:
    append = file.write('\n' + b)
    print('Data successfully appended.')
with open('output.txt', 'r+') as file:
    read = file.read()
    print(read)