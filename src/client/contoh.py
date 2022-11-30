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


# #Get All Menu
# print("\n======== GET ALL MENU ========")
# response = requests.get("http://localhost:5000/api/menus/")
# jsonresponse = response.json()
# print(jsonresponse)

# # # Add Menu
# # print("\n======== ADD MENU ========")
# # response = requests.post("http://localhost:5000/api/menus/add", json={"nama":"Es Teh","harga":5000,"kategori":"minuman","jumlahStok":99,"fotoUrl":""}) #URL Harus Valid
# # if (response):
# #     print("Menu Berhasil Ditambahkan!")
# # else:
# #     print("eror")

# #Get Menu By Nama
# print("\n======== GET MENU BY NAMA ========")
# response = requests.get("http://localhost:5000/api/menus/search-nama/Es%20Teh")
# jsonresponse = response.json()

# print(jsonresponse)

# #Add Pesanan
# print("\n======== ADD PESANAN ========")
# response = requests.post("http://localhost:5000/api/pesanan/add", json={"id_pesanan":1,"id_menu":1,"kuantitas": 3}) #Kalau udah ada pesanannya bakal eror
# if (response):
#     print("Pesanan Berhasil Ditambahkan!")
# else:
#     print("eror")

#Get Pesanan All

# print("\n======== GET PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/*")
# jsonresponse2 = response.json()
# test2 = len(jsonresponse2)
# print(jsonresponse2)
# print(test2)

# print("\n======== GET PESANAN All (HASIL) ========")
# response = requests.get("http://localhost:5000/api/detail-pesanan/")
# jsonresponse1 = response.json()
# test1 = len(jsonresponse1)
# print(jsonresponse1)
# print(test1)

# print("\n======== GET PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/2")
# jsonresponse = response.json()
# test = len(jsonresponse)
# print(test)
# print(jsonresponse)

# #Update Kuantitas Menu Pada Pesanan
# print("\n======== UPDATE KUANTITAS MENU PADA PESANAN BY ID ========")
# response = requests.put("http://localhost:5000/api/pesanan/update/kuantitas/1/1", json={"kuantitas":1})

# if (response):
#     print("Kuantitas Menu Pada Pesanan Berhasil Diperbarui!")

# #Get Pesanan By ID
# print("\n======== GET PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/1")
# jsonresponse = response.json()

# print(jsonresponse)

# #Update Catatan Menu Pada Pesanan
# print("\n======== UPDATE CATATAN MENU PADA PESANAN BY ID ========")
# response = requests.put("http://localhost:5000/api/pesanan/update/catatan/1/1", json={"catatan": "ini misalnya catatan"})

# if (response):
#     print("Catatan Menu Pada Pesanan Berhasil Diperbarui!")

# #Get Pesanan By ID
# print("\n======== GET PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/1")
# jsonresponse = response.json()

# print(jsonresponse)

# #Delete Menu Pada Pesanan By ID
# print("\n======== DELETE MENU IN PESANAN ========")
# response = requests.delete("http://localhost:5000/api/pesanan/delete/1/1")
# if (response):
#     print("Menu Pada Pesanan Berhasil Dihapus")

# #Get Pesanan By ID
# print("\n======== GET PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/1")
# if (response):
#     jsonresponse = response.json()
#     print(jsonresponse)
# else:
#     print("Pesanan Tidak Ada")

# #Delete Pesanan By ID
# print("\n======== DELETE PESANAN ========")
# response = requests.delete("http://localhost:5000/api/pesanan/delete/1")
# if (response):
#     jsonresponse = response.json()
#     print(jsonresponse)
# else:
#     print("Pesanan Tidak Ada")

# #Get All Pesanan
# print("\n======== GET ALL PESANAN (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/")
# jsonresponse = response.json()

# print(jsonresponse)


# #Add Detail Pesanan
# print("\n======== ADD DETAIL PESANAN ========")
# response = requests.post("http://localhost:5000/api/detail-pesanan/add", json={"dine_in_status": False}) #Kalau udah ada pesanannya bakal eror
# if (response):
#     print("Detail Pesanan Berhasil Ditambahkan!")
# else:
#     print("eror")

#Get Pesanan By ID
# print("\n======== GET DETAIL PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/detail-pesanan/0")
# jsonresponse = response.json()

# print(jsonresponse)

# #Update Dine In Status 
# print("\n======== UPDATE DINE IN STATUS DETAIL PESANAN BY ID ========")
# response = requests.put("http://localhost:5000/api/detail-pesanan/update/dine-in-status/1", json={"dine_in_status": True})

# if (response):
#     print("Dine In Status Detail Pesanan Berhasil Diperbarui!")

# #Get Detail Pesanan By ID
# print("\n======== GET DETAIL PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/detail-pesanan/1")
# jsonresponse = response.json()

# print(jsonresponse)

# #Update Nomor Meja Detail Pesanan
# print("\n======== UPDATE NOMOR MEJA DETAIL PESANAN BY ID ========")
# response = requests.put("http://localhost:5000/api/detail-pesanan/update/nomor-meja/1", json={"nomor_meja": 1})

# if (response):
#     print("Nomor Meja Detail Pesanan Berhasil Diperbarui!")

# #Get Detail Pesanan By ID
# print("\n======== GET DETAIL PESANAN BY ID (HASIL) ========")
# response = requests.get("http://localhost:5000/api/pesanan/1")
# jsonresponse = response.json()

# print(jsonresponse)

# #Delete Detail Pesanan By ID
# print("\n======== DELETE DETAIL PESANAN BY ID ========")
# response = requests.delete("http://localhost:5000/api/detail-pesanan/delete/1")
# if (response):
#     print("Detail Pesanan Berhasil Dihapus")

# #Get All Pesanan
# print("\n======== GET ALL DETAIL PESANAN (HASIL) ========")
# response = requests.get("http://localhost:5000/api/detail-pesanan/")
# jsonresponse = response.json()

# print(jsonresponse)