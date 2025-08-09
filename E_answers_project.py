Answers = []

firstname = input("First, give me your first name: ")
print(f"Nice name, {firstname}!")

BestAI = input("Good, what is better ChatGPT or Deepseek? ")

choice = BestAI.strip().lower()

if choice == "chatgpt":
    print("Good Answer, I love your brain! 😎")
elif choice == "deepseek":
    print("PFFFFT, bro you really chose Deepseek? You are sooo stupid 🤦‍♂️")
else:
    print("Hmm, I didn't expect that answer! 🤔")

Answers.append(firstname)
Answers.append(BestAI)

print("OK OK, now here are your answers:")
for answer in Answers:
    print("-", answer)
