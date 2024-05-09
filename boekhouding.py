import csv
def presenteer(dictionary, totaal):
    for item, bedrag in dictionary.items():
        print(f"{item}: {bedrag} euro")
    print("==========================")
    print(f"totaal:{totaal} euro")
mijn_dict={'vis': 10, 'vlees': 25, 'overig': 15}
totaal=50
presenteer(mijn_dict, totaal)
def som(dictionary):
    return sum(dictionary.values())
inkomsten = {
    "Aardbeien-ijst-totaal": 1000,
    "Vanille-ijst-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}
totaal_inkomsten=som(inkomsten)
presenteer(inkomsten, totaal_inkomsten)
with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])