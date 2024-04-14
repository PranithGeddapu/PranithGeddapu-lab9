state= 1


def enc(inp):
    encpa = " "
    for d in inp:
        encd = str((int(d) + 3) % 10)
        encpa = encpa + encd

    return encpa




while state == 1:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    if option == "1":
        inp = input("Please enter your password to encode: ")
        enc(inp)

        encda = enc(inp)
        print ("Your password has been encoded and stored!")

    if option == "3":

        state = 0
def decode(encoded_password):
    decoded_passwordList = []
    for i in range (0, len(encoded_password)):
        decoded_passwordList.append(int(encoded_password[i])-3)
        decoded_passwordList[i] = (str(decoded_passwordList[i]))
    return ''.join(decoded_passwordList)





