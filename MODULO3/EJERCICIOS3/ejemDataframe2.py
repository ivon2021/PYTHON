import pandas as pd

data = {'Nombre': ['Sigrid', 'Joe', 'Theodoric', 'Kennedy',
                  'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'Apellido': ['Mannock', 'Hinners', 'Rivers', 'Donnell',
                     'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'Edad': [27, 31, 36, 53, 48, 36, 40, 34],
        'monto_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'monto_2': [8.06, "?", 5.90, "?", "?", 7.48, 4.37, "?"]}

df = pd.DataFrame(data, columns = ['Nombre', 'Apellido', 'Edad', 'monto_1', 'monto_2'])
df.to_excel('example.xlsx',sheet_name='example')
#para exportar los datos excel se ha utilizado to_excel del dataframe
#opcional se puede indicar el nombre de la hoja del 
# libro excel la propiedad sheet_name
