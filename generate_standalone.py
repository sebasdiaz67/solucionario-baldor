#!/usr/bin/env python3
"""
Generador de Solucionario de Álgebra (Baldor) - Versión Standalone
Crea ejercicios de álgebra con soluciones paso a paso y genera sitio web estático
"""

import json
import os
from pathlib import Path

# Datos de ejemplo pre-generados (sin dependencias externas)
SAMPLE_EXERCISES = {
    "chapters": [
        {
            "title": "Operaciones Básicas",
            "slug": "operaciones-basicas",
            "exercises": [
                {
                    "id": "O001",
                    "problem": "(3x + 2) + (2x - 1)",
                    "steps": [
                        "Agrupar términos semejantes",
                        "3x + 2x + 2 - 1",
                        "5x + 1"
                    ],
                    "solution": "5x + 1"
                },
                {
                    "id": "O002", 
                    "problem": "(4x^2 - 3x + 1) - (2x^2 + x - 2)",
                    "steps": [
                        "Distribuir el signo negativo",
                        "4x^2 - 3x + 1 - 2x^2 - x + 2",
                        "Agrupar términos semejantes",
                        "(4x^2 - 2x^2) + (-3x - x) + (1 + 2)",
                        "2x^2 - 4x + 3"
                    ],
                    "solution": "2x^2 - 4x + 3"
                },
                {
                    "id": "O003",
                    "problem": "(2x + 3)(x - 1)",
                    "steps": [
                        "Aplicar propiedad distributiva",
                        "2x·x + 2x·(-1) + 3·x + 3·(-1)",
                        "2x^2 - 2x + 3x - 3",
                        "2x^2 + x - 3"
                    ],
                    "solution": "2x^2 + x - 3"
                },
                {
                    "id": "O004",
                    "problem": "(x^2 + 2x + 1) + (3x^2 - x + 4)",
                    "steps": [
                        "Agrupar términos semejantes",
                        "x^2 + 3x^2 + 2x - x + 1 + 4",
                        "4x^2 + x + 5"
                    ],
                    "solution": "4x^2 + x + 5"
                },
                {
                    "id": "O005",
                    "problem": "(2x - 5)(3x + 2)",
                    "steps": [
                        "Aplicar propiedad distributiva",
                        "2x·3x + 2x·2 - 5·3x - 5·2",
                        "6x^2 + 4x - 15x - 10",
                        "6x^2 - 11x - 10"
                    ],
                    "solution": "6x^2 - 11x - 10"
                }
            ]
        },
        {
            "title": "Productos Notables",
            "slug": "productos-notables",
            "exercises": [
                {
                    "id": "P001",
                    "problem": "(2x + 3)^2",
                    "steps": [
                        "Aplicar fórmula: (a + b)² = a² + 2ab + b²",
                        "a = 2x, b = 3",
                        "(2x)² + 2(2x)(3) + 3²",
                        "4x² + 12x + 9"
                    ],
                    "solution": "4x^2 + 12x + 9"
                },
                {
                    "id": "P002",
                    "problem": "(x - 4)^2",
                    "steps": [
                        "Aplicar fórmula: (a - b)² = a² - 2ab + b²",
                        "a = x, b = 4",
                        "x² - 2(x)(4) + 4²",
                        "x² - 8x + 16"
                    ],
                    "solution": "x^2 - 8x + 16"
                },
                {
                    "id": "P003",
                    "problem": "(3x + 2)(3x - 2)",
                    "steps": [
                        "Aplicar fórmula: (a + b)(a - b) = a² - b²",
                        "a = 3x, b = 2",
                        "(3x)² - 2²",
                        "9x² - 4"
                    ],
                    "solution": "9x^2 - 4"
                },
                {
                    "id": "P004",
                    "problem": "(x + 1)^3",
                    "steps": [
                        "Aplicar fórmula: (a + b)³ = a³ + 3a²b + 3ab² + b³",
                        "a = x, b = 1",
                        "x³ + 3x²(1) + 3x(1)² + 1³",
                        "x³ + 3x² + 3x + 1"
                    ],
                    "solution": "x^3 + 3x^2 + 3x + 1"
                },
                {
                    "id": "P005",
                    "problem": "(2x - 1)^3",
                    "steps": [
                        "Aplicar fórmula: (a - b)³ = a³ - 3a²b + 3ab² - b³",
                        "a = 2x, b = 1",
                        "(2x)³ - 3(2x)²(1) + 3(2x)(1)² - 1³",
                        "8x³ - 12x² + 6x - 1"
                    ],
                    "solution": "8x^3 - 12x^2 + 6x - 1"
                }
            ]
        },
        {
            "title": "Factorización",
            "slug": "factorizacion",
            "exercises": [
                {
                    "id": "F001",
                    "problem": "x^2 + 5x + 6",
                    "steps": [
                        "Buscar dos números que multipliquen 6 y sumen 5",
                        "Los números son 2 y 3",
                        "x^2 + 2x + 3x + 6",
                        "x(x + 2) + 3(x + 2)",
                        "(x + 2)(x + 3)"
                    ],
                    "solution": "(x + 2)(x + 3)"
                },
                {
                    "id": "F002",
                    "problem": "x^2 - 9",
                    "steps": [
                        "Reconocer diferencia de cuadrados: a² - b² = (a + b)(a - b)",
                        "a = x, b = 3",
                        "(x + 3)(x - 3)"
                    ],
                    "solution": "(x + 3)(x - 3)"
                },
                {
                    "id": "F003",
                    "problem": "4x^2 - 12x + 9",
                    "steps": [
                        "Reconocer cuadrado perfecto: a² - 2ab + b² = (a - b)²",
                        "a = 2x, b = 3",
                        "(2x - 3)²"
                    ],
                    "solution": "(2x - 3)^2"
                },
                {
                    "id": "F004",
                    "problem": "6x^2 + 11x + 3",
                    "steps": [
                        "Buscar dos números que multipliquen 18 y sumen 11",
                        "Los números son 9 y 2",
                        "6x^2 + 9x + 2x + 3",
                        "3x(2x + 3) + 1(2x + 3)",
                        "(3x + 1)(2x + 3)"
                    ],
                    "solution": "(3x + 1)(2x + 3)"
                },
                {
                    "id": "F005",
                    "problem": "3x^2 - 6x",
                    "steps": [
                        "Identificar factor común: 3x",
                        "3x(x - 2)"
                    ],
                    "solution": "3x(x - 2)"
                }
            ]
        },
        {
            "title": "Fracciones Algebraicas",
            "slug": "fracciones-algebraicas",
            "exercises": [
                {
                    "id": "R001",
                    "problem": "\\frac{x^2 - 4}{x + 2}",
                    "steps": [
                        "Factorizar el numerador: x² - 4 = (x + 2)(x - 2)",
                        "\\frac{(x + 2)(x - 2)}{x + 2}",
                        "Cancelar factor común (x + 2)",
                        "x - 2"
                    ],
                    "solution": "x - 2"
                },
                {
                    "id": "R002",
                    "problem": "\\frac{2x}{3} + \\frac{x}{6}",
                    "steps": [
                        "Encontrar común denominador: 6",
                        "\\frac{2x·2}{3·2} + \\frac{x}{6}",
                        "\\frac{4x}{6} + \\frac{x}{6}",
                        "\\frac{5x}{6}"
                    ],
                    "solution": "\\frac{5x}{6}"
                },
                {
                    "id": "R003",
                    "problem": "\\frac{x^2 - 1}{x^2 + 2x + 1}",
                    "steps": [
                        "Factorizar numerador: x² - 1 = (x + 1)(x - 1)",
                        "Factorizar denominador: x² + 2x + 1 = (x + 1)²",
                        "\\frac{(x + 1)(x - 1)}{(x + 1)(x + 1)}",
                        "Cancelar factor común (x + 1)",
                        "\\frac{x - 1}{x + 1}"
                    ],
                    "solution": "\\frac{x - 1}{x + 1}"
                },
                {
                    "id": "R004",
                    "problem": "\\frac{3x}{4} \\cdot \\frac{2}{x}",
                    "steps": [
                        "Multiplicar numeradores y denominadores",
                        "\\frac{3x·2}{4·x}",
                        "\\frac{6x}{4x}",
                        "Cancelar x",
                        "\\frac{6}{4} = \\frac{3}{2}"
                    ],
                    "solution": "\\frac{3}{2}"
                },
                {
                    "id": "R005",
                    "problem": "\\frac{x^2}{x + 1} \\div \\frac{x}{x + 1}",
                    "steps": [
                        "Multiplicar por el recíproco",
                        "\\frac{x^2}{x + 1} \\cdot \\frac{x + 1}{x}",
                        "\\frac{x^2(x + 1)}{x(x + 1)}",
                        "Cancelar (x + 1) y x",
                        "x"
                    ],
                    "solution": "x"
                }
            ]
        },
        {
            "title": "Ecuaciones Lineales",
            "slug": "ecuaciones-lineales",
            "exercises": [
                {
                    "id": "L001",
                    "problem": "2x + 3 = 7",
                    "steps": [
                        "Restar 3 de ambos lados",
                        "2x = 7 - 3",
                        "2x = 4",
                        "Dividir por 2",
                        "x = 2"
                    ],
                    "solution": "x = 2"
                },
                {
                    "id": "L002",
                    "problem": "3x - 5 = x + 7",
                    "steps": [
                        "Agrupar términos con x: 3x - x = 7 + 5",
                        "2x = 12",
                        "Dividir por 2",
                        "x = 6"
                    ],
                    "solution": "x = 6"
                },
                {
                    "id": "L003",
                    "problem": "4(x - 2) = 12",
                    "steps": [
                        "Distribuir el 4",
                        "4x - 8 = 12",
                        "Sumar 8 a ambos lados",
                        "4x = 20",
                        "Dividir por 4",
                        "x = 5"
                    ],
                    "solution": "x = 5"
                },
                {
                    "id": "L004",
                    "problem": "2x + 7 = 3x - 1",
                    "steps": [
                        "Agrupar términos con x: 2x - 3x = -1 - 7",
                        "-x = -8",
                        "Multiplicar por -1",
                        "x = 8"
                    ],
                    "solution": "x = 8"
                },
                {
                    "id": "L005",
                    "problem": "\\frac{x}{3} + 2 = 5",
                    "steps": [
                        "Restar 2 de ambos lados",
                        "\\frac{x}{3} = 3",
                        "Multiplicar por 3",
                        "x = 9"
                    ],
                    "solution": "x = 9"
                }
            ]
        },
        {
            "title": "Ecuaciones Cuadráticas",
            "slug": "ecuaciones-cuadraticas",
            "exercises": [
                {
                    "id": "Q001",
                    "problem": "x^2 - 5x + 6 = 0",
                    "steps": [
                        "Factorizar: buscar dos números que multipliquen 6 y sumen -5",
                        "Los números son -2 y -3",
                        "(x - 2)(x - 3) = 0",
                        "Aplicar propiedad del producto nulo",
                        "x - 2 = 0 → x = 2",
                        "x - 3 = 0 → x = 3"
                    ],
                    "solution": "x₁ = 2, x₂ = 3"
                },
                {
                    "id": "Q002",
                    "problem": "x^2 + 4x + 4 = 0",
                    "steps": [
                        "Reconocer cuadrado perfecto",
                        "(x + 2)² = 0",
                        "x + 2 = 0",
                        "x = -2"
                    ],
                    "solution": "x = -2"
                },
                {
                    "id": "Q003",
                    "problem": "x^2 - 9 = 0",
                    "steps": [
                        "Factorizar como diferencia de cuadrados",
                        "(x + 3)(x - 3) = 0",
                        "Aplicar propiedad del producto nulo",
                        "x + 3 = 0 → x = -3",
                        "x - 3 = 0 → x = 3"
                    ],
                    "solution": "x₁ = -3, x₂ = 3"
                },
                {
                    "id": "Q004",
                    "problem": "2x^2 + 7x + 3 = 0",
                    "steps": [
                        "Aplicar fórmula cuadrática: x = (-b ± √(b² - 4ac)) / 2a",
                        "a = 2, b = 7, c = 3",
                        "Discriminante: b² - 4ac = 49 - 24 = 25",
                        "x = (-7 ± √25) / 4",
                        "x = (-7 ± 5) / 4",
                        "x₁ = (-7 + 5)/4 = -2/4 = -1/2",
                        "x₂ = (-7 - 5)/4 = -12/4 = -3"
                    ],
                    "solution": "x₁ = -\\frac{1}{2}, x₂ = -3"
                },
                {
                    "id": "Q005",
                    "problem": "x^2 + 6x + 8 = 0",
                    "steps": [
                        "Factorizar: buscar dos números que multipliquen 8 y sumen 6",
                        "Los números son 2 y 4",
                        "(x + 2)(x + 4) = 0",
                        "Aplicar propiedad del producto nulo",
                        "x + 2 = 0 → x = -2",
                        "x + 4 = 0 → x = -4"
                    ],
                    "solution": "x₁ = -2, x₂ = -4"
                }
            ]
        }
    ],
    "total_exercises": 30
}

