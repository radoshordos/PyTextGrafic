from ptg import picture

print('https://github.com/radoshordos/PyTextGrafic')
choice = ""


def valid_command(inp, cmd):
    if inp.lower() == cmd:
        return True
    return False


while choice != 'exit':
    choice = str(input("Zadej příkaz:").lower())
    command = choice.split(" ")
    print(command)

    if valid_command(command[0], 'create'):
        picture.create(str(command[1]), str(command[2]), str(command[3]))
        picture.show()
    elif valid_command(command[0], 'show'):
        picture.show()
    else:
        print("CHYBNY PRIKAZ")



        #    if choice.lower() insdf