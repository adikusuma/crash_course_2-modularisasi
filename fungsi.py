"""
menghitung fungsi luas segitiga tanpa dan dengan function

"""

print('luas segitiga tanpa fungsi')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga adalah = {luas_segitiga}')
print('-' * 20)

alas = 20
tinggi = 10
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga adalah = {luas_segitiga}')
print('-' * 20)

print('luas segitiga dengan fungsi')


def hitung_luas_segitiga(alas, tinggi):
    luas = alas * tinggi
    return luas


hitung_luas_segitiga(10, 8)
print('luas segitiga dengan alas {} dan tinggi {} adalah {}'.format(alas, tinggi, hitung_luas_segitiga(10, 8)))
