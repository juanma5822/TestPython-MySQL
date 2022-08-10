branches = [
            {
                'id': 1,
                'name': 'Sucursal Uno',
                'address': 'Cll 123',
                'isMain': True
            },
            {
                'id': 2,
                'name': 'Sucursal Dos',
                'address': 'Cll 12 # 1-23',
                'isMain': True
            },
            {
                'id': 3,
                'name': 'Sucursal Tres',
                'address': 'Cll 1 # 11-23',
                'isMain': False
            },
            {
                'id': 4,
                'name': 'Sucursal Cuatro',
                'address': 'Cll 4 # 4-32',
                'isMain': True
            },
            {
                'id': 5,
                'name': 'Sucursal Cinco',
                'address': 'Cll 5 # 5-43',
                'isMain': False
            }
        ]

def consulta(data):
    a=int(input("Ingrese id de sucursal: "))
    
    object = list(filter(lambda x: x['id']==a,data))
    print(a)
    print(object)

consulta(branches)
