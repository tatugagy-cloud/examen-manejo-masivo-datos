# Análisis de sensores industriales

## Descripción

Este proyecto realiza un análisis de datos de sensores industriales utilizando Python y pandas.

El conjunto de datos contiene 100,000 registros de sensores industriales.

## Objetivo

Analizar los datos de temperatura de los sensores, obtener estadísticas por planta, identificar la temperatura máxima y detectar alertas de temperatura.

## Datos

El archivo utilizado es:

`data/sensores_industriales.csv`

Las variables principales son:

- `id_registro`
- `fecha_hora`
- `id_sensor`
- `planta`
- `temperatura_c`
- `vibracion_mm_s`

## Análisis realizado

El programa permite:

- Contar los registros.
- Contar los sensores diferentes.
- Calcular el promedio de temperatura por planta.
- Identificar la temperatura máxima.
- Identificar el sensor y fecha de la temperatura máxima.
- Detectar temperaturas mayores a 85 °C.
- Contar las alertas por planta.
- Generar un archivo con las alertas.

## Resultado

El análisis genera:

`resultados/alertas.csv`

## Ejecución

Para ejecutar el programa:

```bash
python analisis.py