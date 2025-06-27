"""Caesar Cipher Hacker, by Al Sweigart
this program hacks messages encrypted with the Caesar cipher by 
doing a brute force attack against every possible key."""

print('Caesar Cipher Hacker by Al Sweigart')

#allow the user to enter the encrypted message
print('Enter the encrypted message to hack:')
message = input('> ')

#Every possible symbol that can be ecrypted/decrypted
#matches symbols used when encrypting
SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): #loop through each possible key
    translated=''

    #decript each symbol in message
    for symbol in message:
        if symbol in SYMBOLS:
            num=SYMBOLS.find(symbol) #get the number of the symbol
            num=num-key #decrypt the number

            if num<0:
                num=num+len(SYMBOLS)

            #Add the decrypted number's symbol to translated
            translated=translated + SYMBOLS[num]


        else:    
            #add decrypted numbers symbol to translated
            translated=translated + symbol

    #display the key being tested, along with it's decrypted text.
    print('Key #{}:{}'.format(key,translated))

