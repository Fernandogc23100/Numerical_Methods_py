# 📊 Examen Corto #2 - Cálculo Numérico (CDA135)

Este proyecto corresponde al Examen Corto #2 de la asignatura **Cálculo Numérico para Desarrollo de Aplicaciones (CDA135)**.

El programa implementa varios métodos numéricos de manera interactiva, modular y documentada.

---

## 🚀 Funcionalidades implementadas

- 📌 Evaluación polinomial por el **método de Horner**
- 📌 Cálculo de raíces por el **método de Muller**
- 📌 **Interpolación Lineal**
- 📌 Evaluación de polinomios de **Lagrange**
- 📌 Generación del **Polinomio de Lagrange** simbólico
- 📌 **Regresión lineal por Mínimos Cuadrados**

Todo el sistema es modular, interactivo y permite el ingreso dinámico de datos.

---

## 📂 Estructura del proyecto
```bash
proyecto_examen_cda135/
│
├── main.py               # Menú principal
├── horner.py             # Método de Horner
├── muller.py             # Método de Muller
├── interpolacion_lineal.py  # Interpolación de Lineal
├── lagrange.py           # Interpolación de Lagrange
├── minimos_cuadrados.py  # Regresión lineal
├── utils.py              # Funciones auxiliares
└── bibliografia.txt      # Referencias consultadas
```

## ⚙️ Requisitos
  
El proyecto utiliza:

- ✅ Python 3.x
- ✅ Librería `sympy` (para manejo simbólico de polinomios)
- ✅ (No requiere numpy ni otras librerías externas)

Puedes instalar las dependencias ejecutando:

```bash
pip install sympy

```



📌 Ejecución

Desde la carpeta raíz del proyecto:
```bash
python main.py

```
El menú interactivo te guiará para ejecutar cada método.
