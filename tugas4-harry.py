# a = int(9853)
# dua_angka_belakang = a%100
# dua_angka_depan_ribuan = a - dua_angka_belakang
# dua_angka_depan = dua_angka_depan_ribuan//100
# dua_angka_belakang_ribuan = dua_angka_belakang * 100
# final_output = dua_angka_belakang_ribuan + dua_angka_depan
#print(final_output)

'''# jawaban no 1
try:
    number = int(input('Masukkan 4 digit angka: '))
    if number < 0:
        print('Tidak menerima angka negatif')
    elif number <= 999 or number > 9999:
        print('Hanya menerima angka 4 digit')
    else:
        dua_angka_belakang = number % 100
        dua_angka_depan_ribuan = number - dua_angka_belakang
        dua_angka_depan = dua_angka_depan_ribuan//100
        dua_angka_belakang_ribuan = dua_angka_belakang * 100
        final_output = dua_angka_belakang_ribuan + dua_angka_depan
        print(final_output,'\n')
        data_type = type(final_output)
        print(f'Tipe data {final_output} adalah: {data_type}')
except:
    print('Tidak menerima string atau desimal')
'''

# jawaban no 2
try:
    number1 = int(input('Masukkan 2 digit angka pertama: '))
    number2 = int(input('Masukkan 2 digit angka kedua: '))
    if number1 < 0 or number2 < 0:
        print('Tidak menerima angka negatif')
    elif (number1 <= 9 or number1 > 99) or (number2 <= 9 or number2 > 99):
        print('Hanya menerima angka 2 digit')
    else:
        dua_angka_depan_ribuan = number1*100
        final_output = dua_angka_depan_ribuan + number2
        data_type = type(final_output)
        print(f'Tipe data {final_output} adalah: {data_type}')
except:
    print('Tidak menerima string atau desimal')
