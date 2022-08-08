students = ["Ishan", "Riddhi", "Yash"]
subjects = ["Python", "CCNA", "Networking"]

result = {students[i]: subjects[i] for i in range(len(students))}
print("output is:" + str(result))

x = zip(students, subjects)
print(dict(x))