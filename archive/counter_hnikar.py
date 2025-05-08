


# try to open a file
def startup():
    try :
        with open("file.txt", "r") as file:
            initial_count = int(file.read())
    except :
        with open("file.txt", "w") as file:
            initial_count = 0
            file.write(str(initial_count))
    print(initial_count)
    return initial_count


def button_input(initial_count):
    count = int(initial_count)
    while True:
        button = input("+ or - or done:")
        if button == "+":
            count = count + 1
        elif button == "-":
            count = count - 1
        elif button == "done":
            break
        with open("file.txt", "w") as file:
            file.write(str(count))
        print(count)

def main():
    initial_count = startup()
    button_input(initial_count)

main()
