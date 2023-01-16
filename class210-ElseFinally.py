while True:
    try:
        age=int(input('age: '))
    except ValueError:
        print("invalid input")  
    except:
        print("unexpected error")

    else:
        print(f'user input={age}')
        break
    finally: # this will always run
        print("finally")