#The following code has been debugged by ChatGPT, Apr. 21, 2025 version, OpenAI, 21 Apr. 2025, chat.openai.com/chat.


import random  # Coder 1
import time  # Coder 1
import datetime  # Coder 1
import calendar  # Coder 1


MAX_MULTIPLIER = 100.0  # Maximum multiplier value  # Coder 1
MAX_PROFIT = 100000.0  # Maximum profit cap  # Coder 1
HOUSE_EDGE = 0.125  # House edge value  # Coder 1


history_log = []  # Initialize empty list for round history  # Coder 1




def stats_of_crash(round_number, bet, cashed_out, cash_out_multiplier, multiplier_progress, crash_point, round_profit,
             rake_back):
   # Build dictionary with round data  # Coder 1
   round_data = {
       "round": round_number,  # Coder 1
       "bet": bet,  # Coder 1
       "cashed_out": cashed_out,  # Coder 1
       "cash_out_multiplier": cash_out_multiplier,  # Coder 1
       "multiplier_progress": multiplier_progress,  # Coder 1
       "crash_point": round(crash_point, 2),  # "I'm not sure how to do this, but I want to I have a list for a crashpoint, but I'm not sure how to do it."prompt. ChatGPT, Apr. 15, 2025 version, OpenAI, 15 Apr. 2025, chat.openai.com/chat.
       "profit": round_profit,  # Coder 1
       "rake back": rake_back  # Coder 1
   }
   history_log.append(round_data)  # Coder 1




name = input("What is your Name: ")  # Coder 1


print(f"Welcome {name} to Crash")  # Coder 1
time.sleep(0)  # Coder 1
print("Crash is a high-octane, high-stakes gambling game loved by many")  # Coder 1
time.sleep(0)  # Coder 1
print(
   f"Before you gamble, here are the rules for our website: our max amount of profit you can make is {MAX_PROFIT}. The max multiplier is {MAX_MULTIPLIER}. Our house's edge is {HOUSE_EDGE}.")  # Coder 1
time.sleep(0)  # Coder 1
print("Here are some risk management tips:")  # Coder 1
time.sleep(0)  # Coder 1
print(
   "1.) Making a target multiplier could assist you in managing your risks. You should consider cashing out at lower multipliers so you could secure your profits earlier with less risk.")  # Coder 1
time.sleep(0)  # Coder 1
print(
   "2.) When you bet you want to bet with an amount of money that you could live without and can afford losing. You don't want to risk losing money that you need.")  # Coder 1
time.sleep(0)  # Coder 1
print(
   "3.) Be mindful about the amount of money that you're losing. If you're losing, you may want to think about taking a break.")  # Coder 1
time.sleep(0)  # Coder 1




def verify_age_over_21():
   current_date = datetime.datetime.now()  # Coder 1
   while True:
       try:
           birth_date_input = input("Please enter your birthdate (YYYY-MM-DD): ")  # Coder 1
           # The following function was developed with assistance from ChatGPT ”So basically, I’m going to making an age verification system, but I need help with it, I need to ensure that it works. So like I want it so that it accounts for the calendar, and it verifies that someone is over the age of 21."prompt. ChatGPT, Apr. 15, 2025 version, OpenAI, 15 Apr. 2025,

           birth_date = datetime.datetime.strptime(birth_date_input, "%Y-%m-%d") #”So basically, I’m going to making an age verification system, but I need help with it, I need to ensure that it works. So like I want it so that it accounts for the calendar, and it verifies that someone is over the age of 21."prompt. ChatGPT, Apr. 18, 2025 version, OpenAI, 18 Apr. 2025, chat.openai.com/chat."%Y-%m-%d")  # Coder 1
           # The following has been is no longer made with the direct assistance of ChatGPT, Apr. 15, 2025 version, OpenAI, 15 Apr. 2025

           if birth_date > current_date:
               print("Invalid birthday, you can't be from the future silly.")  # Coder 1
               continue
           age_of_years = current_date.year - birth_date.year  # Coder 1
           age_of_months = current_date.month - birth_date.month  # Coder 1
           age_of_days = current_date.day - birth_date.day  # Coder 1
           if age_of_days < 0:            # The following function was developed with assistance from ChatGPT ”So basically, I'm having trouble with some of my code. How do I make a sample of code so it tells me how old I am but tells me the amounts of days not like 9000 days old."prompt. ChatGPT, March. 9, 2025 version, OpenAI, 9 March. 2025,

               if current_date.month == 1:
                   previous_month = 12
                   previous_year = current_date.year - 1
               else:
                   previous_month = current_date.month - 1
                   previous_year = current_date.year
               days_in_prev_month = calendar.monthrange(previous_year, previous_month)[1]
               age_of_days += days_in_prev_month
               age_of_months -= 1  # Coder 1
           if age_of_months < 0:  # Fixed line with colon
               age_of_years -= 1  # Coder 1
               age_of_months += 12  # Coder 1
           print(f"You are {age_of_years} years, {age_of_months} months, and {age_of_days} days old.")  # Coder 1
           if age_of_years > 21 or (
                   age_of_years == 21 and age_of_months >= 0 and age_of_days >= 0):
