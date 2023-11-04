import openai


class GPT:
    def __init__(self, init_message):
        with open("API_KEY.txt") as mytxt:
            for line in mytxt:
                print(line)
                self.API_KEY = line
                self.messages = init_message  # = [ {"role": "system", "content": "You are a intelligent assistant."} ]

    def makeCall(self, text, model, message):
        if message:
            self.messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.chat.completions.create(
                model="gpt-4", messages=self.messages
            )
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            self.messages.append({"role": "assistant", "content": reply})
        else:
            Exception("Please put in a message")
