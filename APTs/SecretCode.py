def decrypt(message, numbers):
    listStr = []
    listMessage = message.split()
    index = len(listMessage)
    for i in range(index):
        if numbers[i] <= (len(listMessage[i])-1):
            if numbers[i] >= -1 * len(listMessage[i]):
                char = listMessage[i][numbers[i]]
                listStr.append(char)
    finalStr = ''.join(listStr)
    return finalStr