#CONCAT
#se ha de agregar el registro,para los que se puede utilizar
# el metodo CONCAT de pandas.
import pandas as pd

clients = {'first_name' : ['Oralie', 'Imojean', 'Michele',
                           'Ailbert', 'Stevy'],
           'last_name' : ['Fidgeon', 'Benet', 'Woodlands', 'Risdale',
                          'MacGorman'],
           'age' : [30, 21, 29, 22, 24]}


#Se indica los datos a concatenar
new_clients = pd.DataFrame ({'first_name' : ['Rebe'],
                            'last_name' : ['MacCrossan'],
                            'age' : [21]},
                           columns = ['first_name', 'last_name', 'age'])

ids = pd.DataFrame({'client_id': [1, 2, 3, 4, 5, 6]}, columns = ['client_id'])

clients = pd.DataFrame(clients, columns= ['first_name', 'last_name', 'age'])
#clients = pd.concat([clients, new_clients])
clients = pd.concat([ids, clients], axis=1,)
print(clients)
