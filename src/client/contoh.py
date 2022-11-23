#Ini contoh buat dapetin data pakai API di server
#Janlup run dulu servernya, baru buka terminal baru buat ngerun file ini

import requests
import json

#Get All Menu
# print("\n======== GET ALL MENU ========")
# response = requests.get("http://localhost:5000/api/menus/")
# jsonresponse = response.json()

# for i in range(len(jsonresponse)):
#     print(jsonresponse[i]["harga"])
    
# menu_list = []
# for item in jsonresponse:
#     menu_details = {"id": None, "nama": None, "kategori": None, "harga": None, "jumlahStok": None}
#     menu_details['id'] = item['id']
#     menu_details['nama'] = item['nama']
#     menu_details['kategori'] = item['kategori']
#     menu_details['harga'] = item['harga']
#     menu_details['jumlahStok'] = item['jumlahStok']
#     menu_list.append(menu_details)
    
# print(menu_list)

#Get All Menu
print("\n======== GET ALL MENU ========")
response = requests.get("http://localhost:5000/api/menus/")
jsonresponse = response.json()
print(jsonresponse)

# Add Menu
print("\n======== ADD MENU ========")
response = requests.post("http://localhost:5000/api/menus/add", json={"nama":"Es Teh","harga":5000,"kategori":"minuman","jumlahStok":99,"fotoUrl":""}) #URL Harus Valid
if (response):
    print("Menu Berhasil Ditambahkan!")
else:
    print("eror")

#Get Menu By Nama
print("\n======== GET MENU BY NAMA ========")
response = requests.get("http://localhost:5000/api/menus/search-nama/Es%20Teh")
jsonresponse = response.json()

print(jsonresponse)