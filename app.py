from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route to serve static files (CSS and JavaScript)
@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = 'static'  # Change this to the directory where your static files are located
    return send_from_directory(root_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
