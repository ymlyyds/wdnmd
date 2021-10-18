lb = [1,2,3,3,5,4,1,2,3,5,4,1,2,3,5,5]
dict={}
for key in lb:
    if key not in dict:
        dict[key] = 1
    else:
        dict[key] += 1
print(dict)

