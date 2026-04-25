<<<<<<< HEAD
# 📚 Solucionario de Álgebra (Baldor)

Un solucionario interactivo de álgebra generado automáticamente con ejercicios y soluciones paso a paso, publicado como sitio web estático.

## 🎯 Características

- **6 Capítulos completos** con 30 ejercicios cada uno
- **Soluciones paso a paso** para cada ejercicio
- **Renderizado matemático** con MathJax
- **Diseño responsivo** para cualquier dispositivo
- **Sitio estático** - no requiere servidor
- **Navegación intuitiva** entre capítulos

## 📖 Capítulos Incluidos

1. **Operaciones Básicas** - Suma, resta y multiplicación de polinomios
2. **Productos Notables** - Cuadrados y cubos de binomios
3. **Factorización** - Factor común, diferencia de cuadrados, etc.
4. **Fracciones Algebraicas** - Simplificación y operaciones
5. **Ecuaciones Lineales** - Resolución de ecuaciones de primer grado
6. **Ecuaciones Cuadráticas** - Fórmula cuadrática y factorización

## 🛠️ Tecnologías Utilizadas

- **Python 3** - Lenguaje principal
- **SymPy** - Cálculo simbólico y álgebra
- **Jinja2** - Motor de plantillas HTML
- **MathJax** - Renderizado de fórmulas matemáticas
- **HTML5 + CSS3 + JavaScript** - Frontend

## 📋 Requisitos

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)

## 🚀 Instalación y Ejecución

### 1. Clonar o descargar el proyecto

```bash
# Si tienes git
git clone <repositorio>
cd solucionario-baldor

# O simplemente descarga y extrae los archivos
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Generar el solucionario

```bash
python generate.py
```

### 4. Ver el sitio web

Abre el archivo `dist/index.html` en tu navegador web:

```bash
# En Windows
start dist/index.html

# En macOS
open dist/index.html

# En Linux
xdg-open dist/index.html
```

O simplemente haz doble clic en el archivo `index.html` dentro de la carpeta `dist`.

## 📁 Estructura del Proyecto

```
solucionario-baldor/
├── data/
│   └── chapters.json          # Datos generados (JSON)
├── templates/
│   ├── base.html             # Plantilla base
│   ├── index.html            # Página principal
│   └── chapter.html          # Plantilla de capítulos
├── dist/
│   ├── index.html            # Sitio web principal
│   ├── capitulo-*.html       # Páginas de capítulos
│   └── (assets CSS/JS)       # Estilos y scripts
├── generate.py                # Script generador principal
├── requirements.txt           # Dependencias Python
└── README.md                 # Este archivo
```

## 🎮 Cómo Usar el Solucionario

### Para Estudiantes

1. **Elige un capítulo** desde el menú lateral
2. **Intenta resolver** cada ejercicio por tu cuenta
3. **Verifica tu respuesta** haciendo clic en "Ver Solución"
4. **Estudia los pasos** detallados de la solución
5. **Practica** con otros ejercicios del mismo capítulo

### Funciones Interactivas

- **👁️ Ver/Ocultar Solución** - Control individual de cada ejercicio
- **👁️ Mostrar/Ocultar Todas** - Control masivo de soluciones
- **🔢 Navegación Rápida** - Salta a cualquier ejercicio
- **📊 Barra de Progreso** - Visualiza tu avance
- **⌨️ Atajos de Teclado** - Usa números para saltar a ejercicios

## 🔧 Personalización

### Modificar la Cantidad de Ejercicios

Edita `generate.py` y cambia los valores en la función `main()`:

```python
# Cambia 30 por el número deseado
chapters = [
    {
        "title": "Operaciones Básicas",
        "slug": "operaciones-basicas",
        "exercises": exercise_gen.generate_basic_operations(50)  # 50 ejercicios
    },
    # ... otros capítulos
]
```

### Cambiar la Semilla Aleatoria

Modifica la constante `SEED` en `generate.py` para generar diferentes conjuntos de ejercicios:

```python
SEED = 123  # Cambia este número para diferentes ejercicios
```

### Añadir Nuevos Capítulos

1. **Crea un nuevo método** en `ExerciseGenerator`
2. **Añade el capítulo** a la lista en `main()`
3. **Actualiza las plantillas** si es necesario

## 🐛 Solución de Problemas

### Problemas Comunes

**Error: ModuleNotFoundError**
```bash
# Asegúrate de instalar las dependencias
pip install -r requirements.txt
```

**Error: Permission denied**
```bash
# En Linux/macOS
chmod +x generate.py
python generate.py
```

**Las fórmulas no se renderizan**
- Asegúrate de tener conexión a Internet (MathJax se carga desde CDN)
- Verifica la consola del navegador para errores

**El sitio se ve mal**
- Limpia la caché del navegador
- Asegúrate de abrir `dist/index.html` (no otro archivo)

### Regenerar el Sitio

Si modificas algo en el código Python:

```bash
python generate.py
```

Los archivos HTML se regenerarán automáticamente.

## 🎨 Personalización Visual

### Cambiar Colores

Edita el CSS en `templates/base.html`:

```css
/* Color principal */
.sidebar {
    background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
}

/* Color de acento */
.nav-menu a:hover {
    background-color: #3498db;
}
```

### Modificar el Logo

Reemplaza el emoji en el sidebar:

```html
<h1>📚 Solucionario de Álgebra</h1>
<!-- Cambia 📚 por tu icono o logo -->
```

## 📚 Referencias

- **SymPy Documentation**: https://docs.sympy.org/
- **MathJax Documentation**: https://docs.mathjax.org/
- **Jinja2 Documentation**: https://jinja.palletsprojects.com/

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## 🙏 Agradecimientos

- **SymPy Team** - Por la excelente biblioteca de matemáticas simbólicas
- **MathJax Team** - Por el renderizado de fórmulas matemáticas
- **Jinja2 Team** - Por el motor de plantillas

---

**¡Feliz aprendizaje! 🎓**

Si tienes algún problema o sugerencia, no dudes en abrir un issue en el repositorio.
=======
# solucionario-baldor
Ejercicio con python y html generado con IA para solucionar algunos ejercicios matemáticos
>>>>>>> 0d5dbb9efbbd870606f1c90524427d205b62925f
