register ={}
# key: name
# value: mon da dki 
number_of_register=int(input("Nhap n: "))
for i in range (number_of_register):
    inp=input()
    name,subject =" ".join(inp.split()[:-1]), inp.split()[:-1]
    if name not in register:
        register[name]=set()
    register[name].add(subject)

for name, subjects in register.items():
    print(name,"registered",len(subjects))
