import pandas as pd 

invoices ={'invoice_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
          'client_id': [3, 2, 7, 2, 7, 3, 1, 4, 2, 3, 6, 2],
          'amount': [77.91, 24.36, 74.65, 19.65, 27.46, 17.13, 45.77,
                     81.7, 14.41, 52.69, 32.03, 12.78]}

invoices = pd.DataFrame( invoices, columns= ['invoice_id', 'client_id', 'amount'])
print(invoices)