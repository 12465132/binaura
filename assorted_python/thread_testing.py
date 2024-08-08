import threading as thd
import os

def splitToProcessed(file_name):
    print(os.path.join(os.getcwd(),'raw',file_name))

if __name__ =="__main__":
    t1 = thd.Thread(target=splitToProcessed,args=('Cosign.mp3',))
    t1.start()
    t1.join()
    print("Done!")
