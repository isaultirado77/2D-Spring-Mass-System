# Simulación de un Sistema Masa-Resorte en 2D

Este proyecto simula el comportamiento de un sistema masa-resorte en dos dimensiones utilizando el método de Runge-Kutta de cuarto orden (RK4). 
La masa está conectada a un resorte ideal, y el sistema incluye un término opcional de amortiguamiento.


## Análisis y Resultados
Los resultados, incluyendo trayectorias, espacio fase y energía, se encuentran en el notebook:

[![Ver Análisis en Jupyter](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/isaultirado77/2D-Spring-Mass-System/blob/main/mass_spring_simulation.ipynb)



## Requisitos

- Python 3.7+
- Librerías: `numpy`, `matplotlib`
## Ejecución

1. Clona este repositorio:
```bash
git clone <https://github.com/isaultirado77/2D-Spring-Mass-System>
```

2. Navega al directorio del proyecto:
```bash
cd 2d_spring_mass_system
```

3. Ejecuta el script principal:
```bash
python 2d_mass_spring_system.py
```

## Parámetros iniciales

- **Masa:** `1.0 kg`
- **Constante de resorte:** `10.0 N/m`
- **Longitud de reposo:** `1.0 m`
- **Amortiguamiento:** `0.1`
- **Posición inicial:** `[1.0, 0.0]`
- **Velocidad inicial:** `[0.0, 2.0]`

## Resultados

El programa genera los datos y una gráfica de la trayectoria de la partícula en el espacio bidimensional.

---