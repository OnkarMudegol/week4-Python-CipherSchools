# execptions: errors that come while excecution

# try execpt: use when we know what error can come
while True: # will run until user enter correct input
    try:
        age=int(input('age: '))
        break
    except ValueError: # will run if error was valueerror
        print("invalid input")  # if input is string
    except:
        print("unexpected error")
        
if age<18:
    print("can't paly this game")
else:
    print("yes you can play this game")

#try except else finally