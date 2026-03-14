from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

@app.route("/", methods=["GET", "POST"])
def index():

    improved_prompt = ""

    if request.method == "POST":

        user_prompt = request.form["prompt"]

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Improve the user's prompt so it becomes clearer and better for AI."},
                {"role": "user", "content": user_prompt}
            ]
        )

        improved_prompt = response.choices[0].message.content

    return render_template("index.html", improved_prompt=improved_prompt)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)