"""
Aplikasi Deteksi Gempa Terkini
"""

def ekstrasi_data():
    """
    Tanggal : 08 September 2023
    Waktu : 02:20:11 WIB
    Magnitudo : 5.7
    Kedalaman : 130 km
    Lokasi : LS=4.57 - BT=127.76
    Keterangan : Pusat gempa berada di 78 km Tenggara PULAUKARATUNG-SULUT
    Dirasakan : Dirasakan (Skala MMI): II-III Sumur, II Munjul
    :retrun:
    """
    hasil = dict()
    hasil['tanggal'] = '05 Juli 2023'
    hasil['waktu'] =  '14:31:29 WIB'
    print(hasil)
    return hasil

def tampilkan_data(result):
    pass

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstrasi_data()
    tampilkan_data(result)



