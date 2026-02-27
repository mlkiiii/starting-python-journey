def multiline_input():
    print("Enter your message (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines
def insertmessage():
    message=str(input("Enter your message: "))
    return message
def bitmap_message(lines,message):
    print("Your message:")
    for line in lines:
        print(line)
    for line in lines:
        multiline_message=line
        multiline_message_length=len(multiline_message)
        message_length=len(message)
        j=0
        for i in range(multiline_message_length):
            if multiline_message[i]!=" ":
                multiline_message=multiline_message[:i]+message[j]+multiline_message[i+1:]
                if j==message_length-1:
                    j=0
                else:
                    j+=1
        lines[lines.index(line)]=multiline_message
    print("Bitmaped message:")
    for line in lines:
        print(line)
bitmap_message(multiline_input(),insertmessage())