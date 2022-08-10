import  data


def order():
    lista1= []
    dic1={}
    dic2= data.companies
    lista2=[]
    for company in data.thirds:
        if company['tradename'] != '':
            dic1[company['tradename']] = company['companyid']
        elif company['tradename'] == '':
           dic1[company['firstname'],company['lastname']] = company['companyid'] 
            
    print(dic1)      
    
order() 