import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Convertidor General")
ventana.geometry("400x500")
ventana.configure(bg="#1C1C1E") 

# Función para mostrar una nueva pantalla
def mostrar_pantalla_convertidor():
    limpiar_ventana()

    tk.Label(ventana, text="Ingresa el número para convertir:", font=("Helvetica Neue", 16), bg="#1C1C1E", fg="white").pack(pady=20)

    entrada = tk.Entry(ventana, font=("Helvetica Neue", 14), justify="center", bg="#2C2C2E", fg="white", relief="flat")
    entrada.pack(pady=10, ipadx=10, ipady=5)

    resultado = tk.Label(ventana, text="", font=("Helvetica Neue", 14), bg="#1C1C1E", fg="white")
    resultado.pack(pady=10)

    def convertir_a_decimal():
        valor = entrada.get().strip()
        try:
            if valor.startswith("0b"):
                decimal = int(valor, 2)
            elif valor.startswith("0x"):
                decimal = int(valor, 16)
            else:
                decimal = int(valor)
            resultado.config(text=f"Decimal: {decimal}")
        except ValueError:
            messagebox.showinfo("Error", "Por favor, ingresa un valor binario (0b) o hexadecimal (0x) válido.")

    def convertir_a_binario():
        valor = entrada.get().strip()
        try:
            decimal = int(valor)
            binario = bin(decimal)[2:]
            resultado.config(text=f"Binario: {binario}")
        except ValueError:
            messagebox.showinfo("Error", "Por favor, ingresa un número decimal válido para convertir a binario.")

    def convertir_a_hexadecimal():
        valor = entrada.get().strip()
        try:
            decimal = int(valor)
            hexadecimal = hex(decimal)[2:].upper()
            resultado.config(text=f"Hexadecimal: {hexadecimal}")
        except ValueError:
            messagebox.showinfo("Error", "Por favor, ingresa un número decimal válido para convertir a hexadecimal.")

    tk.Button(ventana, text="Convertir a Binario", font=("Helvetica Neue", 14), bg="#32D74B", fg="#1C1C1E", command=convertir_a_binario, relief="flat", activebackground="#28A745", activeforeground="#1C1C1E").pack(pady=5, ipadx=10, ipady=5)
    tk.Button(ventana, text="Convertir a Hexadecimal", font=("Helvetica Neue", 14), bg="#32D74B", fg="#1C1C1E", command=convertir_a_hexadecimal, relief="flat", activebackground="#28A745", activeforeground="#1C1C1E").pack(pady=5, ipadx=10, ipady=5)
    tk.Button(ventana, text="Convertir a Decimal", font=("Helvetica Neue", 14), bg="#32D74B", fg="#1C1C1E", command=convertir_a_decimal, relief="flat", activebackground="#28A745", activeforeground="#1C1C1E").pack(pady=5, ipadx=10, ipady=5)

    tk.Button(ventana, text="Regresar", font=("Helvetica Neue", 14), bg="#FF453A", fg="#1C1C1E", command=mostrar_pantalla_principal, relief="flat", activebackground="#D32F2F", activeforeground="#1C1C1E").pack(pady=20, ipadx=10, ipady=5)

# Función para limpiar la ventana actual
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

# Pantalla principal
def mostrar_pantalla_principal():
    limpiar_ventana()

    tk.Label(ventana, text="Convertidor General", font=("Helvetica Neue", 18, "bold"), bg="#1C1C1E", fg="white").pack(pady=30)

    tk.Button(ventana, text="Convertidor ASCII", font=("Helvetica Neue", 14), bg="#007AFF", fg="white", command=mostrar_pantalla_ascii, relief="flat", activebackground="#005BB5", activeforeground="white").pack(pady=10, ipadx=20, ipady=10)
    tk.Button(ventana, text="Convertidor Binario/Decimal", font=("Helvetica Neue", 14), bg="#007AFF", fg="white", command=mostrar_pantalla_convertidor, relief="flat", activebackground="#005BB5", activeforeground="white").pack(pady=10, ipadx=20, ipady=10)

# Pantalla del convertidor ASCII
def mostrar_pantalla_ascii():
    limpiar_ventana()

    tk.Label(ventana, text="Ingresa el texto para convertir a ASCII:", font=("Helvetica Neue", 16), bg="#1C1C1E", fg="white").pack(pady=20)

    entrada = tk.Entry(ventana, font=("Helvetica Neue", 14), justify="center", bg="#2C2C2E", fg="white", relief="flat")
    entrada.pack(pady=10, ipadx=10, ipady=5)

    resultado = tk.Label(ventana, text="", font=("Helvetica Neue", 14), bg="#1C1C1E", fg="white")
    resultado.pack(pady=10)

    def convertir_a_ascii():
        texto = entrada.get().strip()
        if texto:
            ascii_resultado = ' '.join(str(ord(c)) for c in texto)
            resultado.config(text=f"ASCII: {ascii_resultado}")
        else:
            messagebox.showinfo("Error", "Por favor, ingresa texto válido para convertir.")

    tk.Button(ventana, text="Convertir a ASCII", font=("Helvetica Neue", 14), bg="#32D74B", fg="#1C1C1E", command=convertir_a_ascii, relief="flat", activebackground="#28A745", activeforeground="#1C1C1E").pack(pady=20, ipadx=10, ipady=5)

    tk.Button(ventana, text="Regresar", font=("Helvetica Neue", 14), bg="#FF453A", fg="#1C1C1E", command=mostrar_pantalla_principal, relief="flat", activebackground="#D32F2F", activeforeground="#1C1C1E").pack(pady=20, ipadx=10, ipady=5)
    
mostrar_pantalla_principal()
ventana.mainloop()
