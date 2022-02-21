# Data Pasien Rumah Sakit Purwadhika!
pasien = [{'NOMOR PASIEN':'RI1', 'NAMA PASIEN' : 'ARDI', 'ALAMAT' : 'JAKARTA','JENIS KELAMIN':'L', 'STATUS PERAWATAN':'RAWAT INAP'}, 
{'NOMOR PASIEN': 'RJ1', 'NAMA PASIEN' : 'INTAN', 'ALAMAT':'DEPOK', 'JENIS KELAMIN':'P', 'STATUS PERAWATAN':'RAWAT JALAN'}]

# 1. Read Data
def Read_Data():
    read = True
    while read != '3':
        print('''\n====Data Pasien Rumah Sakit Purwadhika====\n
Pilihan Menu:
1. Tampilkan Seluruh Data Pasien
2. Mencari Data Pasien
3. Kembali Ke Menu Utama
==========================================''')
        read = input("Silahkan Pilih Nomor [1-3]: ")
        if read == '1':
                if len(pasien) != 0 :
                        print("==========================================")
                        print('\nDAFTAR PASIEN RUMAH SAKIT PURWADHIKA: ')
                        for j, i in enumerate(pasien):
                                print(f"{j+1}. NOMOR PASIEN : {i['NOMOR PASIEN']}, NAMA PASIEN : {i['NAMA PASIEN']}, JENIS KELAMIN : {i['JENIS KELAMIN']}, ALAMAT : {i['ALAMAT']}, STATUS PERAWATAN : {i['STATUS PERAWATAN']}")
                else:
                        print('\nNomor Pasien Belum Ditambahkan!')
                continue
        elif read =='2':
                if len(pasien) !=0 :
                        print("==========================================")
                        psn = input('Masukkan Nomor Pasien: ')
                        print(f"\nData Pasien dengan Nomor Pasien : {psn}")
                        for j, i in enumerate(pasien):
                                if i ['NOMOR PASIEN'] == psn :
                                        print(f"{j+1}. NAMA PASIEN : {i['NAMA PASIEN']}, JENIS KELAMIN : {i['JENIS KELAMIN']}, ALAMAT : {i['ALAMAT']}, STATUS PERAWATAN : {i['STATUS PERAWATAN']}")
                                        break
                        else:
                                print('\nNomor Pasien Belum Ditambahkan!')
                else:
                        print('\nNomor Pasien Belum Ditambahkan!')
        elif read == '3':
                break
        else:
                print('\nError!, Silahkan Pilih Nomor [1-3]')
                
# 2. Menambahkan Data Pasien    
def Menambahkan_Data():
        add = True
        while add != '2':
                print('''\n========Menambahkan Data Pasien========\n
Pilihan Menu:
1. Tambah Data Pasien
2. Kembali Ke Menu Utama
=======================================''')
                add = input("Silahkan Pilih Nomor [1-2]: ")
                if add == '1':
                        addNomorPasien = str(input('\nMasukan Nomor Pasien: '))
                        allKey = [pasien[i]["NOMOR PASIEN"] for i in range(len(pasien))]
                        if addNomorPasien in allKey:
                                print('Nomor Pasien Sudah Ada!')
                        else:
                                addNama = input('Masukan Nama Pasien: ')
                                addGender = input('Masukan Jenis Kelamin Pasien: ')
                                addALAMAT = input('Masukan Alamat Pasien: ')
                                addStatus = input('Masukan Status Perawatan: ')
                                while True: 
                                        addConfirm = input('Apakah data akan disimpan? (Y/N)')
                                        if addConfirm == 'Y'or addConfirm == 'y':
                                                if addConfirm == 'Y':
                                                        pasien.append({
                                                'NOMOR PASIEN': addNomorPasien.upper(),
                                                'NAMA PASIEN': addNama.upper(),
                                                'JENIS KELAMIN': addGender.upper(),
                                                'ALAMAT': addALAMAT.upper(),
                                                'STATUS PERAWATAN': addStatus.upper()
                                                })
                                                print('\nData Pasien Berhasil Tersimpan!')
                                                break
                                        elif addConfirm == 'N'or addConfirm == 'n' :
                                                print('\nData Pasien Tidak Tersimpan')
                                                break
                elif add == '2':
                        break
                else:
                        print('\nError!, Silahkan Pilih Nomor [1-2]') 
                                           
