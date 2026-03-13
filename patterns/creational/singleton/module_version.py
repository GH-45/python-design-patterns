"""Ejemplo de implementación del patrón Singleton utilizando modulos.

Este método de implementación aprovecha la naturaleza del sistema de importación de Python.

En Python, los módulos son objetos "singleton" por definición.
La primera vez que se importa un módulo, este se ejecuta y se almacena en `sys.modules`.
Las importaciones posteriores del mismo módulo retornan el objeto ya existente en caché.

Al instanciar la clase directamente dentro del módulo y exponer solo dicha instancia,
se garantiza que cualquier parte del programa que la importe esté trabajando exactamente con el mismo objeto.
"""

__all__ = ["my_singleton"]


class _Singleton:
    """Clase que define la estructura del objeto único."""

    def __init__(self) -> None:
        """Ejemplo de método constructor que puede contener la lógica de construcción de la clase."""

    def some_business_logic(self) -> None:
        """Ejemplo de método que puede contener la lógica de negocio de la clase."""


# Se crea la instancia única de la clase al momento de cargar el módulo.
# Cualquier referencia a 'MySingleton' en otros archivos apuntará a este objeto.
my_singleton = _Singleton()
