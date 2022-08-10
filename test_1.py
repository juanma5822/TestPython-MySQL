from data import Data

companies = [
            {
                'id': 1,
                'name': 'Empresa Uno',
                'nit': '123456789',
                'dv': '1',
                'branches': [1, 3, 5]
            },
            {
                'id': 2,
                'name': 'Empresa Dos',
                'nit': '987654321',
                'dv': '2',
                'branches': [2]
            },
            {
                'id': 3,
                'name': 'Empresa Tres',
                'nit': '987654333',
                'dv': '3',
                'branches': [4]
            }
        ] 


def run(data):
    
    object= {companie['name']: companie['branches'] for companie in data}
       
    print(object)
      
run(companies)
    


    
