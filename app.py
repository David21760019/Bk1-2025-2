from flask import Flask
from flask import render_template
app = Flask(__name__)
from flask import Flask, jsonify

data = {
    "name":"alice",
    "age":30,
    "city":"New York",
    "is_student": False,
    "hobbies": ["reading","coding"]
    }

@app.route("/")
def hello_world():
    return  """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Buenos Días Amorcito</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                background-color: #f4f4f4; /* color minimalista */
                color: #333; /* texto suave */
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
                padding: 10px;
            }

            .container {
                max-width: 90%;
            }

            marquee p {
                font-size: 4vw; /* responsivo */
                font-weight: bold;
                color: #e63946; /* rojo suave */
                text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            }

            .message {
                font-size: 3vw;
                margin-top: 2rem;
                color: #1d3557; /* azul suave */
            }

            .love {
                font-size: 3vw;
                margin-top: 1rem;
                color: #f77f00; /* naranja suave */
                font-weight: bold;
            }

            @media (max-width: 600px) {
                marquee p { font-size: 6vw; }
                .message { font-size: 5vw; }
                .love { font-size: 5vw; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <marquee behavior="scroll" direction="left" scrollamount="6">
                <p>Buenos Días Amorcito ❤️</p>
            </marquee>
            <div class="message">Que tengas un día lleno de alegría 🌞💖</div>
            <div class="love">Te amo muchísimo ❤️</div>
        </div>
    </body>
    </html>
    """
@app.route("/jason")
def saluda():
    return data

@app.route("/json")
def saludajson():
    return jsonify(data)

@app.route("/pagina")
@app.route("/pagina/<name>")
def pagina(name=None):
    return render_template('pagina.html', person=name)
