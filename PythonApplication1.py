
#11

n=int(input("sisestage t�htede arv: ")) #zapros
lowercase_alphabet=[chr(i) for i in range(97, 97 + n)]  # lower spisok sozdanie
more_lowercase_alphabet=[letter*(i + 1) for i, letter in enumerate(lowercase_alphabet)] #spisok povtorenija
print("alaregistri j�rjend:",lowercase_alphabet)
print("rohkem j�rjend:",more_lowercase_alphabet)

#12

import random
numb=[random.randint(1, 100) for _ in range(10)] #spisok generation
print("enne:", numb)
min_value=min(numb)
max_value=max(numb)
min_index=numb.index(min_value)
max_index=numb.index(max_value)
numb[min_index],numb[max_index]=numb[max_index],numb[min_index] # zamena min na max
print("parast:", numb)

#10

tootajad=[                                                                      #spisok rabotnikov
    {"nimi": "Aadu Suur", "vanus": 56, "palk": 2500},
    {"nimi": "Malle Kapsas", "vanus": 42, "palk": 1500},
    {"nimi": "Uudo Koba", "vanus": 32, "palk": 700},
    {"nimi": "Tiit Kopikas", "vanus": 22, "palk": 550},
    {"nimi": "Vahur Vana", "vanus": 67, "palk": 870}
]
suurima_palgaga_tootaja=max(tootajad, key=lambda x: x["palk"])                      #max rich daddy
print("k�ige suurema palgaga t��taja:", suurima_palgaga_tootaja["nimi"])
print("palga suurus:", suurima_palgaga_tootaja["palk"])
keskmine_palk=sum(tootaja["palk"] for tootaja in tootajad)/len(tootajad)            # srednee po palate
print("keskmine palk:", keskmine_palk)
rohkem_keskmisest_teenijaid=sum(1 for tootaja in tootajad if tootaja["palk"] > keskmine_palk)   #pogoda chut po luche
print("keskmisest palgast rohkem teenijaid:", rohkem_keskmisest_teenijaid)
keskmine_vanus=sum(tootaja["vanus"] for tootaja in tootajad) / len(tootajad)        
print("keskmine vanus:", keskmine_vanus)
keskmisest_vahem_teenijad=[tootaja["vanus"] for tootaja in tootajad if tootaja["palk"] <= keskmine_palk]    #srednii vozrast
keskmisest_rohkem_teenijad=[tootaja["vanus"] for tootaja in tootajad if tootaja["palk"] > keskmine_palk]    #chut srednee
print("keskmised vanused neile, kes teenivad keskmisest v�hem:", sum(keskmisest_vahem_teenijad) / len(keskmisest_vahem_teenijad))
print("keskmised vanused neile, kes teenivad keskmisest rohkem:", sum(keskmisest_rohkem_teenijad) / len(keskmisest_rohkem_teenijad))
