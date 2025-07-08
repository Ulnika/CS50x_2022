def main():
    message = input()
    print(convert(message))

def convert(message):
    message = message.replace(':(', '🙁')
    message = message.replace(':)', '🙂')
    return(message)

main()