def generate_html_files(chapters_data, output_dir="dist"):
    """Genera archivos HTML básicos sin Jinja2"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Generar index.html
    index_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solucionario de Álgebra</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Georgia, serif; line-height: 1.6; color: #333; background: #fafafa; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
        h1 {{ text-align: center; color: #2c3e50; margin-bottom: 2rem; font-size: 2.5rem; }}
        .chapters {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem; }}
        .chapter-card {{ background: white; border: 2px solid #3498db; border-radius: 10px; padding: 1.5rem; transition: transform 0.3s ease; }}
        .chapter-card:hover {{ transform: translateY(-5px); box-shadow: 0 8px 25px rgba(52, 152, 219, 0.3); }}
        .chapter-title {{ color: #2c3e50; margin-bottom: 1rem; font-size: 1.3rem; }}
        .chapter-link {{ display: inline-block; background: #3498db; color: white; text-decoration: none; padding: 0.75rem 1.5rem; border-radius: 5px; transition: background 0.3s ease; }}
        .chapter-link:hover {{ background: #2980b9; }}
        .stats {{ background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Solucionario de Álgebra</h1>
        
        <div class="stats">
            <h2>📊 Estadísticas</h2>
            <p>Total de capítulos: {len(chapters_data['chapters'])}</p>
            <p>Total de ejercicios: {chapters_data['total_exercises']}</p>
        </div>
        
        <div class="chapters">
            {"".join([f'''
            <div class="chapter-card">
                <h3 class="chapter-title">Capítulo {i+1}: {chapter['title']}</h3>
                <p>Ejercicios: {len(chapter['exercises'])}</p>
                <p>ID Range: {chapter['exercises'][0]['id']} - {chapter['exercises'][-1]['id']}</p>
                <a href="capitulo-{chapter['slug']}.html" class="chapter-link">📝 Ver Ejercicios</a>
            </div>
            ''' for i, chapter in enumerate(chapters_data['chapters'])])}
        </div>
    </div>
</body>
</html>"""
    
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    
    # Generar HTML para cada capítulo
    for chapter in chapters_data["chapters"]:
        chapter_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter['title']} - Solucionario</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Georgia, serif; line-height: 1.6; color: #333; background: #fafafa; }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 2rem; }}
        h1 {{ text-align: center; color: #2c3e50; margin-bottom: 2rem; font-size: 2rem; }}
        .nav {{ background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 1rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        .nav a {{ color: white; text-decoration: none; margin: 0 1rem; padding: 0.5rem 1rem; border-radius: 5px; transition: background 0.3s ease; }}
        .nav a:hover {{ background: rgba(255,255,255,0.2); }}
        .controls {{ text-align: center; margin-bottom: 2rem; }}
        .btn {{ background: #27ae60; color: white; border: none; padding: 0.75rem 1.5rem; margin: 0 0.5rem; border-radius: 5px; cursor: pointer; font-size: 1rem; transition: background 0.3s ease; }}
        .btn:hover {{ background: #229954; }}
        .exercise {{ background: white; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 2rem; overflow: hidden; }}
        .exercise-header {{ background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 1rem; }}
        .exercise-problem {{ padding: 1.5rem; font-size: 1.2rem; text-align: center; background: #f8f9fa; }}
        .solution {{ padding: 1.5rem; display: none; }}
        .solution.show {{ display: block; }}
        .step {{ margin-bottom: 1rem; padding: 0.75rem; background: #f1f8ff; border-left: 4px solid #3498db; border-radius: 0 5px 5px 0; }}
        .final {{ background: linear-gradient(135deg, #f39c12, #e67e22); color: white; padding: 1rem; border-radius: 5px; text-align: center; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📖 {chapter['title']}</h1>
        
        <div class="nav">
            <a href="index.html">🏠 Inicio</a>
            {"".join([f'<a href="capitulo-{ch["slug"]}.html">{i+1}. {ch["title"]}</a>' for i, ch in enumerate(chapters_data["chapters"])])}
        </div>
        
        <div class="controls">
            <button class="btn" onclick="showAll()">👁️ Mostrar Todas</button>
            <button class="btn" onclick="hideAll()">🙈 Ocultar Todas</button>
        </div>
        
        {"".join([f'''
        <div class="exercise">
            <div class="exercise-header">
                <strong>Ejercicio {exercise['id']}</strong> ({i+1}/{len(chapter['exercises'])})
            </div>
            <div class="exercise-problem">
                <strong>Problema:</strong> $ {exercise['problem']} $
            </div>
            <div class="solution" id="sol-{i}">
                <h4>📝 Pasos de la Solución:</h4>
                {"".join([f'<div class="step">{j+1}. {step}</div>' for j, step in enumerate(exercise['steps'])])}
                <div class="final">
                    <strong>💡 Solución Final:</strong> $ {exercise['solution']} $
                </div>
            </div>
            <div style="padding: 1rem; text-align: center;">
                <button class="btn" onclick="toggleSolution({i})">👁️ Ver Solución</button>
            </div>
        </div>
        ''' for i, exercise in enumerate(chapter['exercises'])])}
    </div>
    
    <script>
        function toggleSolution(index) {{
            const sol = document.getElementById('sol-' + index);
            const btn = event.target;
            sol.classList.toggle('show');
            btn.textContent = sol.classList.contains('show') ? '🙈 Ocultar Solución' : '👁️ Ver Solución';
            if (sol.classList.contains('show')) {{
                MathJax.typesetPromise([sol]);
            }}
        }}
        
        function showAll() {{
            document.querySelectorAll('.solution').forEach(sol => sol.classList.add('show'));
            document.querySelectorAll('.btn').forEach(btn => {{
                if (btn.textContent.includes('Ver Solución')) {{
                    btn.textContent = '🙈 Ocultar Solución';
                }}
            }});
            MathJax.typesetPromise();
        }}
        
        function hideAll() {{
            document.querySelectorAll('.solution').forEach(sol => sol.classList.remove('show'));
            document.querySelectorAll('.btn').forEach(btn => {{
                if (btn.textContent.includes('Ocultar Solución')) {{
                    btn.textContent = '👁️ Ver Solución';
                }}
            }});
        }}
        
        window.MathJax = {{
            tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }}
        }};
    </script>
</body>
</html>"""
        
        filename = f"capitulo-{chapter['slug']}.html"
        with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
            f.write(chapter_html)

def main():
    """Función principal"""
    print("🚀 Generando Solucionario de Álgebra (Versión Standalone)...")
    
    # Guardar JSON
    print("💾 Guardando datos...")
    os.makedirs("data", exist_ok=True)
    with open("data/chapters.json", "w", encoding="utf-8") as f:
        json.dump(SAMPLE_EXERCISES, f, ensure_ascii=False, indent=2)
    
    # Generar HTML
    print("🌐 Generando HTML...")
    generate_html_files(SAMPLE_EXERCISES)
    
    # Estadísticas
    print(f"✅ Solucionario generado exitosamente!")
    print(f"📊 Total de capítulos: {len(SAMPLE_EXERCISES['chapters'])}")
    print(f"📝 Total de ejercicios: {SAMPLE_EXERCISES['total_exercises']}")
    print(f"📂 Archivos generados en 'dist/'")
    print(f"📄 Datos guardados en 'data/chapters.json'")
    print(f"\n🌐 Para ver el sitio, abre 'dist/index.html' en tu navegador")

if __name__ == "__main__":
    main()
