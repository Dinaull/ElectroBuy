import os
import csv
import pandas as pd
import time as ts
import datetime
from tabulate import tabulate
from collections import defaultdict

def pembukaan():
    os.system("cls")
    print("="*82)
    greating = "Selamat datang di aplikasi"
    greating_2 = "ELECTROBUY"
    greating = greating.center(82)
    greating_2 = greating_2.center(82)
    print(greating)
    print(greating_2)
    print("="*82)
    print("="*82)
    greating = "Login sebagai Pegawai atau Owner"
    greating = greating.center(82)
    print(greating)
    print("="*82)

def login():
    alert = "Login".center(82)
    print(alert)
    print("")
    user = input("Username : ")
    pas = input("Password : ")
    data = {'user': ["Pegawai", "Owner"],
            'Password': ["Pegawai", "Owner"]
            }

    data_user = data['user']
    data_pass = data['Password']

    if user in data_user:
        lokasi = data_user.index(user)
        if pas == data_pass[lokasi]:
            role = data_user[lokasi] 
            status = "Safe"
        else:
            status = "invalid"
    else:
        status = "invalid"
        
    if status == "invalid":
        for x in range(2):
            os.system("cls")
            alert = "Login Gagal"
            alert = alert.center(82)
            print("="*82)
            print(alert)
            print("="*82)
            print("[1] Retry\n[2] Exit")
            pilihan = input("Pilihan : ")
            os.system("cls")
            while pilihan != "1" and pilihan != "2":
                        os.system("cls")
                        alert = "Login Gagal"
                        alert = alert.center(82)
                        print("="*82)
                        print(alert)
                        print("="*82)
                        print("[1] Retry\n[2] Exit")
                        pilihan = input("Pilihan : ")
                        os.system("cls")
            match pilihan:
                        case "1":
                            os.system("cls")
                            pembukaan()
                            alert = "login".center(82)
                            print("")
                            print(alert)
                            print("")
                            user = input("Username : ")
                            pas = input("Password : ")
                            data_user = data['user']
                            data_pass = data['Password']

                            if user in data_user:
                                lokasi = data_user.index(user)
                                if pas == data_pass[lokasi]:
                                    status = "Safe"
                                    break
                            else:
                                status = "invalid"
                        
                        case "2":
                            os.system("cls")
                            closing = "Terima Kasih Telah Menggunakan Layanan Kami"
                            closing = closing.center(82)
                            print("="*82)
                            print(closing)
                            print("="*82)
                            input("Tekan Enter Untuk Lanjut")
                            os.system("cls")
                            break
        else:
            status = "invalid"
            os.system("cls")
            alert = "Anda Telalu Sering Gagal Login"
            alert = alert.center(82)
            print(alert)
            closing = "Terima Kasih Telah Menggunakan Layanan Kami"
            closing = closing.center(82)
            print("="*82)
            print(closing)
            print("="*82)
            input("Tekan Enter Untuk Lanjut")
            os.system("cls")

    return status, role

def menu(role):
    if role == "Pegawai":
        print("=" * 82)
        header = "Daftar Layanan ElectroBuy"
        header = header.center(82)
        print(header)
        print("=" * 82)
        print("[1] Tambah Stok Barang\n[2] Keluarkan Stok Barang dari Gudang\n[3] Barang Satuan\n[4] Daftar Seluruh Barang\n[5] History Keluar Masuk Barang\n[6] Tambah Barang\n[7] Hapus Barang\n[8] Edit Data Barang\n[9] Laporan Mingguan\n[10] Laporan Bulanan\n[11] Penjualan Terpopuler\n[12] Exit")
    elif role == "Owner":
        print("=" * 82)
        header = "Menu Owner ElectroBuy"
        header = header.center(82)
        print(header)
        print("=" * 82)
        print("[1] History Keluar Masuk Barang\n[2] Daftar Satuan\n[3] Daftar Seluruh Barang\n[4] Laporan Mingguan\n[5] Laporan Bulanan\n[6] Penjualan Terpopuler\n[7] Exit")

