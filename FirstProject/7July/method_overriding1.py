class AIModel:
    def generate_response(self, prompt):
        print("Generating response by using general AI Model")

class OpenAIModel:
    def generate_response(self, prompt):
        print("Generating response using OpenAI GPT model")
        print("Prompt:",prompt)

class GeminiModel(AIModel):
    def generate_response(self, prompt):
        print("Generating response using Gemini Model")
        print("prompt:", prompt)

model1= OpenAIModel()
model1.generate_response("Explain Python Decorators")
print("=" * 35)
model2= GeminiModel()
model2.generate_response("Explain Python File Handling")

