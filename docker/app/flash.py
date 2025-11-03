from flask import Flask, render_template_string
app = Flask(__name__)

with open("README.md", "r") as f:
    readme_content = f.read()
@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Infra Tag Gate</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #fff8b3; /* soft yellow */
                padding: 40px;
                line-height: 1.6;
                animation: fadeIn 1.5s ease-in;
            }
            .content-box {
                background: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                white-space: pre-wrap;
                animation: slideUp 1s ease-out;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes slideUp {
                from { transform: translateY(20px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
        </style>
    </head>
    <body>
        <h1 class="fade-in">🚀 Infra Tag Gate Demo</h1>
        <div class="content-box">{{ content }}</div>
    </body>
    </html>
    """, content=readme_content)














if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

