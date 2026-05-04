"""Implementación del patrón de diseño Builder utilizando el enfoque de GoF (Gang of Four).

El enfoque clásico utiliza una interfaz abstracta para definir los pasos de fabricación
y un Director para gestionar la lógica de montaje.

Componentes clave:
-----------------
*   Builder (ABC): Interfaz que declara los métodos de construcción para
    las distintas partes del objeto producto.
*   Director: Clase encargada de orquestar el proceso de construcción en un
    orden específico, desacoplando al cliente de la lógica de montaje.
*   ConcreteBuilder: Implementaciones específicas que ejecutan los pasos de
    fabricación y mantienen el estado del producto hasta su entrega.
*   Product: El objeto complejo resultante, cuya estructura interna puede
    variar significativamente entre distintos constructores.

Flujo de trabajo:
----------------
El Director recibe una instancia de un ConcreteBuilder y ejecuta sus métodos
de construcción. Finalmente, el cliente recupera el producto terminado
directamente desde el constructor concreto.
"""

from abc import ABC, abstractmethod


class Product:
    """Clase que representa el producto final a ser construido.

    Esta clase encapsula todas las partes que conforman el producto.
    """

    def __init__(self) -> None:
        """Inicializa una instancia del producto con partes no definidas."""
        self.part_a: str | None = None
        self.part_b: int | None = None
        self.part_c: bool | None = None


class Builder(ABC):
    """Clase base abstracta que define la interfaz para construir productos.

    Esta clase abstracta establece los métodos que deben implementar todas
    las subclases concretas para construir diferentes variantes del producto.
    """

    @property
    @abstractmethod
    def product(self) -> Product:
        """Propiedad abstracta que retorna el producto en construcción."""
        pass

    @abstractmethod
    def build_part_a(self) -> None:
        """Método abstracto para construir la parte A del producto."""
        pass

    @abstractmethod
    def build_part_b(self) -> None:
        """Método abstracto para construir la parte B del producto."""
        pass

    @abstractmethod
    def build_part_c(self) -> None:
        """Método abstracto para construir la parte C del producto."""
        pass


class Director:
    """Clase encargada de orquestar el proceso de construcción.

    El Director conoce los pasos necesarios para construir un producto,
    pero delega la responsabilidad de cada paso al builder concreto.

    Attributes:
        _builder: El builder concreto que se utilizará para construir el producto.
    """

    def __init__(self, builder: Builder) -> None:
        """Inicializa una instancia del Director con un builder específico.

        Args:
            builder: Una instancia de una clase que implementa la interfaz Builder.
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
            builder: Nueva instancia de Builder a utilizar.
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

    Esta clase demuestra cómo una implementación específica del Builder
    define sus propios valores para las partes del producto.
    """

    def __init__(self) -> None:
        """Inicializa una instancia de ConcreteBuilderA con un producto vacío."""
        # Se llama a reset para inicializar el producto,
        # lo cual es equivalente a `self._product = Product()`
        self.reset()

    @property
    def product(self) -> Product:
        """Obtiene el producto en construcción."""
        product = self._product
        self.reset()

        return product

    def reset(self) -> None:
        """Resetea el producto en construcción a un estado vacío.

        Este método no es parte de la implementación original, sin embargo,
        es una buena práctica para evitar que objetos posteriores
        creados por el mismo builder puedan heredar el estado anterior.
        """
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
    distintas del mismo producto utilizando diferentes valores.
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
