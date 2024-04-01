import pandas as pd

'''
Las definiciones de las variables categoricas se puedes obtener en el diccionario de datos de la GEIH:
https://microdatos.dane.gov.co/index.php/catalog/819/data-dictionary/F69?file_name=Datos%20del%20hogar%20y%20la%20vivienda
'''

binario = {
    1: 'Si',
    2: 'No'
}

clase = {
    1: 'Urbano',
    2: 'Rural'}

categorias = {
    1: 'Casa',
    2: 'Apartamento',
    3: 'Cuarto(s) en inquilinato',
    4: 'Cuarto(s) en otro tipo de estructura',
    5: 'Vivienda indígena',
    6: 'Otra vivienda (carpa, vagón, embarcación, cueva, refugio natural, etc.)'
}

diccionario_departamentos = {
    5: 'Antioquia',
    8: 'Atlántico',
    11: 'Bogotá D.C.',
    13: 'Bolívar',
    15: 'Boyacá',
    17: 'Caldas',
    18: 'Caquetá',
    19: 'Cauca',
    20: 'Cesar',
    23: 'Córdoba',
    25: 'Cundinamarca',
    27: 'Chocó',
    41: 'Huila',
    44: 'La Guajira',
    47: 'Magdalena',
    50: 'Meta',
    52: 'Nariño',
    54: 'Norte de Santander',
    63: 'Quindío',
    66: 'Risaralda',
    68: 'Santander',
    70: 'Sucre',
    73: 'Tolima',
    76: 'Valle del Cauca',
    81: 'Arauca',
    85: 'Casanare',
    86: 'Putumayo',
    88: 'San Andrés',
    91: 'Amazonas',
    94: 'Guainía',
    95: 'Guaviare',
    97: 'Vaupés',
    99: 'Vichada'
}

materiales_paredes = {
    1: "Ladrillo, bloque, material prefabricado, piedra",
    2: "Madera pulida",
    3: "Adobe o tapia pisada",
    4: "Bahareque",
    5: "Madera burda, tabla, tablón",
    6: "Guadua",
    7: "Caña, esterilla, otro tipo de material vegetal",
    8: "Zinc, tela, cartón, latas, desechos, plástico",
    9: "Sin paredes"
}

materiales_pisos = {
    1: "Tierra, arena",
    2: "Cemento, gravilla",
    3: "Madera burda, tabla, tablón, otro vegetal",
    4: "Baldosín, ladrillo, vinisol, otros materiales sintéticos",
    5: "Mármol",
    6: "Madera pulida",
    7: "Alfombra o tapete de pared a pared"
}

sanitario = {
    1: "Inodoro conectado a alcantarillado",
    2: "Inodoro conectado a pozo séptico",
    3: "Inodoro sin conexión",
    4: "Letrina",
    5: "Bajamar",
    6: "No tiene servicio sanitario"
}

eliminacion_basura = {
    1: "Por recolección pública o privada",
    2: "La tiran a un río, quebrada, caño o laguna",
    3: "La tiran a un patio, lote, zanja o baldío",
    4: "La queman o entierran",
    5: "La eliminan de otra forma"
}

fuentes_agua = {
    1: "De acueducto por tubería",
    2: "De otra fuente por tubería",
    3: "De pozo con bomba",
    4: "De pozo sin bomba, aljibe, jagüey o barreno",
    5: "Aguas lluvias",
    6: "Río, quebrada, nacimiento ó manantial",
    7: "De pila pública",
    8: "Carro tanque",
    9: "Aguatero",
    10: "Agua embotellada o en bolsa"
}

tenencia_vivienda = {
    1: "Propia, totalmente pagada",
    2: "Propia, la están pagando",
    3: "En arriendo o subarriendo",
    4: "En usufructo",
    5: "Posesión sin título (ocupante de hecho) ó propiedad colectiva",
    6: "Otra, ¿cuál?___________________"
}

# Datos del hogar y la vivienda: Cargar datos
path_valores = r"C:\Users\mianm\OneDrive\Escritorio\Miguel Moreno\Personal Projects\GEIH - House Materials\Ene_2024\CSV\Datos del hogar y la vivienda.CSV"
df_valores = pd.read_csv(path_valores, encoding='latin-1', sep=';', header=0)

