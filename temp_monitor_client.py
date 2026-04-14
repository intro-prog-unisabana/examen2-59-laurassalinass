# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
   
    namearchivo = input("Nombre del archivo: ")
    
    archivo = open(namearchivo, 'n')
    n = int(archivo.readline())
    
    monitor = temp_monitor.init(n)
    
    # TODO: Leer las n temperaturas y agregarlas con temp_monitor.add_reading()
    
    # TODO: Imprimir la racha creciente mas larga
    #       usando temp_monitor.longest_rising_streak()
    
    pass


if __name__ == "__main__":
    main()
