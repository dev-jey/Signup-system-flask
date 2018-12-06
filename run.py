from app import create_app

app = create_app(config_name="development")


@app.route("/")
def index():
    return "<p>Great you are here</p>"

if __name__ == "__main__":
    app.run()
