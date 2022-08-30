# -*- coding: utf-8 -*-
# BCRPData

## Librerias

import pandas as pd
import requests

## Metadatos de series

metadata = pd.read_csv('https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata',
                       delimiter=';',
                       encoding='latin-1')

## Funcion para consultar datos

def bcrp_data(serie, inicio, fin):
  
  # Establecer consulta
  periodo = '/'+inicio+'/'+fin
  url = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'+serie+'/json'+periodo
  
  # Consulta de datos
  serie_api = requests.get(url)
  serie_json = serie_api.json()
  
  serie = serie_json.get('config')['series'][0]['name']
  periodos = serie_json.get('periods')
  
  valores = []
  for p in periodos:
    values = p['values']
    for v in values:
      v = float(v)
      valores.append(v)
  fechas = []
  for p in periodos:
    name = p['name']
    fechas.append(name)
  
  serie_dic = {"Fecha":fechas, str(serie):valores}
  serie_df = pd.DataFrame(serie_dic)
  return(serie_df)

## Ejemplo

fecha_inicio = '2017-01'
fecha_fin = '2022-08'
pbi = 'PN01770AM'

bcrp_data(pbi, fecha_inicio, fecha_fin)
