import os
import time
from datetime import datetime

saldo_anda1 = 5250000
pin_user = "123456"

data_member = {
    "001": {"nama": "Mulyono", "tagihan": 50000},
    "002": {"nama": "Wowok", "tagihan": 75000},
    "003": {"nama": "Lil nepotism", "tagihan": 20000}
}

def simpan_history(jenis, nominal, saldo_akhir):
    with open("history.txt", "a") as f:
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        f.write(f"[{waktu}] {jenis} | Nominal: Rp {nominal:,} | Saldo: Rp {saldo_akhir:,}\n")

def lihat_history():
    if not os.path.exists("history.txt"):
        print("\n(!) Belum ada riwayat transaksi.")
        return
    with open("history.txt", "r") as f:
        isi = f.read()
    print("\n=== RIWAYAT TRANSAKSI ===")
    print(isi if isi else "(!) Belum ada riwayat transaksi.")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    layar_utama = f"""
+------------------------------------------------+
| MENU UTAMA                                     |
+------------------------------------------------+
| SALDO ANDA : Rp {saldo_anda1:,}                      |
+------------------------------------------------+
|                                                |
|  [1] TARIK TUNAI             INFO SALDO  [5]   |
|                                                |
|  [2] SETOR TUNAI             TRANSFER    [6]   |
|                                                |
|  [3] PEMBAYARAN              UBAH PIN    [7]   |
|                                                |
|  [4] RIWAYAT TRANSAKSI       KELUAR      [0]   |
|                                                |
+------------------------------------------------+
|       SILAKAN PILIH TRANSAKSI ANDA             |
+------------------------------------------------+
"""
    print(layar_utama)

    try:
        iuser1 = int(input("Pilih Menu: "))
    except ValueError:
        print("\n(!) MASUKKAN ANGKA SAJA!")
        time.sleep(1)
        continue

    if iuser1 == 1:
        nominal = int(input("\nJUMLAH TARIK : "))
        if nominal > saldo_anda1:
            print("SALDO KURANG!")
        else:
            saldo_anda1 -= nominal
            simpan_history("TARIK TUNAI", nominal, saldo_anda1)
            print(f"BERHASIL! Sisa: Rp {saldo_anda1:,}")

    elif iuser1 == 2:
        setoran = int(input("\nNOMINAL SETOR: "))
        if setoran % 50000 == 0:
            saldo_anda1 += setoran
            simpan_history("SETOR TUNAI", setoran, saldo_anda1)
            print(f"BERHASIL! Saldo: Rp {saldo_anda1:,}")
        else:
            print("HARUS KELIPATAN 50K/100K")

    elif iuser1 == 3:
        id_user = input("MASUKKAN ID MEMBER: ").strip()
        member = data_member.get(id_user)

        if member:
            print(f"\n> NAMA    : {member['nama']}")
            print(f"> TAGIHAN : Rp {member['tagihan']:,}")

            pilih = input("\nBayar sekarang? (y/n): ")
            if pilih.lower() == 'y':
                if saldo_anda1 >= member['tagihan']:
                    tagihan = member['tagihan']
                    saldo_anda1 -= tagihan
                    member['tagihan'] = 0
                    simpan_history(f"PEMBAYARAN ({member['nama']})", tagihan, saldo_anda1)
                    print("PEMBAYARAN BERHASIL!")
                else:
                    print("SALDO TIDAK CUKUP!")
        else:
            print("(!) ID TIDAK DITEMUKAN!")

    elif iuser1 == 4:
        lihat_history()

    elif iuser1 == 5:
        print(f"\nSALDO ANDA : Rp {saldo_anda1:,}")

    elif iuser1 == 6:
        rek = input("\nREK TUJUAN : ")
        nominal = int(input("NOMINAL    : Rp "))
        if nominal <= saldo_anda1:
            saldo_anda1 -= nominal
            simpan_history(f"TRANSFER ke {rek}", nominal, saldo_anda1)
            print(f"TRANSFER KE {rek} BERHASIL!")
        else:
            print("SALDO KURANG!")

    elif iuser1 == 7:
        if input("PIN LAMA: ") == pin_user:
            pin_user = input("PIN BARU: ")
            print("PIN BERHASIL DIUBAH")

    elif iuser1 == 0:
        print("\nTerima kasih!")
        break

    input("\nTekan ENTER untuk kembali...")
