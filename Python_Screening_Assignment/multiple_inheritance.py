class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
son_1 = Son()
son_1.fathername = "Narendra"
son_1.mothername = "Anita"
son_1.parents()
