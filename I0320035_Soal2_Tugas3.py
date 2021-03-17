print("==========================================")
print("==== Identitas Diri dengan Dictionary ====")
print("==========================================")
#Pembuatan dictionary
My_identity = {"Nama":"Ervizal Buana", "Hobi 1":"Berenang", "Hobi 2":"Bermain gitar", "Hobi 3":"Memanah",
			   "Sosmed 1":"instagram @eb_putra", "Sosmed 2":"linkedin: Ervizal Buana", "Sosmed 3":"twitter: @awgledek",
			   "Lagu favorit 1":"Westlife - If I Let You Go", "Lagu Favorit 2":"Travis Atreo - As Long As You Love Me",
			   "Lagu favorit 3":"Maroon 5 - Memories", "Makanan favorit 1":"Chicken Steak", "Makanan favorit 2":"Nasi Goreng",
			   "Makanan favorit 3":"Micin"}
print(My_identity)                              #Menampilkan output dictionary
My_identity["Hobi 1"] = "Travelling"            #Mengubah isi dari dictionary ["Hobi 1"]
My_identity["Sosmed 2"] = "Zenly: vizaall"      #Mengubah isi dari dictionary ["Sosmed 2"]
del My_identity["Makanan favorit 1"]            #Menghapus dictionary ["Makanan favorit 1"]
del My_identity["Makanan favorit 2"]            #Menghapus dictionary ["Makanan favorit 2"]
My_identity["Hobi 4"] = "Bersepeda"             #Menambahkan dictionary baru ["Hobi 4"]
print(My_identity)                              #Menampilkan output dictionary yang baru