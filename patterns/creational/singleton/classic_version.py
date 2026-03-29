"""Ejemplo de implementación del patrón Singleton utilizando el método clasico.

Este método de implementación consiste en sobrescribir el método especial __new__,
el cual es el encargado de crear la instancia de clase.

Al llamar al constructor de la clase, __new__ verifica si ya existe una instancia almacenada en un atributo de clase;
si existe, la retorna, de lo contrario, delega la creación a la superclase y la almacena para futuras llamadas.
"""

from typing import Any, TypeVar

# Variable de tipo vinculada a la clase Singleton para asegurar la consistencia del tipo de retorno
T = TypeVar("T", bound="Singleton")


class Singleton:
    """Clase base para la implementación del patrón Singleton.

    Attributes:
        _instance: Atributo de clase que actúa como contenedor de la instancia única.
    """

    _instance: Any = None

    def __new__(cls: type[T], *args: Any, **kwargs: Any) -> T:
        """Método encargado de controlar la creación de una nueva instancia.

        Args:
            cls: La clase que se está intentando instanciar.
            *args: Argumentos posicionales para la inicialización.
            **kwargs: Argumentos de palabra clave para la inicialización.

        Returns:
            La instancia única de la clase, ya sea recién creada o recuperada desde caché.
        """
        # Si el atributo _instance es None, significa que no existe una instancia previamente creada,
        # por lo que se crea una y se guardarla en _instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        # Se retorna la instancia única de la clase instanciada
        return cls._instance
