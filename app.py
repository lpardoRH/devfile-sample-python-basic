from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def hello():
    if request.args.get('c'):
        return render_template_string(request.args.get('c'))
    else:
        return "Hello!"

if __name__ == "__main__":
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
