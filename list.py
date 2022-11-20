# membuat 5 list dengan type data yang berbeda
listData = ["Teknik Informatika", "UPB", 650000, True, "Fakultas Teknik"]
################################
# mengakses elment list #
############################
# menampilkan elment ke-3 pada sebuah list
print(listData[2])
# menampilkan elment ke-2 sampai ke-4
print(listData[1:4])
# menampilkan elment terakhir
print(listData[4])
# atau bisa juga seperti ini
print(listData[-1])
#################################
# mengubah elment list #
###########################
# merubah elment ke-4 dengan nilai lain
listData[3] = False
print(listData)
# merubah elment ke-4 sampai dengan terakhir dengan nilai lain
listData[3:5] = [True, "TI22B1"]
print(listData)
##################################
# menambah elment list #
############################
# membuat listA dan diisi oleh elment yang ada di listData
listA = listData
# membuat list B dengan elment masih  kosong
listB = []
# mengambil 2 nilai dari listA lalu simpan ke listB
listB = listA[0:2]
print(listB)
# menambahkan list B dengan nilai String
listB.append("Fakultas Teknik")
print(listB)
# menambahkan list B dengan 3 nilai
listB.append(["Teknik Sipil", "Teknik Lingkungan", "Teknik Industri"])
print(listB)
# menggabungkan list B dengan listA
listGabungan = listA + listB
print(listGabungan)