# 3. Mengubah Data Pasien                       
def Mengubah_Data():
        change = True
        while change != '2':
                print('''\n========Mengubah Data Pasien========\n
Pilihan Menu:
1. Ubah Data Pasien
2. Kembali Ke Menu Utama
====================================''')
                change = input("Silahkan Pilih Nomor [1-2]: ")
                if change == '1':
                        if len(pasien) != 0 :
                                nomorPasien = input('\nMasukan Nomor Pasien yang ingin diubah : ')
                                print('\nData Nomor Pasien : {}\n'.format(nomorPasien).upper())
                                print('NO\t|NOMOR PASIEN\t|NAMA PASIEN\t|JENIS KELAMIN\t|ALAMAT                         \t|STATUS PERAWATAN')
                                for j,i in enumerate(pasien) :
                                        if i['NOMOR PASIEN'] == nomorPasien:
                                                print(f"{j+1}\t|{i['NOMOR PASIEN']}     \t|{i['NAMA PASIEN']}   \t|{i['JENIS KELAMIN']}          \t|{i['ALAMAT']}                               \t|{i['STATUS PERAWATAN']}")
                                                break
                                else:
                                        print('\nPasien Belum Terdaftar!')
                                        continue  
                                while True:
                                        ubahData1 = input('Anda Yakin Data Akan Diubah? [Y/N] : ')
                                        if ubahData1 == 'Y' or ubahData1 == 'y':
                                                ubahKolom = input('\ninput kolom data yang ingin diubah : '.upper())
                                                kolomBaru = input('Input data {} baru : '.format(ubahKolom).upper())
                                                if ubahKolom == 'NOMOR PASIEN':
                                                        i['NOMOR PASIEN'] = kolomBaru.upper()
                                                elif ubahKolom == 'NAMA PASIEN':
                                                        i['NAMA PASIEN'] = kolomBaru.upper()
                                                elif ubahKolom == 'JENIS KELAMIN':
                                                        i['JENIS KELAMIN'] == kolomBaru.upper()
                                                elif ubahKolom == 'ALAMAT':
                                                        i['ALAMAT'] = kolomBaru.upper()
                                                elif ubahKolom == 'STATUS PERAWATAN':
                                                        i['STATUS PERAWATAN'] = kolomBaru.upper()
                                                else:
                                                        print('\nkolom tidak tersedia!')
                                                        break
                                                print('\nData Berhasil Diubah!')
                                                break
                                        elif ubahData1 == 'N' or ubahData1 == 'n':
                                                print('\nData Tidak Diubah')
                                                break
                        else :
                                print('\nData Pasien Tidak Ditemukan!')
                elif change == '2':
                        break
                else:
                        print('\nError!, Silahkan Pilih Nomor [1-2]')
        return
                
             
# 4. Menghapus Data Pasien
def Menghapus_Data():
        remove = True
        while remove != '2':
                print('''\n======Menghapus Data Pasien======\n
Pilihan Menu:
1. Hapus Data Pasien
2. Kembali Ke Menu Utama
=================================''')
                remove = input("Silahkan Pilih Nomor [1-2]: ")
                if remove == '1':
                        if len(pasien) != 0 :
                                nomorPasien = input('\nMasukan Nomor Pasien yang ingin Hapus : ')
                                print('\nData Nomor Pasien : {}\n'.format(nomorPasien).upper())
                                print('NO\t|NOMOR PASIEN\t|NAMA PASIEN\t|JENIS KELAMIN\t|ALAMAT                         \t|STATUS PERAWATAN')
                                for j,i in enumerate(pasien) :
                                        if i['NOMOR PASIEN'] == nomorPasien:
                                                print(f"{j+1}\t|{i['NOMOR PASIEN']}     \t|{i['NAMA PASIEN']}   \t|{i['JENIS KELAMIN']}          \t|{i['ALAMAT']}                               \t|{i['STATUS PERAWATAN']}")
                                                break
                                else:
                                        print('\nPasien Belum Terdaftar!')
                                        continue            
                        while True:
                                remove1 = input('konfirmasi data akan dihapus [Y/N] : ')
                                if remove1 == 'Y' or remove1 == 'y':
                                        del pasien[j]
                                        print('\nData Berhasil Dihapus!')
                                        break
                                elif remove1 == 'N' or remove1 == 'n':
                                        print('\nData Tidak Dihapus')
                                        break
                                else:
                                        print('\nPilihan Tidak Sesuai')
                                continue
                elif remove == '2':
                        break
                else:
                        print('\nError!, Silahkan Pilih Nomor [1-2]')
        return 
        
# Menu Data
while True :
        pilihMenu = input('''
============= Selamat Datang di Rumah Sakit Purwadhika! ==============
=================== Semoga Sehat & Bahagia Selalu! ===================

Menu Utama:
1. Data Pasien
2. Menambahkan Data Pasien
3. Mengubah Data Pasien
4. Menghapus Data Pasien
5. Exit Program      
======================================================================
Silahkan Pilih Nomor [1-5]: ''')
        
        if(pilihMenu == '1'):
                Read_Data()
        elif(pilihMenu == '2'):
                Menambahkan_Data()
        elif(pilihMenu == '3'):
                Mengubah_Data()
        elif(pilihMenu == '4'):
                Menghapus_Data()
        elif(pilihMenu == '5'):
                print('Terima Kasih, Semoga Sehat Selalu!\n')
                break
        else:
                print('\nError, Silahkan Pilih Nomor [1-5]')
         