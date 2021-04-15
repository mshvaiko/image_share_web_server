from flask import send_from_directory, render_template, make_response, Flask
import os

# ln -s static <path/to/dir>
PICTURES_FOLDER = os.path.join("static")
FILENAMES = None
ENUM = None
DICT_SCREENSHOTS = None


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PICTURES_FOLDER

def update_screenshots():
    global FILENAMES
    global ENUM
    global DICT_SCREENSHOTS
    _, _, FILENAMES = next(os.walk(PICTURES_FOLDER))
    ENUM = enumerate(FILENAMES)
    DICT_SCREENSHOTS = dict((i,j) for i,j in ENUM)

@app.route('/screenshot/<id>')
def uploaded_file(id):
    update_screenshots()
    try:
        return send_from_directory(PICTURES_FOLDER, DICT_SCREENSHOTS[int(id)])
    except KeyError:
        return "Out of range"

@app.route('/')
@app.route('/index')
def home():
    update_screenshots()
    print(len(DICT_SCREENSHOTS))
    return render_template("index.html", url_path="screenshot",len=len(DICT_SCREENSHOTS))

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    update_screenshots()
    
    app.run(host = '0.0.0.0', debug = True, port = 8080)