# Reemplazar las categorias con los diccionarios correspondientes
df_valores['CLASE'] = df_valores['CLASE'].replace(clase)
df_valores['DPTO'] = df_valores['DPTO'].replace(diccionario_departamentos)
df_valores['P4000'] = df_valores['P4000'].replace(categorias)
df_valores['P4010'] = df_valores['P4010'].replace(materiales_paredes)
df_valores['P4020'] = df_valores['P4020'].replace(materiales_pisos)
df_valores['P4030S1'] = df_valores['P4030S1'].replace(binario)
df_valores['P4030S2'] = df_valores['P4030S2'].replace(binario)
df_valores['P4030S3'] = df_valores['P4030S3'].replace(binario)
df_valores['P4030S4'] = df_valores['P4030S4'].replace(binario)
df_valores['P4030S5'] = df_valores['P4030S5'].replace(binario)
df_valores['P5020'] = df_valores['P5020'].replace(sanitario)
df_valores['P5040'] = df_valores['P5040'].replace(eliminacion_basura)
df_valores['P5050'] = df_valores['P5050'].replace(fuentes_agua)
df_valores['P5090'] = df_valores['P5090'].replace(tenencia_vivienda)

# Identificación de las variables relevantes
nombres_columnas = {
    'DIRECTORIO': 'DIRECTORIO',
    'PERIODO': 'Fecha',
    'CLASE': 'Zona',
    'DPTO': 'Departamento',
    'P4000': 'Tipo de vivienda',
    'P4010': 'Paredes',
    'P4020': 'Pisos',
    'P4030S1': 'Electricidad',
    'P4030S2': 'Gas natural',
    'P4030S3': 'Alcantarillado',
    'P4030S4': 'Recolección de basuras',
    'P4030S5': 'Acueducto',
    'P70': 'HogaresxVivienda',
    'P5000': 'Cuartos totales',
    'P5010': 'Cuartos para dormir',
    'P5020': 'Sanitario',
    'P5040': 'Eliminación basura',
    'P5050': 'Fuente de Agua',
    'P5090': 'Tenencia vivienda',
    'P5090S1': 'Otra vivienda',
    'P5140': 'Arriendo',
    'P5222S1': 'Cuenta Corriente',
    'P5222S2': 'Cuenta Ahorros',
    'P5222S3': 'CDT',
    'P5222S4': 'Préstamo para compra de vivienda',
    'P5222S5': 'Préstamo para compra de vehículo',
    'P5222S6': 'Préstamo de libre inversión',
    'P5222S7': 'Tarjeta de crédito',
    'P5222S8': 'Otro',
    'P5222S9': 'Ninguno',
    'P5222S10': 'No sabe',
    'P6008': 'Total de personas en el hogar'
}

# Cambiar el nombre de las varialbes
df_valores = df_valores.rename(columns=nombres_columnas)

# Filtrar el DataFrame para incluir solo las columnas relevantes
columnas_modificadas = nombres_columnas.values()
df_modificado = df_valores[columnas_modificadas]

'''
Para conocer el ingreso laboral del hogar es necesario obtener está variable del archivo "ocupados.CSV"
Diccionario: https://microdatos.dane.gov.co/index.php/catalog/819/data-dictionary/F64?file_name=Ocupados
'''

# Ingresos laborales: Cargar datos
path_ingresos = r"C:\Users\mianm\OneDrive\Escritorio\Miguel Moreno\Personal Projects\GEIH - House Materials\Ene_2024\CSV\Ocupados.CSV"
df_ingresos = pd.read_csv(path_ingresos, encoding='latin-1', sep=';', header=0)

#  Cambiar nombre de la variable de interés
df_ingresos = df_ingresos.rename(columns={'INGLABO': 'Ingresos laborales'})

# Fusionar los DataFrames en función de la columna 'DIRECTORIO'
df_final = pd.merge(df_modificado, df_ingresos[['DIRECTORIO', 'Ingresos laborales']], on='DIRECTORIO', how='left')

# Exportar el DataFrame filtrado a un archivo Excel
ruta_exportacion = r'C:\Users\mianm\OneDrive\Escritorio\Miguel Moreno\Personal Projects\GEIH - House Materials\GEIH_materiales_ingreso.xlsx'
df_final.to_excel(ruta_exportacion, sheet_name='Data', index=False)

print()
print("Exportación exitosa")
print()