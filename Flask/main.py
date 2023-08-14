from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def generate():
    count = 0
    while True:
        yield f"data: {count}\n\n"
        count += 1


@app.route('/stream')
def stream():
    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
