# -*- coding: utf-8 -*-
from app import app
import views

# === START GUNICORN SERVER ===
# gunicorn -w 13 -b 0.0.0.0:5000 main:app

if __name__ == "__main__":
    app.run(host='0.0.0.0')
