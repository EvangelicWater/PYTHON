user_input = input("Enter the input ")

try:
    int(user_input)
    it_is = True
except ValueError:
    it_is = False



if it_is==True:print('El recíproco de', value, 'es', 1/value)
else:print("ERROR")





