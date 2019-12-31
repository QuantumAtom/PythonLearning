why = ''
reason = 'text_files/poll.txt'

while (why != 'exit'):
    why = input("What reason are you excited about programming?: ")
    if (why == "exit"):
        break
    else:
        with open(reason, 'a') as pollinfo:
            pollinfo.write(why + "\n")
            print("Thank you for your reason. We hope it encourages others to take up the field.")

