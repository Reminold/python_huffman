import tkinter as tk
from tkinter import filedialog

# Sugerencia: Importar las funciones del backend
# Estas funciones se les proporcionan a los botones de la interfaz
from mock_backend import compression, decompression

# Definimos la clase para nuestra interfaz grafica
class Interface:
  def __init__(self, width=640, height=480, title="Huffman Algorithm Interface"):
    # Variables adicionales para el programa
    self.file_content = ""
    self.text = ""
    self.char_count = {}

    # Inicializamos la ventana de Tkinter
    self.window = tk.Tk()
    self.window.title(title)

    # Cambiamos el color de fondo de la ventana
    self.window.configure(bg="#3296C8")  # RGB (50, 150, 200)

    # Llamamos los metodos auxiliares para configurar la interfaz
    self.set_dimensions(width, height)
    self.generate_elements()

    # Mantenemos la ventana abierta
    self.window.mainloop()


  def set_dimensions(self, width, height):
    # Obtenemos las dimensiones de la pantalla
    screen_width = self.window.winfo_screenwidth()
    screen_height = self.window.winfo_screenheight()

    # Variables para la posicion en pantalla de la ventana
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    # Se inicializa las dimensiones de la pantalla y su posicion
    self.window.geometry(f"{width}x{height}+{x_position}+{y_position}")

  def generate_elements(self):
    # Se agrega la etiqueta con el titulo de programa
    label = tk.Label(self.window, text="Huffman Compression Algorithm", font=("Comic Sans MS", 30), bg="#3296C8", fg="white")
    label.pack(pady=20)

    # Crear un marco para contener el widget de texto
    frame = tk.Frame(self.window)
    frame.pack(padx=10, pady=10)

    # Crear un widget de texto dentro del marco
    self.text = tk.Text(frame, wrap="word", width=40, height=10)
    self.text.pack(side="left", fill="both", expand=True)

    # Agregar una barra de desplazamiento al widget de texto
    scrollbar = tk.Scrollbar(frame, command=self.text.yview)
    scrollbar.pack(side="right", fill="y")
    self.text.config(yscrollcommand=scrollbar.set)

    # Creamos el boton para abrir el archivo
    self.open_file_button = tk.Button(self.window, text="Examinar", command=self.open_file)
    self.open_file_button.pack()

    # Los siguientes dos botones usan lambda para que el boton funcione dependiendo del contexto, en relacion a los argumentos
    # Creamos el boton para comprimir el texto, deshabilitado por default
    self.compress_button = tk.Button(self.window, text="Comprimir", state="disabled", command=lambda: compression(self.char_count))
    self.compress_button.pack()

    # Creamos el boton para descomprimir el texto, deshabilitado por default
    self.decompress_button = tk.Button(self.window, text="Descomprimir", state="disabled", command=lambda: decompression(self.file_content))
    self.decompress_button.pack()

  def open_file(self):
    # Deshabilitamos los botones hasta abrir el archivo
    self.file_content = ""
    self.compress_button.config(state="disabled")
    self.decompress_button.config(state="disabled")

    # El fialogo para abrir archivo admite extensiones txt y binarios
    file = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Archivos binarios", "*.bin")])
    if file:
      # El open admite archivos con codificacion utf-8
      with open(file, "r", encoding="utf-8") as f:
        self.file_content = f.read()

      # Se habilita el boton correspondiente segun el tipo de archivo
      if file.endswith(".txt"):
        self.count_characters()
      elif file.endswith(".bin"):
        self.decompress_button.config(state="normal")

  def count_characters(self):
    # Obtenemos el texto del contenido del archivo
    text = self.file_content
    
    self.char_count = {}
    for char in text:
      if char in self.char_count:
        self.char_count[char] += 1
      else:
        self.char_count[char] = 1
    
    # Se borra el texto anterior en el widget de texto
    self.text.delete(1.0, tk.END)

    # Se crea el diccionario con los valores ordenados y se sobreescribe
    sorted_char_count = dict(sorted(self.char_count.items(), key=lambda item: item[1], reverse=True))
    self.char_count = sorted_char_count

    # Actualizamos el objeto texto de la interfaz con la cuenta actualizada
    for c, i in self.char_count.items():
      self.text.insert(tk.END, f"{c}: {i}\n")

    # Se habilita el boton de compresion
    self.compress_button.config(state="normal")
  
    
my_interface = Interface()
