def mijn_functie_2(num1, num2):
    result=[
        num1+num2, #optellen
        num1-num2, #aftrekken
        num1*num2, #vermenigvuldigen
        num1/num2, #delen
    ]   
    return result
#test de functie met argumenten 12 en 3
output=mijn_functie_2(12,3)
print(output) #output: [15,9,36,4]        
def aanbieding_1(smaak,prijs,korting):
    nieuwe_prijs=prijs*(1-korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak aardbei, van 4 euro voor 3,60 euro."
from reclame import aanbieding_1
resultaat=aanbieding_1("aardbei", 4, 0.1)
print(resultaat)
def inkomsten_totaal(inkomsten,btw):
    totaal_inkomsten=sum(inkomsten)
    btw_kosten=totaal_inkomsten*btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_kosten:.2f} euro btw betaald dient te worden."
from reclame import inkomsten_totaal
inkomsten_per_dag= [220, 430, 125, 160, 205, 90, 345]
btw_kosten= 0.09
resultaat_inkomsten=inkomsten_totaal(inkomsten_per_dag, btw_kosten)
print(resultaat_inkomsten)
def laag_en_hoog(mijn_lijst):
    laagste= min(mijn_lijst)
    hoogste= max(mijn_lijst)
    return[laagste, hoogste]
from reclame import laag_en_hoog
inkomsten_per_dag=[220, 430, 125, 160, 205, 90, 345]
resultaat=laag_en_hoog(inkomsten_per_dag)
print("laagste en hoogste inkomen deze week:", resultaat)
def gemiddelde(mijn_lijst):
    gemiddelde_inkomsten=sum(mijn_lijst)/len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro."
from reclame import gemiddelde
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
gemiddelde_inkomsten = gemiddelde(inkomsten_per_dag)
print(gemiddelde_inkomsten)
def meervoudig(invoer_lijst):
    hoogste= max(invoer_lijst)
    laagste= min(invoer_lijst)
    return[laagste, hoogste]
def hoog_en_laag(lijst):
    hoogste= max(lijst)
    laagste= min(lijst)
    return[laagste,hoogste]
from reclame import hoog_en_laag, meervoudig
invoer_lijst= [10, 5, 3, 2, 1, 2, 9]
resultaat_meervoudig = meervoudig(invoer_lijst)
print("Hoogste en laagste waarden:", resultaat_meervoudig)
from reclame import mijn_functie_2
from reclame import meervoudig
def combinatie(invoer_lijst_2):
    korte_lijst=meervoudig(invoer_lijst_2)
    return mijn_functie_2(*korte_lijst)