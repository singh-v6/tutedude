try :
    with open('sample.txt','r') as file:
        reading = file.read()
        print('Reading file content:')
        print(reading)
except Exception as e:
    print ("Error: The file 'sample.txt' was not found")
finally :
    print('good to see you!')
