from app import app

@app.route("/")
def index():
    return "hello World"


@app.route("/home")
def home():
    return "welcome to home"