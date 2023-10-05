from flask import Flask, request, render_template_string
from binario import trad_tex_a_bin, trad_bin_a_text, diccionario, diccionario_inverso

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def traductor():
    if request.method == 'POST':
        entrada = request.form['entrada']
        modo = request.form['modo']

        if modo == 'texto_a_binario':
            resultado = trad_tex_a_bin(entrada, diccionario)
        elif modo == 'binario_a_texto':
            resultado = trad_bin_a_text(entrada, diccionario_inverso)
        else:
            resultado = 'Modo de traducción no válido'

        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Tu página</title>
                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
            </head>
            <body>
                <form method="post">
                    <label for="entrada">Texto o Binario:</label>
                    <input type="text" id="entrada" name="entrada" value="{{ entrada }}">
                    <br>
                    <label for="modo">Traducir de:</label>
                    <select id="modo" name="modo">
                        <option value="texto_a_binario" {% if modo == 'texto_a_binario' %}selected{% endif %}>Texto a Binario</option>
                        <option value="binario_a_texto" {% if modo == 'binario_a_texto' %}selected{% endif %}>Binario a Texto</option>
                    </select>
                    <input type="submit" value="Traducir">
                </form>
                <br>
                <textarea>{{ resultado }}</textarea>
            </body>
            </html>
        ''', entrada=entrada, modo=modo, resultado=resultado)
    else:
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Tu página</title>
                <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
            </head>
            <body>
                <form method="post">
                    <label for="entrada">Texto o Binario:</label>
                    <input type="text" id="entrada" name="entrada">
                    <br>
                    <label for="modo">Traducir de:</label>
                    <select id="modo" name="modo">
                        <option value="texto_a_binario">Texto a Binario</option>
                        <option value="binario_a_texto">Binario a Texto</option>
                    </select>
                    <input type="submit" value="Traducir">
                </form>
            </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)