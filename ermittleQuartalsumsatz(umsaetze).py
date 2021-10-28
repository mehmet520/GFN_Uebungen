# ermittleQuartalsumsatz(umsaetze)
testdaten = [2000.00, 1000.00, 4000.00, 5000.00]
umsatzQuartal = 0
for i in range (0,3,1):
    umsatzQuartal= umsatzQuartal + int (testdaten [i])
    print ('i: ', i)
    print (umsatzQuartal)

print ('umsatzQuartal: \n', umsatzQuartal)

