text = input("Text: ")
schluessel = int(input("Schlüssel: "))
value1 = input("Möchten Sie den Text verschlüsseln (v) oder entschlüsseln (e): ")
geheimtext = ""

if value1 == "v":
    for i in text:
        if i==" ":   
            number = i
            geheimtext = geheimtext + number
        else:
            number = ord(i)
            number = number + schluessel
            if number >90:
                number-=26
            geheimtext = geheimtext + chr(number)
    print("verschluesselter Text: " + geheimtext)

elif value1 == "e":
    geheimtext=""
    for i in text:
     if i==" ":
        number = i
        geheimtext = geheimtext + number
     else:
        number=ord(i)
        number= number - schluessel
        if number>90:
            number+=26
        geheimtext = geheimtext + chr(number)
    print("verschluesselter Text: " + geheimtext)
