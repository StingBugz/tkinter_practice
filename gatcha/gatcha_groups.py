import csv, random

group = int(input("how many group : "))+1 
member = int(input("how many member : "))
classroom = str(input("which class : "))

all = []

with open(f'/data/{classroom}.csv', 'r') as file:   #read file csv
    read = csv.DictReader(file)
    for item in read:
        all.append(item)

rand_data = list(all)


for i in range(1,group): #penamaan kelompok
    restore = []
    if len(rand_data) > member:
        print(f"kelompok {i} : ")
        for j in range(member):   # choose member remove and append to restore
            choose = random.choice(rand_data)
            rand_data.remove(choose)
            restore.append(choose)
    else:
        print(rand_data)
        print("data empty")
    print(restore)