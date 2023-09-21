import cv2
import keyboard

# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Función para capturar una foto y guardarla
def capture_and_save():
    ret, frame = cap.read()  # Captura un fotograma de la cámaras
    if ret:
        file_name = input("Ingresa el nombre de la foto: ")
        cv2.imwrite(f"{file_name}.jpg", frame)  # Guarda la foto
        print(f"Foto guardada como {file_name}.jpg")

# Escucha las teclas presionadas
keyboard.add_hotkey('s', capture_and_save)

print("Presiona la tecla 's' para tomar una foto. Presiona 'Esc' para salir.")

while True:
    if keyboard.is_pressed('esc'):  # Sale si se presiona la tecla 'Esc'
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()
