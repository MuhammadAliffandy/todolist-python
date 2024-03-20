from modules.singleton import SingletonMeta #mengambil control meta class dari design pattern singleton meta
import os
import json
import random

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data_folder_path = os.path.join(parent_dir, "data")
json_path = os.path.join(data_folder_path, "user.json")
cache_json_path = os.path.join(data_folder_path, "user_cache.json")

# digunakan untuk mendapatkan relative path pada directory file data/file_name.json

class Auth(metaclass=SingletonMeta):

# Class Auth ini yang merupakan penerapan menggunakan design pattern singleton
# Dalam python ada sebuah teknik yaitu metaclass yang akan mengontrol
# proses dalam pembuatan class    

    @staticmethod
    def session():
        with open(cache_json_path, "r") as file:
            cacheData = json.load(file)
        return cacheData    
    
# static method / function untuk melakukan parse reading json file yang mengambil data account cache

    def signIn(self , username , password  ): #function sign in untuk pengecekan data account dalam json file
        with open(json_path, "r") as file:
            userData = json.load(file)

# mengambil data dari json file untuk reading file 

        for data in userData:
            if(data['username'] == username and data['password'] == password ):
                with open(cache_json_path, "w") as file:
                    json.dump(data,file)

                return {
                    "status" : True,
                    "msg" : 'Sign in is Successfully',
                }
# membuat logical condition dari trigger username dan password params yang akan dilakukan pengecekan 
# pada json file yang telah di reading dan akan mengembalikan respon data json

    def signUp(self,username,password): #function sign up untuk menambahkan data kedalam account json file data
            
        id = random.randint(1,10000)

# Membuat  random integer atau angka dari 1 - 10000
        
        userJsonData = {
            "id" : id,
            "username": f"{username}",
            "password": f"{password}"
        }

# melakukan inisiasi structure  json yang akan di kembalikan dan disimpan

        try:
            with open(json_path, "r") as file:
                prevData = json.load(file)

            userData = [
                *prevData,
                userJsonData,
            ]

        except json.JSONDecodeError:
            userData = [
                userJsonData,
            ]

        with open(json_path, "w") as file:
            json.dump(userData,file)

            return userJsonData

# membuat logical operation json added dan mengembalikan hasil data yang akan ditambahkan
                


            


                