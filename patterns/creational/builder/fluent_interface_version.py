"""Implementación del patrón de diseño Builder mediante Interfaz Fluida (Fluent Interface).

Esta variante se caracteriza por el encadenamiento de métodos (method chaining),
en donde cada paso de construcción devuelve la propia instancia del constructor.
Esto permite una sintaxis declarativa que elimina, generalmente,
la necesidad de un Director externo, centralizando la lógica en el Builder.

Componentes clave:
-----------------
*   ConcreteBuilder: Implementa los pasos de fabricación, asegurando que cada
    método retorne la propia instancia para habilitar el encadenamiento.
*   Product: El objeto complejo resultante.

Flujo de trabajo:
----------------
El cliente interactúa directamente con el constructor en una sola sentencia continua,
por ejemplo: `builder.add_part_a().add_part_b().build()`.
"""

from dataclasses import dataclass
from typing import Self


# Note: En este ejemplo, se usa dataclass para mostrar otros escenarios,
# pero se puede reemplazar por una clase normal sin problemas
# u otro tipo de estructura de datos, según lo que se requiera.
@dataclass
class Product:
    """Clase que representa el producto final a ser construido.

    Esta clase encapsula todas las partes que conforman el producto.
    """

    part_a: str
    part_b: int
    part_c: bool


class ConcreteBuilder:
    """Clase concreta que implementa la construcción del producto utilizando una interfaz fluida.

    Esta clase proporciona métodos encadenados para configurar cada parte del producto,
    permitiendo una construcción más legible y concisa.
    """

    def __init__(self) -> None:
        """Inicializa una instancia de ConcreteBuilder con un producto vacío."""
        # Según la necesidad, se pueden inicializar con valores por defecto, dejar como None,
        # inicializar con un producto vacío, entre otros enfoques.
        self._part_a = "foo"
        self._part_b = 0
        self._part_c = False

    def build_part_a(self, value: str) -> Self:
        """Construye la parte A del producto.

        Args:
            value: El valor a asignar a la parte A.

        Returns:
            La instancia actual de ConcreteBuilder para permitir el encadenamiento.
        """
        self._part_a = value
        return self

    def build_part_b(self, value: int) -> Self:
        """Construye la parte B del producto.

        Args:
            value: El valor a asignar a la parte B.

        Returns:
            La instancia actual de ConcreteBuilder para permitir el encadenamiento.
        """
        self._part_b = value
        return self

    def build_part_c(self, value: bool) -> Self:
        """Construye la parte C del producto.

        Args:
            value: El valor a asignar a la parte C.

        Returns:
            La instancia actual de ConcreteBuilder para permitir el encadenamiento.
        """
        self._part_c = value
        return self

    def build(self) -> Product:
        """Construye el producto final a partir de las partes configuradas.

        Returns:
            Una instancia de Product con las partes configuradas.
        """
        return Product(part_a=self._part_a, part_b=self._part_b, part_c=self._part_c)
