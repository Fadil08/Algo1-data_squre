import datetime
import os
import json
import datetime

file_data = 'Transaksi.json'
databases = []


def clear():
    print ('\n')
    input ('Tekan enter untuk kembali ke menu utama!!!')
    #menu_utama()

def tambah_data():
    os.system('cls')
    show()
    nama = input ("Barang: ")
    jumlah = int (input("Jumlah: " ))
    harga = int (input("Harga: " ))
    item = ({"Barang": nama,
            "Jumlah": jumlah,
            "Harga": harga})
    databases.append(item)
    with open(file_data, 'w') as output:
            output.write(json.dumps(databases, indent=4))
    os.system('cls')


def parsing():
    with open(file_data, 'w') as output:
            output.write(json.dumps(databases, indent=1))


def kembali():
    with open(file_data,'r') as output:
        data = json.load(output)
        return data

def edit():
    with open (file_data,'w') as output:
        data = json.load(output)
        return data

def show():
    os.system('cls')
    datum = kembali()
    print ('List Daftar Obat '.center(40))
    print ('='*40)
    print ('|%-3s|%-10s   |%-5s  |%-8s  |'%('#',"Barang","Jumlah","Harga"))
    print ('='*40)
    for indek in range (len(datum)):
        print ('|%-3s|%-10s   |%-5s  | %-8s  |'%(indek, datum[indek]["Barang"],datum[indek]["Jumlah"], datum[indek]["Harga"]))
        
def menghapus():
    os.system('cls')
    show()
    kembali()
    hapus = int(input('masukkan indek yang akan di hapus: '))
    databases.pop(hapus)
    parsing()
    os.system('cls')
    show()
rekap_pembelian= []
def penjualan():
    os.system('cls')
    show()
    data = []
    datum = kembali()
    for i in datum:
        data.append(i)
    print ('Obat yang di Beli'.center(40))
    obat  = input('indeks obat yang di beli: ')
    jumlah = int(input('Banyak obat: '))
    bayar = int(input ('Nominal Pembayaran: '))
    for x in data :
        if x["Barang"] == obat:
            x ["Jumlah"] = ( int(x["Jumlah"]) - jumlah)
            total = int(x["Harga"]) * jumlah
            kembalian = bayar - total
            rekap_pembelian.append({"Barang" : x["Barang"],"Jumlah": jumlah,"Harga":x["Harga"],"total harga": total,"Uang": bayar, "Kembalian": kembalian})
            with open(file_data, 'w') as output:
                output.write(json.dumps(data, indent=4))
            


def rekap_pembayaran():
    os.system('cls')
    for i in  rekap_pembelian:
        print ('Slip Pembayaran'.center(40))
        print ('='*40)
        today = datetime.date.today()
        tanggal = today.strftime('%d-%m-%Y')
        print ('Tanggal           :\t',tanggal)
        print ('nama Barang       :\t',  i["Barang"])
        print ('Jumlah barang     :\t',i ["Jumlah"] )
        print ('Harga per pack    :\t', i["Harga"])
        print ('Nominal Pembayaran:\t', i ["Uang"])
        print ('Total Harga       :\t', i["total harga"])
        print ('Nominal Kembalian :\t', i["Kembalian"])
        print ('='*40)
        print('Terimakasih dan selamat Berbelanja Kembali')
        print ('='*40)
        break
def lis_menu ():
    daftar = ("""
            1. \t Tambah barang
            2. \t penjualan barang
            3. \t melihat data
            4. \t menghapus barang 
             """)
    print (daftar)


def menu_utama():
    while True:
        clear()
        lis_menu()
        menu = int(input('masukkan menu yang kalian pilih: '))
        if menu == 1:
            tambah_data()
        elif menu == 2:
            penjualan()
            rekap_pembayaran()
        elif menu == 3:
            show()
        elif menu == 4:
            menghapus()
        elif menu == 5:
            print (rekap_pembelian)
            break
        else:
            print ('Mohon maaf Menu Tersebut Tidak Tersedia!!!')


simpan_login = []
while True:
    print ('menu \n 1. login \n da')
    menu = int(input ('pilih menu yang kalian pilih [1] or [2]: '))
    if menu == 1:
        data_login = {'admin': '123'}
        login = input ('masukkan username: ')
        passwd = input ('masukkan password: ')
        for i in data_login:
            if login in i:
                if passwd in data_login[i]:
                        print ('anda berhasil login')
                        menu_utama()
                else:
                        print ('coba lagi')
            else:
                    continue
    if menu == 2:
        nama = input('masukkan nama anda: ')
        nim = input ('masukkan nim anda: ')
        user = input ('masukkan username yang anda inginkan: ')
        pasword  = input ('masukkan password yang anda inginkan: ')
        simpan_login.append({nama : nim, user :pasword})
        print ("anda Berhasil melakukan Registrasi")
        print (simpan_login)
        continue
    
