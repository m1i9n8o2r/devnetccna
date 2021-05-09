x = 0
while True:
    try:
        filename = input("Please enter a filename: ")
        with open(filename, "r") as data:
            file_data = data.read()
    except FileNotFoundError:
        print(f'Sorry, file {filename} was not found, please try again!')
    else:
        print(file_data)
        x = 0
        break
    finally:
        x += 1
        if x == 3:
            print("Wrong filename 3 times.\nCheck the name and try again!")
            break