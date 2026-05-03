"""Ejemplo de implementación del patrón Prototype utilizando Dunder Methods.

Este método de implementación se basa en la sobrecarga de los métodos especiales __copy__ y __deepcopy__,
los cuales son utilizados por la biblioteca estándar copy para realizar copias superficiales y profundas de objetos,
respectivamente.
"""

import copy
from typing import Any


class SomeObject:
    """Clase que implementa el patrón Prototype usando Dunder Methods."""

    def __init__(
        self,
        some_immutable: str,
        some_mutable: list[Any],
        some_instance_only: dict[str, Any] | None = None,
    ) -> None:
        """Inicializa una instancia clonable de la clase.

        Args:
            some_immutable: Ejemplo de atributo inmutable.
            some_mutable: Ejemplo de atributo mutable.
            some_instance_only: Ejemplo de atributo que se desea que sea único para cada instancia.
        """
        self.some_immutable = some_immutable
        self.some_mutable = some_mutable
        self.some_instance_only = some_instance_only if some_instance_only is not None else {}

    def __copy__(self) -> "SomeObject":
        """Crea una una copia superficial de la instancia (shallow copy).

        Returns:
            Nueva instancia con referencias copiadas.
        """
        # Crea una nueva instancia con copias superficiales
        return self.__class__(
            # str es inmutable, no necesita copia
            self.some_immutable,
            # list es mutable, se copia superficialmente
            copy.copy(self.some_mutable),
            # atributo que se desea que sea único para cada instancia, se inicializa como un nuevo diccionario
            {},
        )

    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> "SomeObject":
        """Crea una copia profunda de la instancia (deep copy).

        Args:
            memo: Diccionario interno usado por copy.deepcopy() para evitar referencias circulares.

        Returns:
            Nueva instancia completamente independiente con copias profundas de todos sus atributos.
        """
        if memo is None:
            memo = {}

        # Crea una nueva instancia con copias profundas
        return self.__class__(
            # str es inmutable, no necesita copia
            self.some_immutable,
            # list es mutable, se copia profundamente
            copy.deepcopy(self.some_mutable, memo),
            # A efecto practico de este ejemplo, en este caso,
            # a diferencia de __copy__ en donde no se quiere que persista la referencia a some_instance_only,
            # en __deepcopy__ se desea que se mantenga la independencia total,
            # por lo que se hace una copia profunda de este atributo también
            copy.deepcopy(self.some_instance_only, memo),
        )

    def __repr__(self) -> str:
        """Representación legible del objeto.

        Note: Metodo solo para fines de demostración, no es parte del patrón Prototype.
        """
        return (
            f"{self.__class__.__name__}("
            f"some_immutable={self.some_immutable!r}, "
            f"some_mutable={self.some_mutable}, "
            f"some_instance_only={self.some_instance_only})"
        )