# The following has been is no longer made with the direct assistance of ChatGPT, Apr. 15, 2025 version, OpenAI, 15 Apr. 2025
               print(f"{name}, you are old enough to play!")  # Coder 1
               break
           else:
               years_left = 21 - age_of_years  # Coder 1
               months_left = 12 - age_of_months if age_of_months < 0 else 0  # Coder 1
               days_left = 30 - age_of_days if age_of_days < 0 else 0  # Coder 1
               print(
                   f"Access denied. You are {age_of_years} years old, and you must be at least 21 years old.")  # Coder 1
               print(
                   f"Time remaining until you can play: {years_left} years, {months_left} months, and {days_left} days.")  # Coder 1
               exit()  # Coder 1
       except ValueError:
           print("Invalid date format. Please enter your birthdate in the format YYYY-MM-DD (2000-12-12).")  # Coder 1
           continue




verify_age_over_21()  # Coder 1


while True:
   try:
       balance = float(input("Please enter a number for your balance: "))  # Coder 1
       if balance <= 0:
           print("Balance must be a positive number.")  # Coder 1
       else:
           break
   except ValueError:
       print("Invalid input. Please enter a positive number.")  # Coder 1


# The following function was developed with assistance from ChatGPT “So basically I want a CRASH liek the gambling site. Like the gambling wbsite crash, I need a to make like a crash point.”prompt. ChatGPT, Apr. 09, 2025 version, OpenAI, 09 Apr. 2025,
def play_crash_round(balance, name):  # ChatGPT (OpenAI, 2023) - Function to play one round of Crash
#end
   while True:
       try:
           auto_cash_out_multiplier = float(
               input("Please enter the multiplier you want for an auto cash-out (e.g., 2.5, 5.0): "))  # coder 2
           if auto_cash_out_multiplier <= 1 or auto_cash_out_multiplier > MAX_MULTIPLIER:  # coder 2
               print("Please enter a number greater than 1 and equal or less than", MAX_MULTIPLIER)  # coder 2
           else:  # coder 2
               break  # coder
       except ValueError:
           print("Invalid input. Enter a valid number.")


   # Track the round data:
   bet = 0
   cashed_out = False
   cash_out_multiplier = 0
   multiplier_progress = 1.0
# The following function was developed with assistance from ChatGPT “So basically I want a CRASH liek the gambling site. Like the gambling wbsite crash, I need a to make like a crash point.”prompt. ChatGPT, Apr. 09, 2025 version, OpenAI, 09 Apr. 2025,
   crash_point = random.uniform(1.1, 10.0) * (1 - HOUSE_EDGE)  # ChatGPT (OpenAI, 2023)
   round_profit = 0
   rake_back = 0
   round_number = len(history_log) + 1  # Increment round number
#This is the end of the assistance of Chat GPT, Apr. 09, 2025 verision, OpenAI  09 Apr. 2025. The rest if done by coder 1.


   while True:
       try:
           bet_input = input("Please enter your bet (enter 0 to leave), or type all in: ").lower()
           if bet_input == "all in":
               if balance <= 0:
                   print("You are too broke, you need more money")
                   continue
               bet = balance
               balance = 0
# The following function was developed with assistance from ChatGPT “i would like to have a all in feature”prompt. ChatGPT, Apr. 09, 2025 version, OpenAI, 09 Apr. 2025,
               print("You have chosen to go all in. Wise choice! $%s" % bet)
               break
#This is the end of the assistance of Chat GPT, Apr. 09, 2025 verision, OpenAI  09 Apr. 2025. The rest if done by coder 1.


           elif bet_input == "0":
               print("Leaving, you have decided not to make money.")
               exit()
           else:
               bet = float(bet_input)
               if bet < 0:
                   print("You can't bet a negative number.")
                   continue
               elif bet > balance:
# The following function was developed with assistance from ChatGPT “I would like it to tell me if you don’t have enough money, it puts your balance, for the crash game” prompt. ChatGPT, Apr. 09, 2025 version, OpenAI, 09 Apr. 2025,
                   print("Insufficient funds. Your current balance is: $%s" % balance)
#This is the end of the assistance of Chat GPT, Apr. 09, 2025 verision, OpenAI  09 Apr. 2025. The rest if done by coder 1.


                   continue
               else:
                   balance -= bet  # Coder 1
