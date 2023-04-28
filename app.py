from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    if request.args.get('c'):
        return render_template_string(request.args.get('c'))
    else:
        return "Hello!"

if __name__ == "__main__":
    app.run()
