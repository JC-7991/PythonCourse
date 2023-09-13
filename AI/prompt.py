def decode(message_file):

    sorted = []

    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.split()
            sorted.append((int(number), word))
    
    sorted.sort()
    
    message = ' '.join(word for _, word in sorted)

    return message

file = open("message.txt")
decoded_message = decode(file)
print(decoded_message)