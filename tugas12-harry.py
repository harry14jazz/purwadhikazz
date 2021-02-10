def email_checker(email):
    # cek @
    counter_at = email.count('@')
    if counter_at != 1:
        return 'Format Email Salah'
    else:
        email_split = email.split('@')
        username = email_split[0]
        hosting = email_split[1]

        # cek username & hosting
        if len(hosting) == 0 or len(username) == 0:
            return 'Format Email Salah'
        else:
            username_checker = str(username)
            first_char = username_checker[0]
            forbiden_char = ['!', '#', '@', '$', '%', '^', '&', '*',
                             '(', ')', '+', '-', '=', '{', '}', '[', ']', '<', '>', '?', '/', ' ']

            forbiden_char_ext = ['!', '#', '@', '$', '%', '^', '&', '*',
                                 '(', ')', '+', '-', '=', '{', '}', '[', ']', '<', '>', '?', '/', ' ', '_']

            # cek username sampai tuntas
            for char in username_checker:
                if char in forbiden_char:
                    return 'Format Username yg anda masukkan salah'
                    break
            else:
                if not first_char.isalnum():
                    return 'Format Username yg anda masukkan salah'
                else:
                    # sampai sini berarti username aman

                    # cek hosting apakah ada forbiden char
                    for char_hosting in hosting:
                        if char_hosting in forbiden_char_ext:
                            return 'Format Hosting yg anda masukkan Salah'
                            break
                    else:
                        # cek dot hosting
                        hosting_split = hosting.split('.')

                        # cek format hosting
                        if len(hosting_split) > 3:
                            return 'Format Hosting yg anda masukkan Salah'

                        elif len(hosting_split) == 3:
                            hosting_check = hosting_split[0]
                            extension1 = hosting_split[1]
                            extension2 = hosting_split[2]

                            # cek kehadiran hosting dan format extension
                            if not extension1.isalpha() or len(extension1) > 5:
                                return 'Format Ekstensi yg anda masukkan Salah'
                            elif not extension2.isalpha() or len(extension2) > 5:
                                return 'Format Ekstensi yg anda masukkan Salah'
                            elif len(hosting_check) == 0:
                                return 'Format Email Salah'
                        elif len(hosting_split) == 2:
                            # cek kehadiran hosting dan format extension
                            hosting_check = hosting_split[0]
                            extension1 = hosting_split[1]

                            if not extension1.isalpha() or len(extension1) > 5:
                                return 'Format Ekstensi yg anda masukkan Salah'
                            elif len(hosting_check) == 0:
                                return 'Format Ekstensi yg anda masukkan Salah'
                        else:
                            return 'Format Ekstensi yg anda masukkan Salah'

                        # kalo sampe sini sudah berarti aman
                        return ' Alamat Email yg anda Masukkan: ('+email+') sudah Valid!'


# Main Program #
email_input = input('Masukkan email: ')
print(email_checker(email_input))
