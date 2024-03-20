from modules.singleton import SingletonMeta #mengambil control meta class dari design pattern singleton meta
from datetime import datetime
import os
import json
import random

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data_folder_path = os.path.join(parent_dir, "data")
json_path = os.path.join(data_folder_path, "todo.json")

# digunakan untuk mendapatkan relative path pada directory file data/file_name.json


class ToDo(metaclass=SingletonMeta):

# Class ToDo ini yang merupakan penerapan menggunakan design pattern singleton
# Dalam python ada sebuah teknik yaitu metaclass yang akan mengontrol
# proses dalam pembuatan class

    @staticmethod    
    def loadJsonData():
        with open(json_path, "r") as file:
            prevData = json.load(file)
        
        return prevData
    
# static method / function untuk melakukan parse reading json file

    def create(self, userId, todo , date , ): #function itu menambahkan sebuah data dalam json file

        date_obj = datetime.strptime(date, "%d-%m-%Y")
        date_formatted = date_obj.strftime("%d %B %Y")
# Converted string date time denngan format yang sudah dibuat di dalam parameter
        
        id = random.randint(1,10000)
# Membuat  random integer atau angka dari 1 - 10000

        todoJsonData = {
            "id": id,
            "todo" : todo,
            "date" : date_formatted,
            "userId" : userId,
        }
# melakukan inisiasi structure  json yang akan di kembalikan dan disimpan
        
        try:

            prevData = self.loadJsonData()
            todoData = [
                *prevData,
                todoJsonData,
            ]
        except json.JSONDecodeError:
            todoData = [
                todoJsonData,
            ]
        with open(json_path, "w") as file:
            json.dump(todoData,file)

        return todoJsonData
# membuat logical operation json added dan mengembalikan hasil data yang akan ditambahkan
    

    def readAll(self , userId): #membuat function untuk melakukan reading semua data dalam json file
        try:
            todoData = self.loadJsonData()
# melakukan pemanggilan function class yang telah di inisiasi sebelumnya untuk membaca json file 
# dan mengembalikan semua data json yang bisa di olah

            todoFilter = list(filter(lambda x: x['userId'] == userId, todoData))
            return todoFilter
# melakukan filteriasi data dengan penyesuian userId key yang value nya harus sama dengan params userId 

        except json.JSONDecodeError:
                return {
                        "status" : False,
                        "data" : 0,
                }
    
    def read(self): # function untuk membaca file dengan metode sorted 
        
        try:
            todoFilter = self.readAll()
            sorted_data = sorted(todoFilter, key=lambda x: x['id'])
            todoSorter =  sorted_data
            return todoSorter

# melakukan sortering file berdasarkan id nomor dari yang paling kecil

        except json.JSONDecodeError:
                return {
                        "status" : False,
                        "data" : 0,
                }
    
    def update(self,pick,todo,date): #melakukan function update json file
        data = self.read()
        dataPicked = data[pick]['id']
# mengambil data yang dipilih sesuai params pick yang merupakan key index setiap masing masing array file
# kemudian juga menambahkan pemanggilan key id untuk dipanggil value yang mempunyai key id
        todoData = self.loadJsonData()
        
        for data in todoData:
            if(data['id'] == dataPicked): 
                data['todo'] = todo
                data['date'] = date   

            with open(json_path, "w") as file:
                json.dump(todoData,file)
# melakukan logical checked untuk penyesuian data yang sesuai dengan data yang dipilih 
# kemudian melakukan inisiasi dengan value params yang di update
                
    def delete(self , pick ): #function method delete untuk menghapus data per id
        data = self.read()
        dataPicked = data[pick]['id']
# mengambil data yang dipilih sesuai params pick yang merupakan key index setiap masing masing array file
# kemudian juga menambahkan pemanggilan key id untuk dipanggil value yang mempunyai key id
        prevData = self.loadJsonData()
        
        for index , data in enumerate(prevData): 
            if(data['id'] == dataPicked):
                if(len(prevData) == 1):
                    newData = []
                else:
                    newData = prevData[index - 1 :index]

                with open(json_path, "w") as file:
                    json.dump(newData,file)

# melakukan logical checked untuk penyesuian data yang sesuai dengan data yang dipilih 
# kemudian melakukan inisiasi dengan value params yang akan di hapus