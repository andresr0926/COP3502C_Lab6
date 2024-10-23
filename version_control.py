# Andres E. Rodriguez

def main():
    # while loop to show menu options
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n\n')
        option = int(input('Please enter an option: '))
        # option to encode password
        if option == 1:
            x = encode()
        # option to decode password
        elif option == 2:
            y = decode(x)
            print("The encoded password is " + x + ", and the original password is " + y + ".")
        #option to quit
        elif option == 3:
            break
        # error handling if they do not choose and option 1 - 3
        else:
            print('Please enter and option 1 - 3!')

def encode():
    # create a list with numbers 0-9
    num_list = list(range(10))
    # convert number list to strings
    num_list = [str(num) for num in num_list]
    # while loop to get the password to encode
    while True:
        curr_pass = input('Please enter your password to encode: ')
        curr_pass = [digit for digit in curr_pass]
        x = 0
        # for loop to verify the inputted password is all numbers 0-9
        for item in curr_pass:
            if item not in num_list:
                print('Password not valid')
                x = 1
                break
        if x == 1:
            continue
        # encode password by adding 3 to each digit in the password
        else:
            new_pass = [str(int(num)+ 3) for num in curr_pass]
            final_pass = ''.join(new_pass)
            print('Your password has been encoded and stored!')
            return final_pass

def decode(final_pass):
    r = ""
    for i in final_pass:
        r = r + str(int(i) - 3)
    return r


if __name__ == '__main__':
    main()
