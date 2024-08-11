import google.generativeai as genai 

with open("api-key.txt", "r") as apiKey:
    genai.configure(api_key=apiKey.readline())
    
generationConfig = {
    "temperature": 0.9, 
    "top_p": 1, 
    "top_k": 1, 
    "max_output_tokens": 2048
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    generation_config=generationConfig
)

convo = model.start_chat(history=[])

convo.send_message("Create a Python script printing \"Hello, World!\" to the console")
print(convo.last.text)