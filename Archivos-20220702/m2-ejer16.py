#recordar que la base de datos que se muestra en el video de la clase es solo un ejemplo. Pueden probar cómo funciona este comando borrando algunos valores de la base de datos clientes.csv y luego aplicando la función fillna como se muestra en el video.
df_clientes = df_clientes.fillna("SIN_INFO")
print(df_clientes)