def navigasi(role):
    while True:
        os.system("cls")
        menu(role)
        tanya = input("Pilihan : ")
        os.system("cls")
        if role == "Pegawai":
            if tanya == "1":

                def tampilkan_produk():
                    with open('DataBase.csv', mode='r', newline='') as file:
                        reader = csv.DictReader(file)
                        data = [{k: v for k, v in row.items()} for row in reader]
                    
                    headers = ["Nomor Barang", "Nama Produk"]
                    rows = [[produk["Nomor Barang"], produk["Nama Produk"]] for produk in data]
                    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

                def tambah_stok(nomor_barang, jumlah_barang_masuk):
                    with open('DataBase.csv', mode='r', newline='') as file:
                        reader = csv.DictReader(file)
                        data = list(reader)

                    for row in data:
                        if row['Nomor Barang'] == nomor_barang:
                            row['Stok'] = str(int(row['Stok']) + jumlah_barang_masuk)
                            break
                    else:
                        print("Nomor barang tidak valid.")
                        return

                    with open('DataBase.csv', mode='w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                        writer.writeheader()
                        writer.writerows(data)

                def catat_transaksi_masuk(nomor_barang, jumlah_barang_masuk):
                    with open('DataBase.csv', mode='r', newline='') as file:
                        reader = csv.DictReader(file)
                        data_barang = list(reader)

                    for row in data_barang:
                        if row['Nomor Barang'] == nomor_barang:
                            barang = row
                            break
                    else:
                        print("Nomor barang tidak valid.")
                        return

                    with open('Riwayat.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        today = datetime.date.today()
                        transaksi = [today, nomor_barang, barang['Kode Barang'], barang['Nama Produk'],
                                    barang['Jenis Barang'], barang['Merek Barang'], barang['Warna Barang'],
                                    'Masuk', jumlah_barang_masuk]
                        writer.writerow(transaksi)

                def barang_masuk():
                    tampilkan_produk()

                    header = "Tambah Stok Barang"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    nomor_barang = input("Masukkan nomor barang: ")
                    jumlah_barang_masuk = int(input("Masukkan jumlah barang masuk: "))

                    tambah_stok(nomor_barang, jumlah_barang_masuk)
                    catat_transaksi_masuk(nomor_barang, jumlah_barang_masuk)

                    print("Stok barang berhasil diperbarui dan transaksi masuk berhasil dicatat.")

                barang_masuk()

            elif tanya == "2":
                def barang_keluar():
                    def tampilkan_produk():
                        with open('DataBase.csv', mode='r', newline='') as file:
                            reader = csv.DictReader(file)
                            data = [{k: v for k, v in row.items()} for row in reader]

                        headers = ["Nomor Barang", "Nama Produk"]
                        rows = [[produk["Nomor Barang"], produk["Nama Produk"]] for produk in data]
                        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
                    tampilkan_produk()
                    def display_alert(message):
                        print("="*82)
                        print(message.center(82))
                        print("="*82)
                    def get_barang_input():
                        
                        header = "Kurangi Stok Barang dari Gudang"
                        header = header.center(82)
                        print("="*82)
                        print(header)
                        print("="*82)
                        display_alert("Silahkan Masukkan Nomor Barang dan jumlah")
                        print("")
                        return input("Nomor Barang: ")

                    def validate_barang(barang):
                        return barang.isdigit() and 1 <= int(barang) <= 99

                    def get_jumlah_input():
                        return int(input("Jumlah Barang: "))

                    barang = get_barang_input()

                    while not validate_barang(barang):
                        display_alert("Anda Salah Memasukkan Nomor Barang")
                        print("Retry ?\n[1] Yes\n[2] No")
                        pilihan = input("Pilihan: ")
                        os.system("cls")

                        while pilihan not in ["1", "2"]:
                            display_alert("Anda Salah Memasukkan Nomor Barang")
                            print("Retry ?\n[1] Yes\n[2] No")
                            pilihan = input("Pilihan: ")
                            os.system("cls")
                        
                        if pilihan == "1":
                            barang = get_barang_input()
                            os.system("cls")
                        else:
                            return

                    try:
                        df = pd.read_csv("DataBase.csv")
                        data_barang = df["Nomor Barang"].astype(str).tolist()

                        if barang in data_barang:
                            lokasi = data_barang.index(barang)

                            nomor_barang = df.iloc[lokasi, 0]
                            kode_barang = df.iloc[lokasi, 1]
                            nama_produk = df.iloc[lokasi, 2]
                            jenis_barang = df.iloc[lokasi, 3]
                            merek = df.iloc[lokasi, 4]
                            warna = df.iloc[lokasi, 5]


                            jumlah = get_jumlah_input()

                            df.at[lokasi, 'Stok'] -= jumlah
                            df.to_csv("DataBase.csv", index=False)

                            if os.path.exists("Riwayat.csv") and os.stat("Riwayat.csv").st_size != 0:
                                Riwayat = pd.read_csv("Riwayat.csv")
                            else:
                                Riwayat = pd.DataFrame(columns=['Tanggal', 'Nomor Barang', 'Kode Barang', 'Nama Produk', 'Jenis Barang', 'Merek', 'Warna', 'Status', 'Jumlah'])

                            transaksi_baru = {
                                'Tanggal': datetime.date.today().strftime('%Y-%m-%d'),
                                'Nomor Barang': nomor_barang,
                                'Kode Barang': kode_barang,
                                'Nama Produk': nama_produk,
                                'Jenis Barang': jenis_barang,
                                'Merek': merek,
                                'Warna': warna,
                                'Status': 'Keluar',
                                'Jumlah': jumlah
                            }
                            Riwayat = pd.concat([Riwayat, pd.DataFrame([transaksi_baru])], ignore_index=True, sort=False)

                            Riwayat.to_csv("Riwayat.csv", index=False) 

                            alert = f"{jumlah} barang dengan Nomor {nomor_barang} berhasil ditambahkan ke riwayat."
                            display_alert(alert)
                        else:
                            display_alert(f"Nomor Barang {barang} Belum Terdaftar")
                    except pd.errors.ParserError:
                        display_alert("Error reading DataBase.csv. Please check the file format.")
                barang_keluar()
                
            elif tanya == "3":
                def load_data(csv_filename):
                    data = []
                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            data.append(row)
                    return data

                def print_product_details(product):
                    print(f"Nomor Barang: {product['Nomor Barang']}")
                    print(f"Kode Barang: {product['Kode Barang']}")
                    print(f"Nama Produk: {product['Nama Produk']}")
                    print(f"Jenis Barang: {product['Jenis Barang']}")
                    print(f"Merek Barang: {product['Merek Barang']}")
                    print(f"Warna Barang: {product['Warna Barang']}")
                    print(f"Harga: {product['Harga']}")
                    print(f"Stok: {product['Stok']}")

                def find_product_by_number(data, product_number):
                    for product in data:
                        if product['Nomor Barang'] == product_number:
                            return product
                    return None

                def data_satuan():
                    csv_filename = 'DataBase.csv'
                    data = load_data(csv_filename)
                    
                    table_data = [(product['Nomor Barang'], product['Nama Produk']) for product in data]
                    print(tabulate(table_data, headers=["Nomor Barang", "Nama Produk"], tablefmt="fancy_grid"))

                    header = "Data Barang Satuan"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    
                    product_number = input("Masukkan nomor barang: ")
                    
                    product = find_product_by_number(data, product_number)
                    
                    if product:
                        print("="*82)
                        print_product_details(product)
                        print("="*82)
                    else:
                        alert = "Nomor barang tidak ditemukan."
                        alert = alert.center(82)
                        print("="*82)
                        print(alert)
                        print("="*82)
                data_satuan()
                
            elif tanya == "4":
                def get_unique_values(csv_filename, column_name):
                    values = set()

                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)

                        for row in csv_reader:
                            values.add(row[column_name])

                    return sorted(values)

                def search_by_brand_and_type(csv_filename, brand_name, item_type):
                    results = []

                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)

                        for row in csv_reader:
                            if (row['Merek Barang'].lower() == brand_name.lower() and
                                row['Jenis Barang'].lower() == item_type.lower()):
                                results.append(row)

                    return results

                def seluruh_barang():
                    csv_filename = 'DataBase.csv'

                    while True:
                        unique_brands = get_unique_values(csv_filename, 'Merek Barang')
                        unique_item_types = get_unique_values(csv_filename, 'Jenis Barang')
                        header = "Data Barang Keseluruhan"
                        header = header.center(82)
                        print("="*82)
                        print(header)
                        print("="*82)
                        print("Pilih merek barang yang ingin dilihat:")
                        for idx, brand in enumerate(unique_brands, start=1):
                            print(f"{idx}. {brand}")

                        while True:
                            brand_choice = input("Masukkan nomor pilihan merek (atau tekan 'Enter' untuk kembali ke menu): ")
                            if brand_choice == "":
                                return 
                            try:
                                brand_choice = int(brand_choice)
                                if 1 <= brand_choice <= len(unique_brands):
                                    break
                                else:
                                    print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")
                            except ValueError:
                                print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")

                        selected_brand = unique_brands[brand_choice - 1]

                        print("Pilih jenis barang yang ingin dilihat:")
                        for idx, item_type in enumerate(unique_item_types, start=1):
                            print(f"{idx}. {item_type}")

                        while True:
                            item_type_choice = input("Masukkan nomor pilihan jenis barang: ")
                            try:
                                item_type_choice = int(item_type_choice)
                                if 1 <= item_type_choice <= len(unique_item_types):
                                    break
                                else:
                                    print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")
                            except ValueError:
                                print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")

                        selected_item_type = unique_item_types[item_type_choice - 1]

                        matching_products = search_by_brand_and_type(csv_filename, selected_brand, selected_item_type)

                        if matching_products:
                            print(f"\nBarang-barang dengan merek '{selected_brand}' dan jenis '{selected_item_type}':")
                            headers = matching_products[0].keys()
                            rows = [product.values() for product in matching_products]
                            print(tabulate(rows, headers, tablefmt="fancy_grid"))
                        else:
                            print(f"Tidak ada barang dengan merek '{selected_brand}' dan jenis '{selected_item_type}' yang ditemukan.")
                seluruh_barang()
                
            elif tanya == "5":
                def history():
                    os.system("cls")
                    print("="*82)
                    print("ELECTROBUY".center(82))
                    print("-"*82)
                    print("Daftar Riwayat Gudang".center(82))
                    print("="*82)
                    print(" ")

                    file_path = "riwayat.csv"
                    
                    try:
                        df = pd.read_csv(file_path, on_bad_lines='skip')
                        
                        if df.empty:
                            print("File riwayat.csv kosong. Tidak ada data untuk ditampilkan.")
                        else:
                            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
                    
                    except FileNotFoundError:
                        print(f"File {file_path} tidak ditemukan. Pastikan file tersebut ada dalam lokasi yang benar.")
                    except pd.errors.EmptyDataError:
                        print("File riwayat.csv kosong. Tidak ada data untuk ditampilkan.")
                    except Exception as e:
                        print(f"Terjadi kesalahan: {e}")
                history()
            elif tanya == "6":

                    def input_databaru():
                        try:
                            df = pd.read_csv("DataBase.csv")
                            df.columns = df.columns.str.strip()
                            print("Columns after stripping spaces:", df.columns)

                            required_columns = ['Nomor Barang','Kode Barang', 'Nama Produk', 'Jenis Barang', 'Merek Barang', 'Warna Barang', 'Harga', 'Stok']
                            if not all(column in df.columns for column in required_columns):
                                raise KeyError("Required columns are missing from the CSV file.")

                            Nomor_Barang = df['Nomor Barang'].tolist()
                            Nama_Produk = df['Nama Produk'].tolist()
                            Kode_Barang = df['Kode Barang'].tolist()

                        except FileNotFoundError:
                            print("Error: DatabaseBarang.csv file not found.")
                            return
                        except KeyError as e:
                            print(f"Error: {e}")
                            return

                        while True:
                            os.system("cls")

                            header = "Tambah Barang"
                            header = header.center(82)
                            print("="*82)
                            print(header)
                            print("="*82)
                            print(f"Jumlah barang saat ini ada {len(Nomor_Barang)} macam")
                            
                            try:
                                NoBar = int(input("Nomor Barang: "))
                            except ValueError:
                                print("Nomor Barang harus berupa angka.")
                                continue

                            if NoBar in Nomor_Barang:
                                os.system("cls")
                                alert = f"Nomor Barang {NoBar} Sudah Terdaftar".center(82)
                                print("="*82)
                                print(alert)
                                print("="*82)
                                continue  
                            
                            KodBar = input("Kode Barang: ")
                            os.system("cls")

                            if KodBar in Kode_Barang:
                                os.system("cls")
                                alert = f"Kode Barang {KodBar} Sudah Terdaftar".center(82)
                                print("="*82)
                                print(alert)
                                print("="*82)
                                continue 

                            NaPro = input("Nama Produk: ").upper()
                            os.system("cls")

                            if NaPro in Nama_Produk:
                                os.system("cls")
                                alert = f"Nama Produk {NaPro} Sudah Terdaftar".center(82)
                                print("="*82)
                                print(alert)
                                print("="*82)
                                continue 

                            JenisBarang = input("Jenis Barang: ").upper()
                            os.system("cls")

                            MerekBarang = input("Merek Barang: ").upper()
                            os.system("cls")

                            WarnaBarang = input("Warna Barang: ").upper()
                            os.system("cls")

                            while True:
                                Harga = input("Harga: ")
                                if Harga.isnumeric():
                                    Harga = int(Harga)
                                    break
                                else:
                                    os.system("cls")
                                    print("Harga harus berupa angka!")

                            os.system("cls")

                            while True:
                                Stok = input("Stok: ")
                                if Stok.isnumeric():
                                    Stok = int(Stok)
                                    break
                                else:
                                    os.system("cls")
                                    print("Stok harus berupa angka!")

                            os.system("cls")

                            data = {
                                "Nomor Barang": [NoBar],
                                "Kode Barang": [KodBar],
                                "Nama Produk": [NaPro],
                                "Jenis Barang": [JenisBarang],
                                "Merek Barang": [MerekBarang],
                                "Warna Barang": [WarnaBarang],
                                "Harga": [Harga],
                                "Stok": [Stok]
                            }
                            data_df = pd.DataFrame(data)

                            konfirmasi = "Data Barang".center(54)
                            Data_Barang = (f"Nomor Barang : {NoBar}\nKode Barang : {KodBar}\nNama Produk : {NaPro}\nJenis Barang : {JenisBarang}\nMerek Barang : {MerekBarang}\nWarna Barang : {WarnaBarang}\nHarga : {Harga}\nStok : {Stok}")
                            print("="*82)
                            print(konfirmasi)
                            print("="*82)
                            print(Data_Barang)
                            print("="*82)
                            print("Apakah data sudah benar?\n[1] Ya\n[2] Tidak")
                            perintah = input("Pilihan: ")

                            if perintah == "1":
                                os.system("cls")
                                final = pd.concat([df, data_df], ignore_index=True)
                                final.to_csv("DataBase.csv", index=False)
                                sukses = "Upload data Berhasil".center(82)
                                print("="*82)
                                print(sukses)
                                print("="*82)
                                input("Klik Enter untuk kembali")
                                os.system("cls")
                                menu(role)
                                break
                            elif perintah == "2":
                                os.system("cls")
                                gagal = "Upload Telah Dibatalkan".center(82)
                                print("="*82)
                                print(gagal)
                                print("="*82)
                                os.system("cls")
                                menu(role)
                                continue
                    input_databaru()

            elif tanya == "7":
                def hapus_data():
                    os.system("cls")
                    access = True
    
                    while access:
                        try:
                            os.system("cls")
                            df = pd.read_csv("DataBase.csv")
                            df.columns = df.columns.str.strip()
                            print("="*82)
                            print(tabulate(df[['Nomor Barang', 'Nama Produk']], headers='keys', tablefmt='fancy_grid', showindex=False))
                            print("="*82)

                            header = "Hapus Data Barang"
                            header = header.center(82)
                            print("="*82)
                            print(header)
                            print("="*82)
                            NoBara = input("Nomor Barang : ").strip()
            
                            if not NoBara.isdigit():
                                raise ValueError("Nomor Barang harus berupa bilangan bulat.")

                            Nomor_Barang = df['Nomor Barang'].astype(str).tolist()

                            if NoBara in Nomor_Barang:
                                lokasi = Nomor_Barang.index(NoBara)
                                data_barang = df.iloc[lokasi]

                                Header = "Data Barang"
                                Header = Header.center(82)
                                data_hapus = (f"Nomor Barang : {data_barang['Nomor Barang']}\n"
                                            f"Kode Barang : {data_barang['Kode Barang']}\n"
                                            f"Nama Produk : {data_barang['Nama Produk']}\n"
                                            f"Jenis Barang : {data_barang['Jenis Barang']}\n"
                                            f"Merek Barang : {data_barang['Merek Barang']}\n"
                                            f"Warna Barang : {data_barang['Warna Barang']}\n"
                                            f"Harga : {data_barang['Harga']}\n"
                                            f"Stok : {data_barang['Stok']}")
                                os.system("cls")

                                while True:
                                    os.system("cls")
                                    print("="*82)
                                    print(Header)
                                    print("="*82)
                                    print(data_hapus)
                                    print("="*82)
                                    print("[1] Hapus Data\n[2] Batalkan")
                                    opsi = input("Pilihan : ").strip()

                                    if opsi == "1":
                                        os.system("cls")
                                        df = df.drop(lokasi).reset_index(drop=True)
                                        df.to_csv("DataBase.csv", index=False)
                                        alert = "Penghapusan Data Berhasil"
                                        alert = alert.center(82)
                                        print("="*82)
                                        print(alert)
                                        print("="*82)
                                        input("Klik Enter untuk kembali")
                                        os.system("cls")
                                        menu(role)  
                                        break
                                    elif opsi == "2":
                                        os.system("cls")
                                        alert = "Penghapusan Data Telah Dibatalkan"
                                        alert = alert.center(82)
                                        print("="*82)
                                        print(alert)
                                        print("="*82)
                                        input("Klik Enter untuk kembali")
                                        os.system("cls")
                                        menu(role) 
                                        break
                            else:
                                os.system("cls")
                                alert = "Nomor Barang Belum Terdaftar"
                                alert = alert.center(82)
                                print("="*82)
                                print(alert)
                                print("="*82)
                        except ValueError as ve:
                            os.system("cls")
                            alert = str(ve)
                            alert = alert.center(82)
                            print("="*82)
                            print(alert)
                            print("="*82)
                            input("Klik Enter untuk kembali")
                            os.system("cls")
                            menu(role) 
                            break
                        except FileNotFoundError:
                            print("Error: DataBase.csv file not found.")
                        except KeyError as e:
                            print(f"Error: {e}")

                hapus_data()
                
            elif tanya == "8":
                def edit_data_barang():
                    header = "Edit Data Barang"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    nomor_barang = input("Masukkan nomor barang yang akan diedit: ")
                    file_barang = "DataBase.csv"
    
                    try:
                        df = pd.read_csv(file_barang)
                        barang = df[df['Nomor Barang'] == int(nomor_barang)]
        
                        if not barang.empty:
                            print("Data barang yang akan diedit:")
                            print(tabulate(barang, headers='keys', tablefmt='fancy_grid'))
    
                            nama_produk = input("Nama produk baru: ")
                            jenis_barang = input("Jenis barang baru: ")
                            merek_barang = input("Merek barang baru: ")
                            warna_barang = input("Warna barang baru: ")
                            harga_barang = float(input("Harga barang baru: ")) 
                            stok_barang = int(input("Stok barang baru: ")) 
            
                            df.loc[df['Nomor Barang'] == int(nomor_barang), 'Nama Produk'] = nama_produk
                            df.loc[df['Nomor Barang'] == int(nomor_barang), 'Jenis Barang'] = jenis_barang
                            df.loc[df['Nomor Barang'] == int(nomor_barang), 'Merek Barang'] = merek_barang
                            df.loc[df['Nomor Barang'] == int(nomor_barang), 'Warna Barang'] = warna_barang
                            df.loc[df['Nomor Barang'] == int(nomor_barang), 'Harga'] = harga_barang
                            df.loc[df['Nomor Barang'] == int(nomor_barang), 'Stok'] = stok_barang
            
                            df.to_csv(file_barang, index=False)
            
                            print("Data barang berhasil diperbarui.")
                        else:
                            print("Nomor barang tidak ditemukan dalam database.")
                    except FileNotFoundError:
                        print("File database tidak ditemukan.")
                    except ValueError:
                        print("Input tidak valid. Pastikan memasukkan data yang benar.")
                edit_data_barang()
                
            elif tanya == "9":
                def merge_sort(arr, key, reverse=False):
                    if len(arr) <= 1:
                        return arr
                    
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
                    
                    left_half = merge_sort(left_half, key, reverse=reverse)
                    right_half = merge_sort(right_half, key, reverse=reverse)
                    
                    return merge(left_half, right_half, key, reverse)

                def merge(left, right, key, reverse):
                    result = []
                    left_idx, right_idx = 0, 0
                    
                    while left_idx < len(left) and right_idx < len(right):
                        if (left[left_idx][key] > right[right_idx][key]) if reverse else (left[left_idx][key] <= right[right_idx][key]):
                            result.append(left[left_idx])
                            left_idx += 1
                        else:
                            result.append(right[right_idx])
                            right_idx += 1
                    
                    while left_idx < len(left):
                        result.append(left[left_idx])
                        left_idx += 1
                    
                    while right_idx < len(right):
                        result.append(right[right_idx])
                        right_idx += 1
                    
                    return result
                def buat_laporan_mingguan():
                    riwayat_df = pd.read_csv("Riwayat.csv")

                    riwayat_df['Tanggal'] = pd.to_datetime(riwayat_df['Tanggal']).dt.date

                    header = "Laporan Mingguan Data Barang"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    bulan = int(input("Masukkan bulan (1-12): "))
                    tahun = int(input("Masukkan tahun: "))
                    minggu_ke = int(input("Masukkan minggu ke-: "))

                    start_date = pd.Timestamp(year=tahun, month=bulan, day=1) + pd.Timedelta(weeks=(minggu_ke - 1))
                    start_date -= pd.to_timedelta(start_date.weekday(), unit='d') 
                    end_date = start_date + pd.Timedelta(days=6)  

                    if start_date.month != bulan:
                        start_date = pd.Timestamp(year=tahun, month=bulan, day=1)
                    end_of_month = pd.Timestamp(year=tahun, month=bulan % 12 + 1, day=1) - pd.Timedelta(days=1)
                    if end_date > end_of_month:
                        end_date = end_of_month

                    transaksi_minggu_ini = riwayat_df[(riwayat_df['Tanggal'] >= start_date.date()) & (riwayat_df['Tanggal'] <= end_date.date())]
                    if transaksi_minggu_ini.empty:
                        print("Tidak ada riwayat pada tanggal tersebut.")
                        return

                    print("Pilih jenis pengurutan:")
                    print("1. Barang Masuk")
                    print("2. Barang Keluar")
                    pilihan = int(input("Masukkan pilihan: "))

                    if pilihan == 1:
                        transaksi_terurut = transaksi_minggu_ini[transaksi_minggu_ini['Status'] == 'Masuk']
                        jenis_transaksi = "Masuk"
                    elif pilihan == 2:
                        transaksi_terurut = transaksi_minggu_ini[transaksi_minggu_ini['Status'] == 'Keluar']
                        jenis_transaksi = "Keluar"
                    else:
                        print("Pilihan tidak valid.")
                        return

                    transaksi_terurut = transaksi_terurut.to_dict(orient='records')
                    transaksi_terurut = merge_sort(transaksi_terurut, key='Jumlah', reverse=True)
                    

                    transaksi_terurut = pd.DataFrame(transaksi_terurut)

                    total_transaksi = len(transaksi_terurut)
                    total_barang = transaksi_terurut['Jumlah'].sum()
                    
                    if pilihan == 1:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Masuk", total_barang]
                        ]
                    elif pilihan == 2:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Keluar", total_barang]
                        ]

                    print(f"===== Laporan Minggu ke-{minggu_ke} Bulan {bulan} Tahun {tahun} =====")
                    print(f"Jenis Pengurutan: Barang {jenis_transaksi}")
                    print(tabulate(data_table, headers=["Keterangan", "Jumlah"], tablefmt="fancy_grid"))

                    print("\nData Barang:")
                    print(tabulate(transaksi_terurut, headers="keys", tablefmt="fancy_grid", showindex=False))

                buat_laporan_mingguan()
            elif tanya == "10":
                def merge_sort(arr, key, reverse=False):
                    if len(arr) <= 1:
                        return arr
                    
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
                    
                    left_half = merge_sort(left_half, key, reverse=reverse)
                    right_half = merge_sort(right_half, key, reverse=reverse)
                    
                    return merge(left_half, right_half, key, reverse)

                def merge(left, right, key, reverse):
                    result = []
                    left_idx, right_idx = 0, 0
                    
                    while left_idx < len(left) and right_idx < len(right):
                        if (left[left_idx][key] > right[right_idx][key]) if reverse else (left[left_idx][key] <= right[right_idx][key]):
                            result.append(left[left_idx])
                            left_idx += 1
                        else:
                            result.append(right[right_idx])
                            right_idx += 1
                    
                    while left_idx < len(left):
                        result.append(left[left_idx])
                        left_idx += 1
                    
                    while right_idx < len(right):
                        result.append(right[right_idx])
                        right_idx += 1
                    
                    return result

                def buat_laporan_bulanan():
                    riwayat_df = pd.read_csv("Riwayat.csv")

                    riwayat_df['Tanggal'] = pd.to_datetime(riwayat_df['Tanggal']).dt.date
                    header = "Laporan Bulanan Data Barang"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    bulan = int(input("Masukkan bulan (1-12): "))
                    tahun = int(input("Masukkan tahun: "))

                    start_date = pd.Timestamp(year=tahun, month=bulan, day=1)
                    end_date = pd.Timestamp(year=tahun, month=bulan % 12 + 1, day=1) - pd.Timedelta(days=1)
                    transaksi_bulan_ini = riwayat_df[(riwayat_df['Tanggal'] >= start_date.date()) & (riwayat_df['Tanggal'] <= end_date.date())]

                    if transaksi_bulan_ini.empty:
                        print("Tidak ada riwayat pada tanggal tersebut.")
                        return

                    print("Pilih jenis pengurutan:")
                    print("1. Barang Masuk")
                    print("2. Barang Keluar")
                    pilihan = int(input("Masukkan pilihan: "))

                    if pilihan == 1:
                        transaksi_terurut = transaksi_bulan_ini[transaksi_bulan_ini['Status'] == 'Masuk']
                        jenis_transaksi = "Masuk"
                    elif pilihan == 2:
                        transaksi_terurut = transaksi_bulan_ini[transaksi_bulan_ini['Status'] == 'Keluar']
                        jenis_transaksi = "Keluar"
                    else:
                        print("Pilihan tidak valid.")
                        return

                    transaksi_terurut = transaksi_terurut.to_dict(orient='records')
                    transaksi_terurut = merge_sort(transaksi_terurut, key='Jumlah', reverse=True)

                    transaksi_terurut = pd.DataFrame(transaksi_terurut)

                    total_transaksi = len(transaksi_terurut)
                    total_barang = transaksi_terurut['Jumlah'].sum()
                    
                    if pilihan == 1:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Masuk", total_barang]
                        ]
                    elif pilihan == 2:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Keluar", total_barang]
                        ]

                    print(f"===== Laporan Rekapan Bulan {bulan} Tahun {tahun} =====")
                    print(f"Jenis Pengurutan: Barang {jenis_transaksi}")
                    print(tabulate(data_table, headers=["Keterangan", "Jumlah"], tablefmt="fancy_grid"))

                    print("\nData Barang:")
                    print(tabulate(transaksi_terurut, headers="keys", tablefmt="fancy_grid", showindex=False))

                buat_laporan_bulanan()

            elif tanya == "11":
                def get_data_from_csv(csv_filename):
                    data = []
                    today = datetime.date.today()
                    thirty_days_ago = today - datetime.timedelta(days=30)

                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            if row['Status'].lower() == 'masuk': 
                                row_date = datetime.datetime.strptime(row['Tanggal'], '%Y-%m-%d').date()
                                if row_date >= thirty_days_ago: 
                                    row['Jumlah'] = int(row['Jumlah'])  
                                    data.append(row)
                    return data, thirty_days_ago, today

                def group_by_brand_and_item_type(data):
                    grouped_data = defaultdict(lambda: defaultdict(int))
    
                    for row in data:
                        brand = row['Merek']
                        item_type = row['Jenis Barang']
                        grouped_data[brand][item_type] += row['Jumlah'] 
                    return grouped_data

                def group_by_item_type(data):
                    grouped_data = defaultdict(int)
    
                    for row in data:
                        item_type = row['Jenis Barang']
                        grouped_data[item_type] += row['Jumlah']
                    return grouped_data

                def merge_sort(arr, key, reverse=False):
                    if len(arr) <= 1:
                        return arr
    
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
    
                    left_half = merge_sort(left_half, key, reverse=reverse)
                    right_half = merge_sort(right_half, key, reverse=reverse)
                    return merge(left_half, right_half, key, reverse)

                def merge(left, right, key, reverse):
                    result = []
                    left_idx, right_idx = 0, 0
    
                    while left_idx < len(left) and right_idx < len(right):
                        if (key(left[left_idx]) > key(right[right_idx])) if reverse else (key(left[left_idx]) <= key(right[right_idx])):
                            result.append(left[left_idx])
                            left_idx += 1
                        else:
                            result.append(right[right_idx])
                            right_idx += 1
    
                    while left_idx < len(left):
                        result.append(left[left_idx])
                        left_idx += 1
    
                    while right_idx < len(right):
                        result.append(right[right_idx])
                        right_idx += 1
    
                    return result

                def display_sorted_by_brand(grouped_data, date_range):
                    all_item_types = set()
                    for items in grouped_data.values():
                        all_item_types.update(items.keys())
                    all_item_types = sorted(all_item_types)
    
                    rows = []
                    for brand, items in grouped_data.items():
                        row = [brand] + [items.get(item_type, 0) for item_type in all_item_types]
                        row.append(sum(items.values()))
                        rows.append(row)
    
                    headers = ['Merek'] + all_item_types + ['Total Jumlah']

                    rows = merge_sort(rows, key=lambda x: x[-1], reverse=True)
    
                    print(f"\nKategori merek terpopuler \n(dari {date_range[0]} hingga {date_range[1]}):")
                    print(tabulate(rows, headers, tablefmt="fancy_grid"))

                def display_sorted_by_item_type(grouped_data, date_range):
                    rows = [[item_type, total_jumlah] for item_type, total_jumlah in grouped_data.items()]
    
                    headers = ['Jenis Barang', 'Total Jumlah']

                    rows = merge_sort(rows, key=lambda x: x[1], reverse=True)

                    print(f"\nKategori jenis barang terpopuler \n(dari {date_range[0]} hingga {date_range[1]}):")
                    print(tabulate(rows, headers, tablefmt="fancy_grid"))

                def main():
                    csv_filename = 'Riwayat.csv'

                    data, start_date, end_date = get_data_from_csv(csv_filename)
                    date_range = (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                    print("="*82)
                    print("KATEGORI TERPOPULER ELECTROBUY".center(82))
                    print("-"*82)
                    print("hint: menampilkan barang terpopuler dalam 30 hari terakhir berdasarkan aktivitas\nriwayat. Indikator penilaian berasal dari jumlah barang masuk terbanyak yang\nmasuk ke gudang selama periode tersebut.")
                    print("="*82)
                    print("\nPilih metode pengurutan:")
                    print("1. Berdasarkan merek terpopuler")
                    print("2. Berdasarkan jenis barang terpopuler")
                    choice = input("Masukkan pilihan (1 atau 2): ").strip()

                    if choice == '1':
                        grouped_data = group_by_brand_and_item_type(data)
                        display_sorted_by_brand(grouped_data, date_range)
                    elif choice == '2':
                        grouped_data = group_by_item_type(data)
                        display_sorted_by_item_type(grouped_data, date_range)
                    else:
                        print("Pilihan tidak valid.")
                main()

            elif tanya == "12":
                os.system("cls")
                closing = "Terima Kasih Telah Menggunakan Layanan Kami"
                closing = closing.center(82)
                print("=" * 82)
                print(closing)
                print("=" * 82)
                input("Tekan Enter Untuk Lanjut")
                os.system("cls")
                break
            else:
                print("Pilihan tidak valid")
        elif role == "Owner":
            if tanya == "1":
                def history():
                    os.system("cls")
                    print("="*82)
                    print("ELECTROBUY".center(82))
                    print("-"*82)
                    print("Daftar Riwayat Gudang".center(82))
                    print("="*82)
                    print(" ")

                    file_path = "riwayat.csv"
                    
                    try:
                        df = pd.read_csv(file_path, on_bad_lines='skip')
                        
                        if df.empty:
                            print("File riwayat.csv kosong. Tidak ada data untuk ditampilkan.")
                        else:
                            print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
                    
                    except FileNotFoundError:
                        print(f"File {file_path} tidak ditemukan. Pastikan file tersebut ada dalam lokasi yang benar.")
                    except pd.errors.EmptyDataError:
                        print("File riwayat.csv kosong. Tidak ada data untuk ditampilkan.")
                    except Exception as e:
                        print(f"Terjadi kesalahan: {e}")
                history()
            elif tanya == "2":
                def load_data(csv_filename):
                    data = []
                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            data.append(row)
                    return data

                def print_product_details(product):
                    print(f"Nomor Barang: {product['Nomor Barang']}")
                    print(f"Kode Barang: {product['Kode Barang']}")
                    print(f"Nama Produk: {product['Nama Produk']}")
                    print(f"Jenis Barang: {product['Jenis Barang']}")
                    print(f"Merek Barang: {product['Merek Barang']}")
                    print(f"Warna Barang: {product['Warna Barang']}")
                    print(f"Harga: {product['Harga']}")
                    print(f"Stok: {product['Stok']}")

                def find_product_by_number(data, product_number):
                    for product in data:
                        if product['Nomor Barang'] == product_number:
                            return product
                    return None

                def data_satuan():
                    csv_filename = 'DataBase.csv'
                    data = load_data(csv_filename)
                    
                    table_data = [(product['Nomor Barang'], product['Nama Produk']) for product in data]
                    print(tabulate(table_data, headers=["Nomor Barang", "Nama Produk"], tablefmt="fancy_grid"))

                    header = "Data Barang Satuan"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    
                    product_number = input("Masukkan nomor barang: ")
                    
                    product = find_product_by_number(data, product_number)
                    
                    if product:
                        print("="*82)
                        print_product_details(product)
                        print("="*82)
                    else:
                        alert = "Nomor barang tidak ditemukan."
                        alert = alert.center(82)
                        print("="*82)
                        print(alert)
                        print("="*82)
                data_satuan()
            elif tanya == "3":
                def get_unique_values(csv_filename, column_name):
                    values = set()

                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)

                        for row in csv_reader:
                            values.add(row[column_name])

                    return sorted(values)

                def search_by_brand_and_type(csv_filename, brand_name, item_type):
                    results = []

                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)

                        for row in csv_reader:
                            if (row['Merek Barang'].lower() == brand_name.lower() and
                                row['Jenis Barang'].lower() == item_type.lower()):
                                results.append(row)

                    return results

                def seluruh_barang():
                    csv_filename = 'DataBase.csv'

                    while True:
                        unique_brands = get_unique_values(csv_filename, 'Merek Barang')
                        unique_item_types = get_unique_values(csv_filename, 'Jenis Barang')

                        
                        header = "Data Barang Keseluruhan"
                        header = header.center(82)
                        print("="*82)
                        print(header)
                        print("="*82)
                        print("Pilih merek barang yang ingin dilihat:")
                        for idx, brand in enumerate(unique_brands, start=1):
                            print(f"{idx}. {brand}")

                        while True:
                            brand_choice = input("Masukkan nomor pilihan merek (atau tekan 'Enter' untuk kembali ke menu): ")
                            if brand_choice == "":
                                return 
                            try:
                                brand_choice = int(brand_choice)
                                if 1 <= brand_choice <= len(unique_brands):
                                    break
                                else:
                                    print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")
                            except ValueError:
                                print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")

                        selected_brand = unique_brands[brand_choice - 1]

                        print("Pilih jenis barang yang ingin dilihat:")
                        for idx, item_type in enumerate(unique_item_types, start=1):
                            print(f"{idx}. {item_type}")

                        while True:
                            item_type_choice = input("Masukkan nomor pilihan jenis barang: ")
                            try:
                                item_type_choice = int(item_type_choice)
                                if 1 <= item_type_choice <= len(unique_item_types):
                                    break
                                else:
                                    print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")
                            except ValueError:
                                print("Nomor pilihan tidak valid. Harap masukkan nomor yang valid.")

                        selected_item_type = unique_item_types[item_type_choice - 1]

                        matching_products = search_by_brand_and_type(csv_filename, selected_brand, selected_item_type)

                        if matching_products:
                            print(f"\nBarang-barang dengan merek '{selected_brand}' dan jenis '{selected_item_type}':")
                            headers = matching_products[0].keys()
                            rows = [product.values() for product in matching_products]
                            print(tabulate(rows, headers, tablefmt="fancy_grid"))
                        else:
                            print(f"Tidak ada barang dengan merek '{selected_brand}' dan jenis '{selected_item_type}' yang ditemukan.")
                seluruh_barang()
            elif tanya == "4":
                def merge_sort(arr, key, reverse=False):
                    if len(arr) <= 1:
                        return arr
                    
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
                    
                    left_half = merge_sort(left_half, key, reverse=reverse)
                    right_half = merge_sort(right_half, key, reverse=reverse)
                    
                    return merge(left_half, right_half, key, reverse)

                def merge(left, right, key, reverse):
                    result = []
                    left_idx, right_idx = 0, 0
                    
                    while left_idx < len(left) and right_idx < len(right):
                        if (left[left_idx][key] > right[right_idx][key]) if reverse else (left[left_idx][key] <= right[right_idx][key]):
                            result.append(left[left_idx])
                            left_idx += 1
                        else:
                            result.append(right[right_idx])
                            right_idx += 1
                    
                    while left_idx < len(left):
                        result.append(left[left_idx])
                        left_idx += 1
                    
                    while right_idx < len(right):
                        result.append(right[right_idx])
                        right_idx += 1
                    
                    return result
                def buat_laporan_mingguan():
                    riwayat_df = pd.read_csv("Riwayat.csv")

                    riwayat_df['Tanggal'] = pd.to_datetime(riwayat_df['Tanggal']).dt.date

                    header = "Laporan Mingguan Data Barang"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    bulan = int(input("Masukkan bulan (1-12): "))
                    tahun = int(input("Masukkan tahun: "))
                    minggu_ke = int(input("Masukkan minggu ke-: "))

                    start_date = pd.Timestamp(year=tahun, month=bulan, day=1) + pd.Timedelta(weeks=(minggu_ke - 1))
                    start_date -= pd.to_timedelta(start_date.weekday(), unit='d') 
                    end_date = start_date + pd.Timedelta(days=6)  

                    if start_date.month != bulan:
                        start_date = pd.Timestamp(year=tahun, month=bulan, day=1)
                    end_of_month = pd.Timestamp(year=tahun, month=bulan % 12 + 1, day=1) - pd.Timedelta(days=1)
                    if end_date > end_of_month:
                        end_date = end_of_month

                    transaksi_minggu_ini = riwayat_df[(riwayat_df['Tanggal'] >= start_date.date()) & (riwayat_df['Tanggal'] <= end_date.date())]
                    if transaksi_minggu_ini.empty:
                        print("Tidak ada riwayat pada tanggal tersebut.")
                        return

                    print("Pilih jenis pengurutan:")
                    print("1. Barang Masuk")
                    print("2. Barang Keluar")
                    pilihan = int(input("Masukkan pilihan: "))

                    if pilihan == 1:
                        transaksi_terurut = transaksi_minggu_ini[transaksi_minggu_ini['Status'] == 'Masuk']
                        jenis_transaksi = "Masuk"
                    elif pilihan == 2:
                        transaksi_terurut = transaksi_minggu_ini[transaksi_minggu_ini['Status'] == 'Keluar']
                        jenis_transaksi = "Keluar"
                    else:
                        print("Pilihan tidak valid.")
                        return

                    transaksi_terurut = transaksi_terurut.to_dict(orient='records')
                    transaksi_terurut = merge_sort(transaksi_terurut, key='Jumlah', reverse=True)
                    

                    transaksi_terurut = pd.DataFrame(transaksi_terurut)

                    total_transaksi = len(transaksi_terurut)
                    total_barang = transaksi_terurut['Jumlah'].sum()
                    
                    if pilihan == 1:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Masuk", total_barang]
                        ]
                    elif pilihan == 2:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Keluar", total_barang]
                        ]

                    print(f"===== Laporan Minggu ke-{minggu_ke} Bulan {bulan} Tahun {tahun} =====")
                    print(f"Jenis Pengurutan: Barang {jenis_transaksi}")
                    print(tabulate(data_table, headers=["Keterangan", "Jumlah"], tablefmt="fancy_grid"))

                    print("\nData Barang:")
                    print(tabulate(transaksi_terurut, headers="keys", tablefmt="fancy_grid", showindex=False))

                buat_laporan_mingguan()
            elif tanya == "5":
                def merge_sort(arr, key, reverse=False):
                    if len(arr) <= 1:
                        return arr
                    
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
                    
                    left_half = merge_sort(left_half, key, reverse=reverse)
                    right_half = merge_sort(right_half, key, reverse=reverse)
                    
                    return merge(left_half, right_half, key, reverse)

                def merge(left, right, key, reverse):
                    result = []
                    left_idx, right_idx = 0, 0
                    
                    while left_idx < len(left) and right_idx < len(right):
                        if (left[left_idx][key] > right[right_idx][key]) if reverse else (left[left_idx][key] <= right[right_idx][key]):
                            result.append(left[left_idx])
                            left_idx += 1
                        else:
                            result.append(right[right_idx])
                            right_idx += 1
                    
                    while left_idx < len(left):
                        result.append(left[left_idx])
                        left_idx += 1
                    
                    while right_idx < len(right):
                        result.append(right[right_idx])
                        right_idx += 1
                    
                    return result
                def buat_laporan_bulanan():
                    riwayat_df = pd.read_csv("Riwayat.csv")

                    riwayat_df['Tanggal'] = pd.to_datetime(riwayat_df['Tanggal']).dt.date
                    header = "Laporan Bulanan Data Barang"
                    header = header.center(82)
                    print("="*82)
                    print(header)
                    print("="*82)
                    bulan = int(input("Masukkan bulan (1-12): "))
                    tahun = int(input("Masukkan tahun: "))

                    start_date = pd.Timestamp(year=tahun, month=bulan, day=1)
                    end_date = pd.Timestamp(year=tahun, month=bulan % 12 + 1, day=1) - pd.Timedelta(days=1)
                    transaksi_bulan_ini = riwayat_df[(riwayat_df['Tanggal'] >= start_date.date()) & (riwayat_df['Tanggal'] <= end_date.date())]
                    if transaksi_bulan_ini.empty:
                        print("Tidak ada riwayat pada tanggal tersebut.")
                        return

                    print("Pilih jenis pengurutan:")
                    print("1. Barang Masuk")
                    print("2. Barang Keluar")
                    pilihan = int(input("Masukkan pilihan: "))

                    if pilihan == 1:
                        transaksi_terurut = transaksi_bulan_ini[transaksi_bulan_ini['Status'] == 'Masuk']
                        jenis_transaksi = "Masuk"
                    elif pilihan == 2:
                        transaksi_terurut = transaksi_bulan_ini[transaksi_bulan_ini['Status'] == 'Keluar']
                        jenis_transaksi = "Keluar"
                    else:
                        print("Pilihan tidak valid.")
                        return

                    transaksi_terurut = transaksi_terurut.to_dict(orient='records')
                    transaksi_terurut = merge_sort(transaksi_terurut, key='Jumlah', reverse=True)

                    transaksi_terurut = pd.DataFrame(transaksi_terurut)

                    total_transaksi = len(transaksi_terurut)
                    total_barang = transaksi_terurut['Jumlah'].sum()
                    
                    if pilihan == 1:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Masuk", total_barang]
                        ]
                    elif pilihan == 2:
                        data_table = [
                            ["Total Transaksi", total_transaksi],
                            ["Total Barang Keluar", total_barang]
                        ]

                    print(f"===== Laporan Rekapan Bulan {bulan} Tahun {tahun} =====")
                    print(f"Jenis Pengurutan: Barang {jenis_transaksi}")
                    print(tabulate(data_table, headers=["Keterangan", "Jumlah"], tablefmt="fancy_grid"))

                    print("\nData Barang:")
                    print(tabulate(transaksi_terurut, headers="keys", tablefmt="fancy_grid", showindex=False))

                buat_laporan_bulanan()
            elif tanya == "6":
                def get_data_from_csv(csv_filename):
                    data = []
                    today = datetime.date.today()
                    thirty_days_ago = today - datetime.timedelta(days=30)

                    with open(csv_filename, mode='r', encoding='utf-8') as file:
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            if row['Status'].lower() == 'masuk': 
                                row_date = datetime.datetime.strptime(row['Tanggal'], '%Y-%m-%d').date()
                                if row_date >= thirty_days_ago: 
                                    row['Jumlah'] = int(row['Jumlah'])  
                                    data.append(row)
                    return data, thirty_days_ago, today

                def group_by_brand_and_item_type(data):
                    grouped_data = defaultdict(lambda: defaultdict(int))
    
                    for row in data:
                        brand = row['Merek']
                        item_type = row['Jenis Barang']
                        grouped_data[brand][item_type] += row['Jumlah'] 
                    return grouped_data

                def group_by_item_type(data):
                    grouped_data = defaultdict(int)
    
                    for row in data:
                        item_type = row['Jenis Barang']
                        grouped_data[item_type] += row['Jumlah']
                    return grouped_data

                def merge_sort(arr, key, reverse=False):
                    if len(arr) <= 1:
                        return arr
    
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]
    
                    left_half = merge_sort(left_half, key, reverse=reverse)
                    right_half = merge_sort(right_half, key, reverse=reverse)
                    return merge(left_half, right_half, key, reverse)

                def merge(left, right, key, reverse):
                    result = []
                    left_idx, right_idx = 0, 0
    
                    while left_idx < len(left) and right_idx < len(right):
                        if (key(left[left_idx]) > key(right[right_idx])) if reverse else (key(left[left_idx]) <= key(right[right_idx])):
                            result.append(left[left_idx])
                            left_idx += 1
                        else:
                            result.append(right[right_idx])
                            right_idx += 1
    
                    while left_idx < len(left):
                        result.append(left[left_idx])
                        left_idx += 1
    
                    while right_idx < len(right):
                        result.append(right[right_idx])
                        right_idx += 1
    
                    return result

                def display_sorted_by_brand(grouped_data, date_range):
                    all_item_types = set()
                    for items in grouped_data.values():
                        all_item_types.update(items.keys())
                    all_item_types = sorted(all_item_types)
    
                    rows = []
                    for brand, items in grouped_data.items():
                        row = [brand] + [items.get(item_type, 0) for item_type in all_item_types]
                        row.append(sum(items.values()))
                        rows.append(row)
    
                    headers = ['Merek'] + all_item_types + ['Total Jumlah']

                    rows = merge_sort(rows, key=lambda x: x[-1], reverse=True)
    
                    print(f"\nKategori merek terpopuler \n(dari {date_range[0]} hingga {date_range[1]}):")
                    print(tabulate(rows, headers, tablefmt="fancy_grid"))

                def display_sorted_by_item_type(grouped_data, date_range):
                    rows = [[item_type, total_jumlah] for item_type, total_jumlah in grouped_data.items()]
    
                    headers = ['Jenis Barang', 'Total Jumlah']

                    rows = merge_sort(rows, key=lambda x: x[1], reverse=True)

                    print(f"\nKategori jenis barang terpopuler \n(dari {date_range[0]} hingga {date_range[1]}):")
                    print(tabulate(rows, headers, tablefmt="fancy_grid"))

                def main():
                    csv_filename = 'Riwayat.csv'

                    data, start_date, end_date = get_data_from_csv(csv_filename)
                    date_range = (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                    print("="*82)
                    print("KATEGORI TERPOPULER ELECTROBUY".center(82))
                    print("-"*82)
                    print("hint: menampilkan barang terpopuler dalam 30 hari terakhir berdasarkan aktivitas\nriwayat. Indikator penilaian berasal dari jumlah barang masuk terbanyak yang\nmasuk ke gudang selama periode tersebut.")
                    print("="*82)
                    print("\nPilih metode pengurutan:")
                    print("1. Berdasarkan merek terpopuler")
                    print("2. Berdasarkan jenis barang terpopuler")
                    choice = input("Masukkan pilihan (1 atau 2): ").strip()

                    if choice == '1':
                        grouped_data = group_by_brand_and_item_type(data)
                        display_sorted_by_brand(grouped_data, date_range)
                    elif choice == '2':
                        grouped_data = group_by_item_type(data)
                        display_sorted_by_item_type(grouped_data, date_range)
                    else:
                        print("Pilihan tidak valid.")
                main()
            elif tanya == "7":
                os.system("cls")
                closing = "Terima Kasih Telah Menggunakan Layanan Kami"
                closing = closing.center(82)
                print("=" * 82)
                print(closing)
                print("=" * 82)
                input("Tekan Enter Untuk Lanjut")
                os.system("cls")
                break
            else:
                print("Pilihan tidak valid")
        else:
            print("Pilihan tidak valid")

        input("Tekan Enter Untuk Melanjutkan")
        os.system("cls")
        menu(role)
        tanya = input("Pilihan : ")
        

pembukaan()
status, role = login()
if status == "Safe":
    navigasi(role)
else:
    print("Login gagal. Silakan coba lagi.")
