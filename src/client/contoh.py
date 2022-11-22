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
    

# Add Menu (ini ku comment biar ga ke buat menu baru mulu kalau mau ngetes)
print("\n======== ADD MENU ========")
response = requests.post("http://localhost:5000/api/menus/add", json={"nama":"Es Teh","harga":5000,"kategori":"minuman","jumlahStok":99,"fotoUrl":""})
if (response):
    print("Menu Berhasil Ditambahkan!")
else:
    print("eror")

"""
#Get Menu By Nama
print("\n======== GET MENU BY NAMA ========")
response = requests.get("http://localhost:5000/api/menus/search-nama/burger")
jsonresponse = response.json()

print(jsonresponse)

#Get Menu By Id
print("\n======== GET DATA MENU BY ID ========")
response = requests.get("http://localhost:5000/api/menus/search-id/1")
jsonresponse = response.json()

print(jsonresponse)

#Get Nama Menu By Id
print("\n======== GET NAMA MENU BY ID ========")
response = requests.get("http://localhost:5000/api/menus/nama/1")
jsonresponse = response.json()

print(jsonresponse)

#Get Harga Menu By Id
print("\n======== GET HARGA MENU BY ID ========")
response = requests.get("http://localhost:5000/api/menus/harga/1")
jsonresponse = response.json()

print(jsonresponse)

#Get Kategori Menu By Id
print("\n======== GET KATEGORI MENU BY ID ========")
response = requests.get("http://localhost:5000/api/menus/kategori/1")
jsonresponse = response.json()

print(jsonresponse)

#Get Kuantitas Menu By Id
print("\n======== GET KUANTITAS MENU BY ID ========")
response = requests.get("http://localhost:5000/api/menus/kuantitas/1")
jsonresponse = response.json()

print(jsonresponse)

headers = {"Content-Type": "application/json"}



#Update Nama Menu By ID
print("\n======== UPDATE NAMA MENU BY ID ========")
response = requests.put("http://localhost:5000/api/menus/update/nama/9", json={"nama":"Pepsi"})

if (response):
    print("Menu Berhasil Diperbarui!")

#Update Harga Menu By ID
print("\n======== UPDATE HARGA MENU BY ID ========")
response = requests.put("http://localhost:5000/api/menus/update/harga/9", json={"harga":8000})

if (response):
    print("Menu Berhasil Diperbarui!")

#Update Kuantitas Menu By ID
print("\n======== UPDATE KUANTITAS MENU BY ID ========")
response = requests.put("http://localhost:5000/api/menus/update/kuantitas/9", json={"kuantitas":1})

if (response):
    print("Menu Berhasil Diperbarui!")

#Buat yang pesanan mirip-mirip sama yang di atas, bisa dipelajari sendiri ya bg. smgt
"""