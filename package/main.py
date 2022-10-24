from group import *
from student import *

st1 = Student('Male', 30, 'Steve', 'Jobs', '1')
st2 = Student('Female', 25, 'Liza', 'Taylor', '2')
st3 = Student("Male", 18, "John", "Smith", "3")
st4 = Student("Male", 20, "Vasilii", "Petrov", "4")
st5 = Student("Male", 17, "Alexsey", "Ivanov", "5")
st6 = Student("Female", 19, "Alisa", "Smith", "6")
st7 = Student("Female", 20, "Natasha", "Jobs", "7")
st8 = Student("Male", 21, "Olga", "Pegalo", "8")
st9 = Student("Male", 22, "Valera", "Shpak", "9")
st10 = Student("Male", 23, "Victor", "Maksimov", "10")


gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
except Exception as e:
    print(e)
print(gr)
print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))
gr.delete_student('Jobs')
gr.delete_student('Jobs2')
print(gr)