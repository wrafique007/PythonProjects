from openai import OpenAI

class chatbot():
    
    def __init__(self):
        self.client = OpenAI()
        self.client.api_key="Enter your key here"
        
    def get_response(self,user_input):
        response = self.client.chat.completions.create(
            messages=user_input,
            model='gpt-4',
            stream=True
        ).choices[0].text

        return response
    
if __name__=="__main__":
    bot = chatbot()
    print(bot.get_response("tell me something funny"))