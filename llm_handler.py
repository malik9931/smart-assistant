import google.generativeai as genai

# ضع مفتاح Gemini API هنا
GOOGLE_API_KEY = "urApiKey"
genai.configure(api_key=GOOGLE_API_KEY)

# استخدم نموذج Gemini
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def ask_openai(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"
