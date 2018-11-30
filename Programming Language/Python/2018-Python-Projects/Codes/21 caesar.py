ascii_init = 26

def main():
    print("Welcome to the caesar world!")
    print("(1) encrypt")
    print("(2) decrypt")
    select = int(input("please select number >> "))
    print()

    if select == 1:
        caesar_encrypt()
    if select == 2:
        caeasr_decrypt()

def caesar_encrypt():
    print("[Caesar Encrypt Tool]")
    plain_text = input("please input plain text >> ")
    interval = int(input("please input interval >> "))
    cryptogram = ""

    for i in plain_text:
        if ord('A') <= ord(i) <= ord('Z'):
            if ord(i) + interval > ord('Z'):
                cryptogram += chr(ord(i) - ascii_init + interval)
            elif ord(i) + interval < ord('A'):
                cryptogram += chr(ord(i) + ascii_init + interval)
            else:
                cryptogram += chr(ord(i) + interval)
        elif ord('a') <= ord(i) <= ord('z'):
            if ord(i) + interval > ord('z'):
                cryptogram += chr(ord(i) - ascii_init + interval)
            elif ord(i) + interval < ord('a'):
                cryptogram += chr(ord(i) + ascii_init + interval)
            else:
                cryptogram += chr(ord(i) + interval)
        else:
            cryptogram += i

    print(f"Cryptogram is {cryptogram}")

def caeasr_decrypt():
    print("[Caesar Decrypt Tool]")
    cryptogram = input("please input cryptogram >> ")
    interval = int(input("please input interval >> "))
    plain_text = ""

    for i in cryptogram:
        if ord('A') <= ord(i) <= ord('Z'):
            if ord(i) - interval < ord('A'):
                plain_text += chr(ord(i) + ascii_init - interval)
            elif ord(i) - interval > ord('Z'):
                plain_text += chr(ord(i) - ascii_init - interval)
            else:
                plain_text += chr(ord(i) - interval)
        elif ord('a') <= ord(i) <= ord('z'):
            if ord(i) - interval < ord('a'):
                plain_text += chr(ord(i) + ascii_init - interval)
            elif ord(i) - interval > ord('z'):
                plain_text += chr(ord(i) - ascii_init - interval)
            else:
                plain_text += chr(ord(i) - interval)
        else:
            plain_text += i

    print(f"Plain text is {plain_text}")

if __name__ == "__main__":
    main()
