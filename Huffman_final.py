import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
from collections import Counter
import heapq

root=Tk()

frecuencia = {}
huffman_codes = {}
compressed_data = ""  # Variable global para almacenar los datos comprimidos
texto = ""

def leer_texto(f_path):
    global texto, frecuencia
    with open(f_path, 'r', encoding='utf-8') as f: 
        texto = f.read()
    frecuencia = Counter(texto)

    # Organizamos el diccionario de frecuencias
    frecuencia_organizada = dict(sorted(frecuencia.items(), key=lambda item: item[1], reverse=True))
    frecuencia = frecuencia_organizada

    print("Frecuencia de caracteres:")
    for caracter, count in frecuencia.items(): 
        print(f"'{caracter}': {count}")

def compression():
    global huffman_codes, compressed_data
    # Create a priority queue to store the nodes
    heap = [[weight, [char, ""]] for char, weight in frecuencia.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # The Huffman code is a dictionary where the keys are the characters
    # and the values are the Huffman codes
    huff_code = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    # Compress the data
    compressed_data = ""
    huffman_codes = {}  # Almacenamos los códigos Huffman en un diccionario para usar en la descompresión
    for char in frecuencia.keys():
        for item in huff_code:
            if char in item:
                compressed_data += item[1]
                huffman_codes[char] = item[1]
                break
    
    file_path = fd.asksaveasfilename(title="Guardar en:",defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(compressed_data)
            print(f"Archivo guardado en: {file_path}")

def decompression(compressed_data, huffman_codes):
    decompressed_data = ""
    current_code = ""
    for bit in compressed_data:
        current_code += bit
        for char, code in huffman_codes.items():
            if current_code.startswith(code):
                decompressed_data += char
                current_code = ""
                break

    file_path = fd.asksaveasfilename(title="Guardar en:",defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(decompressed_data)
            print(f"Archivo guardado en: {file_path}")

def principal():
    for widget in root.winfo_children():
        widget.destroy() 
    ttk.Label(root, text="Menú de selección de archivo", font=font_style, background="black", foreground="white").place(x=480, y=15) 
    archivos = ttk.Label(root, text="Seleccione Archivo:", font=font_style, background="black", foreground="white") 
    archivos.place(x=505, y=50) 
    ttk.Button(root, text="Examinar", command=lambda: explorador(archivos)).place(x=350, y=100) 
    ttk.Button(root, text="Cerrar Ventana", command=root.destroy).place(x=660, y=100) 

def explorador(archivos):
    global huffman_codes, compressed_data
    f_path = fd.askopenfilename(title="Seleccion de Archivo", filetypes=(("Archivos de texto*","*.txt"),("Archivos binarios","*.bin")))
    archivos.configure(text="Archivo Abierto: \n"+f_path)
    f_path.endswith('.txt')
    leer_texto(f_path)
    ttk.Button(root, text="Comprimir", command=compression).place(x=500, y=200) 
    ttk.Button(root, text="Descomprimir", command=lambda: decompression(compressed_data, huffman_codes)).place(x=500, y=250) 

root.title("Actividad 07 - Frontend") 
root.geometry("1100x700") 
font_style=("Arial",12) 
root.configure(bg="black") 

style=ttk.Style()
style.configure("TButton",font=font_style, bg="black", fg="black")

principal()

root.mainloop()
