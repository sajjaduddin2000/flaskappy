# filepath: c:\Users\Admin\Downloads\new-flask-app\flask-app\app.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)