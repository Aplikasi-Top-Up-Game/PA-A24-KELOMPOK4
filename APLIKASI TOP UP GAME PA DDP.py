import json
import pwinput
from prettytable import PrettyTable
import os

os.system("cls")

# Path File JSON
USERS_FILE = r"C:\Users\ASUS\Documents\belajar json 1\data_login.json"
GAME_FILE = r"C:\Users\ASUS\Documents\belajar json 1\gametopup.json"

           
def buka_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return []
    except json.JSONDecodeError:
        print("Error saat membaca json")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membuka data pengguna: {e}")
        return[]

def simpan_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data berhasil disimpan.")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan.")

# Fungsi Registrasi user
def buat_akun(users):
    os.system('cls')
    users = buka_data(USERS_FILE)
    print("\n==== Register Akun ====")
    
    while True:
        try:
            username = input("Masukkan username anda: ").strip()
            if not username:
                print("Username tidak boleh kosong.")
                print("-"*40)
                continue

            for user in users:
                if user['username'] == username:
                    print("Username sudah terdaftar. Silakan buat username yang berbeda.")
                    print("-"*40)
                    break 
            else:
                password = pwinput.pwinput("Masukkan password: ").strip()
                if not password:
                    print("Password tidak boleh kosong.")
                    print("-"*40)
                    continue

                role = "user"
                users.append({
                    "username": username,
                    "password": password,
                    "role": role,
                    "saldo": 0  
                })

                simpan_data(USERS_FILE, users)
                print("Registrasi berhasil!")
                return True

        except KeyboardInterrupt:
            print("Pendaftaran dibatalkan. Harap jangan tekan CTRL + C!")
            return False  
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    

