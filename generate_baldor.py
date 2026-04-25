#!/usr/bin/env python3
"""
Generador de Solucionario de Álgebra estilo Baldor
Usa ejercicios reales del libro Baldor con soluciones paso a paso
"""

import json
import os
from jinja2 import Environment, FileSystemLoader
from baldor_exercises import BALDOR_EXERCISES

class BaldorExerciseGenerator:
    """Generador de ejercicios del libro Baldor"""
    
    def __init__(self):
        self.exercise_counter = 1
    
    def get_chapter_exercises(self, chapter_slug: str) -> list:
        """Obtener ejercicios de un capítulo específico"""
        return BALDOR_EXERCISES.get(chapter_slug, [])
    
    def generate_all_chapters(self) -> list:
        """Generar todos los capítulos con ejercicios del Baldor"""
        chapters = [
            {
                "title": "Operaciones Básicas",
                "slug": "operaciones-basicas",
                "exercises": self.get_chapter_exercises("operaciones-basicas")
            },
            {
                "title": "Productos Notables",
                "slug": "productos-notables",
                "exercises": self.get_chapter_exercises("productos-notables")
            },
            {
                "title": "Factorización",
                "slug": "factorizacion",
                "exercises": self.get_chapter_exercises("factorizacion")
            },
            {
                "title": "Fracciones Algebraicas",
                "slug": "fracciones-algebraicas",
                "exercises": self.get_chapter_exercises("fracciones-algebraicas")
            },
            {
                "title": "Ecuaciones Lineales",
                "slug": "ecuaciones-lineales",
                "exercises": self.get_chapter_exercises("ecuaciones-lineales")
            },
            {
                "title": "Ecuaciones Cuadráticas",
                "slug": "ecuaciones-cuadraticas",
                "exercises": self.get_chapter_exercises("ecuaciones-cuadraticas")
            }
        ]
        
        return chapters

class HTMLGenerator:
    """Generador de HTML a partir de plantillas Jinja2"""
    
    def __init__(self, template_dir: str = "templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))
    
    def generate_html_files(self, chapters_data: dict, output_dir: str = "dist"):
        """Generar todos los archivos HTML"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Generar index.html
        index_template = self.env.get_template("index.html")
        index_html = index_template.render(
            chapters=chapters_data["chapters"],
            title="Solucionario de Álgebra - Baldor"
        )
        
        with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html)
        
        # Generar capítulos individuales
        chapter_template = self.env.get_template("chapter.html")
        
        for chapter in chapters_data["chapters"]:
            chapter_html = chapter_template.render(
                chapter=chapter,
                chapters=chapters_data["chapters"],
                title=f"Solucionario Baldor - {chapter['title']}"
            )
            
            filename = f"capitulo-{chapter['slug']}.html"
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(chapter_html)

def main():
    """Función principal"""
    print("Generando Solucionario de Álgebra estilo Baldor...")
    
    # Crear generador
    exercise_gen = BaldorExerciseGenerator()
    html_gen = HTMLGenerator()
    
    # Generar capítulos con ejercicios del Baldor
    chapters = exercise_gen.generate_all_chapters()
    
    # Crear estructura de datos
    data = {
        "chapters": chapters,
        "total_exercises": sum(len(ch["exercises"]) for ch in chapters)
    }
    
    # Guardar JSON
    print("Guardando datos...")
    os.makedirs("data", exist_ok=True)
    with open("data/chapters_baldor.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Generar HTML
    print("Generando HTML...")
    html_gen.generate_html_files(data)
    
    # Estadísticas
    print(f"Solucionario Baldor generado exitosamente!")
    print(f"Total de capítulos: {len(chapters)}")
    print(f"Total de ejercicios: {data['total_exercises']}")
    print(f"Archivos generados en 'dist/'")
    print(f"Datos guardados en 'data/chapters_baldor.json'")
    print(f"\nPara ver el sitio, abre 'dist/index.html' en tu navegador")
    
    # Mostrar resumen por capítulo
    print(f"\nResumen de ejercicios por capítulo:")
    for chapter in chapters:
        print(f"- {chapter['title']}: {len(chapter['exercises'])} ejercicios")

if __name__ == "__main__":
    main()
