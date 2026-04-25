# 📚 Solucionario de Álgebra - Baldor

Un solucionario interactivo de álgebra estilo Baldor con ejercicios reales y soluciones paso a paso.

## 🎯 Características

- ✅ **60 ejercicios auténticos** del libro Baldor (10 por capítulo)
- ✅ **6 capítulos completos** de álgebra fundamental
- ✅ **Soluciones paso a paso** detalladas y explicadas
- ✅ **Interfaz interactiva** para mostrar/ocultar soluciones
- ✅ **Renderizado matemático** con MathJax
- ✅ **Diseño responsivo** para cualquier dispositivo
- ✅ **Sitio estático** - sin servidor necesario

## 📖 Capítulos Disponibles

1. **Operaciones Básicas** (O001-O010)
2. **Productos Notables** (P001-P010)
3. **Factorización** (F001-F010)
4. **Fracciones Algebraicas** (R001-R010)
5. **Ecuaciones Lineales** (L001-L010)
6. **Ecuaciones Cuadráticas** (Q001-Q010)

## 🚀 Cómo Usar

### Opción 1: Directamente en GitHub Pages
Visita: `https://[tu-username].github.io/solucionario-baldor`

### Opción 2: Localmente
1. Clona el repositorio:
   ```bash
   git clone https://github.com/[tu-username]/solucionario-baldor.git
   cd solucionario-baldor
   ```

2. Abre `dist/index.html` en tu navegador

## 🛠️ Estructura del Proyecto

```
solucionario-baldor/
├── dist/                    # Sitio web generado (GitHub Pages)
│   ├── index.html
│   ├── capitulo-*.html
│   └── assets/
├── templates/               # Plantillas Jinja2
├── data/                   # Datos de ejercicios
├── baldor_exercises.py     # Base de datos de ejercicios
├── generate_baldor.py      # Generador principal
└── requirements.txt        # Dependencias Python
```

## 📝 Generar Ejercicios Adicionales

Si quieres agregar más ejercicios:

1. Edita `baldor_exercises.py`
2. Agrega nuevos ejercicios a los capítulos correspondientes
3. Ejecuta el generador:
   ```bash
   pip install -r requirements.txt
   python generate_baldor.py
   ```

## 🎨 Tecnologías Utilizadas

- **Python 3.14+** - Generador de ejercicios
- **SymPy** - Cálculos matemáticos simbólicos
- **Jinja2** - Motor de plantillas
- **MathJax** - Renderizado de fórmulas matemáticas
- **HTML5 + CSS3** - Interfaz web
- **JavaScript** - Interactividad
- **GitHub Pages** - Hosting gratuito

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## 🙏 Agradecimientos

- **Aurora Baldor** - Por su excelente libro de Álgebra
- **SymPy Team** - Por la biblioteca de matemáticas simbólicas
- **MathJax Team** - Por el renderizado de fórmulas
- **GitHub** - Por el hosting gratuito con GitHub Pages

---

**⭐ Si te gusta este proyecto, no olvides darle una estrella en GitHub!**
