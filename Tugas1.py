class student:
 def __init__(self,n,a,h):
    self.full_name = n
    self.age = a
    self.hobby = h
 def get_age(self):
     return self.age
 def get_hobby(self):
     return self.hobby

f = student("Ega Restu G", 19, "Bermain Game")
print("Nama mahasiswa :",f.full_name)
print("Umur :",f.get_age())
print("Hobi :",f.get_hobby())