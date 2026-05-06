"""Implementación del patrón de diseño Prototype utilizando Python Protocols (PEP 544).

Este enfoque sustituye la herencia rígida de las Clases Abstractas (ABC) por
un tipado estructural. Permitiendo definir el contrato de clonación de forma
más flexible y desacoplada.

Componentes clave:
-----------------
*   Prototype (Protocol): Definición estructural que especifica los métodos de clonación.
    Cualquier clase que implemente estos métodos puede ser utilizada como prototipo.
*   ConcretePrototype: Clase independiente que implementa y gestiona las operaciones
    de clonación.

Flujo de trabajo:
----------------
El Cliente mantiene una referencia a un objeto Prototipo. Cuando necesita una nueva
instancia, llama al método de clonación del Prototipo. Este método devuelve una copia
exacta del estado actual del objeto, la cual puede ser modificada por el Cliente de
forma independiente sin alterar el original.
"""

import copy
from typing import Any, Protocol, Self, runtime_checkable


@runtime_checkable  # Habilita la verificación en tiempo de ejecución para este Protocol
class Prototype(Protocol):
    """Protocol que define la interfaz común para objetos clonables."""

    def clone(self) -> Self:
        """Método para hacer una copia superficial (shallow copy)."""
        ...

    def deepclone(self, memo: dict[int, Any] | None = None) -> Self:
        """Método para hacer una copia profunda (deep copy)."""
        ...


class ConcretePrototype:
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

    def clone(self) -> Self:
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

    def deepclone(self, memo: dict[int, Any] | None = None) -> Self:
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
