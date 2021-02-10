'''
1.
Input:
Masukkan jumlah hari: ....
Output:
Nyatakan jumlah hari tsb dalam
....Tahun ... bulan ... minggu ... hari

contoh:
masukkan jumlah hari: 35
output:
00 tahun 01 bulan 00 minggu 05 hari

Ketentuan:
- format output dalam format 2 digit
- 1 tahun = 365 hari
- 1 bulan = 30 hari
- Jumlah hari maksimal 4000 == > jika diatas 4000 keluar notif: Jumlah hari diatas batas
- Jumlah hari tidak bisa menerima nilai dibawah 0 == > Jumlah hari dibawah batas
- Jumlah hari tidak bisa menerima String, atau Angka desimal == > keluar notif: Jumlah hari yg anda masukkan Salah
'''

''' Jawaban no 1
tahun, bulan, minggu, hari = 0, 0, 0, 0
sisa_tahun, sisa_bulan, sisa_minggu, sisa_hari = 0, 0, 0, 0

try:
    h = int(input('Masukkan jumlah hari: '))
    
    if 0 < h < 4000:
        if h >= 365:
            # cari sisa hari modulus tahun
            sisa_tahun = h % 365
            if sisa_tahun == 0:
                tahun = h//365  # sampai sini kita dapat tahun
            else:
                tahun = h//365  # sampai sini kita dapat tahun
                if sisa_tahun > 30:
                    bulan = sisa_tahun//30 # dapat bulan
                else:
                    bulan = 1 # dapat bulan
                    
                sisa_bulan = sisa_tahun % 30 # hitung sisa hari setelah menghitung bulan
                
                if sisa_bulan >= 7:
                    minggu = sisa_bulan//7 # dapet minggu
                    sisa_minggu = sisa_bulan % 7 # hitung sisa hari setelah menghitung minggu
                    hari = sisa_minggu # dapat hari
                else:
                    minggu = 0 # dapat minggu
                    hari = sisa_bulan
        else:
            tahun = 0
            sisa_bulan = h % 30
            if sisa_bulan == 0:
                bulan = h//30
                minggu = sisa_bulan//7
                sisa_minggu = sisa_bulan % 7
                hari = sisa_minggu
            else:
                bulan = h//30
                minggu = sisa_bulan//7
                sisa_minggu = sisa_bulan % 7

                if sisa_minggu == 0:
                    hari = 0
                else:
                    hari = sisa_minggu

        print(f'{tahun:02} tahun, {bulan:02} bulan, {minggu:02} minggu ,{hari:02} hari')
    elif h < 0:
        print('Jumlah hari di bawah batas')
    else:
        print('Jumlah hari di atas batas')
except ValueError:
    print('Jumlah hari yang anda masukkan salah')

'''


'''
2.
Hitung BMI(Body Mass Index)
Rumus BMI: massa(kg) / tinggi(dalam meter) pangkat 2

Input:
Masukkan Tinggi badan(dalam cm):
Masukkan Berat badan(dalam kg):

Output nya:
Tinggi badan anda ... (meter) dan Berat anda ...kg BMI anda ....(nilai BMI)... dan anda termasuk ...(sesuai kondisi)

Kondisi:
BMI < 18.5 == > Berat badan Kurang
18.5 - 24.9 = > Berat badan ideal
25 - 29.9 = > Berat badan berlebih
30 - 39.9 = > Berat badan sangat berlebih
BMI >= 40 = > Obesitas

Ketentuan:
- nilai BMI pada output, dibulatkan 2 angka desimal.
- nilai tinggi dan massa tidak menerima angka negatif == > keluar notif "Tidak menerima angka Negatif"
- Inputan tidak menerima desimal atau string == > keluar notif "Angka yg anda masukkan salah"
- Batas maksimal tinggi badan: 300cm, batas maksimal berat badan: 250kg == > keluar notif "Tinggi / Berat badan anda di atas Batas"
- Notifikasi Keluar setelah user input tinggi dan berat.
'''

''' jawaban no 2    
try:
    tinggi_input = input('Masukkan Tinggi badan(dalam cm): ')
    massa_input = input('Masukkan Berat badan(dalam kg): ')
    tinggi_checking = tinggi_input.isdigit()
    massa_checking = massa_input.isdigit()
    
    tinggi_cm = int(tinggi_input)
    tinggi = tinggi_cm/100
    massa = int(massa_input)
    
    if tinggi_checking and massa_checking:
        if tinggi > 3 or massa > 250:
            print('Tinggi / Berat badan anda di atas Batas')
        else:
            mbi = round(massa/pow(tinggi, 2), 2)
            if mbi < 18.5:
                kondisi = 'Berat badan Kurang'
            elif 18.5 <= mbi < 24.9:
                kondisi = 'Berat badan ideal'
            elif 25 <= mbi < 29.9:
                kondisi = 'Berat badan berlebih'
            elif 30 <= mbi < 39.9:
                kondisi = 'Berat badan sangat sangat berlebih'
            else:
                kondisi = 'Obesitas'
            print(f'Tinggi badan anda {tinggi} meter dan Berat anda {massa}kg BMI anda {mbi} dan anda termasuk {kondisi}')
            
    elif tinggi_cm < 0 or massa < 0:
        print('Tidak menerima angka Negatif')
except:
    print('Angka yg anda masukkan salah')
#'''

