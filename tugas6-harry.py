'''# Jawaban no 1
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']


hari_input = input('Masukkan nama hari: ')

try:
    angka_input = int(input('Masukkan jumlah hari: '))
    
    day = hari_input.title()
    if day not in hari:
        print('Tidak ada nama hari/ Nama hari yg anda masukkan salah')
    else:
        index_hari = hari.index(day)
        new_list_hari = hari[index_hari::]
        for value in hari:
            if value not in new_list_hari:
                new_list_hari.append(value)
            else:
                continue

        expected_day = new_list_hari[angka_input % 7]
        print(
            f'Hari ini hari {day}, {angka_input} hari lagi adalah hari {expected_day} ')
except:
    print('Jumlah tidak bisa desimal maupun string\n')
'''


'''# Jawaban no 2
sentence = input('Masukkan Kalimat: ')
split1 = sentence.split()
status = True
for value in split1:
    for char in value:
        if char.isalpha() == False:
            print('Hanya menerima data bertipe Full String')
            status = False
            break
if status == True:
    sentence_list = sentence.split(" ")
    new_sentence = []
    for value in sentence_list:
        new_sentence.append(value[::-1])
            
    final_sentence = ' '.join(new_sentence)
    print(f'Output: {final_sentence}')
else:
    quit()
'''

# Jawaban no 3
sentence = input('Masukkan kata: ')

sentence_process = sentence.lower()
if sentence_process.isalpha() == True:
    checker_word = sentence_process[::-1]
    if checker_word == sentence_process:
        print(f'Kata tesebut ({sentence}) merupakan Palindrome')
    else:
        print(f'Kata tesebut ({sentence}) bukan Palindrome')
else:
    print('Hanya menerima String')

