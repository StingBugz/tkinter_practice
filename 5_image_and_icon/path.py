import os

path = ".\source\img"
img_list = []

for i in os.listdir(path):
    img_list.append(os.path.join(path,i))

print(img_list)
print(len(img_list))

#experiment