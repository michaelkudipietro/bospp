import sys

bitmap = '''
....................................................................    
   **************   *  *** **  *      ******************************    
  ********************* ** ** *  * ****************************** *     
 **      *****************       ******************************         
          *************          **  * **** ** ************** *         
           *********            *******   **************** * *          
            ********           ***************************  *           
   *        * **** ***         *************** ******  ** *             
               ****  *         ***************   *** ***  *             
                 ******         *************    **   **  *             
                 ********        *************    *  ** ***             
                   ********         ********          * *** ****        
                   *********         ******  *        **** ** * **      
                   *********         ****** * *           *** *   *     
                     ******          ***** **             *****   *     
                     *****            **** *            ********        
                    *****             ****              *********       
                    ****              **                 *******   *    
                    ***                                       *    *    
                    **     *                    *                       
....................................................................       '''

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter a message to display with bitmap.')
message=input('> ')
if message =='':
    sys.exit()

#loop over each line in bitmap
for line in bitmap.splitlines():
    #loop over each character in the line
    for i, bit in enumerate(line):
        if bit == ' ':
            #print an empty epace since there's a space in the bitmap
            print(' ',end=' ')
        else:
            #print the character from the message
            print(message[i %len(message)], end='')
    print()