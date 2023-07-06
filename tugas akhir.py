# # # # # # # #Contoh penggunaan Nested Loop
# # # # # # # #Catatan: Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai True(benar) dan nol sebagai False(salah)
# # # # # # # # print("\n")
# # # # # # # # i = 2
# # # # # # # # while(i < 50):
# # # # # # # #     j = 2
# # # # # # # #     while(j <= (i/j)):
# # # # # # # #         if not(i%j): break
# # # # # # # #         j = j + 1
# # # # # # # #         if (j > i/j) : print(i, " ini adalah bilangan prima")
# # # # # # # #     i = i + 1
# # # # # # # # print("Good bye!")
# # # # # # # # print('\n')

# # # # # # # list = ['fisika', 'kimia', 1993, 2017]
# # # # # # # list.append(2001)
# # # # # # # print('\n')
# # # # # # # print(list)
# # # # # # # del list[2]
# # # # # # # print(list)
# # # # # # # print ("Nilai pada index 3 : ", list[3])
# # # # # # # print ("Nilai pada index 2 : ", list[1])
# # # # # # # print('\n')
# # # # # # # # #Cara mengakses nilai di dalam list Python

# # # # # # # # list1 = ['fisika', 'kimia', 1993, 2017]
# # # # # # # # list2 = [1, 2, 3, 4, 5, 6, 7 ]
# # # # # # # # print('\n')
# # # # # # # # print ("list1[0]: ", list1[0])
# # # # # # # # print ("list2[1:5]: ", list2[1:5])
# # # # # # # # print('\n')

# # # # # # #Contoh cara menghapus nilai pada list python

# # # # # # list = ['fisika', 'kimia', 1993, 2017]
# # # # # # print('\n')
# # # # # # print (list)
# # # # # # del list[2]
# # # # # # print ("Setelah dihapus nilai pada index 2 : ", list)
# # # # # # print('\n')

# # # # # #Cara mengakses nilai tuple

# # # # # # tup1 = ('fisika', 'kimia', 1993, 2017)
# # # # # # tup2 = (1, 2, 3, 4, 5, 6, 7 )
# # # # # # print('\n')
# # # # # # print ("tup1[0]: ", tup1[0])
# # # # # # print ("tup2[1:5]: ", tup2[1:5])
# # # # # # print('\n')

# # # # # #Contoh sederhana pembuatan tuple pada bahasa pemrograman python

# # # # # tup1 = ('fisika', 'kimia', 1993, 2017)
# # # # # tup2 = (1, 2, 3, 4, 5 )
# # # # # tup3 = "a", "b", "c", "d"
# # # # # print('\n')
# # # # # print(tup1)
# # # # # print(tup2)
# # # # # print(tup3)
# # # # # print('\n')

# # # # #Contoh cara membuat Dictionary pada Python

# # # # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# # # # print('\n')
# # # # print ("dict['Name']: ", dict['Name'])
# # # # print ("dict['Age']: ", dict['Age'])

# # # # print('\n')

# # # #Update dictionary python

# # # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# # # dict['Age'] = 8; # Mengubah entri yang sudah ada
# # # dict['School'] = "DPS School" # Menambah entri baru
# # # print('\n')
# # # print(dict)
# # # print ("dict['Age']: ", dict['Age'])
# # # print ("dict['School']: ", dict['School'])
# # # print('\n')


# # #Contoh cara menghapus pada Dictionary Python

# # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# # del dict['Name'] # hapus entri dengan key 'Name'
# # dict.clear() # hapus semua entri di dict
# # del dict # hapus dictionary yang sudah ada
# # print('\n')
# # print ("Hasil : ", dict['Age'])
# # print ("Hasil : ", dict['School'])
# # print('\n')
# # def display():
# #     tampilan = """
# #     ================= HOTEL PANGERAN BEACH ========================
# #     ===============================================================
# #     ||    KODE     ||     Jenis Kamar     ||   Harga per Malam   ||
# #     ===============================================================
# #     ||     S       ||       Single        ||      Rp.100000      ||
# #     ||     D       ||       Double        ||      Rp.350000      ||
# #     ||     F       ||       Family        ||      Rp.550000      ||
# #     ===============================================================
# #     """
# #     print(tampilan)
# # display()

# def printme():
#     a = "This prints a passed string into this function"
#     print(a)
# printme()
# print('\n')
# nama=input('Masukkan nama anda = ')
# nim=input('Masukkan NIM anda = ')

# soal=print('Mencari luas persegi panjang')
# panjang=int(input('Panjang (cm)= ',))
# lebar=int(input('lebar (cm)= ',))
# rumus=panjang*lebar
# print('\n')
# print('Output dari proses diatas')
# print('Nama anda = ',nama)
# print('NIM anda = ', nim)
# print('Hasil luas persegi panjang = ',rumus,'cm') 
# print('\n')

# nama = input('masukkan nama : ')
# if nama == 'alif' or nama == 'Alif':
#     print('Nama anda benar')
# else:
#     print('Nama anda salah')

# print(3)
# i = 0
# while i < 10:
#     i += 1
#     if i == 11:
#         continue
#     print(i,'x',i,'=',i*i)
def sapalisa():
    print('lisa');
def sapaloli():
    print('loli');
sapalisa()
sapaloli()

y = 0
for x in range(9):
    y += 1;print(y);print("=======")