from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Fun Animation</title>
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background-color: black;
                height: 100vh;
                width: 100vw;
                font-family: 'Arial', sans-serif;
                position: relative;
            }
            /* Big festive message with emojis */
            .message {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 3em;
                color: orange;
                font-weight: bold;
                text-shadow: 0 0 20px #ff6600, 0 0 30px #ff6600;
                z-index: 10;
                text-align: center;
                padding: 20px;
            }
            /* Floating circles with glow effect */
            .circle {
                position: absolute;
                border-radius: 50%;
                background: radial-gradient(circle, #ffcc00, #ff6600);
                opacity: 0.8;
                animation: float 10s infinite ease-in-out;
            }
            /* Generate multiple circles with different sizes and positions */
            {% for i in range(20) %}
            .circle:nth-child({{ i+1 }}) {
                width: {{ (i+1) * 10 }}px;
                height: {{ (i+1) * 10 }}px;
                top: {{ (i*5) % 100 }}%;
                left: {{ (i*7) % 100 }}%;
                animation-delay: {{ i * 0.5 }}s;
            }
            {% endfor %}
            @keyframes float {
                0%, 100% { transform: translateY(0) translateX(0); }
                50% { transform: translateY(-20px) translateX(20px); }
            }
        </style>
    </head>
    <body>
        <!-- Awesome Halloween message with emojis -->
        <div class="message">👻 HAPPY HALLOWEEN CODE TEST CHALLENGE 🎃</div>
        <!-- Floating circles -->
        {% for i in range(20) %}
        <div class="circle"></div>
        {% endfor %}
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
