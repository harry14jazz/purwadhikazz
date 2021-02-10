'''
def mode(arr):
    distinct = []
    final = []
    for value in arr:
        if value not in distinct:
            distinct.append(value)
        else:
            pass

    for value2 in distinct:
        counter = 0
        for checker in arr:
            if checker == value2:
                counter += 1
            else:
                pass
        final.append([value2, counter])

    high = final[0][1]
    idx_tmp = 0
    for index in range(len(final)):
        if final[index][1] > high:
            high = final[index][1]
            idx_tmp = index
        else:
            pass

    return final[idx_tmp]


def median(arr):
    final = sorted(arr)

    if len(final) % 2 == 0:
        num = len(final)
        median = (final[(num//2) - 1] + final[num//2]) / 2
        return median
    else:
        num = len(final)
        median = final[((num+1)//2) - 1]
        return median


def mean(arr):
    total = 0
    amount = len(arr)

    for value in arr:
        total += value

    mean = total/amount

    return mean


def q1(arr):
    arr = sorted(arr)
    amount = len(arr)
    loc_q1 = 0.25*(amount + 1)
    loc_q1 = str(loc_q1)
    loc_q1 = loc_q1.split('.')
    if loc_q1[1] == '0':
        idx_q1 = int(loc_q1[0])
        q1 = arr[idx_q1 - 1]
        return q1
    else:
        idx_q1 = int(loc_q1[0])
        idx_q1_next = idx_q1+1
        q1 = (arr[idx_q1 - 1] + arr[idx_q1_next - 1])/2
        return q1


def q3(arr):
    arr = sorted(arr)
    amount = len(arr)
    loc_q3 = 0.75*(amount + 1)
    loc_q3 = str(loc_q3)
    loc_q3 = loc_q3.split('.')
    if loc_q3[1] == '0':
        idx_q3 = int(loc_q3[0])
        q3 = arr[idx_q3 - 1]
        return q3
    else:
        idx_q3 = int(loc_q3[0])
        idx_q3_next = idx_q3+1
        q3 = (arr[idx_q3 - 1] + arr[idx_q3_next - 1])/2
        return q3


def outliers(arr):
    outlier_data = []
    iqr = int(q3(arr) - q1(arr))
    min_q3 = int(q3(arr) + (1.5 * iqr))
    max_q3 = int(q3(arr) + (3 * iqr))
    min_q1 = int(q1(arr) - (1.5 * iqr))
    max_q1 = int(q1(arr) - (3 * iqr))
    # return iqr, min_q1, max_q1, min_q3, max_q3
    for value in arr:
        if min_q1 > value or value > max_q3:
            outlier_data.append(value)
        elif value in range(max_q1, min_q1) or value in range(min_q3, max_q3):
            outlier_data.append(value)
        else:
            continue

    if len(outlier_data) > 0:
        message = 'Terdapat data outlier yaitu: {}'.format(outlier_data)
        return message
    else:
        return 'Himpunan data tidak memiliki data outlier'


# lists = [1, 2, 3, 100, 6, 5, 3, 4, 7, 8, 2, 4, 6, 5, 7, 7, 8, 3]

# print(outliers(lists))

#-------------MAIN-------------------------#
try:
    data_arr = []
    qty = int(input('Masukkan jumlah data yang akan dimasukkan: '))

    for index in range(qty):
        data = int(input('Data ke-{} : '.format(index+1)))
        data_arr.append(data)

    status = True
    while status:
        print('-------------Apps Mini-------------')
        print('1. Cek Mean (Rata-rata) data')
        print('2. Cek Median (Nilai Tengah) data')
        print('3. Cek Modus (Data dominan) data')
        print('4. Cek Q1 data')
        print('5. Cek Q3 data')
        print('6. Cek Outliers (Data Pencilan) data')
        print('7. Keluar\n')

        pilihan = int(input('Masukkan pilihan menu: '))
        if pilihan == 1:
            print('Rata-rata (Mean) data ialah: {}\n'.format(mean(data_arr)))
        elif pilihan == 2:
            print('Median (Nilai Tengah) dari data ialah: {}\n'.format(median(data_arr)))
        elif pilihan == 3:
            print('Modus (Data Dominan) dari data ialah: {}\n'.format(mode(data_arr)))
        elif pilihan == 4:
            print('Q1 dari data ialah: {}\n'.format(q1(data_arr)))
        elif pilihan == 5:
            print('Q3 dari data ialah: {}\n'.format(q3(data_arr)))
        elif pilihan == 6:
            print(outliers(data_arr))
        elif pilihan == 7:
            print('Exit, bye.')
            break
        elif pilihan == 8:
            print(data_arr)
        else:
            print('Pilihan tidak tersedia')
            status = False
            break
except:
    print('Tipe data yang dimasukkan salah!')
'''

