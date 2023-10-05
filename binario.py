""" Creamos un diccionario que contenga los caracteres y números en binario.
He de aclarar que existen funciones nativas de python que traducen directamente
los caracteres a binario, pero el punto del proyecto era hacerlo desde 0"""



diccionario = {
    'A': '01000001',
    'B': '01000010',
    'C': '01000011',
    'D': '01000100',
    'E': '01000101',
    'F': '01000110',
    'G': '01000111',
    'H': '01001000',
    'I': '01001001',
    'J': '01001010',
    'K': '01001011',
    'L': '01001100',
    'M': '01001101',
    'N': '01001110',
    'O': '01001111',
    'P': '01010000',
    'Q': '01010001',
    'R': '01010010',
    'S': '01010011',
    'T': '01010100',
    'U': '01010101',
    'V': '01010110',
    'W': '01010111',
    'X': '01011000',
    'Y': '01011001',
    'Z': '01011010',
    'a': '01100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'o': '01101111',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010',
    '0': '00110000',
    '1': '00110001',
    '2': '00110010',
    '3': '00110011',
    '4': '00110100',
    '5': '00110101',
    '6': '00110110',
    '7': '00110111',
    '8': '00111000',
    '9': '00111001',
    ' ': '00100000',  # Espacio
    '.': '00101110',  # Punto
    '¡': '10100001',  # Signo de exclamación abierta
    '!': '00100001',  # Signo de exclamación cerrada
    '¿': '10111111',  # Signo de interrogación abierta
    '?': '00111111',  # Signo de interrogación cerrada
    ',': '00101100',  # Coma
    ':': '00111010',  # Dos puntos
    ';': '00111011',  # Punto y coma
    '-': '00101101',  # Guion
    '_': '01011111',  # Guión bajo
    '"': '00100010',  # Comillas dobles
    "'": '00100111',  # Comillas simples
    '(': '00101000',  # Paréntesis izquierdo
    ')': '00101001',  # Paréntesis derecho
    '[': '00111011',  # Corchete izquierdo
    ']': '00111001',  # Corchete derecho
    '{': '01111011',  # Llave izquierda
    '}': '01111101',  # Llave derecha
    '<': '00111100',  # Menor que
    '>': '00111110',  # Mayor que
    '/': '00101111',  # Barra diagonal
    '\\': '01011100', # Barra diagonal inversa
    '|': '01111100',  # Barra vertical
    '@': '01000000',  # Símbolo de arroba
    '#': '00100011',  # Almohadilla
    '$': '00100100',  # Signo de dólar
    '%': '00100101',  # Porcentaje
    '^': '01011110',  # Acento circunflejo
    '&': '00100110',  # Ampersand
    '*': '00101010',  # Asterisco
    '+': '00101011',  # Signo más
    '=': '00111101',  # Signo igual
    '`': '01100000',  # Acento grave
    '~': '01111110',  # Tilde
    '\n': '00001010', # Salto de línea
}

# Función que traduce texto a binario.

def trad_tex_a_bin(texto, diccionario):

    caracter = '' # Variable en donde vamos a almacenar la cadena binaria.


    for i in texto: # Recorremos el texto ingresado.
        
        if i in diccionario: # Consultamos las traducciones al diccionario.

            caracter += diccionario[i] # Agregamos el resultado a la variable creada anteriormente.
    
    return caracter

""" Creamos otro diccionario como en anterior pero a la inversa. Podríamos 
usar el diccionario creado anteriormente invirtiendo sus claves, pero no
era problema crear uno dedicado para la nueva función"""



diccionario_inverso = {
    '01000001': 'A',
    '01000010': 'B',
    '01000011': 'C',
    '01000100': 'D',
    '01000101': 'E',
    '01000110': 'F',
    '01000111': 'G',
    '01001000': 'H',
    '01001001': 'I',
    '01001010': 'J',
    '01001011': 'K',
    '01001100': 'L',
    '01001101': 'M',
    '01001110': 'N',
    '01001111': 'O',
    '01010000': 'P',
    '01010001': 'Q',
    '01010010': 'R',
    '01010011': 'S',
    '01010100': 'T',
    '01010101': 'U',
    '01010110': 'V',
    '01010111': 'W',
    '01011000': 'X',
    '01011001': 'Y',
    '01011010': 'Z',
    '01100001': 'a',
    '01100010': 'b',
    '01100011': 'c',
    '01100100': 'd',
    '01100101': 'e',
    '01100110': 'f',
    '01100111': 'g',
    '01101000': 'h',
    '01101001': 'i',
    '01101010': 'j',
    '01101011': 'k',
    '01101100': 'l',
    '01101101': 'm',
    '01101110': 'n',
    '01101111': 'o',
    '01110000': 'p',
    '01110001': 'q',
    '01110010': 'r',
    '01110011': 's',
    '01110100': 't',
    '01110101': 'u',
    '01110110': 'v',
    '01110111': 'w',
    '01111000': 'x',
    '01111001': 'y',
    '01111010': 'z',
    '00110000': '0',
    '00110001': '1',
    '00110010': '2',
    '00110011': '3',
    '00110100': '4',
    '00110101': '5',
    '00110110': '6',
    '00110111': '7',
    '00111000': '8',
    '00111001': '9',
    '00100000': ' ',  # Espacio
    '00101110': '.',  # Punto
    '10100001': '¡',  # Signo de exclamación abierta
    '00100001': '!',  # Signo de exclamación cerrada
    '10111111': '¿',  # Signo de interrogación abierta
    '00111111': '?',  # Signo de interrogación cerrada
    '00101100': ',',  # Coma
    '00111010': ':',  # Dos puntos
    '00111011': ';',  # Punto y coma
    '00101101': '-',  # Guion
    '01011111': '_',  # Guión bajo
    '00100010': '"',  # Comillas dobles
    '00100111': "'",  # Comillas simples
    '00101000': '(',  # Paréntesis izquierdo
    '00101001': ')',  # Paréntesis derecho
    '00111011': '[',  # Corchete izquierdo
    '00111001': ']',  # Corchete derecho
    '01111011': '{',  # Llave izquierda
    '01111101': '}',  # Llave derecha
    '00111100': '<',  # Menor que
    '00111110': '>',  # Mayor que
    '00101111': '/',  # Barra diagonal
    '01011100': '\\',  # Barra diagonal inversa
    '01111100': '|',  # Barra vertical
    '01000000': '@',  # Símbolo de arroba
    '00100011': '#',  # Almohadilla
    '00100100': '$',  # Signo de dólar
    '00100101': '%',  # Porcentaje
    '01011110': '^',  # Acento circunflejo
    '00100110': '&',  # Ampersand
    '00101010': '*',  # Asterisco
    '00101011': '+',  # Signo más
    '00111101': '=',  # Signo igual
    '01100000': '`',  # Acento grave
    '01111110': '~',  # Tilde
    '00001010': '\n'  # Salto de línea
}

# Función que traduce binario a texto.

def trad_bin_a_text(binario, diccionario_inverso):
    
    texto = '' # Variable en donde vamos a almacenar el texto final.
    byte = '' # Variable temporal en donde vamos a almacenar bits

    for bit in binario:
        byte += bit     # Agregamos el bit actual al la variable byte.

        # Nos aseguramos si formamos un byte completo (8 bits)

        if len(byte) == 8:
            if byte in diccionario_inverso:
                caracter = diccionario_inverso[byte]
                texto += caracter

            else:
                # Manejamos errores si la representación binaria no se encuentra en el diccionario inverso.
                texto += '?'
            
            byte = '' # Reiniciamos el byte temporal para el siguiente.
    
    return texto