import random
import numpy as np

def cuantas_figus(figus_total):
    album = []
    i = 0
    while len(album) != figus_total:
        dado = random.randint(1,figus_total)
        if dado not in album:
            album.append(dado)
        i = i + 1
    return i

def generar_paquete(figus_total, figus_paquete):
    paquete = []
    while len(paquete) < figus_paquete:
         dado = random.randint(1,figus_total)
         paquete.append(dado)
    return paquete


#Esta funcion fue usada en la primer parte del Ejercicio y queda en desuso en la segunda parte
def repeticiones(nrep,figus_total):
    albumrep = []
    while len(albumrep) != nrep:
        resultado = cuantas_figus(figus_total)
        albumrep.append(resultado)
    return albumrep

def cuantos_paquetes(figus_total, figus_paquete):
    paquetes_total = 0
    album = []
    while len(album) != figus_total:
         paquete_generado = generar_paquete(figus_total, figus_paquete)
         i = 0
         while i != figus_paquete:
            if paquete_generado[i] not in album:
                album.append(paquete_generado[i])
            i = i + 1
         paquetes_total = paquetes_total + 1
    return paquetes_total

def repetir(nrep, figus_total, figus_paquete):
    figuritas_album = []
    while len(figuritas_album) != nrep:
        cant_paquetes = cuantos_paquetes(figus_total, figus_paquete)
        figuritas_album.append(cant_paquetes)
    return figuritas_album


nrep = 100
figus_total = 669
figus_paquete = 5

resultado = repetir(nrep, figus_total, figus_paquete)
print(resultado)
print("El promedio de paquetes necesarios para llenar un album de", figus_total,"figuritas es de: ", np.mean(resultado))

#No complete los ejercicios optativos.


