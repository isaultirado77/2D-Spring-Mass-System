# Simulación de un Sistema Masa-Resorte en 2D

Este proyecto simula el comportamiento de un sistema masa-resorte en dos dimensiones utilizando el método de Runge-Kutta de cuarto orden (RK4). 
La masa está conectada a un resorte ideal, y el sistema incluye un término opcional de amortiguamiento.

## Descripción

- **Masa:** Representa el objeto conectado al resorte, con propiedades de posición, velocidad y masa.
- **Resorte:** Incluye una constante elástica (k) y una longitud de reposo.
- **Sistema:** Combina la masa y el resorte para calcular las fuerzas y resolver el movimiento usando RK4.

### Características
- Simulación en 2D del movimiento de la masa.
- Implementación del método RK4 para resolver ecuaciones diferenciales.
- Opción para incluir amortiguamiento.
- Representación gráfica de la trayectoria.

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

El programa genera una gráfica de la trayectoria de la masa en el espacio bidimensional.

---