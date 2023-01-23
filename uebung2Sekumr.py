def sek_umr(number):
    
    wochen = number//(60*60*24*7)
    modulo_wochen = number%(60*60*24*7)
    tage = modulo_wochen // (60*60*24)
    modulo_tage = number% (60*60*24)
    stunden = modulo_tage//(60*60)
    moduloStunden = number%(60*60)
    minuten = moduloStunden//60 
    sekunden= number%(60)
    return str(number) +  ": " + " wochen: " + str(wochen) + ";" + " tage: " + str(tage) + " stunden: " + str(stunden) + ";" + " minuten: " + str(minuten) + ";" + " sekunden: " + str(sekunden)
       

print(sek_umr(66))
print(sek_umr(148))
print(sek_umr(86400))
print(sek_umr(789891))



