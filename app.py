from flask import Flask, render_template, request 
import random

app = Flask(__name__)

compliments = [ 
    "You are drop dead gorgeous ;) 💖",
    "I admire the way your brain works gurll woahh 🧠✨",
    "You have a great sense of style dangg!! 👗🌸",
    "You are exquisite💎",
    "Your beauty is incomparable!👑💕",
    "Your energy is lovely :D ☀️🦋",
    "Your kindness is contagious <3 🌈💖"
]

@app.route("/", methods=["GET","POST"])
def home():
    compliment = None
    name = ""

    if request.method == "POST":
        name = request.form["name"]
        compliment = random.choice(compliments)

    return render_template(
        "index.html",
        compliment=compliment,
        name=name
    )
if __name__ == "__main__":
    app.run(debug=True)
