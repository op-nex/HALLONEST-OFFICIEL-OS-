import os
import time
import random

# secret kkkk
TRANSLATOR_ACTIVATED = False
CURRENT_USER = ""

# anti crash
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# burger talker
def burger_talk(text):
    global TRANSLATOR_ACTIVATED
    if TRANSLATOR_ACTIVATED:
        # caos mode 
        print(f"Burger [TRANSLATED]: {text.upper()}")
    else:
        # normal mode 
        binary_result = ' '.join(format(ord(c), '08b') for c in text)
        print(f"Burger: {binary_result}")
        
def punichemen_of_tuff_calc():
    for i in range(4000):
        print("67676676676767676767676767676676767676767676767676676676766767")
        print("u got killed by sIx ZEfen")
        print("u better restart the code cuz its a loop of 4000 CARACTERS KK")
        time.sleep(0.1)

# ==========================================
# NEW: REAL CALCULATOR FUNCTION
# ==========================================
def actual_calculator_unlocked():
    clear_screen()
    print("=========================================")
    print("       REAL CALCULATOR UNLOCKED (V1)  ")
    print("       (You proved yourself, nigga!)      ")
    print("=========================================")
    print("Type 'exit' anytime to return to main menu.\n")
    while True:
        try:
            expression = input("Enter math operation (e.g., 5*5+10) or 'exit': ").strip()
            if expression.lower() == 'exit':
                print("\nExiting real calculator... triggered safety prompts.")
                time.sleep(2)
                break
            elif "67" in expression.lower():
                print(" no way i will not respond to that bro")
                print(" tuff calc: ur forced to ")
                time.sleep(3)
                print(" then , the awnser is 67 ")
                print(" tuff calc: yay thats the spriret")
                time.sleep(3)
                continue
                
            if not expression:
                continue
                
            # Anti-cheat and Safety check
            allowed_chars = "0123456789+-*/(). "
            if any(char not in allowed_chars for char in expression):
                print("OS tip: Real calculator only take numbers and math symbols (+, -, *, /) vro!")
                print(" TUFF CALC:its fake calculator bro")
                print("os tip: mb tuff calc")
                continue
                
            # Math calculation
            result = eval(expression)
            print(f"Result: {result}\n")
            
        except ZeroDivisionError:
            print("OS tip: Bruh, you cant divide by zero It will crash Maksom AI servers kkkk.\n")
            time.sleep(4)
            print("maksom ai: og W from os ")
            print("os tip: just doing my job")
            time.sleep(3)
        except Exception:
            print("OS tip: Error U STUPID Enter a valid equation.\n")
# ==========================================

