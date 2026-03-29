"""Ejemplo de implementación del patrón Singleton utilizando metaclases.

Este método de implementación emplea una metaclase para interceptar el proceso de instanciación de los objetos.

En Python, cuando se crea una instancia de una clase, se invoca internamente el método __call__ de su metaclase.
Al sobrescribir este método, es posible controlar el valor de retorno de dicha instanciación.
De este modo, se modifica el comportamiento estándar para que, ante cada instanciación
siempre se retorne una única instancia para cada clase.
"""

from typing import Any, TypeVar, cast

# Variable de tipo para definir el tipo de instancia a crear con la metaclass SingletonMeta
T = TypeVar("T")


class SingletonMeta(type):
    """Metaclase para la implementación del patrón Singleton.

    Attributes:
        _instances (dict): Un diccionario de clase que actúa como caché para el
                           almacenamiento de las instancias creadas, en donde la llave es la
                           clase misma y el valor es la instancia única para dicha clase.
    """

    _instances: dict[type[Any], Any] = {}

    def __call__(cls: type[T], *args: Any, **kwargs: Any) -> T:
        """Método encargado de controlar la creación de una nueva instancia.

        Args:
            cls: La clase que se está instanciando.
            *args: Argumentos posicionales para la inicialización.
            **kwargs: Argumentos de palabra clave para la inicialización.

        Returns:
            La instancia única de la clase, ya sea recién creada o recuperada desde caché.
        """
        # Si la clase no tiene una instancia creada, se crea una nueva instancia
        # y se almacena en el diccionario _instances
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        # Se retorna la instancia única de la clase instanciada
        return cast(T, cls._instances[cls])
