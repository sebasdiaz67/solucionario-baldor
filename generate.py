#!/usr/bin/env python3
"""
Generador de Solucionario de Álgebra (Baldor)
Crea ejercicios de álgebra con soluciones paso a paso y genera sitio web estático
"""

import json
import random
import os
from pathlib import Path
from typing import List, Dict, Any, Tuple
from jinja2 import Environment, FileSystemLoader
import sympy as sp
from sympy import symbols, simplify, expand, factor, solve, Eq

# Configuración
SEED = 42  # Semilla para reproducibilidad
random.seed(SEED)

# Variables simbólicas comunes
x, y, z, a, b, c, m, n = symbols('x y z a b c m n')

class ExerciseGenerator:
    """Generador de ejercicios de álgebra con SymPy"""
    
    def __init__(self):
        self.exercise_counter = 1
    
    def generate_basic_operations(self, count: int = 30) -> List[Dict]:
        """Capítulo 1: Operaciones básicas con polinomios"""
        exercises = []
        
        for i in range(count):
            # Generar polinomios aleatorios directamente con SymPy
            coeff_range = range(-5, 6)  # Reducir rango para evitar errores
            degree = random.randint(1, 3)
            
            # Crear primer polinomio con SymPy
            p1 = 0
            poly1_terms = []
            for j in range(degree + 1):
                coeff = random.choice(coeff_range)
                if coeff != 0:
                    p1 += coeff * x**j
                    # Formatear para display
                    if j == 0:
                        term = f"{coeff}"
                    elif j == 1:
                        term = f"{coeff}x" if coeff != 1 else "x"
                    else:
                        term = f"{coeff}x^{j}" if coeff != 1 else f"x^{j}"
                    poly1_terms.append(term)
            
            # Crear segundo polinomio con SymPy
            degree2 = random.randint(1, 2)
            p2 = 0
            poly2_terms = []
            for j in range(degree2 + 1):
                coeff = random.choice(coeff_range)
                if coeff != 0:
                    p2 += coeff * x**j
                    # Formatear para display
                    if j == 0:
                        term = f"{coeff}"
                    elif j == 1:
                        term = f"{coeff}x" if coeff != 1 else "x"
                    else:
                        term = f"{coeff}x^{j}" if coeff != 1 else f"x^{j}"
                    poly2_terms.append(term)
            
            # Formatear polinomios para display
            poly1_str = " + ".join(poly1_terms).replace("+ -", "- ")
            poly2_str = " + ".join(poly2_terms).replace("+ -", "- ")
            
            # Operación aleatoria
            operation = random.choice(["suma", "resta", "multiplicación"])
            
            if operation == "suma":
                problem = f"({poly1_str}) + ({poly2_str})"
                result = simplify(p1 + p2)
                steps = [
                    f"Sumar los términos semejantes",
                    f"({poly1_str}) + ({poly2_str}) = {sp.latex(result)}"
                ]
            elif operation == "resta":
                problem = f"({poly1_str}) - ({poly2_str})"
                result = simplify(p1 - p2)
                steps = [
                    f"Restar los términos semejantes",
                    f"({poly1_str}) - ({poly2_str}) = {sp.latex(result)}"
                ]
            else:  # multiplicación
                problem = f"({poly1_str}) \\cdot ({poly2_str})"
                result = expand(p1 * p2)
                steps = [
                    f"Aplicar propiedad distributiva",
                    f"({poly1_str}) \\cdot ({poly2_str}) = {sp.latex(result)}"
                ]
            
            exercises.append({
                "id": f"O{self.exercise_counter:03d}",
                "problem": problem,
                "steps": steps,
                "solution": sp.latex(result)
            })
            self.exercise_counter += 1
        
        return exercises
    
    def generate_notable_products(self, count: int = 30) -> List[Dict]:
        """Capítulo 2: Productos notables"""
        exercises = []
        patterns = [
            ("(a + b)^2", "Cuadrado de binomio suma"),
            ("(a - b)^2", "Cuadrado de binomio resta"),
            ("(a + b)(a - b)", "Diferencia de cuadrados"),
            ("(a + b)^3", "Cubo de binomio suma"),
            ("(a - b)^3", "Cubo de binomio resta")
        ]
        
        for i in range(count):
            pattern, description = random.choice(patterns)
            
            # Generar valores aleatorios para a y b
            a_val = random.randint(1, 10)
            b_val = random.randint(1, 10)
            
            a_sym, b_sym = symbols('a b')
            
            if pattern == "(a + b)^2":
                problem = f"({a_val}x + {b_val})^2"
                expr = (a_val*x + b_val)**2
                result = expand(expr)
                steps = [
                    f"Aplicar fórmula: (a + b)² = a² + 2ab + b²",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x)² + 2({a_val}x)({b_val}) + ({b_val})²",
                    f"{a_val**2}x² + {2*a_val*b_val}x + {b_val**2}"
                ]
            elif pattern == "(a - b)^2":
                problem = f"({a_val}x - {b_val})^2"
                expr = (a_val*x - b_val)**2
                result = expand(expr)
                steps = [
                    f"Aplicar fórmula: (a - b)² = a² - 2ab + b²",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x)² - 2({a_val}x)({b_val}) + ({b_val})²",
                    f"{a_val**2}x² - {2*a_val*b_val}x + {b_val**2}"
                ]
            elif pattern == "(a + b)(a - b)":
                problem = f"({a_val}x + {b_val})({a_val}x - {b_val})"
                expr = (a_val*x + b_val)*(a_val*x - b_val)
                result = expand(expr)
                steps = [
                    f"Aplicar fórmula: (a + b)(a - b) = a² - b²",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x)² - ({b_val})²",
                    f"{a_val**2}x² - {b_val**2}"
                ]
            elif pattern == "(a + b)^3":
                problem = f"({a_val}x + {b_val})^3"
                expr = (a_val*x + b_val)**3
                result = expand(expr)
                steps = [
                    f"Aplicar fórmula: (a + b)³ = a³ + 3a²b + 3ab² + b³",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x)³ + 3({a_val}x)²({b_val}) + 3({a_val}x)({b_val})² + ({b_val})³",
                    f"{a_val**3}x³ + {3*a_val**2*b_val}x² + {3*a_val*b_val**2}x + {b_val**3}"
                ]
            else:  # (a - b)^3
                problem = f"({a_val}x - {b_val})^3"
                expr = (a_val*x - b_val)**3
                result = expand(expr)
                steps = [
                    f"Aplicar fórmula: (a - b)³ = a³ - 3a²b + 3ab² - b³",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x)³ - 3({a_val}x)²({b_val}) + 3({a_val}x)({b_val})² - ({b_val})³",
                    f"{a_val**3}x³ - {3*a_val**2*b_val}x² + {3*a_val*b_val**2}x - {b_val**3}"
                ]
            
            exercises.append({
                "id": f"P{self.exercise_counter:03d}",
                "problem": problem,
                "steps": steps,
                "solution": sp.latex(result)
            })
            self.exercise_counter += 1
        
        return exercises
    
    def generate_factorization(self, count: int = 30) -> List[Dict]:
        """Capítulo 3: Factorización"""
        exercises = []
        
        for i in range(count):
            factor_type = random.choice(["common_factor", "difference_squares", "perfect_square", "quadratic"])
            
            if factor_type == "common_factor":
                # Factor común
                a_val = random.randint(2, 8)
                b_val = random.randint(1, 6)
                c_val = random.randint(1, 4)
                problem = f"{a_val}x² + {a_val*b_val}x + {a_val*c_val}"
                expr = a_val*x**2 + a_val*b_val*x + a_val*c_val
                result = factor(expr)
                steps = [
                    f"Identificar factor común: {a_val}",
                    f"Factorizar: {a_val}(x² + {b_val}x + {c_val})",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            elif factor_type == "difference_squares":
                # Diferencia de cuadrados
                a_val = random.randint(2, 10)
                b_val = random.randint(2, 8)
                problem = f"{a_val**2}x² - {b_val**2}"
                expr = a_val**2*x**2 - b_val**2
                result = factor(expr)
                steps = [
                    f"Reconocer diferencia de cuadrados: a² - b² = (a + b)(a - b)",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x + {b_val})({a_val}x - {b_val})",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            elif factor_type == "perfect_square":
                # Cuadrado perfecto
                a_val = random.randint(2, 8)
                b_val = random.randint(2, 6)
                problem = f"{a_val**2}x² + {2*a_val*b_val}x + {b_val**2}"
                expr = a_val**2*x**2 + 2*a_val*b_val*x + b_val**2
                result = factor(expr)
                steps = [
                    f"Reconocer cuadrado perfecto: a² + 2ab + b² = (a + b)²",
                    f"a = {a_val}x, b = {b_val}",
                    f"({a_val}x + {b_val})²",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            else:  # quadratic
                # Factorización cuadrática
                m_val = random.randint(1, 6)
                n_val = random.randint(1, 6)
                p_val = random.randint(1, 4)
                q_val = random.randint(1, 4)
                problem = f"{m_val*n_val}x² + ({m_val*q_val + n_val*p_val})x + {p_val*q_val}"
                expr = m_val*n_val*x**2 + (m_val*q_val + n_val*p_val)*x + p_val*q_val
                result = factor(expr)
                steps = [
                    f"Buscar dos números que multipliquen {m_val*n_val*p_val*q_val} y sumen {m_val*q_val + n_val*p_val}",
                    f"Factorizar por agrupación",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            exercises.append({
                "id": f"F{self.exercise_counter:03d}",
                "problem": problem,
                "steps": steps,
                "solution": sp.latex(result)
            })
            self.exercise_counter += 1
        
        return exercises
    
    def generate_algebraic_fractions(self, count: int = 30) -> List[Dict]:
        """Capítulo 4: Fracciones algebraicas"""
        exercises = []
        
        for i in range(count):
            operation = random.choice(["simplify", "add", "subtract", "multiply", "divide"])
            
            if operation == "simplify":
                # Simplificar fracción
                num_deg = random.randint(1, 3)
                den_deg = random.randint(1, 3)
                
                num_coeffs = [random.randint(1, 5) for _ in range(num_deg + 1)]
                den_coeffs = [random.randint(1, 5) for _ in range(den_deg + 1)]
                
                num_poly = sum(num_coeffs[j] * x**j for j in range(num_deg + 1))
                den_poly = sum(den_coeffs[j] * x**j for j in range(den_deg + 1))
                
                problem = f"\\frac{{{sp.latex(num_poly)}}}{{{sp.latex(den_poly)}}}"
                result = simplify(num_poly/den_poly)
                steps = [
                    f"Factorizar numerador y denominador",
                    f"Cancelar factores comunes",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            elif operation == "add":
                # Sumar fracciones
                a_val = random.randint(1, 5)
                b_val = random.randint(1, 5)
                c_val = random.randint(1, 5)
                problem = f"\\frac{{{a_val}}}{{x}} + \\frac{{{b_val}}}{{{c_val}x}}"
                result = simplify(a_val/x + b_val/(c_val*x))
                steps = [
                    f"Encontrar común denominador: {c_val}x",
                    f"\\frac{{{a_val*c_val}}}{{{c_val}x}} + \\frac{{{b_val}}}{{{c_val}x}}",
                    f"\\frac{{{a_val*c_val + b_val}}}{{{c_val}x}}",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            elif operation == "multiply":
                # Multiplicar fracciones
                a_val = random.randint(1, 5)
                b_val = random.randint(1, 5)
                c_val = random.randint(1, 5)
                d_val = random.randint(1, 5)
                problem = f"\\frac{{{a_val}x}}{{{b_val}}} \\cdot \\frac{{{c_val}}}{{{d_val}x}}"
                result = simplify((a_val*x/b_val) * (c_val/(d_val*x)))
                steps = [
                    f"Multiplicar numeradores y denominadores",
                    f"\\frac{{{a_val*c_val}x}}{{{b_val*d_val}x}}",
                    f"Cancelar x",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            else:  # divide
                # Dividir fracciones
                a_val = random.randint(1, 5)
                b_val = random.randint(1, 5)
                c_val = random.randint(1, 5)
                d_val = random.randint(1, 5)
                problem = f"\\frac{{{a_val}x}}{{{b_val}}} \\div \\frac{{{c_val}x}}{{{d_val}}}"
                result = simplify((a_val*x/b_val) / (c_val*x/d_val))
                steps = [
                    f"Multiplicar por el recíproco",
                    f"\\frac{{{a_val}x}}{{{b_val}}} \\cdot \\frac{{{d_val}}}{{{c_val}x}}",
                    f"\\frac{{{a_val*d_val}x}}{{{b_val*c_val}x}}",
                    f"Cancelar x",
                    f"Resultado: {sp.latex(result)}"
                ]
            
            exercises.append({
                "id": f"R{self.exercise_counter:03d}",
                "problem": problem,
                "steps": steps,
                "solution": sp.latex(result)
            })
            self.exercise_counter += 1
        
        return exercises
    
    def generate_linear_equations(self, count: int = 30) -> List[Dict]:
        """Capítulo 5: Ecuaciones lineales"""
        exercises = []
        
        for i in range(count):
            # Generar ecuación lineal ax + b = cx + d
            a = random.randint(1, 10)
            b = random.randint(-10, 10)
            c = random.randint(1, 10)
            d = random.randint(-10, 10)
            
            # Asegurar que tenga solución
            if a == c:
                c = random.randint(1, 10)
                while c == a:
                    c = random.randint(1, 10)
            
            # Construir ecuación
            left_terms = []
            if a != 1:
                left_terms.append(f"{a}x")
            else:
                left_terms.append("x")
            
            if b >= 0:
                left_terms.append(f"+ {b}")
            else:
                left_terms.append(f"- {abs(b)}")
            
            right_terms = []
            if c != 1:
                right_terms.append(f"{c}x")
            else:
                right_terms.append("x")
            
            if d >= 0:
                right_terms.append(f"+ {d}")
            else:
                right_terms.append(f"- {abs(d)}")
            
            problem = f"{' '.join(left_terms)} = {' '.join(right_terms)}"
            
            # Resolver
            solution_value = sp.solve(Eq(a*x + b, c*x + d), x)[0]
            
            steps = [
                f"Agrupar términos con x: {a}x - {c}x = {d} - {b}",
                f"({a - c})x = {d - b}",
                f"x = {d - b}/{a - c}",
                f"x = {solution_value}"
            ]
            
            exercises.append({
                "id": f"L{self.exercise_counter:03d}",
                "problem": problem,
                "steps": steps,
                "solution": sp.latex(solution_value)
            })
            self.exercise_counter += 1
        
        return exercises
    
    def generate_quadratic_equations(self, count: int = 30) -> List[Dict]:
        """Capítulo 6: Ecuaciones cuadráticas"""
        exercises = []
        
        for i in range(count):
            method = random.choice(["formula", "factorization"])
            
            if method == "formula":
                # Ecuación cuadrática que requiere fórmula
                a = random.randint(1, 5)
                b = random.randint(-10, 10)
                c = random.randint(-10, 10)
                
                # Asegurar que tenga solución real
                discriminant = b**2 - 4*a*c
                while discriminant < 0:
                    b = random.randint(-10, 10)
                    c = random.randint(-10, 10)
                    discriminant = b**2 - 4*a*c
                
                problem = f"{a}x²"
                if b >= 0:
                    problem += f" + {b}x"
                else:
                    problem += f" - {abs(b)}x"
                
                if c >= 0:
                    problem += f" + {c} = 0"
                else:
                    problem += f" - {abs(c)} = 0"
                
                solutions = sp.solve(Eq(a*x**2 + b*x + c, 0), x)
                
                steps = [
                    f"Aplicar fórmula cuadrática: x = (-b ± √(b² - 4ac)) / 2a",
                    f"Identificar coeficientes: a = {a}, b = {b}, c = {c}",
                    f"Discriminante: b² - 4ac = {b**2 - 4*a*c}",
                    f"x = ({-b} ± √({b**2 - 4*a*c})) / {2*a}"
                ]
                
            else:  # factorization
                # Ecuación cuadrática factorizable
                m = random.randint(1, 6)
                n = random.randint(1, 6)
                p = random.randint(1, 4)
                q = random.randint(1, 4)
                
                a = m * n
                b = m * q + n * p
                c = p * q
                
                problem = f"{a}x² + {b}x + {c} = 0"
                
                solutions = sp.solve(Eq(a*x**2 + b*x + c, 0), x)
                
                steps = [
                    f"Factorizar la ecuación",
                    f"Buscar dos números que multipliquen {a*c} y sumen {b}",
                    f"({m}x + {p})({n}x + {q}) = 0",
                    f"Aplicar propiedad del producto nulo",
                    f"x₁ = -{p}/{m}, x₂ = -{q}/{n}"
                ]
            
            if len(solutions) == 2:
                solution_str = f"x₁ = {sp.latex(solutions[0])}, x₂ = {sp.latex(solutions[1])}"
            else:
                solution_str = f"x = {sp.latex(solutions[0])}"
            
            exercises.append({
                "id": f"Q{self.exercise_counter:03d}",
                "problem": problem,
                "steps": steps,
                "solution": solution_str
            })
            self.exercise_counter += 1
        
        return exercises

class HTMLGenerator:
    """Generador de HTML a partir de plantillas Jinja2"""
    
    def __init__(self, template_dir: str = "templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))
    
    def generate_html_files(self, chapters_data: Dict, output_dir: str = "dist"):
        """Genera todos los archivos HTML"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Cargar plantillas
        base_template = self.env.get_template("base.html")
        index_template = self.env.get_template("index.html")
        chapter_template = self.env.get_template("chapter.html")
        
        # Generar index.html
        index_html = index_template.render(
            chapters=chapters_data["chapters"],
            title="Solucionario de Álgebra"
        )
        
        with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html)
        
        # Generar HTML para cada capítulo
        for chapter in chapters_data["chapters"]:
            chapter_html = chapter_template.render(
                chapter=chapter,
                chapters=chapters_data["chapters"],
                title=f"Solucionario - {chapter['title']}"
            )
            
            filename = f"capitulo-{chapter['slug']}.html"
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(chapter_html)

def main():
    """Función principal"""
    print("Generando Solucionario de Algebra...")
    
    # Crear generadores
    exercise_gen = ExerciseGenerator()
    html_gen = HTMLGenerator()
    
    # Generar ejercicios por capítulo
    chapters = [
        {
            "title": "Operaciones Básicas",
            "slug": "operaciones-basicas",
            "exercises": exercise_gen.generate_basic_operations(30)
        },
        {
            "title": "Productos Notables",
            "slug": "productos-notables", 
            "exercises": exercise_gen.generate_notable_products(30)
        },
        {
            "title": "Factorización",
            "slug": "factorizacion",
            "exercises": exercise_gen.generate_factorization(30)
        },
        {
            "title": "Fracciones Algebraicas",
            "slug": "fracciones-algebraicas",
            "exercises": exercise_gen.generate_algebraic_fractions(30)
        },
        {
            "title": "Ecuaciones Lineales",
            "slug": "ecuaciones-lineales",
            "exercises": exercise_gen.generate_linear_equations(30)
        },
        {
            "title": "Ecuaciones Cuadráticas",
            "slug": "ecuaciones-cuadraticas",
            "exercises": exercise_gen.generate_quadratic_equations(30)
        }
    ]
    
    # Crear estructura de datos
    data = {
        "chapters": chapters,
        "total_exercises": sum(len(ch["exercises"]) for ch in chapters)
    }
    
    # Guardar JSON
    print("Guardando datos...")
    os.makedirs("data", exist_ok=True)
    with open("data/chapters.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Generar HTML
    print("Generando HTML...")
    html_gen.generate_html_files(data)
    
    # Estadísticas
    print(f"Solucionario generado exitosamente!")
    print(f"Total de capítulos: {len(chapters)}")
    print(f"Total de ejercicios: {data['total_exercises']}")
    print(f"Archivos generados en 'dist/'")
    print(f"Datos guardados en 'data/chapters.json'")
    print(f"\nPara ver el sitio, abre 'dist/index.html' en tu navegador")

if __name__ == "__main__":
    main()
