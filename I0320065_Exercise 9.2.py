#mendefinisikan array asosiatif
import sys
kamus = {
        'one'   : 'satu',
        'two'   : 'dua',
        'three' : 'tiga',
        'four'  : 'empat',
        'five'  : 'lima',
        'six'   : 'enam',
        'seven' : 'tujuh',
        'eight' : 'delapan',
        'nine'  : 'sembilan',
        'ten'   : 'sepuluh'
        # ...
        }
def main():
    #meminta user to input a word in english
    kata = input('masukkan kata dalam bahasa inggris : ')

    if not (kata in kamus.keys()):
        print("'%s' tidak ditemukan dalam kamus ini" %kata)
        sys.exit(1)

    print("the '%s' meaning is '%s'"% (kata, kamus[kata]))

if __name__== '__main__':
    main()
