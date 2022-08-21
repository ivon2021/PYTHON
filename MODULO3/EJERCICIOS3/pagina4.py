from ntpath import join
import pandas as pd

df1 = pd.DataFrame({"Month": ["ene", "feb", "mar", "may"],
                   "Sales": [14, 8, 12, 17]
                   })
df1


df2 = pd.DataFrame({"Month": ["feb","ene","mar", "abr"],
                    "Cost": [7, 6, 8, 5]
                    })
df2


df3 = pd.merge(df1, df2)
print(df3)


