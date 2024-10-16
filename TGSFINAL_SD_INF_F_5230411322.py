# UJIAN AKHIR SEMESTER GENAP STRUKTUR DATA

#---------------------------------------------#
#   NAMA : RIVAN GHIBRAN BAHARUDIN SULISTYA   #
#   NPM  : 5230411322                         #
#---------------------------------------------#

from tabulate import tabulate

class Node :
    
    def __init__ (self, noSku, namaBarang, hargaSatuan, jumlahStok ) :
        
        self.noSku = noSku
        self.namaBarang = namaBarang
        self.hargaSatuan = hargaSatuan
        self.jumlahStok = jumlahStok
        self.left = None
        self.right = None
        
class BinarySearchTree :
    
    def __init__(self) :
        
        self.root = None
    
    def insertBarang(self, noSku, namaBarang, hargaSatuan, jumlahStok) :
        
        new_node = Node (noSku, namaBarang, hargaSatuan, jumlahStok)
        if self.root is None :
            self.root = new_node
            return True
        temp = self.root
        while(True) :
            if new_node.noSku == temp.noSku :
                return False
            if new_node.noSku < temp.noSku :
                if temp.left is None :
                    temp.left = new_node
                    return True
                temp = temp.left
            else : 
                if temp.right is None :
                    temp.right = new_node
                    return True
                temp= temp.right
                   
    def contains(self, noSku) :
        
        temp = self.root
        while temp is not None :
            if noSku < temp.noSku :
                temp = temp.left
            elif noSku > temp.noSku :
                temp = temp.right
            else :
                return temp
        return None
    
    def updateTambahStok(self, noSku, tambahStok):
        
        sku = self.contains(noSku)
        if sku is not None :
            sku.jumlahStok += tambahStok

    def updateKurangStok(self, noSku, kurangStok):
        
        sku = self.contains(noSku)
        if sku is not None :
            sku.jumlahStok -= kurangStok
            
    def tampilBarang(self) :
        
        results = []
        def traverse(current_node) :
            results.append((current_node.noSku, 
                            current_node.namaBarang,
                            current_node.hargaSatuan,
                            current_node.jumlahStok))  
            if current_node.left is not None :
                traverse(current_node.left)
            if current_node.right is not None :
                traverse(current_node.right)
            
        traverse(self.root)
        return results

# main program
    
bst = BinarySearchTree()
transaksi = []
headers = ["SKU", "NAMA BARANG", "HARGA", "STOK"]
headers2 = ["NAMA KONSUMEN", "SKU", "JUMLAH BELI", "SUBTOTAL"]
   
def inputBarang() :
    
    print("--------------------------------")
    noSku = input(" masukan 4 digit No. SKU : ")
    if bst.contains(noSku) is None :
        if len(noSku) == 4 : 
            namaBarang = input(" masukan nama barang : ")
            hargaSatuan = int(input(" masukan harga satuan : "))
            jumlahStok = int(input(" masukan jumlah stok : "))
            bst.insertBarang(noSku, namaBarang, hargaSatuan, jumlahStok) 
            print("--------------------------------")
            print(" 1 SKU barang berhasil di inputkan")      
        else :
            print(" (!) No. SKU yang anda masukan tidak sesuai dengan ketentuan")  
            lanjut = input (" apakah anda ingin input ulang ? (Y/N) ") 
            if lanjut == "Y" or lanjut == "y" :
                return inputBarang()                
    else :
        print(" (!) No. SKU yang anda masukan sudah tersedia")
            
               
def restokBarang() : 

    if bst.root is not None :
        lihatBarang()
        noSku = input(" masukan 4 digit No. SKU : ")   
        if bst.contains(noSku)  is not None :
            tambahStok = int(input(" masukan jumlah stok baru : "))
            bst.updateTambahStok(noSku, tambahStok)
            print("--------------------------------")
            print(" data stok barang berhasil di update")
        else:
            print(" (!) No. SKU yang anda inputkan salah ")
            lanjut = input (" apakah anda ingin input ulang ? (Y/N) ") 
            if lanjut == "Y" or lanjut == "y" :
                 return restokBarang()
    else :
        print (" (!) belum ada barang yang di inputkan, silakan input barang terlebih dahulu ")


def lihatBarang() :
    
    if bst.root is not None :
        print("--------------------------------")
        print(" daftar barang : ")
        print(tabulate(insertionSortBarang(bst.tampilBarang()), headers, tablefmt="fancy_grid"))
    else :
        print (" (!) belum ada barang yang di inputkan, silakan input barang terlebih dahulu ")
       
