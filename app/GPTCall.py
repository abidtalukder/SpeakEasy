import openai


class GPT:
    def __init__(self, init_message):
        with open("API_KEY.txt") as mytxt:
            for line in mytxt:
                self.API_KEY = line
                openai.api_key = line
                self.messages = init_message  # = [ {"role": "system", "content": "You are a intelligent assistant."} ]

    def makeCall(self, model, message):
        if message:
            self.messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.chat.completions.create(
                model=model, messages=self.messages
            )
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            self.messages.append({"role": "assistant", "content": reply})
            return reply
        else:
            Exception("Please put in a message")


def hi():
    g = GPT([{"role": "system", "content": "You are a intelligent assistant."}])
    while True:
        hello = input("User: ")
        g.makeCall("gpt-4", hello)

# hi()
