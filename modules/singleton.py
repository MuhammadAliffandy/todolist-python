class SingletonMeta(type):

# Ini adalah class SingletonMeta yang akan dijadikan sebuah blueprint 
# agar dapat dijadika sebagai syarat dalam pembuatan class
# Paramaeter type digunakan unntuk menginisiasi bahwa class ini adalah sebuah metaclass
# Metaclass dalam python bisa dikatakan sebuah teknik untuk mengontrol pembuatan kelas
    
    _instances = {}
# _instances adalam sebuah variabel yang digunakan sebagai wadah hasil dari instances class
    
    def __call__(cls, *args, **kwargs): #argumentasi dari function ini untuk membantu pemrosesan function in

# Kemudian kita mendefinisikan function __call__ untuk melakukan pengecekan ketika
# Sebuah class digunakan atau dipanggil maka akan dilakukan pengecekan

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return cls._instances[cls]
        else:  
            raise Exception("We can not creat another class") 
        
# Selanjutnya kita akan membuat sebuah logical condition untuk melakukan pengecekan 
# Pada class yang akan di instansiasi jika tidak ada maka akan
# di added kedalam _instances variabel dan jika selesai maka akan melakukan 
# pengembalian instansiasi yang sudah di added dalam _instances
        
    def get_instance(cls):
        if cls not in cls._instances:
            cls._instances[cls] = cls()
        return cls._instances[cls]

# dan ini adalah function untuk menngembalikan instance yang sudah ada pada pemanggilan awal