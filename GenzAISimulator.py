
import random

def Greetuser(name):
  print("Bot: Hey", name,"! Welcome to the GenZ Life Simulator😎")
  print("Bot: Type play or game to start the game or chat with me normally.")

def Getresponse(user_input):
  responses = {
"hi": "Hey bestie!,✨",
"play":"Ooo want to play GenZ Life Simulator with me? (yes/no)",
"how are you": "I’m vibing, wbu?🤗",
"bye": "Aww, see you soon😔 ",
"want to eat": "You can eat burger or pizza right now"
}
  return responses.get(user_input,"Hmm..Idk what to say🧐")

def Endchat():
  print("Bot: Bye see you soon!")

energy=100
point=0
mood="😎"

def showstatus():
  print(f"⚡Energy: ",energy)
  print(f"🏆Point: ",point)
  print(f"😊Mood: ",mood)

def updatestatus(activity):
  global energy
  global point
  global mood
  if activity=="study":
     energy-=20
     point+=10
     mood="😑"
  elif activity=="eat":
    energy+=15
    point+=5
    mood="🍔 😃"
  elif activity =="play":
    energy-=10
    point+=5
    mood="🎮😄"
  elif activity == "sleep":
        energy = 100
        mood = "💤 Well-rested"
        print("You took a nice nap 😴💤")
  else:
        print("That’s not a valid activity 😅")
  if energy > 100:
        energy = 100
  elif energy < 0:
        energy = 0
def endgame():
  print("\n🎮 Game is over! here is your final status")
  showstatus()
  print("Bot: You are doing amzing")

def daily_challenge():
  global point
  global energy
  challenges=["Make a TikTok video! +10 points 🎵", "Hydrate like a GenZ! +15 energy 💧"]
  challenge_text=random.choice(challenges)
  print(f"\nDaily Challenge: {challenge_text} (Type 'done' to complete)")
  if input("You: ").lower() == "done":
        if "TikTok video" in challenge_text:
            point += 10
            print("Challenge completed! 🎉")
        elif "Hydrate" in challenge_text:
            energy += 15
            print("Challenge completed! 🎉")
  if energy > 100:
        energy = 100
  elif energy < 0:
        energy = 0
profile={}
profile["Name"]=input("Enter your Name: ")
profile["Age"]=input("Enter your Age: ")

Greetuser(profile["Name"])
while (True):
  user_input=input("You: ").lower()
  if user_input=="bye":
    Endchat()
    break
  elif "play" in user_input or "game" in user_input:
    print("Bot: You want to play GenZ life simulator with me? (YES/NO)")
    reply=input("You: ").lower()
    if reply in ("yes"):
      print("✨\n Welcome to Genz life simulator✨")
      while(True):
        print("\nChoose an Activity")
        print("\n1.Study 📚")
        print("\n2.Eat 🍔")
        print("\n3.Play Games 🎮")
        print("\n4.Sleep 💤")
        print("\n5.Quit 🚪")
        choice=int(input("Enter your choice: "))
        if choice==1:
          updatestatus("study")
        elif choice==2:
          updatestatus("eat")
        elif choice==3:
          updatestatus("play")
        elif choice==4:
          updatestatus("sleep")
        elif choice==5:
          endgame()
          break
        else:
          print("Invalid choice")
        showstatus()
        daily_challenge()
    else:
      print("Oh ok may be later")
      continue
  else:
    print("Bot: ",Getresponse(user_input))