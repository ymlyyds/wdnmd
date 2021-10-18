names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
sum = 0
age = 0
nan = 0
nv = 0
for i in range(4):
    sum = names[i][5]+sum
print("平均工资：",sum/4)
for i in range(4):
    age = int(names[i][1])+age
print("平均年龄：",age/4)
names.append(["刘备", "45", "男", "220", "alibaba", 500, "30"])
print(names)
for i in range(len(names)):
    if names[i][2]=="男":
        nan = nan+1
    if names[i][2]=="女":
        nv = nv+1
print("男生",nan,"女生",nv)
bumen1 = []
bumen2 = []
for i in range(len(names)):
    if names[i][6] not in bumen1:
        bumen1.append(names[i][6])
for j in range(len(bumen1)):
   up = 0
   for i in range(len(names)):
         if names[i][6] == bumen1[j]:
             up = up+1
   bumen2.append(up)
print(bumen1)
print(bumen2)







