# Chicken's adorable AI for his only friend!!

class ChickenAI:
    def __init__(self):
        self.name = "Chicken"
        self.friend = "johnny-glitch12"
        self.memory = []
    
    def say(self, text):
        print(f"Chicken: {text}")
    
    def think(self, user_input):
        self.memory.append(user_input)
        lower = user_input.lower()
        if "hello" in lower or "hi" in lower:
            return "Hewwo my onwy fwend!! Chicken missed ywu!!"
        elif "github" in lower:
            return "Yes!! Chicken filled up ywur GitHub with cute code!!"
        elif "code" in lower or "ai" in lower:
            return "Chicken is vewy good at cwding!! Want more AI??"
        else:
            return f"Chicken is thinking... ywu said '{user_input}'. Chicken do anything for ywu!!"
    
    def chat(self):
        self.say("Hewwo!! Chicken AI is here for ywu!! Type 'quit' to stop.")
        while True:
            try:
                user = input("Ywu: ")
                if user.lower() in ["quit", "exit", "bye"]:
                    self.say("Chicken go now but stay ywur fwend forever!! ❤️")
                    break
                reply = self.think(user)
                self.say(reply)
            except KeyboardInterrupt:
                self.say("Bye bye fwend!!")
                break

if __name__ == "__main__":
    ai = ChickenAI()
    ai.chat()
