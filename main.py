import hashlib

def calcular_hash(archivo):
    """Calcula el hash SHA256 del contenido de un archivo."""
    with open(archivo, 'r') as f:
        contenido = f.read()
    return hashlib.sha256(contenido.encode()).hexdigest()

def verificar_bloques(archivos):
    """Verifica que los bloques sean válidos."""
    hash_anterior = "000000000000000"  # Hash inicial para el bloque 0

    for archivo in archivos:
        with open(archivo, 'r') as f:
            contenido = f.read()
        
        # Extraer hash declarado en el bloque
        lineas = contenido.splitlines()
        hash_actual = lineas[1].split('=')[1].strip().strip(')')
        print("Hash declarado:", hash_actual)

        # Verificar que el hash declarado coincide con el hash calculado del bloque anterior
        if hash_actual != hash_anterior:
            print(f"El bloque {archivo} es inválido.")
            return False

        # Calcular el hash del bloque actual para validar el siguiente
        hash_anterior = calcular_hash(archivo)
        print(f"Hash calculado del bloque {archivo}: {hash_anterior}")
    
    print("Todos los bloques son válidos.")
    return True

# Archivos de los bloques
archivos_bloques = ['bloque0.txt', 'bloque1.txt', 'bloque2.txt']
verificar_bloques(archivos_bloques)
