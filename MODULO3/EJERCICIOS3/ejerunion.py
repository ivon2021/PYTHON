from http import client
import pandas as pd

clients = {'first_name' : ['Oralie', 'Imojean', 'Michele',
                           'Ailbert', 'Stevy'],
           'last_name' : ['Fidgeon', 'Benet', 'Woodlands', 'Risdale',
                          'MacGorman'],
           'age' : [30, 21, 29, 22, 24]}

invoices ={'invoice_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
          'client_id': [3, 2, 7, 2, 7, 3, 1, 4, 2, 3, 6, 2],
          'amount': [77.91, 24.36, 74.65, 19.65, 27.46, 17.13, 45.77,
                     81.7, 14.41, 52.69, 32.03, 12.78]}



clients = pd.merge(clients, invoices, on='client_id')
clients = pd.concat([clients, clients], axis=1,)
print(clients)
