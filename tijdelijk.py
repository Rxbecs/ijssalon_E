prijzen = {
    "Aardbei":3,
    "Vanille":4,
    "Chocolade":5
}
aanbieding=prijzen["Aardbei"]*0.8
reclame_tekst=f"Vandaag in de aanbieding: Aardbeien-ijs, 1 liter - slechts €{aanbieding}" 
reclame_tekst2=reclame_tekst[:reclame_tekst.index('.')+3]
reclame_tekst3=reclame_tekst2.upper()
reclame_tekst4=reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el)>=5:
        print(el.upper())
    else:
        print(el.lower())
