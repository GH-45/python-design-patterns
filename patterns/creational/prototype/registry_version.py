"""Implementación del patrón de diseño Prototype utilizando Registry Pattern.

Este enfoque introduce una clase adicional, que actúa como un registro centralizado
para almacenar y gestionar prototipos. Los clientes pueden registrar prototipos y
luego solicitar clones de esos prototipos a través del registro.

Componentes clave:
-----------------
*   Prototype (Protocol): Definición estructural que especifica los métodos de clonación.
    Cualquier clase que implemente estos métodos puede ser utilizada como prototipo.
*   PrototypeRegistry: Clase que actúa como un registro para almacenar prototipos y clonarlos.

Flujo de trabajo:
----------------
El Cliente registra prototipos en el PrototypeRegistry. Cuando necesita una nueva instancia,
solicita al PrototypeRegistry que clone un prototipo registrado. El PrototypeRegistry
utiliza los métodos de clonación definidos en el prototipo para devolver una nueva instancia,
la cual puede ser modificada por el Cliente de forma independiente sin alterar el original.
"""

import copy
from typing import Any, Protocol, Self


class Prototype(Protocol):
    """Protocol que define la interfaz común para objetos clonables."""

    def __copy__(self) -> Self:
        """Método para hacer una copia superficial (shallow copy)."""
        ...

    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Self:
        """Método para hacer una copia profunda (deep copy)."""
        ...


class PrototypeRegistry:
    """Clase que actúa como un registro para almacenar prototipos y clonarlos.

    Attributes:
        _registry: Diccionario que almacena los prototipos registrados.
    """

    def __init__(self) -> None:
        """Inicializa el registro de prototipos."""
        self._registry: dict[str, Prototype] = {}

    def register(self, name: str, prototype: Prototype) -> None:
        """Registra un prototipo.

        Args:
            name: Nombre único para identificar el prototipo.
            prototype: Instancia del prototipo a registrar.
        """
        # Si se requiere, se puede agregar lógica para
        # evitar sobrescribir prototipos existentes o de validación.
        self._registry[name] = prototype

    def unregister(self, name: str) -> None:
        """Elimina un prototipo registrado.

        Args:
            name: Nombre del prototipo a eliminar.
        """
        try:
            del self._registry[name]
        except KeyError:
            pass  # Se puede optar por lanzar una excepción si el prototipo no existe

    def get_prototype(self, name: str) -> Prototype:
        """Obtiene un prototipo registrado.

        Args:
            name: Nombre del prototipo a obtener.

        Returns:
            El prototipo registrado con el nombre dado.

        Raises:
            ValueError: Si el prototipo no se encuentra en el registro.
        """
        try:
            return self._registry[name]
        except KeyError:
            raise ValueError(f"Prototipo '{name}' no encontrado en el registro.")

    def clone(self, name: str) -> Prototype:
        """Clona un prototipo registrado de forma superficial.

        Args:
            name: Nombre del prototipo a clonar.
        """
        prototype = self.get_prototype(name)
        return copy.copy(prototype)

    def deepclone(self, name: str, memo: dict[int, Any] | None = None) -> Prototype:
        """Clona un prototipo registrado de forma profunda.

        Args:
            name: Nombre del prototipo a clonar.
            memo: Diccionario interno usado por copy.deepcopy() para evitar referencias circulares.
        """
        prototype = self.get_prototype(name)
        return copy.deepcopy(prototype, memo)
