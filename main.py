from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "Bot calisiyor reis!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
