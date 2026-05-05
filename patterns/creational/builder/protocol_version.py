"""Implementación del patrón de diseño Builder utilizando Python Protocols (PEP 544).

Este enfoque sustituye la herencia rígida de las Clases Abstractas (ABC) por
un tipado estructural. Permitiendo definir el contrato del constructor de forma
desacoplada, facilitando el polimorfismo sin jerarquías de clases explícitas.

Componentes clave:
-----------------
*   Builder (Protocol): Definición estructural que especifica los métodos y
    propiedades requeridos para la fabricación del producto. Cualquier clase
    que implemente estos métodos es considerada un Builder válido.
*   Director: Orquestador que recibe una instancia que satisfaga el Protocolo Builder.
    Se encarga de orquestar el proceso de construcción en un orden específico,
    desacoplando al cliente de la lógica de montaje.
*   ConcreteBuilder: Clases independientes que cumplen con la estructura del
    Protocol sin necesidad de heredar de una clase base común.
    Cada una especifica su propia lógica de construcción y
    mantiene el estado del producto hasta su entrega.
*   Product: El objeto complejo resultante, cuya representación interna es
    independiente de la interfaz del constructor.

Flujo de trabajo:
----------------
El Director interactúa con cualquier objeto que coincida con el Protocolo especificado.
El chequeo de tipos garantiza que el ConcreteBuilder posee todos los métodos necesarios.
"""

from typing import Protocol, runtime_checkable


class Product:
    """Clase que representa el producto final a ser construido.

    Esta clase encapsula todas las partes que conforman el producto.
    """

    def __init__(self) -> None:
        """Inicializa una instancia del producto con partes no definidas."""
        self.part_a: str | None = None
        self.part_b: int | None = None
        self.part_c: bool | None = None


@runtime_checkable
class Builder(Protocol):
    """Protocol que define la interfaz común que deben implementar todos los builders."""

    @property
    def product(self) -> Product:
        """Obtiene el producto en construcción."""
        ...

    def build_part_a(self) -> None:
        """Método para construir la parte A del producto."""
        ...

    def build_part_b(self) -> None:
        """Método para construir la parte B del producto."""
        ...

    def build_part_c(self) -> None:
        """Método para construir la parte C del producto."""
        ...


class Director:
    """Clase encargada de orquestar el proceso de construcción.

    El Director conoce los pasos necesarios para construir un producto,
    pero delega la responsabilidad de cada paso al builder concreto.

    Esta implementación es agnóstica respecto a cómo el builder implementa
    la interfaz gracias al uso de Protocols.

    Attributes:
        _builder: El builder concreto que se utilizará para construir el producto.
    """

    def __init__(self, builder: Builder) -> None:
        """Inicializa el Director con un builder que cumple con el Protocol.

        Args:
            builder: Una instancia que implementa la interfaz Builder (Protocol).
        """
        self._builder = builder

    @property
    def builder(self) -> Builder:
        """Obtiene el builder actual."""
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """Cambia el builder utilizado por el Director.

        Args:
            builder: Nueva instancia que implemente la interfaz Builder.
        """
        self._builder = builder

    def build(self) -> None:
        """Orquesta el proceso completo de construcción.

        Este método define el orden y los pasos necesarios para construir
        un producto completo delegando cada paso al builder.
        """
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()

    def get_product(self) -> Product:
        """Obtiene el producto construido.

        Returns:
            El producto final construido por el builder.
        """
        return self._builder.product


class ConcreteBuilderA(Builder):
    """Implementación concreta del Builder que construye variante A del producto.

    Esta clase no hereda de ninguna clase abstracta, simplemente implementa
    la interfaz definida por el Protocol Builder.
    """

    def __init__(self) -> None:
        """Inicializa una instancia de ConcreteBuilderA con un producto vacío."""
        self.reset()

    @property
    def product(self) -> Product:
        """Obtiene el producto en construcción."""
        product = self._product
        self.reset()

        return product

    def reset(self) -> None:
        """Resetea el producto en construcción a un estado vacío."""
        self._product = Product()

    def build_part_a(self) -> None:
        """Construye la parte A del producto."""
        self._product.part_a = "foo"

    def build_part_b(self) -> None:
        """Construye la parte B del producto."""
        self._product.part_b = 0

    def build_part_c(self) -> None:
        """Construye la parte C del producto."""
        self._product.part_c = False


class ConcreteBuilderB(Builder):
    """Implementación concreta del Builder que construye variante B del producto.

    Esta clase demuestra cómo diferentes builders pueden construir variantes
    distintas del mismo producto sin necesidad de herencia explícita.
    """

    def __init__(self) -> None:
        """Inicializa una instancia de ConcreteBuilderB con un producto vacío."""
        self.reset()

    @property
    def product(self) -> Product:
        """Obtiene el producto en construcción."""
        product = self._product
        self.reset()

        return product

    def reset(self) -> None:
        """Resetea el producto en construcción a un estado vacío."""
        self._product = Product()

    def build_part_a(self) -> None:
        """Construye la parte A del producto con valores alternativos."""
        self._product.part_a = "bar"

    def build_part_b(self) -> None:
        """Construye la parte B del producto con valores alternativos."""
        self._product.part_b = 1

    def build_part_c(self) -> None:
        """Construye la parte C del producto con valores alternativos."""
        self._product.part_c = True
