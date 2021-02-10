'''
hari = {
    'Senin': 'Monday',
    'Selasa': 'Tuesday',
    'Rabu': 'Wednesday',
    'Kamis': 'Thursday',
    'Jumat': 'Friday',
    'Sabtu': 'Saturday',
    'Minggu': 'Sunday',
}

try:
    list_hari = []
    hari_input = input('Masukkan Nama Hari: ').capitalize()

    if hari_input.isalpha() != True:
        raise ValueError
    else:
        for items in hari.items():
            list_hari.append(items)
            
        if hari_input in hari.keys():
            print(
                'Hari yg anda pilih {} dalam bahasa inggris adalah {}'.format(hari_input, hari[hari_input]))
        else:
            for value in list_hari:
                if hari_input in value:
                    print(
                        'The Day that you choose is {} in Bahasa is {}'.format(hari_input, value[0]))
                    break
            else:
                print('Nda bisa bahasa enggres')
except ValueError:
    print('Tidak menerima Integer atau Float')
'''

'''
morse = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

list_morse = []

for items in morse.items():
    list_morse.append(items)

word = input('Masukkan kata/sandi: ')
for char in word:    
    if char in '!@#$%^&*()><?:[]':
        print('nda bisa basa enggres')
        break
else:
    if word.isalnum() or word.isalpha():
        print('[word to morse]')
        word = word.lower()
        morse_convert = []
        for char in word:        
            morse_convert.append(morse[char])
        
        final_convert = '|'.join(morse_convert)
        print('Kata yg anda masukkan adalah ({}) Jika diubah menjadi Kode Morse Menjadi: {}'.format(word, final_convert))
    else:
        reverse_morse = []
        for i, j in morse.items():
            reverse_morse.append((j, i))

        new_morse = dict(reverse_morse)
        
        morse_split = word.split('|')
        new_sentence = []
        for value in morse_split:
            if value in morse.values():
                new_sentence.append(new_morse[value])
        
        final_convert = ''.join(new_sentence)
        print('Kode Morse yg anda masukkan {} jika diubah menjadi kata-kata menjadi: {}'.format(word, final_convert.capitalize()))
'''

'''
genap = []
ganjil = []
negatif = []
prima = []
komposit = []

for i in range(1,101):
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)

for i in range(-1, -100, -1):
    negatif.append(i)

for i in range(2,101):
    for y in range(2, i):
        if i % y == 0:
            break
    else:
        prima.append(i)

for i in range(2,101):
    if i not in prima:
        komposit.append(i)
    else:
        continue

set_genap = set(genap)
set_ganjil = set(ganjil)
set_negatif = set(negatif)
set_prima = set(prima)
set_komposit = set(komposit)

print('a. A u B u C u D u E')
print('{}'.format(set_genap|set_ganjil|set_ganjil|set_prima|set_komposit))
print('-'*100)
print('b. (A n B) u (D n E)')
print('{}'.format((set_genap & set_ganjil) | (set_prima & set_komposit)))
print('-'*100)
print('c. (A u B) n (D u E)')
print('{}'.format((set_genap | set_ganjil) & (set_prima | set_komposit)))
print('-'*100)
print('d. (A u B) - (D u E)')
print('{}'.format((set_genap | set_ganjil) - (set_prima | set_komposit)))
print('-'*100)
print('e. (A u B u C) - (A n E)')
print('{}'.format((set_genap | set_ganjil | set_negatif) - (set_genap & set_komposit)))
'''

#################################### tes tes no 2 ##################################################


morse = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '........',
    '.........': ' '
}

list_morse = []

for items in morse.items():
    list_morse.append(items)

try:
    word = input('Masukkan Kalimat / Sandi Morse: ')
    if '|' in word:
        reverse_morse = []
        for i, j in morse.items():
            reverse_morse.append((j, i))

        new_morse = dict(reverse_morse)

        morse_split = word.split('|')
        new_sentence = []
        for value in morse_split:
            if value in morse.values():
                new_sentence.append(new_morse[value])

        final_convert = ''.join(new_sentence)
        print('Kode Morse yg anda masukkan {} jika diubah menjadi kata-kata menjadi: {}'.format(
            word, final_convert.capitalize()))
    else:
        word_process = word.split(' ')
        for value in word_process:
            if '.' in value:
                print('ndabisa float')
                break
        else:
            morse_convert = []
            for word_value in word_process:
                word_value = word_value.lower()
                for char in word_value:
                    morse_convert.append(morse[char])

            final_convert = '|'.join(morse_convert)
            print('Kata yg anda masukkan adalah ({}) Jika diubah menjadi Kode Morse Menjadi: {}'.format(
                word, final_convert))
except:
    print('nda bisa basa enggres')