# Fungsi Login User
def login_admin(users):
    os.system('cls')
    print("=== Login Ke Akun Admin ===")
    while True:
        try:
            username = input("Masukkan username Akun Admin anda: ").strip()
            if not username:
                print("Username tidak boleh kosong.")
                print("-"*40)
                continue
            
            password = pwinput.pwinput("Masukkan password Akun Admin anda: ").strip()
            if not password:
                    print("Password tidak boleh kosong.")
                    print("-"*40)
                    continue
  
            for user in users:
                if user["username"] == username and user["password"] == password:
                    if user["role"] == "admin":
                        print("Login Berhasil!")
                        print(f"\n===== SELAMAT DATANG {username}! ⸜(｡˃ ᵕ ˂ )⸝♡ ======")
                        return user
                    else: 
                        print("Anda bukanlah admin! Silakan login lagi.")
                        break
            
            print("Username atau Password salah. Silakan coba lagi.")
            print("-"*40)
        except KeyboardInterrupt:
            print("Terjadi kesalahan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

      
def login_user(users):
    os.system('cls')
    print("=== Login Ke Akun Pengguna ===")
    while True:
        try:
            username = input("Masukkan username akun user anda: ").strip()
            if not username:
                print("Username tidak boleh kosong.")
                print("-" * 40)
                continue
            
            password = pwinput.pwinput("Masukkan password akun user anda: ").strip()
            if not password:
                print("Password tidak boleh kosong.")
                print("-" * 40)
                continue

            pengguna_ditemukan = False  
            for user in users:
                if user["username"] == username and user["password"] == password:
                    if user["role"] == "user":
                        print("Login Berhasil!")
                        print(f"\n===== SELAMAT DATANG {username}! ⸜(｡˃ ᵕ ˂ )⸝♡ ======")
                        return user
                    else: 
                        print("Anda bukanlah pengguna! Silakan login lagi.")
                        print("-" * 40)
                        break
                pengguna_ditemukan = True  

            if not pengguna_ditemukan:
                print("Username atau Password salah. Silakan coba lagi.")
                print("-" * 40)

        except KeyboardInterrupt:
            print("\nTerjadi kesalahan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def keluar(users):
    os.system('cls')
    while True:
        try:
            print("\n=== Keluar dari menu ===")
            keluar = input("Apakah anda yakin ingin keluar dari menu? (y/t): ")
            if keluar == "t":
                return users
            elif keluar == "y":
                main()
            else:
                print("Input tidak valid.")
                continue
        except KeyboardInterrupt:
            print("\nTerjadi kesalahan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")   

def kembali_admin(users):
    os.system('cls')
    while True:
        try:
            print("\n=== Kembali ke Menu ===")
            kembali = input("Apakah anda yakin ingin kembali? (y/t): ").lower()
            if kembali == "y":
                menu_admin(users)
            elif kembali == "t":
                return users
            else:
                print("Input tidak valid.")
                continue
        except KeyboardInterrupt:
            print("\nTerjadi kesalahan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            
# Fungsi menampilkan game
def tampilkan_game(data, title):
    if not data:
        print(f"\n{title} tidak tersedia.\n")
        return False

    table = PrettyTable()
    table.field_names = ["No", "Game"]
    
    for nomor, info in data.items():
        table.add_row([nomor, info["nama"]])
        
    print(f"\n{title}\n{table}")

# Fungsi menampilkan produk (read)
def tampilkan_produk(data, title):
    table = PrettyTable()
    table.field_names = ["No", "Paket", "Harga"]
    if not data:
        print(f"\n{title} saat ini masih kosong.\n")
        print(table)
        return False
    
    for item in data:
        table.add_row([item["No"], item["paket"], str(item["harga"])])
    print(f"{title}\n{table}")
    return True
  
# Fungsi Menambah game yang tersedia
def tambah_game(data):
    data = buka_data(GAME_FILE)
    tampilkan_game(data, "Game yang tersedia saat ini")
    
    while True: 
        try:
            no_game = input("Masukkan nomor game yang ingin ditambah: ").strip()
            if not no_game:
                print("Nomor game tidak boleh kosong.")
                print("-"*40)
                continue
            
            if not no_game.isdigit():
                print("Nomor game harus berupa angka.")
                print("-"*40)
                continue
            
            
            game = input("Masukkan nama game yang ingin ditambah: ").strip()
            if not game:
                    print("Nama game tidak boleh kosong.")
                    print("-"*40)
                    continue
                
            if no_game in data:
                print("Nomor game sudah terisi. Harap masukkan nomor game yang baru. ")
                print("-"*40)
                continue
            
            if any(game_info["nama"] == game for game_info in data.values()):
                print("Game sudah ada. Harap masukkan game yang berbeda.")
                print("-"*40)
                continue
                
            data[no_game]= {
                "nama": game, 
                "paket_topup": []
            }
                
            simpan_data(GAME_FILE, data)
            print("\n===== Game berhasil ditambahkan =====")   
            tambah_topup(data, no_game)
            tampilkan_game(data, "Game setelah ditambah: ")
            break
        except KeyboardInterrupt:
            print("\nTerjadi kesalahan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

           
# Fungsi menambahkan paket top-up secara dinamis
def tambah_topup(data, no_game):
    while True:
        try:
            if no_game in data:
                data_game = data[no_game]
                game = data_game["nama"]
                paket_topup = data_game["paket_topup"]
                tampilkan_produk(paket_topup, f"=== Paket top up ===")
            
                while True:
                    try: 
                        no = input("Masukkan nomor paket yang ingin ditambahkan: ").strip()
                        if not no:
                            print("Nomor paket tidak boleh kosong.")
                            print("-" * 40)
                            continue

                        if not no.isdigit():
                            print("Nomor paket harus berupa angka.")
                            print("-" * 40)
                            continue
                        
                        if any(paket["No"] == no for paket in paket_topup):
                            print("Nomor paket sudah ada. Harap masukkan nomor yang baru.")
                            print("-" * 40)
                            continue

                        paket = input("Masukkan nama paket Top-up yang ingin ditambahkan: ").strip()
                        if not paket:
                            print("Nama paket tidak boleh kosong.")
                            print("-" * 40)
                            continue
                        
                        if any(paket["paket"] == paket for paket in paket_topup):
                            print("Nama paket sudah ada. Harap masukkan nama yang baru.")
                            print("-" * 40)
                            continue
                        
                        while True:
                            try: 
                                harga = int(input("Masukkan harga paket: "))
                                break
                            except ValueError:
                                print("Input tidak valid. Harap masukkan angka")
                            
                        paket_topup.append({
                            "No": no, 
                            "paket": paket,
                            "harga": harga
                        })

                        simpan_data(GAME_FILE, data)
                        print("Paket Top-Up berhasil ditambahkan!\n")
                        tampilkan_produk(paket_topup, f"===== Paket Top Up =====")
                        return
                
                    except ValueError:
                        print("Input tidak valid.")
                        break
        except KeyboardInterrupt:
            print("Terjadi kesalahan. Harap jangan tekan CTRL + C!") 
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break

# Fungsi update game
def update_product(products):
    while True:
        try:
            tampilkan_game(products, "Game yang tersedia")
            no_game = input("Masukkan nomor game yang ingin di-update: ")
            
            if no_game in products:
                game_baru = input("Masukkan nama game baru: ")
                
                # Cek apakah nama game baru sudah ada
                for data in products.values():
                    if data['nama'] == game_baru:
                        print("Game sudah ada.")
                        return 
                
                # Update nama game
                data_game = products[no_game]
                data_game['nama'] = game_baru  # Update nama game
                simpan_data(GAME_FILE, products)

                print(f"Nama game berhasil di-update dari '{no_game}' menjadi '{game_baru}'!")
                tampilkan_game(products, "==== Game setelah di-update ====")
                break
            else:
                print("Nomor game tidak ditemukan.")
                continue
        except KeyboardInterrupt:
            print("Program mengalami gangguan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

                
# Fungsi update paket top up
def update_paket_topup(products):
    while True:
        try:
            tampilkan_game(products, "Game yang tersedia")

            no_game = input("Masukkan nomor game yang ingin di-update: ") 
            if no_game not in products:
                print("Nomor game tidak ditemukan.")

            game_pilihan = products[no_game]
            print(f"Paket top-up untuk '{game_pilihan['nama']}':")
            tampilkan_produk(game_pilihan['paket_topup'], f"==== Paket top up {game_pilihan['nama']} ====")

            no_paket = input("Masukkan nomor paket yang ingin di-update: ") 

            paket_ditemukan = False
            for paket in game_pilihan['paket_topup']:
                if paket['No'] == no_paket:  
                    paket_ditemukan = True

                    paket_baru = input("Masukkan nama paket baru: ")
                    harga_baru = input("Masukkan harga baru: ")

                    paket['paket'] = paket_baru
                    paket['harga'] = int(harga_baru)  

                    simpan_data(GAME_FILE, products)

                    print(f"Paket top-up berhasil di-update untuk '{game_pilihan['nama']}'!")
                    tampilkan_produk(game_pilihan['paket_topup'], "==== Paket setelah di-update ====")
                    return

            if not paket_ditemukan:
                print("Nomor paket tidak ditemukan.")
                continue
            
        except KeyboardInterrupt:
            print("Program mengalami gangguan. Harap jangan tekan CTRL + C!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
# Fungsi untuk menghapus game

def hapus_game(data):
    while True:
        try:
            data = buka_data(GAME_FILE)
            tampilkan_game(data, "=== Game yang tersedia saat ini ===")
            no_game = input("Masukkan nomor game yang ingin dihapus: ")

            if no_game in data:
    
                data.pop(no_game)

                updated_data = {}
                no_baru = 1
                for key, value in data.items():
                    updated_data[str(no_baru)] = value
                    no_baru += 1

                simpan_data(GAME_FILE, updated_data)
                print("Game berhasil dihapus!")

                tampilkan_game(updated_data, "=== Pilihan Game setelah dihapus ===")
                return
            else:
                print("Game tidak ditemukan. Silakan coba lagi.")
                continue  
        except KeyboardInterrupt:
            print("Program mengalami gangguan. Harap jangan tekan CTRL + C!")
            break
        except FileNotFoundError:
            print("Data tidak ditemukan. Pastikan file data ada dan dapat diakses.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break

# Fungsi menghapus paket top up
def hapus_paketTopup(data):
    while True:
        try:
            data = buka_data(GAME_FILE)
            tampilkan_game(data, "Game yang tersedia saat ini")
            
            no_game = input("Masukkan nomor game yang ingin dipilih: ")
            
            if no_game in data:
                data_game = data[no_game]
                paket_topup = data_game["paket_topup"]
                
                if not paket_topup:
                    print("Paket top-up untuk game ini masih belum tersedia.")
                    return
                
                tampilkan_produk(paket_topup, f"=== Paket Top-Up {data[no_game]['nama']} yang tersedia")
                no_paket = input("Masukkan nomor paket yang ingin dihapus: ")
                
                paket_dihapus = False
                for paket in paket_topup:
                    if paket["No"] == no_paket:
                        paket_topup.remove(paket)
                        paket_dihapus = True
                        break
                        
                if paket_dihapus: 
                    paket_baru = 1
                    for paket in paket_topup:
                        paket["No"] = str(paket_baru)
                        paket_baru += 1
                            
                    simpan_data(GAME_FILE, data)
                    print("Paket berhasil dihapus!")
                    tampilkan_produk(paket_topup, "Paket Top-Up setelah dihapus")
                    return
                
                print("Paket Top-Up tidak ditemukan.")
            else:
                print("Game tidak ditemukan.")
                continue
        except KeyboardInterrupt:
            print("Program mengalami gangguan. Harap jangan tekan CTRL + C!")
            break
        except FileNotFoundError:
            print("Data tidak ditemukan. Pastikan file data ada dan dapat diakses.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break

# Fungsi untuk sorting
def sorting_harga(data):
    return sorted(data, key=lambda x: x['harga'])


# Fungsi apakah ingin sorting
def tanya_sorting(data):
    
    tanya = input("Apakah Anda ingin mengurutkan paket berdasarkan harga? (y/t): ").lower()
    if tanya == "y":
        sorted_data = sorting_harga(data)
        tampilkan_produk(sorted_data) 
    elif tanya == "t":
        print("Sorting dibatalkan.")
    else:
        print("Input tidak valid.")
    
def cek_saldo(user):
    os.system('cls')  
    try:
        if "saldo" in user:
            saldo = user["saldo"]
            print("+" + "-" * 45 + "+")
            print("|" + " " * 18 + "CEK SALDO" + " " * 18 +"|")
            print("+" + "-" * 45 + "+")
            print(f"| {'Saldo Anda saat ini:':<30} Rp {saldo:>10}|")
            print("+" + "-" * 45 + "+")
        else:
            print("Saldo pengguna tidak dapat ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi Topup Saldo
def tambah_saldo(user):
    MIN_TOPUP = 15000  
    MAX_TOPUP = 2000000
    
    users = buka_data(USERS_FILE)
    while True:
        try:
            print("==== Batas Top Up Saldo ====")
            print("+" + "-" * 53 + "+")
            print(f"| {'Jumlah Topup Minimal:':<35} | Rp {MIN_TOPUP:<10} |")
            print(f"| {'Jumlah Topup Maksimal:':<35} | Rp {MAX_TOPUP:<10} |")
            print("+" + "-" * 53+ "+")

            jumlah = int(input("Masukkan nominal saldo yang ingin ditambahkan: Rp. "))
            if jumlah < MIN_TOPUP:
                print(f"Jumlah saldo minimal harus Rp. {MIN_TOPUP}. Silakan coba lagi: ")
                continue
            elif jumlah > MAX_TOPUP:
                print(f"Top up saldo tidak boleh lebih dari Rp. {MAX_TOPUP}. Silakan coba lagi: ")
                continue
            elif jumlah > 0: 
                user["saldo"] += jumlah
                
                for data_user in users:
                    if data_user["username"] == user["username"]:
                        data_user['saldo'] = user['saldo']
                        break
                    
                simpan_data(USERS_FILE, users)
                print("\nSaldo berhasil ditambahkan!")
                print("+" + "-" * 40 + "+")
                print(f"| {'Saldo Anda saat ini: Rp ' + str(user['saldo']):<38} |")
                print("+" + "-" * 40 + "+")
                break
            else:
                print("Jumlah saldo harus positif.")
                continue
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
def transaksi_topup(user):
    while True: 
        try:
            users = buka_data(USERS_FILE)
            data = buka_data(GAME_FILE)  
            tampilkan_game(data, "==== Game yang Tersedia untuk Top-Up ====")
            
            no_game = input("Masukkan nomor game yang anda inginkan: ")
            if no_game not in data:
                os.system('cls')
                print("Nomor game tidak valid. Harap masukkan nomor paket yang sesuai.")
                continue
            
            item = data[no_game]
            os.system('cls') 
            tampilkan_produk(item['paket_topup'], f"Paket Top Up {item['nama']} yang Tersedia")
            
            while True:
                no_paket = input("Masukkan nomor paket yang ingin anda beli: ")
                 
                for info_paket in item['paket_topup']:
                    if info_paket['No'] == no_paket:
                        paket = info_paket
                        break
            
                if paket:  
                    harga = paket['harga']
                    if user['saldo'] >= harga:  
                        user['saldo'] -= harga 
                        
                        for data_user in users:
                            if data_user['username'] == user['username']:
                                data_user['saldo'] = user['saldo']  
                                break
                                
                        simpan_data(USERS_FILE, users)  
                        os.system('cls')
                        print("\n==== Pembelian Paket Top Up ====")
                        print(f"Paket '{paket['paket']}' berhasil dibeli!")
                        print(f"Sisa saldo Anda: Rp {user['saldo']}")
                        buat_invoice(user, paket)
                        return
                    else:
                        print("Saldo tidak mencukupi untuk pembelian paket ini.")
                        return
                else:
                    print("Paket tidak ditemukan. Harap masukkan nomor paket yang sesuai.")
                             
        except ValueError:
            print("Input tidak valid.")
            
def cari_game(data, user):
    users = buka_data(USERS_FILE)  
    while True:
        try:
            print("=== Pencarian Game ===")
            keyword = input("Masukkan nama game yang ingin dicari: ").strip().lower()
            hasil = {no: info for no, info in data.items() if keyword in info['nama'].lower()}
            
            if hasil:
                for no, info in hasil.items():
                    info_game = info["paket_topup"]
                while True:
                    tampilkan_produk(info_game, f"=== Paket top up yang tersedia untuk {info["nama"]} ===")
                    print("[1]. Top up game\n[2]. Kembali")
                    pilih = int(input("Masukkan pilihan anda: "))
                    if pilih == 1:
                        no_paket = input("Masukkan nomor paket yang ingin anda beli: ")
                        
                        # mencari paket berdasarkan nomor paket yang diinputkan
                        for paket in info_game:
                            if paket["No"] == no_paket :
                                paket_dibeli = no_paket
                                break

                        # transaksi jika paket telah ditemukan 
                        if paket_dibeli:
                            harga = paket["harga"]
                            if user["saldo"] >= harga:  
                                user["saldo"] -= harga 
                                
                                for data_user in users:
                                    if data_user["username"] == user["username"]:
                                        data_user["saldo"] = user["saldo"]
                                        break
                                    
                                simpan_data(USERS_FILE, users)       
                                os.system('cls')
                                print("\n==== Pembelian Paket Top Up ====")
                                print(f"Paket '{paket['paket']}' berhasil dibeli!")
                                print(f"Sisa saldo Anda: Rp {user['saldo']}")
                                buat_invoice(user, paket)
                                return
                            else:
                                while True:
                                    print("Saldo tidak mencukupi untuk pembelian paket ini.")
                                    opsi = input("Apakah anda ingin top up saldo? (y/t): ").strip().lower()
                                    if opsi == "y":
                                        tambah_saldo(user)
                                        break 
                                    elif opsi =="t":
                                        return
                                    else:
                                        print("Pilihan tidak tersedia.")
                                        
                        else:
                            print("Paket tidak tersedia.")
                    elif pilih == 2:
                        return
                    else:
                        print("Pilihan tidak tersedia.")
                        return
            else:
                print("Game tidak ditemukan. Harap input nama game yang benar.")
                continue
        except KeyboardInterrupt:
            print("Program mengalami gangguan. Harap jangan tekan CTRL + C!")
        except FileNotFoundError:
            print("Data tidak ditemukan. Pastikan file data ada dan dapat diakses.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
 

def sorting_harga(data):
    while True: 
        try: 
            tampilkan_game(data, "==== Game yang Tersedia untuk Top-Up ====")
                    
            no_game = input("Masukkan nomor game yang anda inginkan: ")
            if no_game not in data:
                os.system('cls')
                print("Nomor game tidak valid. Harap masukkan nomor paket yang sesuai.")
                continue
                    
            item = data[no_game]
            paket_topup = item["paket_topup"]
            paket_termurah = sorted(paket_topup, key=lambda x: x['harga'])
            os.system('cls')
            tampilkan_produk(paket_termurah, f"Paket Top Up {item['nama']} berdasarkan harga termurah: ")
            break
        except KeyboardInterrupt:
            print("Terjadi kesalahan. Harap jangan tekan CTRL + C!")
            break
        except FileNotFoundError:
            print("Data tidak ditemukan. Pastikan file data ada dan dapat diakses.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break
        
def buat_invoice(user, paket_dibeli, filename="invoice.txt"):
    
    invoice = f"=== RIWAYAT TOP-UP ===\n"
    invoice += f"Nama Pengguna: {user['username']}\n"
    invoice += f"Paket yang Dibeli: {paket_dibeli['paket']}\n"
    invoice += f"Harga: Rp {paket_dibeli['harga']}\n"
    invoice += f"Sisa Saldo: Rp {user['saldo']}\n"
    invoice += "========================\n"
    invoice += "Terima kasih telah melakukan top-up!\n"

    with open(filename, 'w') as file:
        file.write(invoice)

    print("\n" + "=" * 30)
    print("=== RIWAYAT TOP-UP ===")
    print("=" * 30)
    print(f"Nama Pengguna: {user['username']}")
    print(f"Paket yang Dibeli: {paket_dibeli['paket']}")
    print(f"Harga: Rp {paket_dibeli['harga']}")
    print(f"Sisa Saldo: Rp {user['saldo']}")
    print("=" * 30)
    print("Terima kasih telah melakukan top-up!")
    print("=" * 30)

# Main menu
def main():
    while True:
        users = buka_data(USERS_FILE) 
        print(" ")   
        print("="*10, "Selamat Datang di Toko DDP Top-Up", "="*10)
        print("[1]. Login sebagai admin\n[2]. Login sebagai user\n[3]. Register akun\n[4]. Keluar") 
        try:
            login = int(input("Masukkan pilihan anda: "))
            if login == 1:
                login_admin(users)
                menu_admin(users)
            elif login == 2:
                menu_user(users)
            elif login == 3:
                buat_akun(users)
            elif login == 4:
                print("\n=== Keluar dari Program ===")
                keluar = input("Apakah anda yakin ingin keluar dari program? (y/t): ").lower()
                if keluar == "t":
                    continue
                elif keluar == "y":
                    print("Terimakasih telah menggunakan program ini! ")
                    print("===== ♡`･ᴗ･`♡ =====")
                    exit()
                else:
                    print("Input tidak valid.") 
                    continue  
            else:
                print("Pilihan tidak tersedia")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka (1-4)")
        except KeyboardInterrupt:
            print("Terjadi kesalahan. Harap jangan tekan CTRL + C!")
            

# fungsi untuk menu admin
def menu_admin(users):
    user = buka_data(USERS_FILE)
    data = buka_data(GAME_FILE)
    products = buka_data(GAME_FILE)

    if user:
        while True:
            print("\n=== Menu Admin ===")
            print("[1]. Tambah produk\n[2]. Lihat produk\n[3]. Perbarui produk\n[4]. Hapus produk\n[5]. Keluar")  
            try: 
                pilihan_admin= int(input("Pilih fitur yang anda mau: "))
                if pilihan_admin== 1:
                    while True:
                        print("\n==== Penambahan Data ====\n[1]. Menambah pilihan game\n[2]. Menambah paket Top-Up\n[3]. Kembali")
                        opsi = int(input("Pilih penambahan yang anda mau: "))
                        if opsi == 1:
                            tambah_game(data)
                        elif opsi == 2:
                            while True:
                                try:
                                    data = buka_data(GAME_FILE)
                                    tampilkan_game(data, "Pilihan game yang tersedia")
                                    no_game = input("Masukkan nomor game yang anda ingin tambahkan: ")
                                    if no_game in data:
                                        tambah_topup(data, no_game)
                                        break
                                    if no_game not in data:
                                        continue
                                except KeyboardInterrupt:
                                    print("Harap jangan tekan CTRL + C!")
                                    break
                        elif opsi == 3:
                            kembali_admin(users)
                        else:
                            print("Pilihan tidak tersedia.")
                elif pilihan_admin == 2:
                    while True:
                        print("\n==== Lihat Produk ====\n[1]. Hanya melihat pilihan game\n[2]. Melihat paket top-up yang tersedia\n[3]. Kembali")
                        opsi = int(input("Pilih fitur yang ingin anda lihat: "))
                        if opsi == 1:
                            os.system('cls')
                            tampilkan_game(data, "==== Game yang tersedia ====")
                        elif opsi == 2:
                            os.system('cls')
                            tampilkan_game(data, "==== Game yang tersedia ====")
                            no_game = input("Masukkan nomor game yang anda inginkan: ")
                            if no_game not in data:
                                print("Nomor game tidak valid.")
                                continue

                            item = data[no_game]
                            tampilkan_produk(item["paket_topup"], f"==== Paket Top-Up {item["nama"]} yang Tersedia ====")
                        elif opsi == 3:
                            kembali_admin(users)
                        else:
                            print("Pilihan tidak tersedia.")

                elif pilihan_admin == 3 :
                    while True:
                        print("\n==== Update Data ====\n[1]. Update pilihan game\n[2]. Update paket Top-Up\n[3]. Kembali")
                        opsi = int(input("Pilih fitur yang ingin di update: "))
                        if opsi == 1:
                            update_product(products)
                        elif opsi == 2:
                            update_paket_topup(products)
                        elif opsi == 3:
                            kembali_admin(users)
                        else:
                            print("Pilihan tidak tersedia.")
                            
                elif pilihan_admin == 4:
                    while True:
                        print("\n==== hapus Produk ====\n[1]. Menghapus Game\n[2]. Menghapus paket top-up\n[3]. Kembali")
                        opsi = int(input("Pilih fitur yang ingin anda hapus: "))
                        if opsi == 1:
                            hapus_game(data)
                        elif opsi == 2:
                            hapus_paketTopup(data)
                        elif opsi == 3:
                            kembali_admin(users)
                        else: 
                            print("Pilihan tidak tersedia. Harap masukkan angka (1/2)")
                            
                elif pilihan_admin == 5:
                    keluar(users)
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka (1-5).")
            except KeyboardInterrupt:
                print("Terjadi kesalahan. Harap jangan tekan CTRL + C!")
                

# fungsi untuk menu user
def menu_user(users):
    
    os.system('cls')
    user = login_user(users) 
    data = buka_data(GAME_FILE)
    
    if user:
        while True:
            print("\n=== Menu User ===")
            print("[1]. Cek Saldo\n[2]. Tambah Saldo\n[3]. Transaksi Top-Up\n[4]. Cari game\n[5]. Sorting harga\n[6]. Keluar ")
            try:
                pilihan = int(input("Masukkan pilihan anda: "))
            except ValueError:
                print("Input tidak valid. Input harus berupa angka.")
            except KeyboardInterrupt:
                print("Terjadi kesalahan. Harap jangan tekan CTRL + C!")
                continue
            if pilihan == 1:
                cek_saldo(user)
            elif pilihan == 2:
                tambah_saldo(user)
            elif pilihan == 3:
                transaksi_topup(user)
            elif pilihan == 4:
                cari_game(data, user)
            elif pilihan == 5:
                sorting_harga(data)
            elif pilihan == 6:
                keluar(users)
            else:
                print("Pilihan tidak tersedia. Silakan coba lagi.")
    else:
        print("Pilihan tidak tersedia.")
        
if __name__ == "__main__":
    main()