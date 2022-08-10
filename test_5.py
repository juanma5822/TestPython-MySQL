import  data


def order():
    lista1=[]
    for companie in data.thirds:
        if companie['tradename'] != '':
            lista1.append(companie['tradename'])

    print(lista1)        

order()    