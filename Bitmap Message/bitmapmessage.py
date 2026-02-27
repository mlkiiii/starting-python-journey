def multiline_input():
    print("Enter your message (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)
def insertmessage():
    message=str(input("Enter your message: "))
    return message
def bitmap_message(multiline_message,message):
    print("Your message:")
    print(multiline_message)
    multiline_message_length=len(multiline_message)
    bitmaped_message=""
    message_length=len(message)
    j=0
    for i in range(multiline_message_length):
        if multiline_message[i]!=" ":
            bitmaped_message+=message[j]
        else:
            bitmaped_message+=" "
        if j==message_length-1:
            j=0
        else:
            j+=1
    print(bitmaped_message)
bitmap_message(multiline_input(),insertmessage())