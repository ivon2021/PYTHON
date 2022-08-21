#utilice un DataFrame pandas para guardar 
# un array Numpy en un archivo CSV

#guardamos la matriz en un dataframe pandas
#y luego convertiremos este dataframe en un archivo CSV

import pandas as pd
import numpy as np

a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
pd.DataFrame(a).to_csv('sample.csv')


#la funcion "pd.dataframe" almacena el arreglo
#en un DataFrame y simplemente lo exportamos
#a un archivo CSV usando la funcion "to_csv()" .