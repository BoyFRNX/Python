with open('learning_python.txt') as file_object:
    message = file_object.read().strip()
    print(message.replace('Python', 'C'))
