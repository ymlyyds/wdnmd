list = ["姓名", "年龄", "性别", "编号", "任职公司", "薪资", "部门编号"]
names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
name = []
for i in range(len(names)):
    name.append(names[i][0])
zs = {}
lb = []
l = 0
for ke in name:
    k = 0
    sz = {}
    for key in list:
        sz[key] = names[l][k]
        k += 1
    lb.append(sz)
    zs[ke] = lb[0]
    l += 1
    del lb[0]
print(zs)
