import random
welcome_message='HAI PERKENALKAN SAYA MUADZ'
muadz_position= random.randint(1,5)


Nama = 'Muadz Muttaqin'
Usia = 19
print ('*************************')
print (f'**{welcome_message}**')
print ('*************************')

print(f'''
nama saya adalah {Nama}
usia saya adalah {Usia}
      ''')

nomor_saya = 5
if nomor_saya == 4:
      
      print('benar nomor saya 4')
      

else:
      print('ah bukan 4 teryata...')
      
buah= 'semangka'  
star = 0
end = 12  
while star < end: #looping
      print(buah)
      star= star+1
  
      
      
      
nama_user =input('masukan nama anda:')

lobanag_goa  = "|_|"
goa_kosong = [lobanag_goa] * 5 # ini tetep harus kosong
goa= goa_kosong.copy()  # ini tempat gua kosong 
goa[muadz_position-1]= '|0-0|'
goa_kosong = '.'.join(goa_kosong)
goa = '.'.join(goa)

print(f'''hallo bang {nama_user} coba isi jawaban ini
{goa_kosong}
''')

pilihan_user = int(input('dimana goa menurut kamu muadz berada? [1/2/3/4/5] '))
confir=input(f'apakah kamau benar ingin melanjutkan degan memilih {pilihan_user} klik [y/n]')

if confir == "n":
      print('program di hentikan')
      exit()

elif confir == "y":
      if pilihan_user == muadz_position:
            print(f'selamat {nama_user} kamu menang! muadz berada di {muadz_position} dan pilihanmu adalah {pilihan_user}')
            print(goa)
      
      else: 
            print(f'kamu kalah muadz bukan berada di situ, tapi muada berada di goa nomor {muadz_position} sedangkan kamu memilih goa {pilihan_user}')
            print(goa)
else:
      print('balik lagi ke awal')
      exit()