# max
def largest_arr(arr):
    tmp = 0
    max_val = 0
    for index in range(len(arr)):
        for value in arr:
            tmp = arr[index]
            if value > tmp:
                max_val = value
            else:
                pass
    return max_val

# min
def smallest_arr(arr):
    tmp = 0
    min_val = arr[0]
    for index in range(len(arr)):
        tmp = arr[index]
        for value in arr:
            if tmp <= value and tmp < min_val:
                min_val = value
            else:
                pass
    return min_val




lists1 = [3,2,4,1,5,1]

# def ascending(arr):
#     tmp = 0
#     min_val = arr[0]
#     final_lists = []
#     for index in range(len(arr)):
#         tmp = arr[index]
#         for value in arr:
#             if tmp <= value and tmp < min_val:
#                 min_val = value
#             else:
#                 pass
            
#     return min_val

# print(ascending(lists1))

my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
def ascending(arr):
    new_list = []

    while arr:
        min = arr[0]  
        for x in arr: 
            if x < min:
                min = x
        new_list.append(min)
        arr.remove(min)    

    return new_list

ascending(lists1)


def descending(arr):
    new_list = []

    while arr:
        max = arr[0]
        for x in arr:
            if x < max:
                pass
            else:
                max = x
            
        new_list.append(max)
        arr.remove(max)

    return new_list

print(descending(lists1))































# lists1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lists2 = [2, 4, 4, 5, 6, 7, 8]
# lists3 = [1, 3, 3, 4, 5, 6, 6, 7]
# lists4 = [1,2,3,100,6,5,3,4,7,8,2,4,6,5,7,7,8,3]
# print(mode(lists1))
# print(modian(lists1))
# print(mean(lists1))
# print(q1(lists1))
# print(q1(lists2))
# print(q1(lists3))
# print('=============')
# print(q3(lists1))
# print(q3(lists2))
# print(q3(lists3))


# idx2 = len(lists2)//2
# idx3 = len(lists3)//2
# arr2 = lists2[:idx2-1]
# arr3 = lists3[:idx3-1]

# print('{} & {}'.format(idx2, arr2))
# print('{} & {}'.format(idx3, arr3))
# median = lists2[((len(lists2)+1)//2) - 1]
# idx = lists2.index(median)
# print(median)
# print(idx)
# print(lists1[10:])

# def q1(arr):
#     arr = sorted(arr)
#     amount = len(arr)
#     if amount % 2 == 0:
#         idx = amount//2
#         arr = arr[:idx]  # different here
#         if len(arr) % 2 == 0:
#             num = len(arr)
#             q1 = (arr[(num//2) - 1] + arr[num//2]) / 2
#             return q1
#         else:
#             num = len(arr)
#             q1 = arr[((num+1)//2) - 1]
#             return q1
#     else:
#         median = arr[((amount+1)//2) - 1]
#         idx = arr.index(median)
#         arr = arr[:idx + 1]  # different here
#         if len(arr) % 2 == 0:
#             num = len(arr)
#             q1 = (arr[(num//2) - 1] + arr[num//2]) / 2
#             return q1
#         else:
#             num = len(arr)
#             q1 = arr[((num+1)//2) - 1]
#             return q1


# def q3(arr):
#     arr = sorted(arr)
#     amount = len(arr)
#     if amount % 2 == 0:
#         idx = amount//2
#         arr = arr[idx:]  # different here
#         if len(arr) % 2 == 0:
#             num = len(arr)
#             q3 = (arr[(num//2) - 1] + arr[num//2]) / 2
#             return q3
#         else:
#             num = len(arr)
#             q3 = arr[((num+1)//2) - 1]
#             return q3
#     else:
#         median = arr[((amount+1)//2) - 1]
#         idx = arr.index(median)
#         arr = arr[idx:]  # different here
#         if len(arr) % 2 == 0:
#             num = len(arr)
#             q3 = (arr[(num//2) - 1] + arr[num//2]) / 2
#             return q3
#         else:
#             num = len(arr)
#             q3 = arr[((num+1)//2) - 1]
#             return q3
