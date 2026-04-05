"""Ejemplo de implementación del patrón Factory Method utilizando el enfoque clásico.

Este método de implementación define una clase abstracta con un método abstracto
que debe ser implementado por subclases concretas. Cada subclase concreta decide qué tipo de producto crear.
"""

from abc import ABC, abstractmethod
from typing import Any


class Product(ABC):
    """Clase base abstracta que define la interfaz común que deben implementar todos los productos."""

    @abstractmethod
    def some_operation(self) -> Any:
        """Ejemplo de método abstracto que debe implementar cada producto."""
        pass


class Creator(ABC):
    """Clase abstracta que define la interfaz para crear productos."""

    @abstractmethod
    def create(self) -> Product:
        """Método abstracto para crear un producto.

        Cada subclase concreta implementa este método para crear un tipo específico de producto.

        Returns:
            Una instancia de `Product`.
        """
        pass

    def some_business_logic(self) -> str:
        """Ejemplo de lógica de negocio que hace uso de un producto creado.

        Este método demuestra cómo el `Creator` usa el producto sin conocer su tipo concreto.

        Returns:
            Una descripción de la operación realizada.
        """
        # Llamamos al método create para obtener un producto
        product = self.create()

        # Usamos el producto a través de su interfaz abstracta
        return f"Creator: Some business logic with product: {product.some_operation()}"


class ConcreteProductA(Product):
    """Implementación concreta del producto A."""

    def some_operation(self) -> str:
        """Realiza una operación específica del producto A.

        Returns:
            Una descripción de la operación del producto A.
        """
        return f"Some operation of product: {self.__class__.__name__}"


class ConcreteProductB(Product):
    """Implementación concreta del producto B."""

    def some_operation(self) -> str:
        """Realiza una operación específica del producto B.

        Returns:
            Una descripción de la operación del producto B.
        """
        return f"Some operation of product: {self.__class__.__name__}"


class ConcreteCreatorA(Creator):
    """Creador concreto que crea productos de tipo A."""

    def create(self) -> Product:
        """Crea y retorna un producto de tipo A.

        Returns:
            Una instancia de `ConcreteProductA`.
        """
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """Creador concreto que crea productos de tipo B."""

    def factory_method(self) -> Product:
        """Crea y retorna un producto de tipo B.

        Returns:
            Una instancia de `ConcreteProductB`.
        """
        return ConcreteProductB()
