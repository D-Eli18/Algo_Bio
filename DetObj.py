import cv2
import numpy as np

def detectar_formas(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    imagen_blur = cv2.GaussianBlur(imagen_gris, (5, 5), 0)
    
    bordes = cv2.Canny(imagen_blur, 50, 150)
    
    contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    formas_detectadas = {
        'Círculos': [],
        'Triángulos': [],
        'Cuadrados': []
    }
    
    for contorno in contornos:
        epsilon = 0.04 * cv2.arcLength(contorno, True)
        approx = cv2.approxPolyDP(contorno, epsilon, True)
        
        # Calcular el número de vértices de la forma
        num_vertices = len(approx)
        
        # Si la forma tiene aproximadamente 4 vértices, se considera un cuadrado
        if num_vertices == 4:
            formas_detectadas['Cuadrados'].append(approx)
        
        # Si la forma tiene aproximadamente 3 vértices, se considera un triángulo
        elif num_vertices == 3:
            formas_detectadas['Triángulos'].append(approx)
        
        # Si la forma tiene entre 8 y 23 vértices, se considera un círculo
        elif 8 <= num_vertices <= 23:
            formas_detectadas['Círculos'].append(approx)
    
    return formas_detectadas

def dibujar_formas(imagen, formas_detectadas):
    # Dibujar los contornos de las formas detectadas en la imagen
    cv2.drawContours(imagen, formas_detectadas['Círculos'], -1, (0, 255, 0), 2)
    cv2.drawContours(imagen, formas_detectadas['Triángulos'], -1, (0, 0, 255), 2)
    cv2.drawContours(imagen, formas_detectadas['Cuadrados'], -1, (255, 0, 0), 2)
    
    # Mostrar la imagen con las formas detectadas
    cv2.imshow('Formas detectadas', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Cargar la imagen de prueba
    imagen = cv2.imread('imagen_prueba.jpg')
    
    # Detectar las formas en la imagen
    formas_detectadas = detectar_formas(imagen)
    
    # Imprimir los resultados
    print('Formas detectadas:')
    print('Círculos:', len(formas_detectadas['Círculos']))
    print('Triángulos:', len(formas_detectadas['Triángulos']))
    print('Cuadrados:', len(formas_detectadas['Cuadrados']))
    
    # Dibujar las formas detectadas en la imagen
    dibujar_formas(imagen, formas_detectadas)

if __name__ == '__main__':
    main()