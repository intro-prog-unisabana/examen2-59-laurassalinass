# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    import temp_monitor

nombre_archivo = input("Nombre del archivo: ")

archivo = open(nombre_archivo, 'r')
n = int(archivo.readline())
monitor = temp_monitor.init(n)

for i in range(n):
    temp = float(archivo.readline())
    monitor = temp_monitor.add_reading(monitor, temp)

archivo.close()

print(temp_monitor.longest_rising_streak(monitor))
    
    pass


if __name__ == "__main__":
    main()
