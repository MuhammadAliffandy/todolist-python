from modules.auth  import Auth
from modules.todo import ToDo
from modules.machine import Machine
import os 

Auth = Auth()
Todo = ToDo()

def textWithLine(text):
    print('==========================')
    print(text)
    print('==========================\n')

# function untuk mengambalikan view string structure dengan arguments text 

status = False
home = 'n'

while(status == False and home =='n'): #menjalankan program pengulangan dengan trigger yang diperlukan

    textWithLine('Welcome to The To Do List')

    print('1. Sign In')
    print('2. Sign Up')
    print('\n==========================\n')

    value = int(input('Answer: '))

    if(value == 1): # menerima input yang akan menjalankan function sign in dari class Auth 
        os.system('cls')
        textWithLine('Sign in with your account')
        username =  input('Username: ')
        password = input('Password: ')
        print('\n==========================\n')

        res = Auth.signIn(username,password)

        try:
            if(res['status'] == True):
                print(res['msg'])
                input("\nPlease , press the Enter Button to Next ...")
                os.system("cls")
                status = True
        except:
            os.system("cls")
            print('Username or Password is Wrong !!')
            input("\nPlease , repeat again ...")
            os.system("cls")
            status = False

    elif(value == 2): # menerima input yang akan menjalankan function sign up dari class Auth 
        os.system('cls')
        textWithLine('Create your account')
        username =  input('Username: ')
        password = input('Password: ')
        print('\n==========================\n')
        user = Auth.signUp(username,password)
        print(f"Halo {user['username']} , Registration is Successfully")
        input("Please , press the Enter Button to Next ...")
        os.system("cls")
        status = False 
        home = 'n'
    else:
        print('\nYour number option is incorrect ')
        os.system("cls")
        status = False

    while(status):
        
        user = Auth.session() # mengambil data user yang mendapatkan cache user ketika selesai sign in
        textWithLine(f"Hello {user['username']},\nPicked your option Menu !!")

        print('1. Create Todo')
        print('2. View Todo')
        print('3. Update Todo')
        print('4. Delete Todo')
        print('5. Logout')
        print('\n==========================\n')

        value = int(input('Answer: '))

        MachineClass = Machine.get_instance()

#inisiasi machine class yang melakukan penerapan singleton pattern

# menerima logical operator value yang dipilih dan menjalankan sesuai masing masing logical function yang diperlukan

        if(value == 1):
            MachineClass.createTodo(Todo,Auth)
            status = True
        elif(value == 2 ):
            MachineClass.readAllTodo(Todo,Auth)
            status = True
        elif(value == 3 ):
            MachineClass.updateTodo(Todo)
            status = True
        elif(value == 4 ):
            MachineClass.deleteTodo(Todo)
            status = True
        elif(value == 5 ):
            os.system('cls')
            print('\nYour Account has been logout...')
            status = False
            home = 'n'
        else:
            print('\nYour number option is incorrect ')
            os.system("cls")
            status = True
        
        input("Please , press the Enter Button to Next ...")
        os.system('cls')
