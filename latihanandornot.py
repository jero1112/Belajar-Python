a = int(input('Masukkan Nilai = '))
b = int(input('Masukkan Nilai = '))
u = not (a > 30)
v = not (a > b)
w = a < 20 or a >= 5
x = a > 10 or b <= 40
y = a <= 30 and a >= 10
z = a < 40 and b < 50

print(u)
print(v)
print(w)
print(x)
print(z)
print(y)

umur_ibu = int(input('Umur Ibu lebih Dari 21 dan tidak sampai 30 : '))
umur_fajar = 20
if (umur_ibu >= umur_fajar ):
    print('Fajar Lebih Muda Dari Pada Ibuk Cyntia')
    if umur_ibu >= 30:
        print('Ibu Lebih Tua Dari Pada Fajar')
else:
    print('Ibu Lebih Muda Dari Pada Fajar')
    
count = 3
while count > 0:
    username = str(input('Masukkan Username Anda : '))
    psw = int(input('Masukkan Password Anda : '))
    if (username == 'user' and psw == 12345 ):
        print('Selamat Datang')
        print('Silahkan Masuk di Kelas ')
        break
    else:
        print('Username atau Password yang Anda Masukkan Salah')
        print('Silahkan Coba Lagi')
        count -=1
if count > 0:
    print('================================')
    alasan = False
    nama = str(input('Masukkan Nama Anda : '))
    kls = str(input('Kelas Anda : '))
    waktu_terlambat = int(input("Berapa Lama Anda Terlambat : "))
    if (waktu_terlambat < 15 or alasan):
        print('Anda Boleh Masuk ')
        print('Lain Kali Tepat Waktu OK')
    else:
        print('Anda Dilarang Masuk Silahkan Mengurus Keterlambatan Anda Ke BAK')
else:
    print('Anda Di Blokir')
            
count = 3
password = 'admin'
while count > 0:
    psw = input('password : ')
    if psw ==password:
        print('Login Sukses')
        break
    else:
        print('password salah\n')
        count -=1