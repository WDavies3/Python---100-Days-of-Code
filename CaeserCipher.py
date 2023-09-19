logo = '''
           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP" 88     `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88    88      
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
def encode(message, offset):
    result = ''
    for c in message:
        encoded_val = ord(c) + offset
        if encoded_val > 126:
            encoded_val -= 94
        result += chr(encoded_val)
    return result

def decode(message, offset):
    result = ''
    for c in message:
        decoded_val = ord(c) - offset
        if decoded_val < 32:
            decoded_val += 94
        result += chr(decoded_val)
    return result

print(logo)
while True:
    choice = input("Would you like to (e)ncode or (d)ecode a message, or (q)uit?\n")[0].lower()
    if choice == 'q':
        break
    if choice == 'e' or choice == 'd':
        message = input("What is the message?\n")
        key = int(input("Enter an integer to use as the key:\n"))
    else:
        print('Invalid selection, please try again.')
    if choice == 'e':
        print(f'Your encoded message is {encode(message,key)}')
    if choice == 'd':
        print(f'Your decoded message is {decode(message,key)}')