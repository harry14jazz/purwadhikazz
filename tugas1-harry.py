''' jawaban no 1
total_hewan = 13
jumlah_kaki = 32
kaki_ayam = 2
kaki_kambing = 4

kambing = 1
ayam = 1

processing_jumlah_ayam = total_hewan - (kaki_ayam+kaki_kambing)//kaki_ayam
processing_jumlah_kambing = total_hewan - processing_jumlah_ayam
print('Andre memiliki ayam {} ekor dan kambing {} ekor'.format(processing_jumlah_ayam, processing_jumlah_kambing))
'''


''' jawaban no 4:

kalimat = input('Masukkan kalimat: ')
processing_kalimat = kalimat.lower()

karakter = input('Masukkan karakter: ')
processing_karakter = karakter.lower()

char_count = processing_kalimat.count(processing_karakter)

print('Jumlah karakter "{}" di dalam kalimat "{}" adalah {}'.format(karakter, kalimat, char_count))
'''

''' jawaban no 5 pakai for
kalimat = input('Masukkan kalimat: ')
karakter = input('Masukkan karakter: ').lower()
for char in kalimat:
    if char in 'aiueoAIUEO':
        if char.isupper() == True:
            upper_karakter = karakter.upper()
            kalimat = kalimat.replace(char, upper_karakter)
        kalimat = kalimat.replace(char, karakter)
print(kalimat)
'''

# ''' jawaban no 5 fix
kalimat = input('Masukkan kalimat: ')
karakter = input('Masukkan karakter: ').lower()
kalimat = kalimat.replace('a', karakter).replace('A', karakter.upper()).replace('i', karakter).replace(
    'I', karakter.upper()).replace('u', karakter).replace('U', karakter.upper()).replace('e', karakter).replace('E', karakter.upper()).replace('o', karakter).replace('O', karakter.upper())
print(kalimat)
# '''

''' jawaban no 3 fix (diskusi di grup wa hehe)
total_usia_sekarang = 50
total_usia_lalu = 42
usia_budi_lalu = total_usia_lalu//7 # '7' datang dari hasil penjumlahan koefisien 6*budi + budi = total_usia_lalu
usia_ayah_lalu = usia_budi_lalu * 6
usia_ayah_skrg = usia_ayah_lalu + 4 # ditambah 4 karena posisi sekarang ada di 4 tahun lalu. jadi tarik lagi kedepan
usia_budi_skrg = usia_budi_lalu + 4 # sama seperti di atas

print(f'Usia ayah saat ini adalah {usia_ayah_skrg} tahun dan usia budi saat ini adalah {usia_budi_skrg} tahun')
'''

''' jawaban no 2
usia_ibu_lalu = 30
usia_anak_lalu = 10
usia_ibu_skrg = 49
usia_anak_skrg = 26
usia_ibu_melahirkan = usia_ibu_skrg - usia_anak_skrg
print('Umur Ibu ketika melahirkan anaknya adalah {}'.format(usia_ibu_melahirkan))
'''
