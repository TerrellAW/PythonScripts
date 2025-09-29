# Dictionary
morseCode = {'A':'.-', 'B': '-...', 'C':'-.-.', 'D':'-..', 'E':'.',
             'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
             'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O': '---', 'P':'.--.',
             'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
             'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
             '?':'', ',':'', '.':'', '!':'', '0':'-----', '1':'.----', '2':'..---', 
             '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
             '8':'---..', '9':'----.'}

# User Input
msg = input("Enter a message, type 'stop' to quit: ")

# Conversion
while msg.lower() != 'stop':
    for ch in msg:
        if (ch == ' '):
            print(" | ", end="")
        else:
            morse = morseCode.get(ch.upper(), "Error")
            print(morse, end="")
    msg = input("\nEnter a message, type 'stop' to quit: ")
