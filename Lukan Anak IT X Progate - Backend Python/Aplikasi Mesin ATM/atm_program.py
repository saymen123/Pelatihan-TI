import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input('Masukkan pin Anda: '))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin Anda salah, silakan masukkan lagi: '))
        trial += 1

        if trial == 3:
            print('Error, silakan ambil kartu dan coba lagi ...')
            exit()
    
    while True:
        print('Selamat datang di ATM Bersama')
        print('\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar')
        selectmenu = int(input('\nSilakan pilih menu: '))

        # menu 1: Cek Saldo
        if selectmenu == 1:
            print('\nSaldo Anda sekarang: Rp. ' + str(atm.checkBalance()) + '\n')

        # menu 2: Debet
        elif selectmenu == 2:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_withdraw = input('Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n ' + 
            str(nominal) + ' ')
            if verify_withdraw == 'y':
                print('Saldo awal Anda adalah: Rp. ' + str(atm.checkBalance()) + '')
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print('Transaksi debet berhasil!')
                print('Saldo sisa sekarang: Rp. ' + str(atm.checkBalance()) + '')
            else:
                print('Maaf, saldo Anda tidak cukup untuk melakukan debet :(')
                print('Silakan lakukan penambahan nominal saldo')

        # menu 3: Simpan
        elif selectmenu == 3:
            nominal = float(input('Masukkan nominal saldo: '))
            verify_deposit = input('Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n ' + 
            str(nominal) + '')

            if verify_deposit == 'y':
                atm.depositBalance(nominal)
                print('Saldo Anda sekarang adalah: Rp. ' + str(atm.checkBalance()) + '\n' )
            else:
                break

        # menu 4: Ganti Pin
        elif selectmenu == 4:
            verify_pin = int(input('Masukkan pin Anda: '))

            while verify_pin != int(atm.checkPin()):
                print('Pin Anda salah, silakan masukkan pin: ')
            
            updated_pin = int(input('Silakan masukkan pin baru: '))
            print('Pin Anda berhasil diganti!')

            verify_newpin = int(input('Coba masukkan pin baru: '))

            if verify_newpin == updated_pin:
                print('Pin baru Anda sukses!')
            else:
                print('Maaf, pin Anda salah :(')

        # menu 5: Keluar
        elif selectmenu == 5:
            print('Resi tercetak otomatis saat Anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi Anda.')
            print('No. Record: ', random.randint(100000, 1000000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBalance())
            print('Terima kasih telah menggunakan ATM Bersama :)')
            exit()
        else:
            print('Error. Maaf, menu tidak tersedia :(')