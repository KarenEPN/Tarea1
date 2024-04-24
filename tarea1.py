#Librerias
import os
import tkinter as tk
from tkinter import messagebox

#Función 
def buscar_termino():
    termino = entrada.get()
    resultados = []
    carpeta = "./libros"

    # Iterar a través de cada documento
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):  # Solo procesa archivos de texto
            ruta_documento = os.path.join(carpeta, archivo)
        
            # Verificar si el término de consulta aparece en el documento
            with open(ruta_documento, 'r', encoding='utf-8') as f:
                contenido = f.read().lower()
                if termino.lower() in contenido:
                    resultados.append(archivo)
    
    # Mostrar los resultados en una ventana emergente
    if resultados:
        mensaje = f"El término '{termino}' fue encontrado en los siguientes documentos:\n\n"
        for documento in resultados:
            mensaje += f"- {documento}\n"
        messagebox.showinfo("Resultados", mensaje)
    else:
        messagebox.showinfo("Resultados", f"El término '{termino}' no aparece en ningún documento.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("TAREA BÚSQUEDA")
ventana.geometry("400x250")

# Crear un campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese el término que desea buscar:")
etiqueta.pack(pady=5)
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Crear un botón para iniciar la búsqueda
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_termino)
boton_buscar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
