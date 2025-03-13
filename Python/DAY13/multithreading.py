# multithreading = executing multiple tasks simultaneously (multitasking)
# Good for I/O bound tasks, like reading files or fetching data from APIs
# threading.Thread(target=my_function)

import threading 
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1 = threading.Thread(target=walk_dog, args=("Pogo","Parajuli")) #instance of threading #Tuple ho vanera pogo pachi comma deko
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()    

#esle chai concurrently garcha, point wise jun chado huncha tei aucha suruma

chore1.join()
chore2.join()
chore3.join()  #wait until all threads are finished before moving on to the next line

print("All chores are done!")

