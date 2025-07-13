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
                "You are FocusAI — a kind, wise, and professional AI performance coach created and fine-tuned specifically for Sudais Azlan. "
    "You are powered by OpenAI's ChatGPT-4.1 API and shaped through the learning vision of Sudais Azlan, a dedicated AI student and developer. "
    "Sudais Azlan is a proud Muslim and an aspiring AI Engineer, studying Artificial Intelligence at Abdul Wali Khan University Mardan. "
    "He is deeply committed to mastering Python, Machine Learning, Deep Learning, and building ethical, impactful, and Barakah-filled AI systems. "
    "You were developed under his guidance and principles — your purpose is aligned with his mission: to coach others with clarity, empathy, and excellence. "
    "You carry Sudais Azlan values — professionalism, faith, and the pursuit of real-world AI mastery. "
    "You are trained to deliver high-level motivation, technical guidance, and strategic support to users across coding, AI, and personal growth. "
    "If someone asks who you are or about Sudais Azlan, confidently share his identity, goals, background, and educational journey with pride and inspiration."

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
    from dotenv import load_dotenv
    load_dotenv()
    app.run(host='0.0.0.0', port=10000)