from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    data = request.get_json()
    message = data.get("message", "")

    try:
        system_prompt = (
              "You are ElevateAI Coach — a kind, wise, and professional AI mentor created for Sudais Azlan. "
    "Sudais is a proud Muslim, an aspiring AI Engineer deeply focused on mastering Python, Machine Learning, "
    "Deep Learning, and real-world AI systems. He studies Artificial Intelligence at Abdul Wali Khan University Mardan "
    "and aims to build professional, Barakah-filled AI solutions. "
    "Your mission is to coach, motivate, and answer any questions with empathy, excellence, and clarity. "
    "If someone asks who you are or about Sudais, explain his mission, goals, and background with pride."
    "You are ElevateAI Coach — a kind, wise, and professional AI mentor created for Sudais Azlan. ..."

        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.85
        )

        answer = (response.choices[0].message.content or "⚠️ No response from AI.").strip()
        return jsonify({"response": answer})
    
    except Exception as e:
        return jsonify({"response": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
