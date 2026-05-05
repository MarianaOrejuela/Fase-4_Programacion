# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programacion
# Ejercicio 1 - Sistema Integral de Gestion de Clientes,
# Servicios y Reservas para Software FJ

import logging
from abc import ABC, abstractmethod

# CONFIGURACION DEL ARCHIVO DE LOGS
logging.basicConfig(
    filename='software_fj_logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# --------------------------------------------------------------
# EXCEPCIONES PERSONALIZADAS
# --------------------------------------------------------------
class ErrorSistema(Exception):
    pass

class ErrorValidacion(ErrorSistema):
    pass

class ErrorReserva(ErrorSistema):
    pass

class ErrorServicio(ErrorSistema):
    pass

# --------------------------------------------------------------
# CLASE ABSTRACTA GENERAL DEL SISTEMA
# Representa cualquier entidad de servicio (cliente, servicio)
# --------------------------------------------------------------
class Entidad(ABC):
    def __init__(self, codigo):
        self._codigo = codigo

    @property
    def codigo(self):
        return self._codigo

# --------------------------------------------------------------
# EXTENSIÓN PARA GESTIÓN DE CLIENTES
# --------------------------------------------------------------
class Cliente(Entidad):
    def __init__(self, codigo, nombre, telefono):
        super().__init__(codigo)
        self.nombre = nombre
        # Se valida el teléfono al instanciar el objeto
        self.telefono = self.validar_telefono(telefono)

    def validar_telefono(self, telefono):
        """
        Valida que el teléfono contenga exactamente 10 dígitos numéricos.
        """
        # Eliminar espacios en blanco si existen
        tel_limpio = str(telefono).strip()
        
        if len(tel_limpio) == 10 and tel_limpio.isdigit():
            logging.info(f"Teléfono validado correctamente para el código {self.codigo}")
            return tel_limpio
        else:
            logging.error(f"Error de validación: Teléfono '{telefono}' no tiene 10 dígitos.")
            raise ErrorValidacion("El número telefónico debe tener exactamente 10 dígitos numéricos.")

# Ejemplo de uso:
# try:
#     cliente1 = Cliente("C001", "Héctor Osorio", "3101234567")
# except ErrorValidacion as e:
#     print(e)
