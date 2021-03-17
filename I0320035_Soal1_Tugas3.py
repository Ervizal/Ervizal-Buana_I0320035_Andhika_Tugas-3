#Pembuatan list array
Identitas_teman = ['Sasa','Rafli','Alam','Yuku','Funny','Zaneta','Sekar','Hani','Stefany','Bonang'] #Mengisi value dari list
print("Identitas_teman[4]: ", Identitas_teman[4])                                                   #Mencetak output list index ke-4
print("Identitas_teman[6]: ", Identitas_teman[6])                                                   #Mencetak output list index ke-6
print("Identitas_teman[7]: ", Identitas_teman[7])                                                   #Mencetak output list index ke-7)
#Mengganti isi dari
Identitas_teman[3] = 'Ilham Fairuzzaman'                                                            #Mengganti value list di index ke-3
Identitas_teman[5] = 'Zaki'                                                                         #Mengganti value list di index ke-5
Identitas_teman[9] = 'Safri'                                                                        #Mengganti value list di index ke-9
#Menambahkan 2 nama teman
Identitas_teman.append("Attar")
Identitas_teman.append("Bagus")
j = 0                                                                                               #Membuat nilai awal variabel untuk perulangan isi list
for i in range (0,12):                                                                              #Perulangan dengan nilai i = 0 hingga i = 10 sehingga dapat melakukan print sebanyak 10 kali
    print(Identitas_teman[j])                                                                       #Melakukan print list Identitas_teman dengan nilai index j = 0 hingga j = 10
    j+=1                                                                                            #Melakukan increment value pada variabel j
print(len(Identitas_teman))