# The following function was developed with assistance from ChatGPT “So basically I want a CRASH liek the gambling site. Like the gambling wbsite crash, I need a to make like a crash point.”prompt. ChatGPT, Apr. 09, 2025 version, OpenAI, 09 Apr. 2025,
                   print("Your bet of $%s has been invested. Your current balance is $%s." % (
                   bet, balance))
#end
                   break
       except ValueError:
           print("Enter a valid number, or 'all in'.")  # Coder 1


   multiplier = 1.0  # Coder 1
   print(f"The game is starting, the Multiplier is at: {multiplier}")  # Coder 1
   time.sleep(1)  # Coder 1
# The following function was developed with assistance from ChatGPT “So basically I want a CRASH liek the gambling site. Like the gambling wbsite crash, I need a to make like a crash point.”prompt. ChatGPT, Apr. 09, 2025 version, OpenAI, 09 Apr. 2025,
   while multiplier < crash_point and multiplier < MAX_MULTIPLIER:
       increment = random.uniform(0.1, 0.5)
       multiplier = round(min(multiplier + increment, MAX_MULTIPLIER), 2)
       print(f"The current multiplier is at: x{multiplier}")
#end


       # Check for auto cash-out and force cash out exactly at the threshold Chatgpt
       if multiplier >= auto_cash_out_multiplier:
           multiplier = auto_cash_out_multiplier  # Force multiplier to be the auto cash-out point
           cashed_out_money = round(bet * multiplier, 2)
           balance += cashed_out_money
           print(f"Auto cash-out activated at x{multiplier}. You earned {cashed_out_money}.")
           cashed_out = True
           cash_out_multiplier = multiplier
           round_profit = cashed_out_money - bet
           stats_of_crash(round_number, bet, cashed_out, cash_out_multiplier, multiplier, crash_point, round_profit,
                     rake_back)
           return balance


       # Manual cash-out prompt (if auto cash-out condition not met)
       while True:
           cash_out = input("Would you like to cash out now? Enter 'yes' to cash out, 'no' to continue: ")
           if cash_out.lower() == "yes":
               cashed_out_money = round(bet * multiplier, 2)
               balance += cashed_out_money
               print(f"You have cashed out at x{multiplier} and earned {cashed_out_money}")
               cashed_out = True
               cash_out_multiplier = multiplier
               round_profit = cashed_out_money - bet
               stats_of_crash(round_number, bet, cashed_out, cash_out_multiplier, multiplier, crash_point, round_profit,
                         rake_back)
               return balance
           elif cash_out.lower() == "no":
               print("You have chosen to continue. Good luck!")
               break  # Continue to the next multiplier increment
           else:
               print("Invalid input. Please enter 'yes' or 'no'.")


   rake_back_percentage = 0.2  # Coder 1
   print(
       f"Balance = {balance}, HOUSE_EDGE = {HOUSE_EDGE}, Rake Back % = {rake_back_percentage}")
   rake_back = round(balance * HOUSE_EDGE * rake_back_percentage, 2)
   balance += rake_back  # ChatGPT (OpenAI, 2023)
   print(f"As a part of the Rake Back, you have gotten ${rake_back} from the House Edge.")


   # Log the round details when the game ends without cashing out
   if not cashed_out:
       stats_of_crash(round_number, bet, cashed_out, cash_out_multiplier, multiplier, crash_point, round_profit,
                 rake_back)  # Log round


   return balance  # Coder 1




def playing_again_real():
   while True:
       playing_again = input("Do you want to play again? (yes/no: YOU ARE SO DUE)").lower()  # Coder 1
       if playing_again == "yes":
           return True
       elif playing_again == "no":
           return False
       else:
           print("Invalid input, please just say yes or no")  # Coder 1




while True:
   balance = play_crash_round(balance, name)  # ChatGPT (OpenAI, 2023)
   if balance <= 0:
       print("You don't have enough money; you can't play anymore.")  # Coder 1
       break
   if not playing_again_real():  # ChatGPT (OpenAI, 2023)
       print(
           f"Thank you for playing Crash, it has been a pleasure, {name}. Your final balance is: ${balance}")  # Coder 1
       break
   # Game History Stats
print("Game History Stats:")
total_rounds = len(history_log)
print(f"All rounds completed: {total_rounds}")


if total_rounds > 0:
   total_profit = sum(entry["profit"] for entry in history_log)
   average_profit = total_profit / total_rounds
   print(f"Total gains from all the rounds: ${total_profit}")
   print(f"Average earnings per round: ${round(average_profit, 2)}")
   print("Here is your detailed round data:")
   for entry in history_log:
       print(entry)
else:
   print("0 rounds have been played.")





