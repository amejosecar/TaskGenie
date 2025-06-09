# import os

#esto es solo para ver carpeta y contenido.

# # Ruta raíz a inspeccionar
# root_dir = r"C:\americo\API\TaskGenie"
# # Ruta de salida para el listado
# output_file = r"C:\americo\API\TaskGenie\utilitys\listado_contenido.txt"

# # Conjuntos para definir los directorios incluidos y excluidos.
# # Solo se incluirán las carpetas "routers" y "templates" (además de la raíz).
# allowed_top = {"routers", "templates"}
# # Directorios que se quieren excluir (en cualquier nivel).
# excludes = {"__pycache__", "utilitys", "venv", ".git"}

# with open(output_file, "w", encoding="utf-8") as archivo_salida:
#     # Recorremos de forma recursiva el directorio raíz.
#     for dirpath, dirnames, filenames in os.walk(root_dir):
#         # Calcular la ruta relativa respecto a la raíz del proyecto.
#         rel_path = os.path.relpath(dirpath, root_dir)

#         # Excluir cualquier ruta que contenga alguno de los directorios excluidos.
#         if any(excl in rel_path.split(os.sep) for excl in excludes):
#             continue

#         # En el nivel raíz (rel_path == ".") se procesan solamente las carpetas permitidas.
#         if rel_path == ".":
#             # Prune (remover) de "dirnames" aquellas carpetas que no estén en allowed_top.
#             dirnames[:] = [d for d in dirnames if d in allowed_top]
#             display_name = "Carpeta Principal"
#         else:
#             # Para cualquier otra ruta, validar que la carpeta de nivel superior esté permitida.
#             first_part = rel_path.split(os.sep)[0]
#             if first_part not in allowed_top:
#                 continue
#             display_name = rel_path

#         # Escribir el nombre de la carpeta actual.
#         archivo_salida.write(f"Carpeta: {display_name}\n")
#         # Escribir los archivos encontrados en esta carpeta.
#         for filename in filenames:
#             archivo_salida.write(f"    Archivo: {filename}\n")

#esto es solo para ver el archvio con la ruta completa.import os

import os

# Ruta raíz a inspeccionar
root_dir = r"C:\americo\API\TaskGenie"
# Ruta de salida para el listado
output_file = r"C:\americo\API\TaskGenie\utilitys\listado_contenido.txt"

# Definir los directorios de primer nivel que se incluyen (además de la raíz)
allowed_top = {"routers", "templates"}
# Definir los directorios que se deben excluir en cualquier nivel
excludes = {"__pycache__", "utilitys", "venv", ".git"}

with open(output_file, "w", encoding="utf-8") as archivo_salida:
    # Recorremos recursivamente el directorio raíz.
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Excluir directorios cuya ruta contenga alguno de los nombres en 'excludes'
        if any(excl in dirpath.split(os.sep) for excl in excludes):
            continue
        
        # Obtener la ruta relativa respecto de root_dir
        rel_path = os.path.relpath(dirpath, root_dir)
        
        # En la raíz (rel_path == ".") se permiten sus archivos;
        # en ese nivel, solo se desea descender a 'routers' y 'templates'
        if rel_path == ".":
            # Solo conservar los directorios permitidos a nivel superior
            dirnames[:] = [d for d in dirnames if d in allowed_top]
        else:
            # Para cualquier otro nivel, validamos que la carpeta de primer nivel pertenezca a allowed_top.
            top_level = rel_path.split(os.sep)[0]
            if top_level not in allowed_top:
                continue
        
        # Para cada archivo encontrado, se compone y escribe su ruta completa.
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            archivo_salida.write(full_path + "\n")