def transaksiBaru() :
    
    print("--------------------------------")
    namaKonsumen = input(" masukan nama konsumen : ")
    def tambahBarang (nama) :
        if bst.root is not None :
            lihatBarang()
            noSku = input(" masukan 4 digit No. SKU : ") 
            node = bst.contains(noSku) 
            if node is not None :
                while True :
                    jumlahBeli = int(input(" masukan jumlah beli : "))
                    if node.jumlahStok >= jumlahBeli :
                        subtotal = node.hargaSatuan * jumlahBeli
                        bst.updateKurangStok(noSku,jumlahBeli)
                        transaksi.append((nama, noSku, jumlahBeli, subtotal))
                        print(" transaksi baru berhasil di inputkan")
                        tambah = input(" apakah anda ingin melanjutkan menambah data transaksi pada konsumen ini ? (Y/N) ")
                        if tambah == "N" or tambah == "n" :
                            break
                        else :
                            return tambahBarang(nama)
                    else :
                        print (" (!) jumlah stok barang yang tersedia tidak mencukupi")
                        lanjut = input (" apakah anda ingin melanjutkan transaksi ? (Y/N) ") 
                        if lanjut == "N" or lanjut == "n" :
                            break                                 
            else :
                print(" (!) No. SKU yang anda inputkan belum terdaftar ")
                lanjut = input (" apakah anda ingin melanjutkan transaksi ? (Y/N) ") 
                if lanjut == "N" or lanjut == "n" :
                    return kelolaTransaksi()
                else :
                    tambahBarang(nama)
        else :
            print(" (!) belum ada stok barang yang tersedia, silakan input barang terlebih dahulu")
            return kelolaTransaksi()
    tambahBarang(namaKonsumen)
         
def lihatTransaksi() : 
    
    if len(transaksi) > 0 :
        print("--------------------------------")
        print(" daftar transaksi : ")
        print(tabulate(transaksi, headers2, tablefmt="fancy_grid"))
    else :
        print(" (!) belum ada daftar transaksi ")

def lihatTransaksiSort() : 
    
    if len(transaksi) > 0 :
        print("--------------------------------")
        print(" daftar transaksi berdasarkan subtotal : ")
        print(tabulate(insertionSortTransaksi(transaksi), headers2, tablefmt="fancy_grid"))
    else :
        print(" (!) belum ada daftar transaksi ")
        
def insertionSortTransaksi(list) : 
    
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while temp[3] > list[j][3] and j > -1:
            list[j+1] = list[j]
            list[j] = temp
            j -= 1
    return list

def insertionSortBarang(list) : 
    
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while temp[0] < list[j][0] and j > -1:
            list[j+1] = list[j]
            list[j] = temp
            j -= 1       
    return list
    
def kelolaTransaksi() :
    
    while True :
        print("--------------------------------")
        print("   KELOLA TRANSAKSI KONSUMEN    ")
        print("--------------------------------")
        print(" 1.) Input Data Transaksi Baru ")
        print(" 2.) Lihat Data Seluruh Transaksi Konsumen")
        print(" 3.) Lihat Data Transaksi Berdasarkan Subtotal" )
        print(" 0.) Kembali")
        print("--------------------------------")
        pilihMenu = input(" pilih menu : ")   
            
        if pilihMenu == "1" :
            transaksiBaru()
        elif pilihMenu == "2" :
            lihatTransaksi()
        elif pilihMenu == "3" :   
            lihatTransaksiSort()
        elif pilihMenu == "0" :
            break
        else :
            print(" (!) pilihan yang anda inputkan tidak valid, silakan input ulang")  
                                       
def kelolaStokBarang() :
    
    while True :
        print("--------------------------------")
        print("       KELOLA STOK BARANG       ")
        print("--------------------------------")
        print(" 1.) Input Data Stok Barang ")
        print(" 2.) Restok Barang")
        print(" 3.) Lihat Data Barang")
        print(" 0.) Kembali" )
        print("--------------------------------")
        pilihMenu = input(" pilih menu : ")   
            
        if pilihMenu == "1" :
            inputBarang()
        elif pilihMenu == "2" :
            restokBarang()
        elif pilihMenu == "3" :
            lihatBarang()
        elif pilihMenu == "0" :
            break
        else :
            print(" (!) pilihan yang anda inputkan tidak valid, silakan input ulang")
                        
def menuUtama () :
    
    while True :
        print("--------------------------------")
        print("           MENU UTAMA           ")
        print("--------------------------------")
        print(" 1.) Kelola Stok Barang ")
        print(" 2.) Kelola Transaksi Konsumen")
        print(" 0.) Exit" )
        print("--------------------------------")
        pilihMenu = input(" pilih menu : ")

        if pilihMenu == "1" :
            kelolaStokBarang()
        elif pilihMenu == "2" :
            kelolaTransaksi()
        elif pilihMenu == "0":
            print("-------------------------------")
            print("|  telah keluar dari program  |")
            print("-------------------------------")
            break
        else:
            print(" (!) menu yang anda inputkan tidak valid, silakan input ulang")

if __name__ == "__main__" :
    menuUtama()

