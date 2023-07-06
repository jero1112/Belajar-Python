def menu():
    daftar =(""""
    |===================================================|         
    |===========##      LIST MENU   ##==================|
    |=========## HOTEL PANGERAN BEACH ##================|
    |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    |  KODE |  JENIS KAMAR         | HARGA PER MALAM    |
    |===================================================|
    |  S    |     Singel           |  Rp. 100.000       |
    |  D    |     Double           |  Rp. 350.000       |
    |  F    |     Family           |  Rp. 550.000       |
    |===================================================|
        """)
    print(daftar)
menu()
def untuk_input():
    br_jenis=int(input("mau sewa berapa jenis kamar: "))
    listkod=[]
    listnap=[]
    #proses
    for i in range(br_jenis):
        print('\nData ke - ',i+1)  
        kode=str(input("masukan kode kamar s,d,f : "))
        listkod.append(kode)
        lama=int(input("masukan lama inap(malam): "))
        listnap.append(lama)
            
    print('============================= HOTEL PANGERAN BEACH =================================')
    print('====================================================================================')
    print('No\tJenis Kamar\tHarga per Malam\t\tLama inap(Malam)\tJumlah Harga')
    print('====================================================================================')
    total=0
    for a in range(br_jenis):
        if(listkod == 'S' or listkod[a] == 's'):
            jenis= 'Single'
            harga= 100000
        elif(listkod[a] == 'D' or listkod[a] == 'd'):
            jenis= 'Double'
            harga= 350000
        elif(listkod[a] == 'F' or listkod[a] == 'f'):
            jenis= 'Family'
            harga= 550000
        else:
            jenis= 'data tidak ditemukan'
            harga = 0
                  
        subtotal = harga*listnap[a]
        total = total + subtotal
        print(a+1,'      ',jenis,'           ',harga,'                    ',listnap[a],'               Rp.',subtotal)
        
    if total > 2000000:
        bonus = 'Handuk'
    else:
        bonus = 'Totebag'
        print('====================================================================================')
        print('\t\t\t\t\t\t\t   Total Bayar : Rp.',total)
        print('\t\t\t\t\t\t\t   Bonus       :',bonus)

    tanya = input("=======================================\napakah anda ingin melanjutkan transaksi?\
        \n       y(iya | t(tidak)  : ")
    
    if tanya=="t":
        print("terima kasih telah bertransaksi")
        
    else:
        menu()
        untuk_input()
        menu()
        untuk_input()
        menu()
        untuk_input()
                
untuk_input()


