# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
   
    namearchivo = input("Nombre del archivo: ")
    
    archivo = open(namearchivo, 'r')
    n = int(archivo.readline())
    
    monitor = temp_monitor.init(n)
    
    for i in range(r):
    tempe = float(archivo.readline())
    monitor = temp_monitor.add_reading(monitor, temp)
    
    # TODO: Imprimir la racha creciente mas larga
    #       usando temp_monitor.longest_rising_streak()
    
    pass


if __name__ == "__main__":
    main()
