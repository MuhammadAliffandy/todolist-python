from modules.singleton import SingletonMeta
import os

def textWithLine(text):
    print('==========================')
    print(text)
    print('==========================\n')

# function untuk mengambalikan view string structure dengan arguments text 

class Machine (metaclass = SingletonMeta): 

# Class Machine ini yang merupakan penerapan menggunakan design pattern singleton
# Dalam python ada sebuah teknik yaitu metaclass yang akan mengontrol
# proses dalam pembuatan class

    @staticmethod
    def renderListView(data):
        for i in range(len(data)):
            print(f"ToDo: {data[i]['todo']}") 
            print(f"date: {data[i]['date']}") 
            print('==========================')
# melakukan rendering string structure dari data json file 

    def createTodo(self , ToDoClass, AuthClass): #function untuk menambahkan proses todo list
        os.system('cls') #clearing cmd line 

        textWithLine('Add your ToDo List') #  title program
        
        todo = input('ToDo :')
        date = input('Date (format : DD-MM-YY): ')

# membuat input value yang akan menerima data todo dan date

        user =  AuthClass.session();
        ToDoClass.create( user['id'] , todo, date )

# ini adalah contoh inisiasi dari instasiasi class auth dan todo class yang
# ditangkap dari inisiasi argumentasi class machine dan menggunakan method class create 

        os.system("cls")
        print(f"To Do has been added")
    

    def readAllTodo(self , ToDoClass, AuthClass): # melakukan reading semua data todo list
        os.system('cls')
        textWithLine('View All your ToDo List')
    
        user =  AuthClass.session();
        todoData = ToDoClass.readAll(user['id'])


# ini adalah contoh inisiasi dari instasiasi class auth dan todo class yang
# ditangkap dari inisiasi argumentasi class machine dan menggunakan method class readAll

        self.renderListView(todoData)
    

    def updateTodo(self , ToDoClass): # melakukan logical update data todo
        os.system('cls')
        textWithLine('View All your ToDo List')

        todoData = ToDoClass.read()


# ini adalah contoh inisiasi dari instasiasi class auth dan todo class yang
# ditangkap dari inisiasi argumentasi class machine dan menggunakan method class read

        self.renderListView(todoData)

        number = int(input("\nPick your number todo to updated : "))        

# mengambil argumentasi paremeter key index yang akan diinisasi data todo

        os.system('cls')
        
        todo = input('ToDo :')
        date = input('Date (format : DD-MM-YY): ')
        ToDoClass.update(number - 1,todo,date)

# ini adalah contoh inisiasi dari instasiasi class auth dan todo class yang
# ditangkap dari inisiasi argumentasi class machine dan menggunakan method class update

        print("\nYour data has been updated")


    def deleteTodo(self, ToDoClass): #melakukan logical delete data todo
        os.system('cls')
        textWithLine('View All your ToDo List')
    
        todoData = ToDoClass.read()

        self.renderListView(todoData)

        number = int(input("\nPick your number todo to deleted : "))        
        os.system('cls')
        
        ToDoClass.delete(number - 1)
        print("\nYour data has been deleted")

# ini adalah contoh inisiasi dari instasiasi class auth dan todo class yang
# ditangkap dari inisiasi argumentasi class machine dan menggunakan method class delete

