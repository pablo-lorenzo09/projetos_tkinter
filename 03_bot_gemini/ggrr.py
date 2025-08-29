from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyB8IWUIm7eGnsx3Hs8VVcsKIde8uEFkEhM")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="oi amigooooo"
)
print(response.text)