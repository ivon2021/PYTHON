import pandas as pd

clients = {'first_name' : ['Oralie', 'Imojean', 'Michele',
                           'Ailbert', 'Stevy'],
           'last_name' : ['Fidgeon', 'Benet', 'Woodlands', 'Risdale',
                          'MacGorman'],
           'age' : [30, 21, 29, 22, 24]}

clients = pd.DataFrame(clients, columns= ['first_name', 'last_name', 'age'])
print(clients)