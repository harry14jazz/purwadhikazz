import string

'''# jawaban no 1
def tambah(num1, num2):
    if '.' in num1 or '.' in num2:    
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = int(num1)
        num2 = int(num2)
        
    result = 'Hasil dari {} + {} = {}'.format(num1, num2, num1+num2)
    return result


def kurang(num1, num2):
    if '.' in num1 or '.' in num2:
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = int(num1)
        num2 = int(num2)
        
    result = 'Hasil dari {} - {} = {}'.format(num1, num2, num1-num2)
    return result


def bagi(num1, num2):
    if '.' in num1 or '.' in num2:    
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = int(num1)
        num2 = int(num2)
        
    result = 'Hasil dari {} / {} = {}'.format(num1, num2, num1/num2)
    return result


def kali(num1, num2):
    if '.' in num1 or '.' in num2:    
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = int(num1)
        num2 = int(num2)
        
    result = 'Hasil dari {} * {} = {}'.format(num1, num2, num1*num2)
    return result


# Main Program
try:
    angka1 = input('Masukkan Angka 1: ')
    angka2 = input('Masukkan Angka 2: ')
    operator = input('Masukkan Operator: ')
    
    if operator == '+':
        print(tambah(angka1, angka2))
    elif operator == '-':
        print(kurang(angka1, angka2))
    elif operator == '/':
        print(bagi(angka1, angka2))
    elif operator == '*':
        print(kali(angka1, angka2))
    else:
        print('Operator yang dimasukkan tidak ada')

except:
    print('Tipe Data yang dimasukkan salah')
'''

# jawaban no 2
alphabet = list(string.ascii_lowercase)


def caesar_cipher(word, num):
    new_word = []
    final_word = []

    if word.isalpha():

        for char in word:
            new_word.append(str(char))

        for new_char in new_word:
            char_idx = alphabet.index(new_char)
            new_alpha = alphabet[(char_idx + num) % 26]

            final_word.append(new_alpha)

        result = ''.join(final_word)
        return result
    else:
        return 'Kata hanya boleh String'


# Main Program
try:
    kata = input('Masukkan Kata: ')
    angka = int(input('Masukkan Angka: '))

    print(caesar_cipher(kata, angka))
except:
    print('Tipe Data yang dimasukkan salah')


# coret 2
# huruf = str(alphabet[7])
# rubahan = huruf.replace(huruf, alphabet[(7+2) % 26])
# print(huruf, rubahan)


# alphabet = list(string.ascii_lowercase)


# def caesar_cipher(word, num):
#     result_word = []
#     word_split = word.split(' ')

#     for word1 in word_split:
#         new_word = []

#         for char in word1:
#             new_word.append(str(char))

#             final_word = []
#             for new_char in new_word:
#                 char_idx = alphabet.index(new_char)
#                 new_alpha = alphabet[(char_idx + num) % 26]

#                 final_word.append(new_alpha)
#             result = ''.join(final_word)

#         result_word.append(result)
#     sentence = ' '.join(result_word)
#     return sentence


# # Main Program
# try:
#     kata = input('Masukkan Kata: ')
#     angka = int(input('Masukkan Angka: '))

#     print(caesar_cipher(kata, angka))
# except:
#     print('Tipe Data yang dimasukkan salah')