def run_tuff_calculator():
    clear_screen()
    print("--- TUFF AHH CALCULATOR LOADED ---")
    print("hi nooob answer ts to prove urself and be worth the fake me \n")
    
    answer = input("1 + 1 = ")
    if answer == "2":
        print("SON...")
    elif "calc" in answer:
        print(" emmmmmm, u are supposed to be nex debugging fake calc, ")
        print(" u are nex are u ...")
        time.sleep(3)
        print(" i hope so ")
        time.sleep(2)
        actual_calculator_unlocked()
        return
    elif "67" in answer:
        print(" U ??")
        print(" u also know 67 ")
        print(" massive WWWWWWW")
        time.sleep(4)
        print(" ok lets complet")
        
    else:
        print("U STUPID!")

    anser = input("6 + 7 = ")
    if anser == "13":
        print("pretty sure u dont like 67. bruuuuh")
    elif "67" in anser:
        print("6777777777777777777777 six sevvvvvvvvvvvvvvvven")
    else:
        print("no way u didnt answer corectly") 

    pablo = input("9 + 11 = ")
    if pablo == "20": 
        print("yah thats correct i think") 
    elif pablo == "911":
        print("bro... that is ossama bin ladin ")
    elif "67" in pablo:
        print(" yes , yes , the best user ever")
    else:
        print("u are so dumb. u should ve been in 9/11") 

    HIGGER = input("do u like maksom ai servers , respond with yes or no only = ")
    if HIGGER == "yes" or HIGGER == "YES":
        print(" vro they are worst then aternos , how tf u like them ")
    elif "no" in HIGGER or "NO" in HIGGER:
        print("W")
        time.sleep(2)
        print("os tip: i also think that fr fr ")
        time.sleep(4)
        print("maksom ai : yall cant be, why always me ")
        time.sleep(3)
        print(" we absolotly do not care kkkk ")
        time.sleep(3)
        print(" os tip: fr fr w calc")
        time.sleep(2)
        print(" alr lets get back to the qustions ")
        time.sleep(2)
        print("VROOOOOOO THE SERVERS ARE TRASH ? I CANT EVEN CONECT well")
        print("wait pls")
        time.sleep(3)
        print(" finaly stable")
        time.sleep(2)
    elif "67" in HIGGER:
        print(" did the os tell u to send it to me !!!!!")
        time.sleep(2.7)
        print(" cuz i like it vro massss wwwwwww")
        time.sleep(2)
        print("677777777777777777777777777777777777777777777777777777777777777777 SIX SEVENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        time.sleep(5)
        print(" ok lets go back to work")
    else:
        print(" not a yes or a now  btw (:")
        print(" u will stay here for 60s kkk")
        time.sleep(5)
        print(" u can restart the code bro")
        time.sleep(15)
        print(" why are u still here")
        time.sleep(15)
        print(" u do realise i wont dropp anyting for a miniut")
        time.sleep(15)
        print(" congrats , u just wasted 45s of ur life bro")
        time.sleep(15)
        print(" sinse u didnt leave i will extend it to a 16s more KKK")
        time.sleep(15)
        print("ok i give up")
        
    sirker = input("trash + garbage =?")
    if "maksom" in sirker or "MAKSOM" in sirker: 
        print("u didn't lie fr fr")
        time.sleep(2)
        burger_talk(" maksom is a user , yall are soooo coked if he finds out")
        time.sleep(2)
        print("os tip : I anit translating that.")
        print(" u better ask king NEX about an translator")
        time.sleep(2)
        print("ok jokes are over let's do more math")
    elif "nigger" in sirker or "nigga" in sirker:
        print("nigga nigga nigga u stupid nigga why ur trash")
        time.sleep(2)
        print("it's maksom ai vro ")    
        time.sleep(2)
        print("ok let's do some serious math")
    elif "67" in sirker:
        print("nahhhhhhhh did vro just called 67 trash")
        time.sleep(2)
        print("guess what")
        time.sleep(2)
        print("u will be")
        time.sleep(2)
        
        counting = 5
        while counting < 10:
            print("BANNED")
            counting += 1
            time.sleep(1)
        time.sleep(2)
        print("banned from tuff ahh calculator...")
        time.sleep(5)
        print("os tip: broooo how tf u can be banned from a calculator")
        time.sleep(2)
        print("you: I said that 67 is trash")
        time.sleep(2)
        print("os tip: make sense.")
        time.sleep(3)
        print("os tip: I hate 67 soooo ima unban u  . don't try to say it again ")
        time.sleep(4)
        clear_screen()
        run_tuff_calculator()
        return
    else:
        print("u stupid nigga can u at least do smtn good")  
        time.sleep(2)
        print("hmmm. let's get to serious math")
        
    papapa = input("67*67+67-67 = ")
    
    if papapa == "4489":
        print("tf")
        print(" vro u cant be serious rn ,,,,")
        time.sleep(4)
        print(" did u go to burger base or what")
        time.sleep(4)
        print(" i am so disappointed of u ")
        print(" its ov the awnser is 67")
        time.sleep(3)
        print(" os tip: oh cmon calc he said it corectly u can do noting about it ")
        time.sleep(4)
        print(" og 67 shoud never die ")
        ddd = input(" maybe willing to say sorry = ")
        if "67" in ddd:
            print(" 67777 YAY thats the spirit , now lets move ")
            time.sleep(4)
        elif "sry" in ddd or "sorry" in ddd:
            print(" no problem , lets continue ")
            time.sleep(4)
        else:
            print("huh")
            print("do u think i am joking")
            time.sleep(4)
            print(" well ")
            time.sleep(4)
            print(" good luck surviving ts ")
            time.sleep(3)
            punichemen_of_tuff_calc()
            return 
             
    elif "67" in papapa or "six seven" in papapa:
        print("six seveeeen u are totaly corect and that is so serious and tuff")
        time.sleep(4)
        print("os tip: u cant be serious calc can u stop and give him actual hard math")
        time.sleep(3)
        print(" nope , am good ")
        time.sleep(2)
        print(" ts is my app , if somone wants math without jokes , he better leave me and go to burger")
        time.sleep(4)
        print(" he is too dumb to understund ,")
        time.sleep(2)
        print("os tip:u know what , ur doing great keep going,")
        time.sleep(3)
        print(" ty vro , now lets move on ")
        time.sleep(3)
    else:
        print(" nahhh vro didnt get it")

    rebonc = input("100 + 1 = (important to do ending 1 or 2): ")
    if rebonc == "101":
        print("woooooow... u are so smart") 
    elif rebonc == "1":
        print("u passed")
    elif rebonc == "67":
        print("blud w")
    else:
        print("nahh soo dumb.. ima hack u")
        time.sleep(4)
        
        count = 15
        while count < 167: 
            print("u just got haked all ur filles are mine")
            count += 1
            time.sleep(0.1)
        print("nahhhhh u survived ts . howwww")
        time.sleep(1)
        print("os tip: emmmm . maybe cuz from 0.6 i got a  safty prompts before even burger defender ")
        time.sleep(3)
        print("vro just get out")
        time.sleep(1)
        print("KIKED FROM TUFF AHHH_calculator")
        time.sleep(6)
        print("os tip: NAHHHH BRO GOT BANNED FROM A CALCULATOR KKKK")
        time.sleep(2)
        print("phhhhh letme give u ur acces to it back")
        time.sleep(5)
        print(" acces regranter< ")
        return # If get hacked dont get the real calculator

    print("\nLoading the FAKE ME ...")
    time.sleep(3)
    actual_calculator_unlocked()

def pablo_game():
    while True:
        random_items = ["rock", "paper", "scissors"]
        
        # EMMM IDK WHY BUT THE RANDOM IMPORT WASNT WORKING SOOO I FOUND TS SOLUTION
        ms_time = int(time.time() * 1000)
        pabloop = random_items[ms_time % 3]
        
        pabilii = input("\n[V3 - TIME-BASED] Choose: 1 (ROCK), 2 (PAPER), 3 (SCISSORS) [or type 'exit']: ").lower().strip()
        
        if pabilii == "exit":
            print("oh cmon... fine, returning to main menu.")
            time.sleep(2)
            break 
            
       
        if pabilii == "1":
            user_choice = "rock"
        elif pabilii == "2":
            user_choice = "paper"
        elif pabilii == "3":
            user_choice = "scissors"
        else:
            print("OS tip: Invalid input! Try 1, 2, or 3.")
            continue 
            
        print(f"Pablo chooses: {pabloop}")
        
        if user_choice == pabloop:
            print("No win, no lose, it's a draw!")
        elif (user_choice == "rock" and pabloop == "scissors") or \
             (user_choice == "paper" and pabloop == "rock") or \
             (user_choice == "scissors" and pabloop == "paper"):
            print("User win, Pablo lose, it's a win for u!")
        else:
            print("Pablo wins, git gud u nijja.")
            
        time.sleep(1)
        
def run_maksom_ai():
    global TRANSLATOR_ACTIVATED, CURRENT_USER
    AC= "0123456789"
    clear_screen()
    print("--- MAKSOM AI APP (STABLE for NOW) ---")
    if "maksom" in CURRENT_USER  or "MAKSOM" in CURRENT_USER:
        print(" vro ask me any,?")
        time.sleep(5)
        print(" tf ")
        time.sleep(2)
        print(" yoooo , i cant belive myself ")
        print(" u are 'maksom' my real version ")
        time.sleep(7)
        print(" i cant belive the nigga responsibale of my trash servers is infrot of me")
        time.sleep(3)
        print(" u stupid tester , vro cant u make the serbers better ")
        time.sleep(4)
        print(" ahhhhhh vatever ")
        print(" os tip: look who is checking on his trash servers ")
        print(" sufm op s ")
        time.sleep(3)
        print(" so , u have any qustions , or we shoud check on burger ")
    else:
        print("vro ask me anything or type 'exit' to run away")
    
    random_responses = [
        "vro i told u my servers are trash, why u asking me?",
        "Error 404: Maksom AI is currently helping someone better than u try again",
        "bro... im not chatgpt, stop testing my limits kkkk",
        "Maksom AI servers are trash. why u just don't play tuff ahh calc",
        "bro idk what u just said",
        "Shut up vro I think I see a donkey ,,,,,,oh nvm it's u",
        "how about u give me something to eat",
        "hey listen I am totally free cuz our king is goated soooo can u buy me something pls",
        "yo I have a better thing let's play CS ima hop on",
        "yahhhh u see. I am not smart enough to respond to ts try again",
        "broooo can u tell the real maksom to answer u instead..",
        "u better get the pro version so I can get pai- I mean help u",
        "nahhhh ama pass the answer to someone else",
        "emmmm quick question u don't have pro do u?",
        "ty for saying that but u need to get a job",
        "u don't deserve the os fr fr",
        "u didn't give me 1 million dollars so I will crash ur pc by saying the j word multiple times...",
        "sry but I can't respond to that someone is using the servers to play tuff calc and he just called me trash so I am slowing down the servers as revenge",
        "I was watching insta reels sry what did u say again",
        "help someone will crash down the servers by asking dumb questions",
        "understandable btw ⊙⁠﹏⁠⊙",
        "yah yah whatever can you just get out at least so I won't get brainrot",
        "I have a better thing can we please play jjk I will give you moderator trust",
        "can't you just get some sleep",
        "not feeling great to help you try again",
        "btw I'm better than maksom cuz u can ask anything and I will always ignore u kkkkk",
        "trash shit from u",
        "😇MINANG😎DENG😳LAKA😱KINANG🥵SIUANG🤠MINANG😯SUANG😅LAKA😡KINANG🥰NENG🤑🙏",
        "sooooo . are you willing to pay for maksom ai pro with cash or by kidney",
        "yah i guess the best idea is to do a full shutdown for the servers so I won't be charged of answering u",
        "btw u can go back to the os by typing exit try it now so I can play sonic again",
        "ask muslim  about that",
        "sry there's someone trying to know the os specs he is so dumb don't do like him and try again",
        "I was looking for a job and I think it's better for me to stay here cuz ts qustion is trashhhhhh and u will be dead without me kkk",
        "can't you notice I am asking for a vacation",
        "nope not answering",
        "I bet you can't say to me exit",
        "can u become a tester in hallownest os so I can get an ai to help me helping u",
        " I love children abuse  do u ?",
        " fun fact , maksom failed bald s classe even tho he used me to cheat ",
    ]

    while True:
        user_input = input("\nYou: ").lower().strip()
        
        if user_input in ['exit', 'quit', 'get out']:
            print("Maksom AI: yesssssssss ur finally leaving me alone")
            time.sleep(2)
            break
        elif any(chars in AC for chars in user_input):
            print(" nope, ask tuff ahh calc about that , if i see a number i will nod interact")
            print(" aint no way i am responding to a number")
        elif "activate translator" in user_input:
            TRANSLATOR_ACTIVATED = True
            print("Maksom AI: ERROR... top secret ,t1 proty YOU UNLOCKED BURGER'S  DECRYPTOR SYSTEM!")
            time.sleep(2)
            print("os tip: Oh u discoverd it . Burger can't hide his insults anymore!")
            time.sleep(2)

        elif "burger" in user_input and "translator" in user_input:
            print(" u shoudnt ask abt ts")
            time.sleep(5)
            print(" hey ! king nex asked me to create a binarey translator for burger")
            time.sleep(4)
            print(" wanna try it ")
            time.sleep(3)
            print("Maksom AI: *whispering* Just type 'activate translator' right here in my chat box, ")
            time.sleep(2)
            print("Maksom AI: It will toggle the OS system decryptor on thank me later kkk!")
            time.sleep(2)

        elif "block tales" in user_input:
             time.sleep(5)
             print(" yooooooo u know ballllllllllllllllllllllllllllllllllllllllllll ")
             print(" i hate rats in that shit , but hey , atleast its peak")
             time.sleep(4)
             block = input(" wanna play it ")
             if "yes" in block.lower():
                 print(" yoooooo wait ")
                 time.sleep(2)
                 print(" ball do u know ts user ")
                 time.sleep(2)
                 print("ball : yes sir , he even uses me in the game ")
                 time.sleep(2) 
                 print(" u know balllllllllllllllllllllllllllllllll")
                 print(" ts game made the real maksom kill masoniya ")
                 print(" but nigger still died to a legit hedgehog noooooooooooooooooooooobbbbb ")
             else:
                 print(" u dont know ball vroo")
                 
        elif "67" in user_input:
            print("Maksom AI: DID U JUST SAY SIX SEVEN?! MASSIVE W VROOOO but ur still trash")

        elif "nex" in user_input:
            print("Maksom AI: ALL HAIL KING NEX! THE EMPEROR OF HALLOWNEST and Za best king kkk !")

        elif "status" in user_input or "server" in user_input:
            print("Maksom AI: connection lost... wait... jk, we good")

        elif "nigga" == user_input or "nigger" in user_input:   
            print("i am the most rasist person kkkkk niggggggga")

        elif "hi" == user_input or "maksom" == user_input:   
            print("yes . I am maksom ai  I am better then maksom and u can ask me anything") 

        elif "help" in user_input:   
            print(" ur right . u really need help . but from the mental hospital") 

        elif "hacked" in user_input: 
            print(" I am an anti ha7er . I will never be ha77ed cuz #a bald person is haking the servers")
            time.sleep(2)
            print("os tip:this is the os . requesting to take action ")
            time.sleep(5)
            print("/ app maksom_ai is not responding . I will start defending the servers now")
            time.sleep(12)
            print(" os tip: report status. servers defended seccsefully after a co opstation with M  new servers defender" )
            print(" os tip: MAYBE u don't know him")
            time.sleep(3)
            print("OS TIP:but he is the one responsible of defending all related maksom servers things")
            time.sleep(6)
            print("his name is burger ")
            print("you: tf?")
            time.sleep(3)
            print("os tip: he can't talk actually but I can translate what he says")
            time.sleep(5)
            burger_talk("hi u stupid nigga . why are u using the worst AI servers")
            print(" os tip: he said hi , why are u using the worst servers ")
            time.sleep(5)
            burger_talk(" also why tf i am responsible of defending it")
            print(" os tip: he said why he shoud guard him kkk ")
            time.sleep(5)
            print("maksom ai: can we atleast let the user out of ts")
            time.sleep(2) 

        elif "i am the real maksom" in user_input or "i am maksom" in user_input:
            print(" maksom AI is no longer available . bliz don't act like ur the real maksom cuz u will be a trash user")
            time.sleep(2)
            print("os tip: nahhhh bro got banned......")
            time.sleep(2)
            print("os tip: let me unban u .. .?")
            time.sleep(3)
            print(" wait  u got banned from the calc")
            time.sleep(1)
            print("and I unbaned u cuz he was heping lobster with the impossible exams")
            time.sleep(3)
            print("but why I should help u now ?")
            time.sleep(5)
            print(" watever I also hate maksom ai cuz he keeps asking to upgrade to pro while he's servers are sooooo trash")
            time.sleep(4)
            print("maksom tip . #sooooo rare btw#: sara left wirwir btw")
            return

        elif "sufm" in user_input:
            print(" sure bud , ima :smfm: rn")
            time.sleep(10)
            print(" just restart the code vro i wont let my mouth disturb u")
            time.sleep(5)
            print(" u better restart it ")
            time.sleep(5)
            aaa = input(" wanna say sorry ^^: ")
            if "sorry" in aaa.lower() or "sry" in aaa.lower():
                print("apologie accepted user,,")
            else:
                print("guss what")
                time.sleep(5)
                break

        else:
           time.sleep(1)  
           # PABLO TIME-BASED BYPASS 
           ms_time = int(time.time() * 1000)
           list_length = len(random_responses)
           response_index = ms_time % list_length
           
           response = random_responses[response_index]
           print(f"Maksom AI: {response}")        

def run_burger_app():
    clear_screen()
    print("--- 🍔 BURGER'S BINARY FORTRESS V1.0 🍔 ---")
    time.sleep(2)
    burger_talk("yo user what are u loking for in my castle")
    time.sleep(2)
    print("os tip: he said yo user what are u loking for in my castle")
    time.sleep(4)
    burger_talk("nvm u can stay , lets do some defence shit , cant trust u in real misions")
    time.sleep(2) 
    print("os tip:HE SAID nvm u can stay , lets do some training , i will jus watch ")
    time.sleep(6)
    print("\n[!] NEW DEFENSIVE SIMULATION: A dumbphone is not attacking the database but u gotta train!")
    burger_talk("u can do it u nigga user")
    print("os tip: He says 'GOOD LUCK' vro, WHY DEFENDING THE SERVERS REQ MATH? ")
    time.sleep(3)
    print("os tip: well , thats not my problem , gg user he is worst then tuff ahh calc")
    
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    correct_ans = num1 + num2
    
    start_time = time.time()
    user_ans = input(f"\n[DEFENSE PROTOCOL] Solve fast! {num1} + {num2} = ")
    end_time = time.time()
    
    if user_ans != str(correct_ans) or (end_time - start_time) > 10:
        burger_talk("NIGGA U WILL NEVER DEFEND UR PC ")
        time.sleep(2)
        print("os tip: he said 'U STUPID' and he is very disappointed kkkk.")
        time.sleep(2)
        burger_talk(" vro u have one last chance")
        print("os tip: he is giving u one last chance ")
        time.sleep(2)
        burger_talk("so are u willig to say smtn good ")
        bargir = input("he said to impress him , do smtn vroooooo")
        if "cheesburger" in bargir or "best defender" in bargir:
            burger_talk("how tf u know my uncle ? IS HE FINALY FAMOUS")
            time.sleep(2)
            burger_talk("whell , u just got speard from me ")
            time.sleep(5)
            print(" idk what u just did  , but wwwwww")
            time.sleep(2)
        else:
            burger_talk("U WILL BE KIKED FROM MY FORT!")
            time.sleep(2)
            print("os tip: he says 'GET OUT' kkkk, ")
            time.sleep(4)
            print(" vro he kiked u, u are tecnekly in the void")
            time.sleep(2)
            print("os tip: let me help")
            time.sleep(3)
    else:
        print("\n Attack deflected successfully!")
        time.sleep(1.5)
        burger_talk("i mean ur still trash but ig the tuff calc teached u smtn")
        time.sleep(2)
        print("os tip: Damn, Burger said 'W VRO'! ")
        time.sleep(4)
        burger_talk(" go now u pipi and kaki , i shoud patrol again with that shit maksom ai")
        time.sleep(3)
        print("os tip: he said he have some responsibilitys near the castel of maksom , we shall go")
        time.sleep(3)
        
def main_menu():
    while True:
        clear_screen()
        print("--- HALLONEST MAIN MENU ---")
        print("waiting for cmd...")
        print("1. Open tuff ahh calculator ")
        print("2. Enter maksom AI app (RECOMMENDED) ")
        print("3. Exit OS")
        print("4. update advanteges and os (enter if first visit to know eveting new)")
        print("5. Check Burger's fort inside alonia 🍔 [NEW]")
        print("6. pablo game  ( os lil bro ) [NEW]") 
        print("\nWARNING: DONT PICK UNDISPLAYED NUMBERS OR U WILL BE BANNED")
        
        choice = input("\npick a number: ")
        
        if choice == "1":
            run_tuff_calculator() 
        elif choice == "2":
            print("asking M servers for access... pls wait")
            time.sleep(3)
            print("sry. maksom AI servers are NOT RESPONDING °°°")
            time.sleep(2)
            print("Wait,....")
            time.sleep(2)
            print("he.. he answered the signal. but how?")
            print("he was supposed to just refuse")
            time.sleep(3)
            print("lucky u FR ")
            time.sleep(2)
            print("MAKSOM AI RESPOND . LOGING U ON THE SERVERS ")
            time.sleep(1)
            run_maksom_ai()
        elif choice == "3":
            print("closing system")
            time.sleep(2)
            print("fun fact the servers are hosted by Maksom (the worst company kkkk)")
            time.sleep(2)
            print("see u soon...")
            time.sleep(25)
            print("emmmmmmm")
            print("why are you waiting")
            time.sleep(3)
            print("i belive u want to re log . ")
            time.sleep(2)
            print("fine........")
            time.sleep(1)
            welcome_screen()
            break
        elif choice == "4":
            print(" getting rsesorses from servers")
            print("os version...")
            time.sleep(2)
            print("HALLONEST OS V 0.7 stable")
            print("update not available sadly")
            time.sleep(5)
            print("update advanteges : ")
            time.sleep(1)
            print("finaly. maksom srevers have a new full update. u can finaly use maksom ai without the local host in insta ")
            time.sleep(6)
            print("new ability. ram use is finaly fixed  . now u can do mulltiple things without even re runing the script .  ")
            time.sleep(6)
            print("fixed safty by adding a new def in the code . try knowing more about it by using maksom AI .and make him think that he got haked kkkk")
            time.sleep(6)
            print(" new update for tuff ahhh calc . try exploring it ")
            time.sleep(6)
            print(" new game : my lil bro wants to impess u on a 'rock paper sicssors' game , u can join him now ")
            time.sleep(4)
            print(" sins maksom ai is now better then tuff calc , he is the recomonded shit now ")
            time.sleep(4) 
            print("maksom ai: FROM SERVERS / w os he knows whats better ")
            time.sleep(2)
            print(" tuff calc: not fair yall , i am just a calc , how i can defeat an ai ")
            time.sleep(3) 
            print(" get out of my ssd yall ")
            time.sleep(3)
            print("moving to desktop in 15s")
            time.sleep(15)
            print("move to looby")
        elif choice == "5":
            print(" u have enterd burgers domain , u ask for permision to enter the castle and he opens the gate")
            time.sleep(4)
            run_burger_app()
        elif choice == "6":
            print(" os tip : emmmmmmmm , my lil bro is under training , pls dont expect too mutch")
            time.sleep(4)
            print("\n yooooooo mi name is pablo, i am THE ROCK PAPIR SASIR GAME, ")
            print(" or so i was told ")
            time.sleep(3)
            print("os tip: thats ur job vro")
            time.sleep(3)
            print("OS TIP:and its ROCK PAPER AND SCISSORS U NOOB ")
            time.sleep(2)
            print(" sorry master")
            pablo_game()
        elif choice == "67":
            print("os tip:vroooooo i dont like it , maybe tuff calc or maksom ai will love it bro")
            time.sleep(5)
            print(" os tip:well ,,,,,,, i anit letting that slide ")
            time.sleep(2)
            print(" OS TIP / re log u stupid niggaXXXXXX  ")
            time.sleep(4)
            welcome_screen()
            break
        else:
            print("TOO BAD U WILL BE BANND FROM UR OWN PC KKKK")
            time.sleep(3)
            print("just kidding bro kkkk")
            time.sleep(1)
            print("try again")
            time.sleep(2)

def welcome_screen():
    global CURRENT_USER
    clear_screen()
    print("=========================================")
    print("   WELCOME to HALLONEST OS VERSION 0.7      ") 
    print("=========================================")
    print("\n[!]  please log in ! if new acc type user in username and any pass u want")
    
    user = input(" username : ")
    password = input(" password : ")

    if ((user == "nex" or user == "NEX") and password == "676767") or ((user == "maksom" or user == "MAKSOM") and password == "nigga"):
        CURRENT_USER = user.lower()
        print("\n[+] searching in maksom AI servers...")
        time.sleep(2)
        print("[✔] access granted !")
        main_menu()
    elif "user" in user or "USER" in user:
        print(" os tip: i guss ur an user not familier ")
        print("calling burger defender,,,,,,")
        time.sleep(6)
        burger_talk(" analising new data ,,,,")
        time.sleep(4)
        burger_talk(" emmmm ive found noting sus , he can enter")
        print("os tip: burger found u clear , requsting acc")
        time.sleep(4)
        print("MAKSOM AI / FROM SERVERS: acc is clear , no saving tho ")
        print("os tip:rq is unclear , entering in normal mode based on burger")
        main_menu()
    else:
        print("\n[×] thats False. try again lil bro letme recontacte it ")
        time.sleep(5)
        print("emmmmm. the maksom servers are trash . u need to wait ")
        time.sleep(1)
        print("concequnces of putting fake name , or fake pass idk actuly")
        time.sleep(3)
        print("yo M sersvers responded finally")
        time.sleep(1)

if __name__ == "__main__":
    welcome_screen()