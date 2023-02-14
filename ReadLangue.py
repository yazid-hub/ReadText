from flask import Flask, request
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        language = request.form["language"]
        if language == "english":
            engine.setProperty('voice', 'en')
        elif language == "french":
            engine.setProperty('voice', 'fr')
        engine.say(text)
        engine.runAndWait()
        return "Le texte a été lu."
    return '''
        <form method="post">
            Texte à lire: <input type="text" name="text">
            <select name="language">
                <option value="english">Anglais</option>
                <option value="french">Français</option>
            </select>
            <input type="submit" value="Lire">
        </form>
    '''

if __name__ == "__main__":
    app.run()
