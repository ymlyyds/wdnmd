import xlrd

fp = xlrd.open_workbook(filename=r"C:\Users\Administrator\Desktop\python\day7\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
sum = 0
sumr = 0
product = 0
list = []
ts = []
c = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [1,11, 12,]]
for i in range(0, 12):
    st = fp.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for j in range(1, rows):
        data = st.row_values(j)
        product = data[2]*data[4]
        sum = sum + product
    sumr = sumr + sum
print("全年销售总额为", sumr)


k = 0
for i in range(0, 12):
    st = fp.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for j in range(1, rows):
        data = st.row_values(j)
        if data[1] not in list:
            list.append(data[1])
            k+=1
ji = {1: '春季', 2: '夏季', 3: '秋季', 4: '冬季'}
for k in range(len(list)):
    dj = 0
    zs = 0
    for m in range(len(c)):
        for i in c[m]:
            st = fp.sheet_by_index(i-1)
            rows = st.nrows
            cols = st.ncols
            for j in range(1, rows):
                data = st.row_values(j)
                zs = zs + data[4]
                if data[1] == list[k]:
                    dj = dj + data[4]
        print(ji[m+1], list[k], '{:.2f}%'.format(dj/zs*100))
        #print("平均每天买",list[k],(dj/yy))
        #print("销售量占比为",list[k],'{:.2f}%'.format(dj/zs*100))
for k in range(len(list)):
    dj = 0
    zs = 0
    #yy = 0
    for i in range(0, 12):
        st = fp.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            data = st.row_values(j)
            zs = zs + data[4]
            if data[1] == list[k]:
                dj = dj + data[4]
      #          yy = yy + 1
    #print("平均每天买",list[k],(dj/yy))
    print("销售量占比为",list[k],'{:.2f}%'.format(dj/zs*100))

for k in range(len(list)):
    ze = 0
    de =0
    for i in range(0, 12):
        st = fp.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            data = st.row_values(j)
            ze = ze + (data[2] * data[4])
            if data[1] == list[k]:
                de = de + (data[2] * data[4])
    print("销售额占比为",list[k],'{:.2f}%'.format(de/ze*100))

for k in range(len(list)):
    for i in range(0, 12):
        st = fp.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        dj = 0
        zs = 0
        for j in range(1, rows):
            data = st.row_values(j)
            zs = zs + data[4]
            if data[1] == list[k]:
                dj = dj +data[4]
        print("第",i+1,"月", list[k], '{:.2f}%'.format(dj / zs * 100))



