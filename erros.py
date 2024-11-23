def errors():
    try:
        for i in ['a', 'b', 'c']:
            print(i**2)
    except TypeError:
        print("General Error! Watch out")


def errors2():
    x=5
    y=0
    z = x / y
    try:
        print(z)
    except ZeroDivisionError:
        print("Zero Division Error")
    finally:
        print("All Done")

def errors3():

    # Waiting for correct response
    waiting = True
    while waiting:
        try:
            n = int(input("Input an integer: "))
        except ValueError:
            print("An error occured! please try again")
            continue
        else:
            waiting = False
        finally:
            print("Great Job!")
    print("tank you, your number squared is: ")
    print(n**2)
