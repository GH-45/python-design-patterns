"""Ejemplo de iomplementación del patrón Singleton utilizando decoradores.

Este método de implementación emplea un decorador para envolver la definición de la clase
haciendo que actué como un Singleton.

En Python, un decorador es una función que recibe una clase o función y devuelve una versión modificada de la misma.
Al aplicar un decorador para implementar un Singleton, cuando se intente instanciar la clase decorada,
el decorador intercepta la llamada, modificando el comportamiento estándar para que, ante cada instanciación
siempre se retorne una única instancia para cada clase.
"""

from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

# Variable de tipo para definir el tipo de instancia a crear mediante el decorador singleton
T = TypeVar("T")


def singleton[T](cls: type[T]) -> Callable[..., T]:
    """Decorador de clase para la implementación del patrón Singleton.

    Args:
        cls: La clase que se está instanciando.

    Returns:
        Una función envolvente (wrapper) que gestiona el acceso a la instancia única.
    """
    # Diccionario que actúa como caché local para almacenar la instancia de la clase decorada
    instances: dict[type[T], T] = {}

    @wraps(cls)
    def get_instance(*args: Any, **kwargs: Any) -> T:
        """Función decoradora que controla la creación de una nueva instancia.

        Args:
            *args: Argumentos posicionales para la inicialización.
            **kwargs: Argumentos de palabra clave para la inicialización.

        Returns:
            La instancia única de la clase, ya sea recién creada o recuperada desde caché.
        """
        # Si la clase no tiene una instancia creada, se crea una nueva instancia
        # y se almacena en el diccionario instances
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        # Se retorna la instancia única de la clase instanciada
        return instances[cls]

    return get_instance
