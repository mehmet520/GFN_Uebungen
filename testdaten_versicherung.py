# Testdaten={}
# Versicherungsart: „gesetzlich"
# Versicherungsart: „gesetzlich“
# Versicherungsart: „privat"
# Versicherungsart: „gesetzlich“
# Versicherungsart: „privat“


# Arzneimittelart: „verschreibungspflichtig"
# Arzneimittelart: „betäubungsmittel“
# Arzneimittelart: „betäubungsmittel"
# Arzneimittelart: „nicht verschreibungspflichtig"
# Arzneimittelart: „verschreibungspflichtig"

# geänderte Funktion
def bestimmeRezeptfarbe():
    Versicherungsart = input ('gesetzlich (g) / privat (p)')
    arzneimittelart = input(" versicherungspflichtig (v)/ nicht versicherungspflichtig (nv)/ Betäubungsmittel(btm)")
    if arzneimittelart == "btm":
        rezeptfarbe = "gelb"
    elif Versicherungsart == "g":
        if arzneimittelart == "v":
            rezeptfarbe = "rosa"
        else:
            rezeptfarbe = "grün"
    else:
        rezeptfarbe = "blau"
    print( "Rezeptfarbe:". rezeptfarbe)
    
def main():
    bestimmeRezeptfarbe()
    main()


# versicherungsart= input ('When Versicherungsart gesetzlich ist, geben Sie 1 ein \n When Versicherungsart gesetzlich ist, geben Sie 2 ein')
# arzneimittelart= input ('Geben Sie Arzneimittelart ein: \n')
# rezeptfarbe= ''

# if versicherungsart== 'gesetzlich':
#     if arzneimittelart == 'verscheibungspflichtig':
#         rezeptfarbe= 'rosa'
#     else:
#         rezeptfarbe= 'grün'
# else:
#     if arzneimittelart == 'nicht verscheibungspflichtig':
#         rezeptfarbe= 'blau'
#     else:
#         rezeptfarbe= 'gelb'
    
# print ('Rezeptfarbe: ')