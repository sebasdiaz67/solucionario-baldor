"""
Base de datos de ejercicios del libro Álgebra de Baldor
Contiene ejercicios reales y típicos del libro con sus soluciones paso a paso
"""

BALDOR_EXERCISES = {
    "operaciones-basicas": [
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
            "problem": "(4x² - 3x + 1) - (2x² + x - 2)",
            "steps": [
                "Distribuir el signo negativo",
                "4x² - 3x + 1 - 2x² - x + 2",
                "Agrupar términos semejantes",
                "(4x² - 2x²) + (-3x - x) + (1 + 2)",
                "2x² - 4x + 3"
            ],
            "solution": "2x² - 4x + 3"
        },
        {
            "id": "O003",
            "problem": "(2x + 3)(x - 1)",
            "steps": [
                "Aplicar propiedad distributiva",
                "2x·x + 2x·(-1) + 3·x + 3·(-1)",
                "2x² - 2x + 3x - 3",
                "2x² + x - 3"
            ],
            "solution": "2x² + x - 3"
        },
        {
            "id": "O004",
            "problem": "(x² + 2x + 1) + (3x² - x + 4)",
            "steps": [
                "Agrupar términos semejantes",
                "x² + 3x² + 2x - x + 1 + 4",
                "4x² + x + 5"
            ],
            "solution": "4x² + x + 5"
        },
        {
            "id": "O005",
            "problem": "(2x - 5)(3x + 2)",
            "steps": [
                "Aplicar propiedad distributiva",
                "2x·3x + 2x·2 - 5·3x - 5·2",
                "6x² + 4x - 15x - 10",
                "6x² - 11x - 10"
            ],
            "solution": "6x² - 11x - 10"
        },
        {
            "id": "O006",
            "problem": "(5x³ + 2x² - x + 3) + (2x³ - 3x² + 4x - 1)",
            "steps": [
                "Agrupar términos semejantes",
                "5x³ + 2x³ + 2x² - 3x² - x + 4x + 3 - 1",
                "7x³ - x² + 3x + 2"
            ],
            "solution": "7x³ - x² + 3x + 2"
        },
        {
            "id": "O007",
            "problem": "(3x² + 2x - 1) - (x² - 4x + 5)",
            "steps": [
                "Distribuir el signo negativo",
                "3x² + 2x - 1 - x² + 4x - 5",
                "Agrupar términos semejantes",
                "(3x² - x²) + (2x + 4x) + (-1 - 5)",
                "2x² + 6x - 6"
            ],
            "solution": "2x² + 6x - 6"
        },
        {
            "id": "O008",
            "problem": "(4x + 1)(2x - 3)",
            "steps": [
                "Aplicar propiedad distributiva",
                "4x·2x + 4x·(-3) + 1·2x + 1·(-3)",
                "8x² - 12x + 2x - 3",
                "8x² - 10x - 3"
            ],
            "solution": "8x² - 10x - 3"
        },
        {
            "id": "O009",
            "problem": "(x³ + 3x² - 2x + 1) + (2x³ - x² + 4x - 3)",
            "steps": [
                "Agrupar términos semejantes",
                "x³ + 2x³ + 3x² - x² - 2x + 4x + 1 - 3",
                "3x³ + 2x² + 2x - 2"
            ],
            "solution": "3x³ + 2x² + 2x - 2"
        },
        {
            "id": "O010",
            "problem": "(3x - 2)(4x + 5)",
            "steps": [
                "Aplicar propiedad distributiva",
                "3x·4x + 3x·5 - 2·4x - 2·5",
                "12x² + 15x - 8x - 10",
                "12x² + 7x - 10"
            ],
            "solution": "12x² + 7x - 10"
        }
    ],
    
    "productos-notables": [
        {
            "id": "P001",
            "problem": "(a + b)²",
            "steps": [
                "Aplicar fórmula: (a + b)² = a² + 2ab + b²",
                "Identificar a = a, b = b",
                "a² + 2ab + b²"
            ],
            "solution": "a² + 2ab + b²"
        },
        {
            "id": "P002",
            "problem": "(x + 3)²",
            "steps": [
                "Aplicar fórmula: (a + b)² = a² + 2ab + b²",
                "Identificar a = x, b = 3",
                "x² + 2·x·3 + 3²",
                "x² + 6x + 9"
            ],
            "solution": "x² + 6x + 9"
        },
        {
            "id": "P003",
            "problem": "(2x - 5)²",
            "steps": [
                "Aplicar fórmula: (a - b)² = a² - 2ab + b²",
                "Identificar a = 2x, b = 5",
                "(2x)² - 2·2x·5 + 5²",
                "4x² - 20x + 25"
            ],
            "solution": "4x² - 20x + 25"
        },
        {
            "id": "P004",
            "problem": "(x + 2)(x - 2)",
            "steps": [
                "Aplicar diferencia de cuadrados: (a + b)(a - b) = a² - b²",
                "Identificar a = x, b = 2",
                "x² - 2²",
                "x² - 4"
            ],
            "solution": "x² - 4"
        },
        {
            "id": "P005",
            "problem": "(3x + 4)(3x - 4)",
            "steps": [
                "Aplicar diferencia de cuadrados: (a + b)(a - b) = a² - b²",
                "Identificar a = 3x, b = 4",
                "(3x)² - 4²",
                "9x² - 16"
            ],
            "solution": "9x² - 16"
        },
        {
            "id": "P006",
            "problem": "(a + b)³",
            "steps": [
                "Aplicar fórmula: (a + b)³ = a³ + 3a²b + 3ab² + b³",
                "Identificar a = a, b = b",
                "a³ + 3a²b + 3ab² + b³"
            ],
            "solution": "a³ + 3a²b + 3ab² + b³"
        },
        {
            "id": "P007",
            "problem": "(x + 2)³",
            "steps": [
                "Aplicar fórmula: (a + b)³ = a³ + 3a²b + 3ab² + b³",
                "Identificar a = x, b = 2",
                "x³ + 3x²·2 + 3x·2² + 2³",
                "x³ + 6x² + 12x + 8"
            ],
            "solution": "x³ + 6x² + 12x + 8"
        },
        {
            "id": "P008",
            "problem": "(2x - 1)³",
            "steps": [
                "Aplicar fórmula: (a - b)³ = a³ - 3a²b + 3ab² - b³",
                "Identificar a = 2x, b = 1",
                "(2x)³ - 3(2x)²·1 + 3·2x·1² - 1³",
                "8x³ - 12x² + 6x - 1"
            ],
            "solution": "8x³ - 12x² + 6x - 1"
        },
        {
            "id": "P009",
            "problem": "(x + y + z)²",
            "steps": [
                "Aplicar fórmula del trinomio cuadrado",
                "x² + y² + z² + 2xy + 2xz + 2yz"
            ],
            "solution": "x² + y² + z² + 2xy + 2xz + 2yz"
        },
        {
            "id": "P010",
            "problem": "(x + 3y - 2z)²",
            "steps": [
                "Aplicar fórmula del trinomio cuadrado",
                "x² + 9y² + 4z² + 6xy - 4xz - 12yz"
            ],
            "solution": "x² + 9y² + 4z² + 6xy - 4xz - 12yz"
        }
    ],
    
    "factorizacion": [
        {
            "id": "F001",
            "problem": "x² + 6x + 9",
            "steps": [
                "Reconocer trinomio cuadrado perfecto",
                "Verificar si es (a + b)² = a² + 2ab + b²",
                "a² = x² → a = x",
                "b² = 9 → b = 3",
                "2ab = 2·x·3 = 6x ✓",
                "Por lo tanto: (x + 3)²"
            ],
            "solution": "(x + 3)²"
        },
        {
            "id": "F002",
            "problem": "x² - 25",
            "steps": [
                "Reconocer diferencia de cuadrados",
                "Verificar si es a² - b² = (a + b)(a - b)",
                "a² = x² → a = x",
                "b² = 25 → b = 5",
                "Por lo tanto: (x + 5)(x - 5)"
            ],
            "solution": "(x + 5)(x - 5)"
        },
        {
            "id": "F003",
            "problem": "2x² + 8x",
            "steps": [
                "Extraer factor común",
                "Identificar el máximo común divisor: 2x",
                "2x² ÷ 2x = x",
                "8x ÷ 2x = 4",
                "Por lo tanto: 2x(x + 4)"
            ],
            "solution": "2x(x + 4)"
        },
        {
            "id": "F004",
            "problem": "x² + 5x + 6",
            "steps": [
                "Factorizar trinomio de la forma x² + bx + c",
                "Buscar dos números que multipliquen c = 6 y sumen b = 5",
                "Los números son 2 y 3",
                "Verificar: 2 × 3 = 6 y 2 + 3 = 5 ✓",
                "Por lo tanto: (x + 2)(x + 3)"
            ],
            "solution": "(x + 2)(x + 3)"
        },
        {
            "id": "F005",
            "problem": "x² - 7x + 12",
            "steps": [
                "Factorizar trinomio de la forma x² + bx + c",
                "Buscar dos números que multipliquen c = 12 y sumen b = -7",
                "Los números son -3 y -4",
                "Verificar: (-3) × (-4) = 12 y (-3) + (-4) = -7 ✓",
                "Por lo tanto: (x - 3)(x - 4)"
            ],
            "solution": "(x - 3)(x - 4)"
        },
        {
            "id": "F006",
            "problem": "3x² - 12",
            "steps": [
                "Extraer factor común: 3",
                "3(x² - 4)",
                "Reconocer diferencia de cuadrados en x² - 4",
                "x² - 2² = (x + 2)(x - 2)",
                "Por lo tanto: 3(x + 2)(x - 2)"
            ],
            "solution": "3(x + 2)(x - 2)"
        },
        {
            "id": "F007",
            "problem": "x³ + 8",
            "steps": [
                "Reconocer suma de cubos: a³ + b³ = (a + b)(a² - ab + b²)",
                "a³ = x³ → a = x",
                "b³ = 8 → b = 2",
                "Por lo tanto: (x + 2)(x² - 2x + 4)"
            ],
            "solution": "(x + 2)(x² - 2x + 4)"
        },
        {
            "id": "F008",
            "problem": "x³ - 27",
            "steps": [
                "Reconocer diferencia de cubos: a³ - b³ = (a - b)(a² + ab + b²)",
                "a³ = x³ → a = x",
                "b³ = 27 → b = 3",
                "Por lo tanto: (x - 3)(x² + 3x + 9)"
            ],
            "solution": "(x - 3)(x² + 3x + 9)"
        },
        {
            "id": "F009",
            "problem": "4x² - 9y²",
            "steps": [
                "Reconocer diferencia de cuadrados",
                "4x² = (2x)² → a = 2x",
                "9y² = (3y)² → b = 3y",
                "Por lo tanto: (2x + 3y)(2x - 3y)"
            ],
            "solution": "(2x + 3y)(2x - 3y)"
        },
        {
            "id": "F010",
            "problem": "x² + 8x + 16",
            "steps": [
                "Reconocer trinomio cuadrado perfecto",
                "Verificar si es (a + b)² = a² + 2ab + b²",
                "a² = x² → a = x",
                "b² = 16 → b = 4",
                "2ab = 2·x·4 = 8x ✓",
                "Por lo tanto: (x + 4)²"
            ],
            "solution": "(x + 4)²"
        }
    ],
    
    "fracciones-algebraicas": [
        {
            "id": "R001",
            "problem": "\\frac{x² - 4}{x + 2}",
            "steps": [
                "Simplificar la fracción",
                "Factorizar el numerador: x² - 4 = (x + 2)(x - 2)",
                "\\frac{(x + 2)(x - 2)}{x + 2}",
                "Cancelar factor común (x + 2)",
                "x - 2"
            ],
            "solution": "x - 2"
        },
        {
            "id": "R002",
            "problem": "\\frac{2x² + 4x}{2x}",
            "steps": [
                "Simplificar la fracción",
                "Extraer factor común del numerador: 2x(x + 2)",
                "\\frac{2x(x + 2)}{2x}",
                "Cancelar factor común 2x",
                "x + 2"
            ],
            "solution": "x + 2"
        },
        {
            "id": "R003",
            "problem": "\\frac{x² - 9}{x² - 6x + 9}",
            "steps": [
                "Factorizar numerador y denominador",
                "Numerador: x² - 9 = (x + 3)(x - 3)",
                "Denominador: x² - 6x + 9 = (x - 3)²",
                "\\frac{(x + 3)(x - 3)}{(x - 3)²}",
                "Cancelar factor común (x - 3)",
                "\\frac{x + 3}{x - 3}"
            ],
            "solution": "\\frac{x + 3}{x - 3}"
        },
        {
            "id": "R004",
            "problem": "\\frac{3x + 6}{x² + 4x + 4}",
            "steps": [
                "Factorizar numerador y denominador",
                "Numerador: 3(x + 2)",
                "Denominador: (x + 2)²",
                "\\frac{3(x + 2)}{(x + 2)²}",
                "Cancelar factor común (x + 2)",
                "\\frac{3}{x + 2}"
            ],
            "solution": "\\frac{3}{x + 2}"
        },
        {
            "id": "R005",
            "problem": "\\frac{x² - 16}{4x + 16}",
            "steps": [
                "Factorizar numerador y denominador",
                "Numerador: (x + 4)(x - 4)",
                "Denominador: 4(x + 4)",
                "\\frac{(x + 4)(x - 4)}{4(x + 4)}",
                "Cancelar factor común (x + 4)",
                "\\frac{x - 4}{4}"
            ],
            "solution": "\\frac{x - 4}{4}"
        },
        {
            "id": "R006",
            "problem": "\\frac{2x² - 8}{x² - 4}",
            "steps": [
                "Factorizar numerador y denominador",
                "Numerador: 2(x² - 4) = 2(x + 2)(x - 2)",
                "Denominador: (x + 2)(x - 2)",
                "\\frac{2(x + 2)(x - 2)}{(x + 2)(x - 2)}",
                "Cancelar factores comunes",
                "2"
            ],
            "solution": "2"
        },
        {
            "id": "R007",
            "problem": "\\frac{x³ + 8}{x + 2}",
            "steps": [
                "Factorizar el numerador (suma de cubos)",
                "x³ + 8 = (x + 2)(x² - 2x + 4)",
                "\\frac{(x + 2)(x² - 2x + 4)}{x + 2}",
                "Cancelar factor común (x + 2)",
                "x² - 2x + 4"
            ],
            "solution": "x² - 2x + 4"
        },
        {
            "id": "R008",
            "problem": "\\frac{x² - 25}{x² + 10x + 25}",
            "steps": [
                "Factorizar numerador y denominador",
                "Numerador: (x + 5)(x - 5)",
                "Denominador: (x + 5)²",
                "\\frac{(x + 5)(x - 5)}{(x + 5)²}",
                "Cancelar factor común (x + 5)",
                "\\frac{x - 5}{x + 5}"
            ],
            "solution": "\\frac{x - 5}{x + 5}"
        },
        {
            "id": "R009",
            "problem": "\\frac{4x² - 9}{2x - 3}",
            "steps": [
                "Factorizar el numerador",
                "4x² - 9 = (2x + 3)(2x - 3)",
                "\\frac{(2x + 3)(2x - 3)}{2x - 3}",
                "Cancelar factor común (2x - 3)",
                "2x + 3"
            ],
            "solution": "2x + 3"
        },
        {
            "id": "R010",
            "problem": "\\frac{x² + 6x + 9}{x + 3}",
            "steps": [
                "Factorizar el numerador",
                "x² + 6x + 9 = (x + 3)²",
                "\\frac{(x + 3)²}{x + 3}",
                "Cancelar factor común (x + 3)",
                "x + 3"
            ],
            "solution": "x + 3"
        }
    ],
    
    "ecuaciones-lineales": [
        {
            "id": "L001",
            "problem": "2x + 3 = 7",
            "steps": [
                "Despejar x",
                "2x = 7 - 3",
                "2x = 4",
                "x = 4/2",
                "x = 2"
            ],
            "solution": "x = 2"
        },
        {
            "id": "L002",
            "problem": "3x - 5 = 10",
            "steps": [
                "Despejar x",
                "3x = 10 + 5",
                "3x = 15",
                "x = 15/3",
                "x = 5"
            ],
            "solution": "x = 5"
        },
        {
            "id": "L003",
            "problem": "4x + 7 = 2x + 15",
            "steps": [
                "Agrupar términos con x",
                "4x - 2x = 15 - 7",
                "2x = 8",
                "x = 8/2",
                "x = 4"
            ],
            "solution": "x = 4"
        },
        {
            "id": "L004",
            "problem": "5x - 3 = 2x + 9",
            "steps": [
                "Agrupar términos con x",
                "5x - 2x = 9 + 3",
                "3x = 12",
                "x = 12/3",
                "x = 4"
            ],
            "solution": "x = 4"
        },
        {
            "id": "L005",
            "problem": "2(x + 3) = 10",
            "steps": [
                "Aplicar propiedad distributiva",
                "2x + 6 = 10",
                "Despejar x",
                "2x = 10 - 6",
                "2x = 4",
                "x = 4/2",
                "x = 2"
            ],
            "solution": "x = 2"
        },
        {
            "id": "L006",
            "problem": "3x - 7 = 5x + 1",
            "steps": [
                "Agrupar términos con x",
                "3x - 5x = 1 + 7",
                "-2x = 8",
                "x = 8/(-2)",
                "x = -4"
            ],
            "solution": "x = -4"
        },
        {
            "id": "L007",
            "problem": "x/2 + 3 = 7",
            "steps": [
                "Despejar x",
                "x/2 = 7 - 3",
                "x/2 = 4",
                "x = 4 × 2",
                "x = 8"
            ],
            "solution": "x = 8"
        },
        {
            "id": "L008",
            "problem": "2x/3 + 1 = 5",
            "steps": [
                "Despejar x",
                "2x/3 = 5 - 1",
                "2x/3 = 4",
                "2x = 4 × 3",
                "2x = 12",
                "x = 12/2",
                "x = 6"
            ],
            "solution": "x = 6"
        },
        {
            "id": "L009",
            "problem": "4(x - 2) = 3x + 2",
            "steps": [
                "Aplicar propiedad distributiva",
                "4x - 8 = 3x + 2",
                "Agrupar términos con x",
                "4x - 3x = 2 + 8",
                "x = 10"
            ],
            "solution": "x = 10"
        },
        {
            "id": "L010",
            "problem": "3x + 5 = 2(x + 4)",
            "steps": [
                "Aplicar propiedad distributiva",
                "3x + 5 = 2x + 8",
                "Agrupar términos con x",
                "3x - 2x = 8 - 5",
                "x = 3"
            ],
            "solution": "x = 3"
        }
    ],
    
    "ecuaciones-cuadraticas": [
        {
            "id": "Q001",
            "problem": "x² + 5x + 6 = 0",
            "steps": [
                "Factorizar el trinomio",
                "Buscar dos números que multipliquen 6 y sumen 5",
                "Los números son 2 y 3",
                "(x + 2)(x + 3) = 0",
                "Aplicar propiedad del producto nulo",
                "x + 2 = 0 → x = -2",
                "x + 3 = 0 → x = -3"
            ],
            "solution": "x = -2, x = -3"
        },
        {
            "id": "Q002",
            "problem": "x² - 9 = 0",
            "steps": [
                "Factorizar como diferencia de cuadrados",
                "x² - 3² = 0",
                "(x + 3)(x - 3) = 0",
                "Aplicar propiedad del producto nulo",
                "x + 3 = 0 → x = -3",
                "x - 3 = 0 → x = 3"
            ],
            "solution": "x = -3, x = 3"
        },
        {
            "id": "Q003",
            "problem": "x² - 4x - 5 = 0",
            "steps": [
                "Factorizar el trinomio",
                "Buscar dos números que multipliquen -5 y sumen -4",
                "Los números son -5 y 1",
                "(x - 5)(x + 1) = 0",
                "Aplicar propiedad del producto nulo",
                "x - 5 = 0 → x = 5",
                "x + 1 = 0 → x = -1"
            ],
            "solution": "x = 5, x = -1"
        },
        {
            "id": "Q004",
            "problem": "2x² + 8x = 0",
            "steps": [
                "Extraer factor común",
                "2x(x + 4) = 0",
                "Aplicar propiedad del producto nulo",
                "2x = 0 → x = 0",
                "x + 4 = 0 → x = -4"
            ],
            "solution": "x = 0, x = -4"
        },
        {
            "id": "Q005",
            "problem": "x² + 6x + 9 = 0",
            "steps": [
                "Reconocer trinomio cuadrado perfecto",
                "(x + 3)² = 0",
                "x + 3 = 0",
                "x = -3"
            ],
            "solution": "x = -3"
        },
        {
            "id": "Q006",
            "problem": "x² - 8x + 16 = 0",
            "steps": [
                "Reconocer trinomio cuadrado perfecto",
                "(x - 4)² = 0",
                "x - 4 = 0",
                "x = 4"
            ],
            "solution": "x = 4"
        },
        {
            "id": "Q007",
            "problem": "x² + x - 12 = 0",
            "steps": [
                "Factorizar el trinomio",
                "Buscar dos números que multipliquen -12 y sumen 1",
                "Los números son 4 y -3",
                "(x + 4)(x - 3) = 0",
                "Aplicar propiedad del producto nulo",
                "x + 4 = 0 → x = -4",
                "x - 3 = 0 → x = 3"
            ],
            "solution": "x = -4, x = 3"
        },
        {
            "id": "Q008",
            "problem": "3x² - 12 = 0",
            "steps": [
                "Despejar x²",
                "3x² = 12",
                "x² = 12/3",
                "x² = 4",
                "x = ±√4",
                "x = ±2"
            ],
            "solution": "x = 2, x = -2"
        },
        {
            "id": "Q009",
            "problem": "x² - 7x + 10 = 0",
            "steps": [
                "Factorizar el trinomio",
                "Buscar dos números que multipliquen 10 y sumen -7",
                "Los números son -5 y -2",
                "(x - 5)(x - 2) = 0",
                "Aplicar propiedad del producto nulo",
                "x - 5 = 0 → x = 5",
                "x - 2 = 0 → x = 2"
            ],
            "solution": "x = 5, x = 2"
        },
        {
            "id": "Q010",
            "problem": "x² - 16 = 0",
            "steps": [
                "Factorizar como diferencia de cuadrados",
                "x² - 4² = 0",
                "(x + 4)(x - 4) = 0",
                "Aplicar propiedad del producto nulo",
                "x + 4 = 0 → x = -4",
                "x - 4 = 0 → x = 4"
            ],
            "solution": "x = -4, x = 4"
        }
    ]
}
