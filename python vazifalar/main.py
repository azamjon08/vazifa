# import time
# def link():
#     print("Qizil")
#     time.sleep(1)
#     print("3 soniya kuting")
#     time.sleep(3)
#     print("Sariq")
#     print("2 soniya kuting")
#     time.sleep(2)
#     print("Yashil")
#     time.sleep(2)
#     print("Yurishingiz mumkun: ")
#     time.sleep(1)
    
# link()   
import threading as thr

def list():
    print("hello")
t1 = thr.Thread(target=list)
t1.start()   

 