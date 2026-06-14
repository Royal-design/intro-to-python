# class computer:
#     def __init__(self):
#         print("running")
#         self.cpu = "10"
#         self.ram = "16gb"
#         self.ssd = "256gb"
    
#     def config(self):
#         print("configuring", self.cpu, self.ram, self.ssd)

class computer:
    brand = 'Python AI'
    def __init__(self, cpu, ram, ssd):
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
    
    def config(self):
        print("configuring", self.cpu, self.ram, self.ssd)
    
    @classmethod
    def info(cls):
        return cls.brand
    
    @staticmethod
    def convert_to_bytes(gb):
        size = int(gb[:2])
        return size * (1024 **3 ) 
        
        
comp1 = computer("10", "16gb", "256gb")
comp2 = computer("15", "16gb", "512gb")

comp1.config()
comp2.config()

print(comp1.info())
print(comp1.convert_to_bytes(comp1.ram))








