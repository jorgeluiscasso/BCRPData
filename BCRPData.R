# BCRPData ----

## Librerias ----

#install.packages("httr")
library(httr)
#install.packages("jsonlite")
library(jsonlite)

## Metadatos de series ---

metadata <- read.csv(url("https://estadisticas.bcrp.gob.pe/estadisticas/series/metadata"),
                     sep=";")

## Funcion para consultar datos ----

bcrp_data <- function(serie, inicio, fin){
  
  # Establecer consulta
  periodo <- paste("/", inicio, "/", fin, sep="")
  url <- paste("https://estadisticas.bcrp.gob.pe/estadisticas/series/api/",
               serie,
               "/json",
               periodo,
               sep="")
  
  # Consulta de datos
  serie_api <- GET(url)
  serie_json <- fromJSON(rawToChar(serie_api$content))
  serie_df <- as.data.frame(serie_json$periods)
  names(serie_df)[1] <- "Fecha"
  names(serie_df)[2] <- as.character(serie_json$config$title)
  return(serie_df)
  
}

## Ejemplo ----

fecha_inicio <- "2017-01"
fecha_fin <- "2022-08"
pbi <- "PN01770AM"

bcrp_data(pbi, fecha_inicio, fecha_fin)
