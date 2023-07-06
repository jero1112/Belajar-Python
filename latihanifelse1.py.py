umur=int(input('masukkan umur anda = '))
TD = int(input('Tekanan Darah Anda = '))
if (umur >= 50):
    print('Kategori anda = adi yuswa')
else:
    if (umur > 17 ):
        print('Kategori anda = dewasa')
    else:
        if ( umur > 10):
            print('Kategori anda = remaja')
        else:
            print('Kategori anda = anak anak')
if (TD < 80):
    kategori = 'Darah Rendah'
    print('Tekanan darah anda = ',kategori)
else:
    if (TD > 120 ):
        kategori = 'Darah Tinggi'
        print('Tekanan darah anda = ',kategori)
    else:
        print('Darah anda normal')
