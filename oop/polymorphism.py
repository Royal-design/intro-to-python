class Laptop:
     def build(self):
         print("building laptop")

class Desktop:
     def build(self):
         print("building Desktop")

class Tablet:
    def open_pdf(self):
        print("opening pdf")
         
class Alien:
    def build(self, machine:Laptop, pdf=None):
        print("building alien")
        machine.build()
        if pdf is not None:
            pdf.open_pdf()
        

hp = Laptop()
beast = Desktop()
alien = Alien()
lenov0_pdf = Tablet()
alien.build(hp)
alien.build(beast, lenov0_pdf)
