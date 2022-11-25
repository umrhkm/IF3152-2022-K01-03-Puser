from server.config.db import get_connection

class Pesanan():
    def __init__(self, id_pesanan, id_menu, kuantitas):
        self.id_pesanan = id_pesanan
        self.id_menu = id_menu

        if (kuantitas < 0):
            raise Exception(f"{kuantitas} tidak valid, hurus lebih dari atau sama dengan 0!")
        else:
            self.kuantitas = kuantitas

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO pesanan (id_pesanan, id_menu, kuantitas) VALUES (%s, %s, %s)", (self.id_pesanan, self.id_menu, self.kuantitas,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)
    
    def getAllPesanan():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pesanan")
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            hasil = []

            for pesanan in resultset:
                datapesanan = {}
                datapesanan["id_pesanan"] = pesanan[0]
                datapesanan["id_menu"] = pesanan[1]
                datapesanan["kuantitas"] = pesanan[2]
                datapesanan["catatan"] = pesanan[3]
                hasil.append(datapesanan)
            
            return (hasil)

        except Exception as err:
            raise Exception(err)

    @classmethod
    def getPesananById(self, id_pesanan):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pesanan WHERE id_pesanan = (%s)", (id_pesanan,))
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            hasil = []

            for pesanan in resultset:
                datapesanan = {}
                datapesanan["id_pesanan"] = pesanan[0]
                datapesanan["id_menu"] = pesanan[1]
                datapesanan["kuantitas"] = pesanan[2]
                datapesanan["catatan"] = pesanan[3]
                hasil.append(datapesanan)
            
            return (hasil)

        except Exception as err:
            raise Exception(err)
    
    @classmethod
    def getMenuPesananById(cls, id_pesanan, id_menu):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pesanan WHERE id_pesanan = (%s) AND id_menu = (%s)", (id_pesanan, id_menu,))
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()
            

            if resultset is None:
                raise Exception(f"Data tidak ditemukan!")
            else:
                print(resultset[0])
                id_pesanan, id_menu, kuantitas, catatan = resultset[0]

                self = cls.__new__(cls)
                self.id_pesanan = id_pesanan
                self.id_menu = id_menu
                self.kuantitas = kuantitas
                self.catatan = catatan

                return self

        except Exception as err:
            raise Exception(err)
    
    def getPesananData(self):
        return ({"id_pesanan" : self.id_pesanan, "id_menu" : self.id_menu, "kuantitas" : self.kuantitas, "catatan" : self.catatan})
    
    def getKuantitas(self):
        return self.kuantitas

    def setKuantitas(self, kuantitasbaru, id_pesanan, id_menu):
        if(kuantitasbaru < 0):
            raise Exception(f"{kuantitasbaru} tidak valid, harus lebih dari 0!")
        else:
            self.kuantitas = kuantitasbaru
            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE pesanan SET kuantitas = (%s) WHERE id_pesanan = (%s) AND id_menu = (%s)", (self.kuantitas, id_pesanan, id_menu,))
                connection.commit()
                connection.close()

            except Exception as err:
                raise Exception(err)
    
    def getCatatan(self):
        return self.catatan

    def setCatatan(self, catatanbaru, id_pesanan, id_menu):
        if(len(catatanbaru) > 254):
            raise Exception("Catatan harus kurang dari 255 karakter!")
        else:
            self.catatan = catatanbaru
            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE pesanan SET catatan = (%s) WHERE id_pesanan = (%s) AND id_menu = (%s)", (self.catatan, id_pesanan, id_menu,))
                connection.commit()
                connection.close()

            except Exception as err:
                raise Exception(err)
    
    def deleteMenuInPesanan(self, id_pesanan, id_menu):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pesanan WHERE id_pesanan = (%s) AND id_menu = (%s)", (id_pesanan, id_menu,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)

    def deletePesanan(id_pesanan):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM pesanan WHERE id_pesanan = (%s)", (id_pesanan,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)