"""Ejemplo de implementación del patrón Prototype utilizando Protocols.

Este método de implementación utiliza tipado estructural (Protocol)
para definir la estructura que debe tener un prototipo.

Cada clase que implementa el patrón Prototype debe cumplir con la interfaz definida por el Protocol,
lo que permite una mayor flexibilidad y desacoplamiento entre las clases.
"""

import copy
from typing import Any, Protocol, TypeVar, runtime_checkable

# Variable de tipo vinculada a la clase Prototype para asegurar la consistencia del tipo de retorno
T = TypeVar("T", bound="Prototype")


@runtime_checkable  # Habilita la verificación en tiempo de ejecución para este Protocol
class Prototype(Protocol):
    """Clase que define la interfaz común que deben implementar todos los objetos clonables."""

    def clone(self: T) -> T:
        """Metodo que deben implementar los prototipos para hacer una copia superficial (shallow copy)."""
        ...

    def deepclone(self: T, memo: dict[int, Any] | None = None) -> T:
        """Metodo que deben implementar los prototipos para hacer una copia profunda (deep copy)."""
        ...


class SomeObject:
    """Clase que implementa el patrón Prototype usando Protocols."""

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

    def clone(self) -> "SomeObject":
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

    def deepclone(self, memo: dict[int, Any] | None = None) -> "SomeObject":
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
