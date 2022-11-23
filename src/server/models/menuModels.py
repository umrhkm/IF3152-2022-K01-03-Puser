from server.config.db import get_connection
import validators

class Menu():
    def __init__(self, nama, harga, kategori, jumlahStok):
        self.nama = nama

        if (harga <= 0):
            raise Exception(f"{harga} tidak valid, hurus lebih dari 0!")
        else:
            self.harga = harga

        if ((kategori != "makanan") and (kategori != "minuman")):
            raise Exception(f"{kategori} tidak valid, harus antara makanan atau minuman!")
        else:
            self.kategori = kategori
        
        if (jumlahStok < 0):
            raise Exception(f"{harga} tidak valid, hurus lebih dari atau sama dengan 0!")
        else:
            self.jumlahStok = jumlahStok

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO menu (nama, harga, kategori, jumlahStok) VALUES (%s, %s, %s, %s)", (self.nama, self.harga, self.kategori, self.jumlahStok))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)


    def getAllMenu():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM menu")
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            hasil = []

            for menu in resultset:
                datamenu = {}
                datamenu["id"] = menu[0]
                datamenu["nama"] = menu[1]
                datamenu["harga"] = menu[2]
                datamenu["kategori"] = menu[3]
                datamenu["jumlahStok"] = menu[4]
                hasil.append(datamenu)
            
            return (hasil)

        except Exception as err:
            raise Exception(err)
    

    @classmethod
    def getMenuByNama(self, nama):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM menu WHERE nama iLIKE '%" + nama + "%'")
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            hasil = []

            for menu in resultset:
                datamenu = {}
                datamenu["id"] = menu[0]
                datamenu["nama"] = menu[1]
                datamenu["harga"] = menu[2]
                datamenu["kategori"] = menu[3]
                datamenu["jumlahStok"] = menu[4]
                hasil.append(datamenu)
            
            return (hasil)

        except Exception as err:
            raise Exception(err)
    

    @classmethod
    def getMenuById(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM menu WHERE id = %s", id)
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            if resultset is None:
                raise Exception(f"Id menu {id} tidak ada!")
            else:
                id, nama, harga, kategori, jumlahStok = resultset[0]

                self = cls.__new__(cls)
                self.id = id
                self.nama = nama
                self.harga = harga
                self.kategori = kategori
                self.jumlahStok = jumlahStok

                return self

        except Exception as err:
            raise Exception(err)

    def getMenuData(self):
        return ({"id" : self.id, "nama" : self.nama, "harga" : self.harga, "kategori": self.kategori, "jumlahStok": self.jumlahStok})


    def getNamaMenu(self):
        return self.nama


    def setNama(self, namabaru, id):
        try:
            self.nama = namabaru
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE menu SET nama = %s WHERE id = %s", (self.nama, id))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)
    

    def getHargaMenu(self):
        return self.harga
        
    
    def setHarga(self, hargabaru, id):
        if (hargabaru <= 0):
            raise Exception(f"{hargabaru} tidak valid, hurus lebih dari 0!")
        else:
            self.harga = hargabaru
            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE menu SET harga = %s WHERE id = %s", (self.harga, id))
                connection.commit()
                connection.close()

            except Exception as err:
                raise Exception(err)
    

    def getKategoriMenu(self):
        return self.kategori


    def getJumlahStokMenu(self):
        return self.jumlahStok


    def setJumlahStok(self, jumlahstokbaru, id):
        if(jumlahstokbaru < 0):
            raise Exception(f"{jumlahstokbaru} tidak valid, harus lebih dari 0!")
        else:
            self.jumlahStok = jumlahstokbaru
            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE menu SET jumlahStok = %s WHERE id = %s", (self.jumlahStok, id))
                connection.commit()
                connection.close()

            except Exception as err:
                raise Exception(err)
    

    def deleteMenu(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM menu WHERE id = %s", (id))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)