'''
3.
Input:
Masukkan Nilai: ...

Ouput:
Nilai anda .... dan anda .... (sesuai kondisi)

Kondisi:
90 keatas: Grade A
85 keatas: Grade A-
80 keatas: Grade B
75 keatas: Grade B-
70 keatas: Grade C
65 keatas: Grade D
dibawah 65 dan di atas 40: Perlu REMEDIAL
dibawah 40: TIDAK LULUS

Ketentuan:
- Nilai maksimum 100, nilai minimum 0
- Jika nilai diatas 100: Nilai diluar jangkauan
- Jika nilai dibawah 0: Tidak menerima angka negatif
- Jika nilai bukan angka: Angka yg anda masukkan Salah
- Dapat menerima nilai desimal
'''

''' jawaban no 3
try:
    nilai = input('Masukkan Nilai: ')
    value = round(float(nilai))
    #value = round(value)
    #print(type(value))
    if value >= 0:
        if value > 100:
           print('Nilai diluar jangkauan') 
        elif 90 <= value <= 100:
            print(f'Nilai anda {nilai} dan anda Grade A')
        elif 85 <= value < 90:
            print(f'Nilai anda {nilai} dan anda Grade A-')
        elif 80 <= value < 85:
            print(f'Nilai anda {nilai} dan anda Grade B')
        elif 75 <= value < 80:
            print(f'Nilai anda {nilai} dan anda Grade B-')
        elif 70 <= value < 75:
            print(f'Nilai anda {nilai} dan anda Grade C')
        elif 65 <= value < 70:
            print(f'Nilai anda {nilai} dan anda Grade D')
        elif 40 <= value < 65:
            print(f'Nilai anda {nilai} dan anda Perlu Remedial')
        elif 0 <= value < 40:
            print(f'Nilai anda {nilai} dan anda Tidak Lulus')
    elif value < 0:
        print('Tidak menerima angka negatif')
except:
    print('Angka yg anda masukkan salah')

'''


# coret-coret


# '''
# try:
#     nilai = input('Masukkan Nilai: ')
#     nilai_checking = nilai.isdigit()
#     value = float(nilai)
#     if nilai_checking:
#         if 90 <= value < 100:
#             print('a')
#         elif 85 <= value < 90:
#             print('b')
#         elif 80 <= value < 85:
#             print('c')
#         elif 75 <= value < 80:
#             print('d')
#         elif 70 <= value < 75:
#             print('e')
#         elif 65 <= value < 70:
#             print('f')
#         elif 40 <= value < 65:
#             print('Perlu Remedial')
#         else:
#             print('Tidak Lulus')
#     elif value < 0:
#         print('Tidak menerima angka negatif')
# except:
#     print('Angka yg anda masukkan salah')
# '''

#     if tinggi_checking != True or massa_checking != True:
#         raise ValueError
#     else:
#         tinggi_cm = int(tinggi_input)
#         tinggi = tinggi_cm/100
#         massa = int(massa_input)
#         # if 0 >= tinggi_cm > 300 or 0 > massa > 250:
#         #     raise ValueError

#         if tinggi_cm < 0 or massa < 0:
#             print('Tidak menerima angka Negatif')
#         elif tinggi_cm > 300 or massa > 250:
#             print('Tinggi / Berat badan anda di atas Batas')

#         bmi = massa / pow(tinggi, 2)
#         print(bmi)

# except ValueError:
#     print('Angka yg anda masukkan salah')

# try:
#     tinggi_cm = int(tinggi_input)
#     tinggi = tinggi_cm/100
#     massa = int(massa_input)

#     if 0 >= tinggi_cm > 300 or 0 > massa > 250:
#         raise ValueError

# except ValueError:
#     if tinggi_cm < 0 or massa < 0:
#         print('Tidak menerima angka Negatif')
#     elif tinggi_cm > 300 or massa > 250:
#         print('Tinggi / Berat badan anda di atas Batas')
# tinggi_cm2 = int(tinggi_cm)
# tinggi = tinggi_cm2/100
# massa = int(massa_input)

# if tinggi < 0 and massa < 0:
#     print('Tidak menerima angka Negatif')
# elif tinggi > 300 or massa > 250:
#     print('Tinggi / Berat badan anda di atas Batas')
# else:
#     print('Seluruh inputan bener')


'''
nilai = 85.0
if nilai in range(90.0, 100.0):
    print('yes')
'''
