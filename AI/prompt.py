def decode(message):

    sorted = []

    with open(message, 'r') as file:
        for line in file:
            number, word = line.split()
            sorted.append((int(number), word))
    
    sorted.sort()
    
    message = ' '.join(word for _, word in sorted)

    return message

decoded_message = decode('D:\JC\Python Course\AI\message.txt')
print(decoded_message)