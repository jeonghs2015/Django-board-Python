input_id = input('id : ')
id1 = 'jeonghs'
id2 = 'dauda'
password1 = '1111'
password2 = '2222'
if(input_id == id1):
    input_password = input('password : ')
    if(input_password == password1):
        print('Welcome jeonghs!!!')
    else:
        print('''incorrect password!!! 
Security alarm Detected...''')
elif(input_id == id2):
    input_password = input('password : ')
    if(input_password == password2):
        print('Welcome dauda!!!')
    else:
       print('''incorrect password!!! 
Security alarm Detected...''')
else:
    print('''incorrect ID!!!
Large BIOMASS Detected....''')