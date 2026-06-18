from threading import Thread
from time import sleep, time


# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             print(f"hello {i+1}")
#             sleep(0.3)

# class hi(Thread):
#     def run(self):
#         for i in range(5):
#             print(f"hi {i+1}")
#             sleep(0.3)


# if __name__ == "__main__":

#     t1= hello()
#     sleep(0.2)
#     t2= hi()
    
#     t1.start()
#     t2.start()




# def Hello():
#     for i in range(5):
#         print(f"hello {i+1}")
#         sleep(0.3)

# def Hi():
#     for i in range(5):
#         print(f"hi {i+1}")
#         sleep(0.3)

# if __name__ == "__main__":
#     t1= Thread(target=Hello)
#     sleep(0.2)
#     t2= Thread(target=Hi)
    
#     t1.start()
#     t2.start()
    
#     t1.join()
#     t2.join()


def download(file_name):
    print(f"downloading {file_name}")
    sleep(0.3)
    print("download complete")
    
   
    
if __name__ == "__main__":
    downloads = ["file1.jpg", "file2.csv", "file3.txt"]

    start = time()
    
    for f in downloads:
        download(f)
        
    end = time()
    print(f"total time taken: {end - start:.2f} seconds")
    
    threads = []
    for f in downloads:
        t=Thread(target=download, args=(f,))
        threads.append(t)
    
    start = time()
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    end = time()
    print(f"Parallel time taken: {end - start:.2f} seconds")
    print("Bye")