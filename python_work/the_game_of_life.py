try:
    """
    Money is very important in this game, you need 5 million to win the game. For health, it is lost for anything you do.
    Regardless if good or bad, at the beginning of every thing you do, you will lose at least 1 healh. If you have no health,
    you lose as if you lost all money, you lose. Try to win 5 million dollars by the least amount of actions.
    Only few/some actions will include health loss. Some will only include money loss. ADDITIONALLY, you can earn credits.
    You earn credits ONLY when if you shop for stuff and do a business. BEWARE it costs many health point loss. 
    When you earn 4 credits, you win. So watch out for those three things: health, money, and credits.
    """

    import random, time, math

    # Set default value if you have a job. Currently, it will be False
    has_job = False

    name = input("What is your name?: ")
    print(f"Hello, {name}!")

    gender = input("What is your gender? (male, female): ")
    while gender not in ['male', 'female']:
        print("Please choose 'male' or 'female'.")
        gender = input("What is your gender? (male, female): ")

    which_path = input("Which path, college or career?:  ").lower()
    while which_path not in ['college', 'career']:
        print("Invalid difficulty. Please choose from 'college' and 'career.")
        which_path = input("Choose your difficulty (college, career): ").lower()
    if which_path == 'college':
        print(f"You picked college path! You will have to pay $500,000 later!")
        paid_for_college = False
        time.sleep(5)
        graduated_or_not_options = ['graduate', 'not graduate']
        graduated_or_not = random.choice(graduated_or_not_options)
        print(f"You did {graduated_or_not} from college!")
        if graduated_or_not == 'not graduate':
            print(f"NO GOOD!!! -- You didn't graduate")
        else:
            jobs_for_college = ['doctor', 'scientist', 'buisnessman', 'lawyer', 'software engineer', 'teacher',
                                'video game designer', 'vet', 'fashion designer', 'secret agent']
            your_job = random.choice(jobs_for_college)
            has_job = True
            print(f"Your job is: {your_job} (you work for 8 hours)")
            print(f"Calculating salary per day:")
            time.sleep(2.5)
            if your_job == 'doctor':
                salary = random.randint(800, 1000)
            if your_job == 'scientist':
                salary = random.randint(300, 500)
            if your_job == 'buisnessman':
                salary = random.randint(320, 520)
            if your_job == 'lawyer':
                salary = random.randint(500, 700)
            if your_job == 'software engineer':
                salary = random.randint(560, 760)
            if your_job == 'teacher':
                salary = random.randint(280, 480)
            if your_job == 'video game designer':
                salary = random.randint(600, 800)
            if your_job == 'vet':
                salary = random.randint(640, 840)
            if your_job == 'fashion designer':
                salary = random.randint(250, 450)
            if your_job == 'secret agent':
                salary = random.randint(310, 510)
            print(f"Your salary is ${salary} per day!")
    if which_path == 'career':
        print(f"You picked career path!")
        jobs_for_college = ['artist', 'police officer', 'athlete', 'salesperson', 'singer', 'chef', 'race car driver',
                            'inventor', 'actor', 'dancer']
        your_job = random.choice(jobs_for_college)
        has_job = True
        print(f"Your job is: {your_job} (you work for 8 hours)")
        print(f"Calculating salary per day:")
        time.sleep(2.5)
        if your_job == 'artist':
            salary = random.randint(200, 250)
        if your_job == 'police officer':
            salary = random.randint(180, 230)
        if your_job == 'athlete':
            salary = random.randint(210, 260)
        if your_job == 'salesperson':
            salary = random.randint(280, 330)
        if your_job == 'singer':
            salary = random.randint(130, 180)
        if your_job == 'chef':
            salary = random.randint(150, 200)
        if your_job == 'race car driver':
            salary = random.randint(160, 210)
        if your_job == 'inventor':
            salary = random.randint(200, 250)
        if your_job == 'actor':
            salary = random.randint(260, 310)
        if your_job == 'dancer':
            salary = random.randint(180, 230)
        print(f"Your salary is ${salary} per day!")
    
    game_difficulty = input("Choose your difficulty (easy, medium, hard, hardcore): ").lower()
    while game_difficulty not in ['easy', 'medium', 'hard', 'hardcore']:
        print("Invalid difficulty. Please choose from 'easy', 'medium', 'hard', or 'hardcore'.")
        game_difficulty = input("Choose your difficulty (easy, medium, hard, hardcore): ").lower()

    if game_difficulty == 'medium':
        money = random.randint(80, 500)
        health = random.randint(100, 200)
        game_credits = 0.1
    elif game_difficulty == 'hardcore':
        money = random.randint(40, 100)
        health = 75
        game_credits = 0.01
    elif game_difficulty == 'hard':
        money = random.randint(50, 400)
        health = random.randint(75, 120)
        game_credits = 0.05
    elif game_difficulty == 'easy':
        money = random.randint(100, 1000)
        health = random.randint(200, 300)
        game_credits = 0.2

    # Set a limit for doctor attempts. First make the value to 0.
    doctor_attempts = 0

    # Set a limit for shop attempts. First make value to 0.
    shop_attempts = 0

    # Flag if you have a wife
    has_wife = False

    # Every 5 turns, you earn your salary. Count every action.
    actions_count = 0

    # Initialize loan-related variables
    has_loan = False
    loan_when_dead = False
    loan_amount = 0
    if game_difficulty == 'easy':
        loan_repayment_actions = 10
    elif game_difficulty == 'medium':
        loan_repayment_actions = 7
    elif game_difficulty == 'hard':
        loan_repayment_actions = 5
    elif game_difficulty == 'hardcore':
        loan_repayment_actions = 4
    actions_since_loan = 0

    print(f"You start with ${money}")
    print(f"You start with {health} health.")
    print(f"You start with {game_credits} credits.")
    print(f"You currently have 3 doctor attempts. You used 0 doctor attempts.")

    while True:
        welcome_message = input(f"Welcome to your life! What do you want to do?\nEnter 'quit' to quit: ")
        discount_attempts = 0
        money = round(money, 2)
        game_credits = round(game_credits, 3)
        salary = round(salary, 2)

        if welcome_message == 'quit':
            print(f"Thanks for playing, {name}!")
            break
        
        if money <= 0:
            if has_loan:
                print(f"{name}, GAME OVER: YOU RAN OUT OF MONEY AND FAILED TO REPAY THE LOAN")
                break
            else:
                if loan_when_dead == False:
                    print(f"You have no money!")
                    want_a_loan_for_money = input("Want a loan? (yes, no)  ")
                    if want_a_loan_for_money == 'yes':
                        if has_loan:
                            print("You already have a loan! Repay it before taking another one.")
                        else:
                            time.sleep(4)
                            actions_count += 1
                            loan_amount = int(input("How much money you want: $"))
                            if actions_count < 24:
                                print(f"You took a loan of ${loan_amount}. You need to repay it within {loan_repayment_actions} actions.")
                                money = money + loan_amount
                                has_loan = True
                                loan_when_dead = True
                            else:
                                print(f"Sorry you can't get a loan due to many actions played!")
                    else:
                        print(f"{name}, GAME OVER: YOU RAN OUT OF MONEY")
                        break
                else:
                    print(f"{name}, GAME OVER: YOU RAN OUT OF MONEY")
                    break
        
        if health <= 0:
            print("You lost all of your health!")
            time.sleep(1)
            print("If you want to live, guess the number I am thinking about from 1-10. Enter any positive integer to quit!")

            guessing_choice = input("Let's play the guessing game! If you guess the number between 1-10, you gain health! If you lose, you snooze!  ")
            possible_actions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            computer_action = random.choice(possible_actions)
            print(f"\nYou chose {guessing_choice}, we chose {computer_action}.\n")
            game_host_name = "Anish Pasumarthi"
            if int(guessing_choice) < 1 or int(guessing_choice) > int(possible_actions[-1]):
                print("You chose a number outside the valid range! The game is terminated.")
                time.sleep(2)
                print(f"{game_host_name}, GAME OVER: YOU RAN OUT OF HEALTH")
                break
            else:
                if int(guessing_choice) == int(computer_action):
                    health_for_guessing = random.randint(1, 10)
                    print(f"Congrats {game_host_name}, You WON the game, you have {health_for_guessing} health!")
                    health = health_for_guessing
                    print(f"You now have {health} health!")
                else:
                    print(f"Sorry {game_host_name}, you DID NOT win the game. SO YOU DIE!!!!!")
                    time.sleep(2)
                    print(f"{game_host_name}, GAME OVER: YOU RAN OUT OF HEALTH")
                    break
                    
        if which_path == 'college':
            if paid_for_college == False:
                if money > 500_000:
                    print(f"You have enough to pay for your college funds!")
                    money -= 500_000
                    print(f"You have ${money} left.")
                    paid_for_college = True

        if welcome_message == 'take loan':
            if has_loan:
                print("You already have a loan! Repay it before taking another one.")
            else:
                time.sleep(4)
                actions_count += 1
                loan_amount = int(input("How much money you want: $"))
                print(f"You took a loan of ${loan_amount}. You need to repay it within {loan_repayment_actions} actions.")
                money = money + loan_amount
                has_loan = True
        
        if has_loan:
            actions_since_loan += 1
            if actions_since_loan >= loan_repayment_actions:
                print(f"GAME OVER: You failed to repay the loan of ${loan_amount} within {loan_repayment_actions} actions.")
                break
        
        if welcome_message == 'repay loan':
            actions_count += 1
            repay_amount = int(input("Enter the amount to repay: $"))
            interest_rate = round(random.uniform(0.1, 1), 1)
            print(f"You also have an interest of {interest_rate}%")
            interest_rate = loan_amount * interest_rate
            loan_amount = loan_amount + interest_rate
            print(f"You will have to pay ${loan_amount}")
            repay_amount = int(input("Enter again, enter the amount to repay: $"))
            if repay_amount <= money:
                money -= repay_amount
                loan_amount -= repay_amount
                print(f"You repaid ${repay_amount}. Remaining loan amount: ${loan_amount}")
                if loan_amount <= 0:
                    print("Congratulations! You have successfully repaid the loan.")
                    has_loan = False
                    actions_since_loan = 0
            else:
                print("You don't have enough money to repay that amount.")
        
        if welcome_message == 'get coupon':
            actions_count += 1
            if game_difficulty == 'hardcore':
                health -= 3
            else:
                health -= 1
            print(f"You have {health} health left.")
            message_forced_pay = random.randint(1,10)
            print(f"You pay ${message_forced_pay} for discounts. Pretty cheap!")
            money = money - message_forced_pay
            print(f"You have ${money} left.")
            if discount_attempts < 1:
                discounts = [95, 90, 85, 80, 75, 72, 70, 65, 60, 50, 45, 40, 35, 33, 30, 25, 20, 15, 10, 5]
                d_prices = random.choices(discounts, weights=[0.001, 0.002, 0.002, 0.002, 0.003, 0.01, 0.01, 0.01, 0.02, 
                                                                0.02, 0.02, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 
                                                                0.30, 0.39])[0]
                your_discount_price = d_prices
                print(f"Here is your discount price ticket: {your_discount_price}% off for any item.")
                discount_attempts += 1
            else:
                print("Max amount of attempts reached, sorry!")
        
        if welcome_message == 'shop':
            if shop_attempts < 4:
                actions_count += 1
                if game_difficulty == 'hardcore':
                    health -= random.randint(80, 120)
                elif game_difficulty == 'easy':
                    health -= random.randint(40, 85)
                else: 
                    health -= random.randint(50, 100)
                print(f"You have {health} health left.")
                print("You have chose to shop!!!")
                shop_message = input("What do you want to shop?: ")
                if len(shop_message) < 3:
                    price = 10
                elif len(shop_message) < 4:
                    price = 20
                elif len(shop_message) < 6:
                    price = 35
                elif len(shop_message) < 8:
                    price = 72
                elif len(shop_message) < 10:
                    price = 90
                elif len(shop_message) < 12:
                    price = 100
                elif len(shop_message) < 20:
                    price = random.randint(101, 500)
                else:
                    price = random.randint(501, 1000)
                print(f"Price of item: ${price}")
                do_you_want_to_pay = input("Do you want to pay? (yes, no) ")
                if do_you_want_to_pay == 'yes':
                    if money >= price:
                        if_you_want_to_use_coupon = input("Do you want to use a coupon, if you have one? (yes, no) ")
                        if if_you_want_to_use_coupon == 'yes':
                            new_price = price * (100 - your_discount_price) / 100
                            print(f"New price: ${new_price}")
                            money = money - new_price
                            del your_discount_price
                            print(f"You have ${money} left.")
                            get_credits = round(random.uniform(0, 0.5), 2)
                            game_credits = game_credits + get_credits
                            coupon_extra_credits = round(random.uniform(0, 0.5), 2)
                            print(f"You got an extra {coupon_extra_credits} credits for using a coupon.")
                            game_credits = game_credits + coupon_extra_credits
                            print(f"You have now {game_credits} credits.")
                            if game_difficulty == 'easy':
                                shop_attempts += 0.5
                            elif game_difficulty == 'hardcore':
                                shop_attempts += 1.5
                            else:
                                shop_attempts += 1
                        else:
                            print("Okay then pay up!")
                            money = money - price
                            print(f"You have ${money} left.")
                            get_credits = round(random.uniform(0, 0.5), 2)
                            game_credits = game_credits + get_credits
                            print(f"You have now {game_credits} credits.")
                            if game_difficulty == 'easy':
                                shop_attempts += 0.5
                            elif game_difficulty == 'hardcore':
                                shop_attempts += 1.5
                            else:
                                shop_attempts += 1
                    else:
                        print("Sorry, you don't have enough money to buy the item!")
                else:
                    print("Ok, have a good day!")
                    print(f"You have ${money} left.")
            else:
                print("You have max shopping attempts.")

        if welcome_message == 'fair business for credits':
            if game_difficulty == 'hardcore':
                health -= 7
            elif game_difficulty == 'hard':
                health -= 5
            else:
                health -= 4
            print(f"You have {health} health left.")
            money_amount = random.randint(500_000, 10_000_000)
            credits_recieved = round(random.uniform(0, 2), 2)
            print(f"\nHere is the offer: ${money_amount} for {credits_recieved} credits.")
            will_you_do_business = input("Are you going to accept the offer? (yes, no) ")
            if will_you_do_business == 'yes':
                actions_count += 1
                money = money - money_amount
                game_credits = game_credits + credits_recieved
                print(f"You have ${money} left.\nYou have {game_credits} credits.")
            else:
                print("Ok, have a nice day!")

        if welcome_message == 'get money':
            if game_difficulty == 'hardcore':
                health -= 3
            else:
                health -= 1
            print(f"You have {health} health left.")
            starting_money = random.randint(1,100)
            if_do_you_want_to_pay = input(f"Do you want to pay ${starting_money} to enter? ")
            if if_do_you_want_to_pay == 'yes':
                actions_count += 1
                money = money - starting_money
                more_money = random.randint(-10000, 10000)
                print(f"Here is the amount increased: ${more_money}")
                money = money + more_money
                print(f"\nAdded money successfully!\nNew amount: ${money}")
            else:
                print("Okay, have a good day!")
        
        if welcome_message == 'stats':
            print("\nHere are your stats:")
            print(f"{health} health\nMoney: ${money}\n{game_credits} credits.")
            print(f"Has wife: {has_wife}\nHas Job: {has_job}\nTotal actions played: {actions_count}")
            if has_job == True:
                print(f"Job: {your_job}\nSalary: {salary}")
            

        if welcome_message == 'eminem101greatone':
            if game_difficulty != 'hardcore':
                health -= 5
                print(f"You have {health} health left.")
                starting_money = random.randint(10,250)
                if_do_you_want_to_pay = input(f"Do you want to pay ${starting_money} to enter? You are in the BONUS money: ")
                if if_do_you_want_to_pay == 'yes':
                    actions_count += 1
                    money = money - starting_money
                    more_money = random.randint(-2_000_000, 2_000_000)
                    print(f"Here is the amount increased: ${more_money}")
                    money = money + more_money
                    print(f"\nAdded money successfully!\nNew amount: ${money}")
                else:
                    print("Okay, have a good day!")
            else:
                print(f"This feature is disabled for hardcore mode!")
        
        if welcome_message == 'action':
            actions_count += 1
            if game_difficulty == 'hardcore':
                health -= random.randint(2,5)
            else:
                health -= random.randint(1,3)
            print(f"You have {health} health left.")
            actions = ['get money', 'lose money', 'get coupon', 'bad stock rates', 'geoperdy', 'good stock rates',
                        'paying taxes', 'sue person', 'doctor', 'sleep', 'entertainment', 'work', 'socializing', 
                        'money earner', 'hardcore ONLY action', 'credit geoperdy', 'travel', 'gaming', 'wife/husband', 'divorce wife/husband',
                        'wife/husband rewards', 'kill wife/husband', 'double geoperdy', 'math challenge', 'sightsee',
                        'poo', 'get money', 'describe yourself for fun', 'sports', 'pee', 'multiplication', 'division',
                        'loser', 'merry', 'school', 'bad brother', 'choose your adventure', 'eminem', 'sofa', 'more money',
                        'less money', 'job result', 'job result', 'job result', 'risky trade', 'story mode', 'log', 'safety',
                        'best friend', 'credit holder', 'earn money yes', 'lose money no']
            result = random.choice(actions)
            if result == 'get money':
                additional_money_result = random.randint(100, 10000)
                money = money + additional_money_result
                print(f"You got an additional ${additional_money_result}!")
                print(f"\nYou have ${money} in total currently.")
            if result == 'lose money':
                losing_money_result = random.randint(100, 1000)
                money = money - losing_money_result
                print(f"You lost ${losing_money_result}!")
                print(f"\nYou have ${money} in total currently.")
            if result == 'get coupon':
                discounts = [90, 75, 70, 60, 50, 30, 25, 20, 15, 10, 5]
                d_prices = random.choices(discounts, weights=[0.002, 0.003, 0.005, 0.01, 0.01, 0.02, 0.02, 0.03, 0.03,
                                                                0.17, 0.70])[0]
                your_discount_price = d_prices
                print(f"Here is your discount price ticket: {your_discount_price}% off for any item.")
            if result == 'bad stock rates':
                print("Oh no! Bad stock rates have been occuring.")
                lose_stocks = random.randint(10, 1000)
                money = money - lose_stocks
                print(f"You lost ${lose_stocks}\nYou now currently have ${money}.")
            if result == 'geoperdy':
                geoperdy_questions = {
                "Capital of France?": "Paris",
                "Year World War II ended?": "1945",
                "Largest planet in the solar system?": "Jupiter",
                "Number of continents on Earth?": "7",
                "Element with the symbol 'H'?": "Hydrogen",
                "Currency used in Japan?": "Yen",
                "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
                "Current US President (as of 2024)?": "Joe Biden",
                "Square root of 64?": "8",
                "Country with the longest coastline?": "Canada",
                "The Great Barrier Reef is located in which ocean?": "Pacific Ocean",
                "What is the smallest prime number?": "2",
                "The Mona Lisa was painted by?": "Leonardo da Vinci",
                "First man to step on the moon?": "Neil Armstrong",
                "What is the capital of Australia?": "Canberra",
                "What is the speed of light?": "299,792 kilometers per second",
                "Who developed the theory of relativity?": "Albert Einstein",
                "In what year did the Titanic sink?": "1912",
                "The Eiffel Tower is located in which city?": "Paris",
                "What is the largest mammal in the world?": "Blue Whale",
                "Who painted the Sistine Chapel ceiling?": "Michelangelo",
                "What is the largest desert in the world?": "Antarctica",
                "The currency of China is called?": "Renminbi",
                "What is the capital of Brazil?": "Brasília",
                "How many planets are in our solar system?": "8",
                "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
                "The Great Wall of China is approximately how long?": "13,170 miles",
                "Which planet is known as the Red Planet?": "Mars",
                "Who is known as the 'Father of Computers'?": "Charles Babbage",
                "What is the currency of South Africa?": "Rand",
                "Who discovered penicillin?": "Alexander Fleming",
                "What is the national flower of Japan?": "Cherry Blossom",
                "The Nile River is located on which continent?": "Africa",
                "Who painted 'Starry Night'?": "Vincent van Gogh",
                "What is the capital of South Korea?": "Seoul",
                "How many bones are in the human body?": "206",
                "What is the main ingredient in guacamole?": "Avocado",
                "Who wrote '1984'?": "George Orwell",
                "What is the largest bird in the world?": "Ostrich",
                "Who is the author of 'Harry Potter' series?": "J.K. Rowling",
                "What is the currency of Japan?": "Yen",
                "What is the national animal of Australia?": "Kangaroo",
                "Who developed the polio vaccine?": "Jonas Salk",
                "What is the smallest country in the world?": "Vatican City",
                "What is the largest ocean on Earth?": "Pacific Ocean",
                "Who discovered the law of gravity?": "Isaac Newton",
                "What is the capital of Russia?": "Moscow",
                "What is the currency of Mexico?": "Peso",
                "Who wrote 'Pride and Prejudice'?": "Jane Austen",
                "What is the capital of China?": "Beijing",
                "What is the largest fish in the world?": "Whale Shark",
                "In what year did the Berlin Wall fall?": "1989",
                "Who discovered electricity?": "Benjamin Franklin",
                "What is the smallest ocean on Earth?": "Arctic Ocean",
                "Who is the lead singer of the band Queen?": "Freddie Mercury",
                "What is the largest volcano in the world?": "Mauna Loa",
                "Who is the Greek god of the sea?": "Poseidon",
                "What is the national sport of Japan?": "Sumo Wrestling",
                "Which planet is known as the 'Morning Star' or 'Evening Star'?": "Venus",
                "What is the capital of South Africa?": "Pretoria",
                "Who painted the 'Mona Lisa'?": "Leonardo da Vinci",
                "What is the main ingredient in hummus?": "Chickpeas",
                "In what year was the Declaration of Independence signed?": "1776",
                "Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
                "What is the national flower of the United States?": "Rose",
                "Which element has the chemical symbol 'O'?": "Oxygen",
                "What is the currency of India?": "Indian Rupee",
                "What is the capital of Argentina?": "Buenos Aires",
                "Who wrote 'The Great Gatsby'?": "F. Scott Fitzgerald",
                "Which planet is known as the 'Red Planet'?": "Mars",
                "What is the largest island in the world?": "Greenland",
                "Who painted 'The Starry Night'?": "Vincent van Gogh",
                "What is the main ingredient in sushi?": "Rice",
                "In what year did the Renaissance begin?": "14th century",
                "Who is the founder of Microsoft?": "Bill Gates",
                "What is the largest mammal on land?": "Elephant",
                "What is the currency of Brazil?": "Brazilian Real",
                "Who wrote 'The Catcher in the Rye'?": "J.D. Salinger",
                "What is the speed of sound in air?": "343 meters per second",
                "What is the smallest prime number?": "2",
                "In what year did the Titanic sink?": "1912",
                "Who discovered penicillin?": "Alexander Fleming",
                "What is the largest ocean on Earth?": "Pacific Ocean",
                "What is the capital of Italy?": "Rome",
                "Who is the author of 'The Lord of the Rings' series?": "J.R.R. Tolkien",
                "What is the national animal of China?": "Giant Panda",
                "What is the chemical symbol for gold?": "Au",
                "What is the capital of Australia?": "Canberra",
                "Who is the author of 'War and Peace'?": "Leo Tolstoy",
                "Which gas do plants primarily absorb from the atmosphere?": "Carbon Dioxide",
                "What is the largest moon in our solar system?": "Ganymede",
                "In what year did the American Civil War end?": "1865",
                "Who is the lead singer of the Rolling Stones?": "Mick Jagger",
                "What is the main component of Earth's atmosphere?": "Nitrogen",
                "Which river is the longest in the world?": "Nile",
                "Who painted the 'Girl with a Pearl Earring'?": "Johannes Vermeer",
                "What is the currency of South Korea?": "Korean Won",
                "What is the largest desert in Africa?": "Sahara",
                "Who developed the theory of evolution by natural selection?": "Charles Darwin",
                "What is the capital of Canada?": "Ottawa",
                "Which element has the chemical symbol 'Fe'?": "Iron",
                "Who is known as the 'Father of Medicine'?": "Hippocrates",
                "What is the national bird of the United States?": "Bald Eagle",
                "In what year did Christopher Columbus first reach the Americas?": "1492",
                "Who is the author of 'The Great Escape'?": "Paul Brickhill",
                "What is the speed of light in a vacuum?": "299,792 kilometers per second",
                "What is the largest city in India?": "Mumbai",
                "Who directed the movie 'Schindler's List'?": "Steven Spielberg",
                "What is the currency of Egypt?": "Egyptian Pound",
                "Who wrote 'The Chronicles of Narnia' series?": "C.S. Lewis",
                "What is the boiling point of water in Celsius?": "100 degrees",
                "Who is the Roman god of war?": "Mars",
                "What is the smallest bone in the human body?": "Stapes",
                "Who was the first woman to win a Nobel Prize?": "Marie Curie",
                }
                print(f"Welcome to geoperdy! If you win, you get MONEY, if you lose, pay the wager amount.")
                wager = input(f"Choose ANY amount to wager for GEOPERDY! ")
                wager = int(wager)
                question, answer = random.choice(list(geoperdy_questions.items()))
                user_answer = input(f"Question: {question}\nYour Answer: ").strip().lower()
                if user_answer.lower() == answer.lower():
                    money += wager
                    print(f"Correct! You now have ${money}!")
                else:
                    money -= wager
                    print(f"Wrong! The correct answer was '{answer}'. You lose ${wager}. Your remaining balance: ${money}")
                
            if result == 'good stock rates':
                print("There are some great stock rates happening around here...")
                xtra_money = random.randint(0,5)
                reasons = ['eating', 'hunting', 'playing', 'paying', 'dancing', 'rapping', 'eating humans', 
                            'hating aliens', 'singing barbie world', 'video game developing', 'being successful',
                            'killing harmless animals', 'reading', 'writing', 'learning', 'kissing a girl', 'hugging nabo']
                random_reason = random.choice(reasons)
                print(f"You earn ${xtra_money} for {random_reason}!")
                gain_stocks = random.randint(10, 2000)
                print(f"\nHere is the actual stock earnings: ${gain_stocks}")
                money = money + gain_stocks + xtra_money
                print(f"You currently have ${money}.")
            if result == 'paying taxes':
                are_you_paying_taxes = input("Are you going to pay taxes (yes, no): ")
                if are_you_paying_taxes == 'yes':
                    tax_amount = random.randint(50, 200)
                    print(f"\nTime to pay your taxes!")
                    print(f"You pay ${tax_amount}")
                    money = money - tax_amount
                    print(f"You now have ${money}.")
                else:
                    print("\nYou don't know when to give in and pay!\nPAY YOUR STUPID TAXES!!!!!!")
                    punishment_for_not_paying = random.randint(25, 100)
                    print(f"You lost {punishment_for_not_paying} health.")
                    health = health - punishment_for_not_paying
                    print(f"You now have {health} health.")
            if result == 'sue person':
                amount_sued = random.randint(50, 200)
                random_sueing_iphones = [7, 8, 9, 10, 11, 12, 13, 14, 15]
                yp = random.choice(random_sueing_iphones)
                reasons_to_sue = ['stealing your tomatoes', 'eating your birthday cake', 'sleeping on your bed',
                                    f'breaking your iPhone {yp}', 'taking your book', 'drooling on your dog', 'losing a bet',
                                    'kissing your girlfriend', 'murdering your mother', 'sueing your father', 'robbing you',
                                    'calling you a black monkey', 'dancing around with dirty shoes on your favorite shirt',
                                    'stalling around in your bathroom', 'starting a fire in your fancy driveway', 'vaping']
                the_actual_sueing_reason = random.choice(reasons_to_sue)
                print(f"You sued ${amount_sued} for {the_actual_sueing_reason}!")
                money = money + amount_sued
                print(f"You now have ${money}.")
            if result == 'doctor':
                do_you_want_to_go_doctor = input("Do you want to go to the doctor? (yes, no) ")
                if do_you_want_to_go_doctor == 'yes':
                    cost_for_doctor = random.randint(10, 25)
                    print(f"You pay ${cost_for_doctor}")
                    doctor_health_increase = random.randint(-50, 50)
                    health = health + doctor_health_increase
                    money = money - cost_for_doctor
                    print(f"You have now {health} health.")
                    print(f"You have ${money} left.")
                else:
                    print("Ok, have a nice day!")
            if result == 'sleep':
                print("You are enjoying a very nice sleep!")
            if result == 'entertainment':
                print("You are having fun with entertainment.")
            if result == 'work':
                work_reward = random.randint(10, 1000)
                print(f"You are doing work! Here is your work time reward:\n${work_reward}")
                money = money + work_reward
                if has_wife == True:
                    print(f"Since you have a wife, you gain money and health!")
                    money += random.randint(100, 1000)
                    health += random.randint(10, 20)
                print(f"You now have ${money}.")

            if result == 'socializing':
                print("You are socializing with some friends!")
                if has_wife == True:
                    print(f"You get extra credits for having a wife!")
                    game_credits += round(random.uniform(0, 0.5), 2)

            if result == 'money earner':
                if money <= 1_000:
                    m_money = random.randint(-1000, 100)
                elif money <= 10_000:
                    m_money = random.randint(-10, 1000)
                elif money <= 100_000:
                    m_money = random.randint(10, 10000)
                elif money <= 2_000_000:
                    m_money = random.randint(2000, 200_000)
                elif money <= 5_000_000:
                    m_money = random.randint(10_000, 1_500_000)
                else:
                    m_money = random.randint(100_000, 2_000_000)
                money = money + m_money
                print(f"You earned ${m_money}!!! You now have ${money}")
            
            if result == 'hardcore ONLY action':
                if game_difficulty != 'hardcore':
                    print("Sorry, this action is only available in hardcore mode!")
                else:
                    print("Lets generate you a random money and credit amount to help you for HARDCORE MODE.")
                    credit_hardcore_amount = round(random.uniform(0, 0.5), 2)
                    money_hardcore_amount = random.randint(100_000, 1_000_000)
                    if money > 5_000_000:
                        additional_hardcore_money_amount = random.randint(1_000_000, 2_000_000)
                    else:
                        additional_hardcore_money_amount = 0
                    if game_credits > 2.5:
                        additional_hardcore_credit_amount = round(random.uniform(0, 1), 2)
                    else:
                        additional_hardcore_credit_amount = 0
                    money = money + additional_hardcore_money_amount + money_hardcore_amount
                    game_credits = game_credits + additional_hardcore_credit_amount + credit_hardcore_amount
                    print(f"You now have ${money} and {game_credits} credits.")
            
            if result == 'credit geoperdy':
                geoperdy_line = "Welcome to geoperdy, but in credit rewarding instead of money."
                geoperdy_line += "Please wager less or equal to the amount of credits you have."
                geoperdy_line += f"You currently have {game_credits} credits."
                user_line = input(geoperdy_line)
                user_line = float(user_line)
                if user_line > game_credits:
                    print("You don't have that much credits to wager.")
                else:
                    answers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    the_answer = random.choice(answers)
                    question_for_geoperdy = input("What number am I thinking of from 1-10: ")
                    question_for_geoperdy = int(question_for_geoperdy)
                    print(f"You picked {question_for_geoperdy} and we picked {the_answer}.")
                    if question_for_geoperdy == the_answer:
                        print(f"YOU WIN!!! Here is your {user_line} credits.")
                        game_credits = user_line + game_credits
                    else:
                        game_credits = game_credits - user_line
                        print(f"You lost! You are now dropped down to {game_credits} credits.")
                print(f"You have currently {game_credits} credits.")
            
            if result == 'travel':
                msg_to_travel = input("Do you want to travel across the world and leave your country to earn? (yes, no) ")
                if msg_to_travel == 'yes':
                    travel_money = random.randint(1000, 50000)
                    money = money + travel_money
                    if game_credits > 1:
                        travel_credits = round(random.uniform(0, 0.5), 2)
                        game_credits = game_credits - travel_credits
                    health_lost_to_travel = random.randint(10, 25)
                    health = health - health_lost_to_travel
                    if has_wife == True:
                        print(f"You get more money since you have a wife.")
                        money += random.randint(100, 1000)
                    print(f"You have {health} heath, ${money} and {game_credits} credits.")
                else:
                    print("Ok, have a nice day!")
                    game_credits = game_credits + 0.1
                    print(f"You gained 0.1 credits for supporting your country and not going.")
                print(f"You have {health} health, ${money}, and {game_credits} credits.")
            
            if result == 'gaming':
                if has_wife == True:
                    print("Your wife does not allow you to do gaming!")
                    health -= 5
                    print(f"You lost 5 health, so you now have {health} health!")
                else:
                    video_game_money = random.randint(10, 100)
                    print(f"You are playing games and you won! You gained 5 health and ${video_game_money} in the process.")
                    health += 5
                    money = money + video_game_money
                    print(f"You now have {health} health and ${money}.")

            if result == 'wife/husband':
                if has_wife == True:
                    print("You already have a wife/husband! Enter 'action' to divorce a wife/husband if needed.")
                else:
                    has_wife = True
                    if gender == 'male':
                        lover_names = ['amelia', 'angelina', 'olivia', 'ella', 'ellie', 'samira', 'emma', 'charlotte', 'ava', 'emily',
                                    'abigail', 'harper', 'evelyn', 'rylie', 'sophia', 'clara', 'chloe', 'natalie', 'mia', 'summer']
                    else:
                        lover_names = [
                        "Liam", "Noah", "Oliver", "Elijah", "William",
                        "James", "Benjamin", "Lucas", "Henry", "Alexander",
                        "Mason", "Ethan", "Logan", "Jackson", "Aiden",
                        "Sebastian", "Caleb", "Matthew", "Samuel", "David"
                        ]
                    ywn = random.choice(lover_names)
                    wife_amount = random.randint(10_000, 100_000)
                    wife_choose_giving_money_options = ['yes', 'no', 'you give money']
                    wife_choose_giving_money = random.choice(wife_choose_giving_money_options)
                    if wife_choose_giving_money == 'yes':
                        print(f"You got a wife/husband, {ywn.title()}. He/She chose to give her money to you as his/her net worth is ${wife_amount}!")
                        money = money + wife_amount
                    elif wife_choose_giving_money == 'no':
                        print(f"You got a wife/husband, {ywn.title()}. He/she chose to NOT give her money to you as his/her net worth is ${wife_amount}!")
                    elif wife_choose_giving_money == 'you give money':
                        amount_wife_wants = random.randint(1000, 10000)
                        print(f"You got a wife/husband, {ywn.title()}. He/She wants you to give ${amount_wife_wants} to him/her!")
                        money = money - amount_wife_wants
                    print(f"You have ${money} left.")
                    del actions[18]
            
            if result == 'divorce wife/husband':
                if has_wife == True:
                    do_you_want_to_divorce = input("Do you want to divorce your wife/husband? (yes, no) ")
                    if do_you_want_to_divorce == 'yes':
                        actions.insert(18, 'wife/husband')
                        has_wife = False
                        print(f"You divorced {ywn.title()}!")
                    else:
                        print("Ok, have a nice day.")
                else:
                    print(f"You don't have a wife/husband! Action cannot be completed.")
            
            if result == 'wife/husband rewards':
                if has_wife == True:
                    print("You get your wife/husband rewards:")
                    game_credits = game_credits + round(random.uniform(0, 0.5), 2)
                    money += random.randint(100, 10000)
                    print(f"You have ${money} and {game_credits} credits.")
                else:
                    print("Cannot recieve wife/husband rewards because no wife/husband!")
            
            if result == 'kill wife/husband':
                if has_wife == True:
                    has_wife == False
                    print(f"Your wife/husband died! You arranged a funeral for {ywn.title()} for this sad moment.")
                    actions.insert(18, 'wife')
                else:
                    print(f"Action: wife/husband dead, cannot be done. Reason: NO WIFE/HUSBAND!")
            
            if result == 'double geoperdy':
                questions_and_answers = {
                "Capital of France?": "Paris",
                "Year World War II ended?": "1945",
                "Largest planet in the solar system?": "Jupiter",
                "Number of continents on Earth?": "7",
                "Element with the symbol 'H'?": "Hydrogen",
                "Currency used in Japan?": "Yen",
                "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
                "Current US President (as of 2024)?": "Joe Biden",
                "Square root of 64?": "8",
                "Country with the longest coastline?": "Canada",
                "The Great Barrier Reef is located in which ocean?": "Pacific Ocean",
                "What is the smallest prime number?": "2",
                "The Mona Lisa was painted by?": "Leonardo da Vinci",
                "First man to step on the moon?": "Neil Armstrong",
                "What is the capital of Australia?": "Canberra",
                "What is the speed of light?": "299,792 kilometers per second",
                "Who developed the theory of relativity?": "Albert Einstein",
                "In what year did the Titanic sink?": "1912",
                "The Eiffel Tower is located in which city?": "Paris",
                "What is the largest mammal in the world?": "Blue Whale",
                "Who painted the Sistine Chapel ceiling?": "Michelangelo",
                "What is the largest desert in the world?": "Antarctica",
                "The currency of China is called?": "Renminbi",
                "What is the capital of Brazil?": "Brasília",
                "How many planets are in our solar system?": "8",
                "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
                "The Great Wall of China is approximately how long?": "13,170 miles",
                "Which planet is known as the Red Planet?": "Mars",
                "Who is known as the 'Father of Computers'?": "Charles Babbage",
                "What is the currency of South Africa?": "Rand",
                "Who discovered penicillin?": "Alexander Fleming",
                "What is the national flower of Japan?": "Cherry Blossom",
                "The Nile River is located on which continent?": "Africa",
                "Who painted 'Starry Night'?": "Vincent van Gogh",
                "What is the capital of South Korea?": "Seoul",
                "How many bones are in the human body?": "206",
                "What is the main ingredient in guacamole?": "Avocado",
                "Who wrote '1984'?": "George Orwell",
                "What is the largest bird in the world?": "Ostrich",
                "Who is the author of 'Harry Potter' series?": "J.K. Rowling",
                "What is the currency of Japan?": "Yen",
                "What is the national animal of Australia?": "Kangaroo",
                "Who developed the polio vaccine?": "Jonas Salk",
                "What is the smallest country in the world?": "Vatican City",
                "What is the largest ocean on Earth?": "Pacific Ocean",
                "Who discovered the law of gravity?": "Isaac Newton",
                "What is the capital of Russia?": "Moscow",
                "What is the currency of Mexico?": "Peso",
                "Who wrote 'Pride and Prejudice'?": "Jane Austen",
                "What is the capital of China?": "Beijing",
                "What is the largest fish in the world?": "Whale Shark",
                "In what year did the Berlin Wall fall?": "1989",
                "Who discovered electricity?": "Benjamin Franklin",
                "What is the smallest ocean on Earth?": "Arctic Ocean",
                "Who is the lead singer of the band Queen?": "Freddie Mercury",
                "What is the largest volcano in the world?": "Mauna Loa",
                "Who is the Greek god of the sea?": "Poseidon",
                "What is the national sport of Japan?": "Sumo Wrestling",
                "Which planet is known as the 'Morning Star' or 'Evening Star'?": "Venus",
                "What is the capital of South Africa?": "Pretoria",
                "Who painted the 'Mona Lisa'?": "Leonardo da Vinci",
                "What is the main ingredient in hummus?": "Chickpeas",
                "In what year was the Declaration of Independence signed?": "1776",
                "Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
                "What is the national flower of the United States?": "Rose",
                "Which element has the chemical symbol 'O'?": "Oxygen",
                "What is the currency of India?": "Indian Rupee",
                "What is the capital of Argentina?": "Buenos Aires",
                "Who wrote 'The Great Gatsby'?": "F. Scott Fitzgerald",
                "Which planet is known as the 'Red Planet'?": "Mars",
                "What is the largest island in the world?": "Greenland",
                "Who painted 'The Starry Night'?": "Vincent van Gogh",
                "What is the main ingredient in sushi?": "Rice",
                "In what year did the Renaissance begin?": "14th century",
                "Who is the founder of Microsoft?": "Bill Gates",
                "What is the largest mammal on land?": "Elephant",
                "What is the currency of Brazil?": "Brazilian Real",
                "Who wrote 'The Catcher in the Rye'?": "J.D. Salinger",
                "What is the speed of sound in air?": "343 meters per second",
                "What is the smallest prime number?": "2",
                "In what year did the Titanic sink?": "1912",
                "Who discovered penicillin?": "Alexander Fleming",
                "What is the largest ocean on Earth?": "Pacific Ocean",
                "What is the capital of Italy?": "Rome",
                "Who is the author of 'The Lord of the Rings' series?": "J.R.R. Tolkien",
                "What is the national animal of China?": "Giant Panda",
                "What is the chemical symbol for gold?": "Au",
                "What is the capital of Australia?": "Canberra",
                "Who is the author of 'War and Peace'?": "Leo Tolstoy",
                "Which gas do plants primarily absorb from the atmosphere?": "Carbon Dioxide",
                "What is the largest moon in our solar system?": "Ganymede",
                "In what year did the American Civil War end?": "1865",
                "Who is the lead singer of the Rolling Stones?": "Mick Jagger",
                "What is the main component of Earth's atmosphere?": "Nitrogen",
                "Which river is the longest in the world?": "Nile",
                "Who painted the 'Girl with a Pearl Earring'?": "Johannes Vermeer",
                "What is the currency of South Korea?": "Korean Won",
                "What is the largest desert in Africa?": "Sahara",
                "Who developed the theory of evolution by natural selection?": "Charles Darwin",
                "What is the capital of Canada?": "Ottawa",
                "Which element has the chemical symbol 'Fe'?": "Iron",
                "Who is known as the 'Father of Medicine'?": "Hippocrates",
                "What is the national bird of the United States?": "Bald Eagle",
                "In what year did Christopher Columbus first reach the Americas?": "1492",
                "Who is the author of 'The Great Escape'?": "Paul Brickhill",
                "What is the speed of light in a vacuum?": "299,792 kilometers per second",
                "What is the largest city in India?": "Mumbai",
                "Who directed the movie 'Schindler's List'?": "Steven Spielberg",
                "What is the currency of Egypt?": "Egyptian Pound",
                "Who wrote 'The Chronicles of Narnia' series?": "C.S. Lewis",
                "What is the boiling point of water in Celsius?": "100 degrees",
                "Who is the Roman god of war?": "Mars",
                "What is the smallest bone in the human body?": "Stapes",
                "Who was the first woman to win a Nobel Prize?": "Marie Curie",
                }
                print(f"You have ${money}!")
                print(f"Welcome to double geoperdy! If you win, you get double MONEY, if you lose, pay the price 1-3 times amount.")
                wager = input(f"Choose an amount to wager for DOUBLE GEOPERDY! (amount should be less or equal to your money) ")
                wager = int(wager)
                if wager > money:
                    print(f"You can't wager that much money as you don't have that much!")
                else:
                    question, answer = random.choice(list(questions_and_answers.items()))
                    user_answer = input(f"Question: {question}\nYour Answer: ").strip().lower()
                    if user_answer.lower() == answer.lower():
                        money = money + wager * 2
                        print(f"Correct! You now have ${money}!")
                    else:
                        loss = wager * random.randint(1, 3)
                        money -= loss
                        print(f"Wrong! The correct answer was '{answer}'. You lose ${loss}. Your remaining balance: ${money}")
            
            if result == 'math challenge':
                msg_for_math_enter = input("Do you want to enter the math challenge to earn rewards? (yes, no):  ")
                if msg_for_math_enter == 'no':
                    print(f"Ok, so long!")
                    money -= random.randint(100, 2000)
                    print(f"You have ${money} left.")
                else:
                    print("Great! If you lose, you lose money, every time you survive a round, you get credits.")
                    print("When you win, you get money!")
                    print("Here is round 1...")
                    num1 = random.randint(1, 100000000)
                    num2 = random.randint(1, 100000000)
                    correct_answer = num1 + num2

                    user_answer = int(input(f"What is {num1} + {num2}? "))
                    if user_answer == correct_answer:
                        print(f"Great! You gained 0.05 credits.")
                        game_credits += 0.05
                        print(f"Lets start round 2...")
                        num1 = random.randint(100000, 100000000)
                        num2 = random.randint(100000, 100000000)
                        correct_answer = num1 - num2
                        user_answer = float(input(f"What is {num1} - {num2}? "))
                        if user_answer == correct_answer:
                            print(f"Great you gained 0.05 credits.")
                            game_credits += 0.05
                            print(f"Lets start round 3...")
                            num1 = random.randint(1, 100000)
                            num2 = random.randint(1, 100000)
                            correct_answer = num1 * num2
                            user_answer = int(input(f"What is {num1} * {num2}? "))
                            if user_answer == correct_answer:
                                print(f"Great, you gained 0.05 credits.")
                                game_credits += 0.05
                                print(f"Wow... Lets start round 4!")
                                num1 = random.randint(1, 100000)
                                num2 = random.randint(1, 100000)
                                correct_answer = round(num1 / num2, 2)
                                user_answer = float(input(f"What is {num1} ÷ {num2}? Round to nearest hundreth if nessesary! "))
                                if user_answer == correct_answer:
                                    print("Great! You earned 0.05 credits.")
                                    game_credits += 0.05
                                    print(f"Lets start round 5... THE FINAL ROUND!!!")
                                    num1 = random.uniform(100, 1000)
                                    num2 = random.uniform(100, 1000)
                                    num3 = random.uniform(10, 1000)
                                    operator = random.choice(['+', '*', '/', '-'])
                                    operator2 = random.choice(['+', '*', '/', '-'])
                                    expression = f"{num1} {operator} {num2} {operator2} {num3}"
                                    correct_answer = round(eval(expression), 2)
                                    user_answer = float(input(f"What is {expression}? Round to nearest hundreth if nessesary! "))
                                    if user_answer == correct_answer:
                                        print(f"Nice! You get 0.10 credits.")
                                        print(f"YOU DID IT!!! You get money, health, and much more. See your stats for updates.")
                                        game_credits += 0.05
                                        if game_difficulty == 'medium':
                                            health += 15
                                            money += 1_500_000
                                            game_credits += 0.01
                                        elif game_difficulty == 'easy':
                                            health += 20
                                            money += 1_500_000
                                            game_credits += 0.05
                                        elif game_difficulty == 'hard':
                                            health += 10
                                            money += 1_000_000
                                        else:
                                            health += 5
                                            money += 750_000
                                        
                                        if game_difficulty != 'hardcore':
                                            more_money_for_math_win = random.randint(1000, 100000)
                                            money = money + more_money_for_math_win
                                    else:
                                        loss_money_for_math = random.randint(100000, 500000)
                                        print(f"OH NO!!! You lost ${loss_money_for_math}")
                                        print(f"The correct answer is {correct_answer}!")
                                        money = money - loss_money_for_math
                                    
                                else:
                                    loss_money_for_math = random.randint(50000, 100000)
                                    print(f"OH NO!!! You lost ${loss_money_for_math}.")
                                    print(f"The correct answer is {correct_answer}!")
                                    money = money - loss_money_for_math
                            else:
                                loss_money_for_math = random.randint(20000, 50000)
                                print(f"OH NO!!! You lost ${loss_money_for_math}.")
                                print(f"The correct answer is {correct_answer}!")
                                money = money - loss_money_for_math
                        else:
                            print("OH NO!!! You lost $20000")
                            print(f"The correct answer is {correct_answer}!")
                            money -= 20000
                    else:
                        print(f"OH NO!!! You MAY lose $5000")
                        print(f"The correct answer is {correct_answer}!")
                        if game_difficulty != 'easy':
                            money -= 5000
            
            if result == 'sightsee':
                money -= 1000
                health += 15
                print(f"You chose to sightsee! You paid $1000 and gained 15 health.")
                print(f"You currently have ${money} and {health} health")
            
            if result == 'more money':
                more_money_amount_for_the_action_that_is_unique = random.randint(1000, 5000)
                print(f"You earned ${more_money_amount_for_the_action_that_is_unique}!")
                money = money + more_money_amount_for_the_action_that_is_unique
                print(f"You have ${money} left.")
            
            if result == 'less money':
                less_money_amount_for_the_action_that_is_unique = random.randint(1000, 5000)
                print(f"You lost ${less_money_amount_for_the_action_that_is_unique}!")
                money = money - less_money_amount_for_the_action_that_is_unique
                print(f"You have ${money} left.")
            
            if result == 'sports':
                kind_sport = ['basketball', 'football', 'baseball', 'soccer', 'volleyball', 'hockey', 'swimming']
                random_kind_sport = random.choice(kind_sport)
                print(f"You joined in the professional sports team, {random_kind_sport}.")
                print(f"You went to the final game! Lets see if your team won...")
                time.sleep(3)
                if_sport_team_won = ['yes', 'no']
                sport_team_result = random.choice(if_sport_team_won)
                if sport_team_result == 'yes':
                    print(f"Your team won!\nYou earned $7500 and 15 health!")
                    money += 7500
                    health += 15
                else:
                    print(f"Your team lost!\nYou lost $5000 and 10 health.")
                    money -= 5000
                    health -= 10
            
            if result == 'describe yourself for fun':
                characteristics = ['funny', 'smart', 'kind', 'mean', 'rude', 'bad', 'dumb', 'serious', 'cool',
                                   'not funny', 'brave', 'clever', 'cheerful', 'an idiot', 'amusing', 'bright', 'right',
                                   'comfortable', 'dashing', 'gentle', 'popular', 'famous', 'strong', 'talented']
                random_characteristic = random.choice(characteristics)
                print(f"I am {random_characteristic}!")

            if result == 'poo':
                print(f"You went poo!")
                health += 1
                print(f"You have {health} health!")
            
            if result == 'pee':
                print(f"You went pee!")
                health += 1
                print(f"You have {health} health!")
            
            if result == 'job result':
                if has_job:
                    print(f"Your company decided to do something for your job!")
                    time.sleep(2)
                    job_actions = ['nothing', 'removal', 'decrease salary', 'increase salary']
                    random_action_job = random.choice(job_actions)
                    if random_action_job == 'nothing':
                        print(f"Nothing happened! Lucky your on the same side...")
                    elif random_action_job == 'decrease salary':
                        amount_decrease_salary = round(random.uniform(1, 3), 2)
                        print(f"Your salary has been decreased by {amount_decrease_salary} times!")
                        salary = salary / amount_decrease_salary
                        print(f"Your salary is now ${salary}.")
                    elif random_action_job == 'increase salary':
                        amount_increase_salary = round(random.uniform(1, 3), 2)
                        print(f"Your salary has been increased by {amount_increase_salary} times!")
                        salary = salary * amount_increase_salary
                        print(f"Your salary is now ${salary}.")
                    elif random_action_job == 'removal':
                        print(f"You got removed from your job!")
                        has_job = False
                    
            if result == 'bad brother':
                what_kind_of_brother = ['younger', 'older', 'twin', 'alien', 'super', 'idiotic', 'autistic']
                what_kind_of_brother_result = random.choice(what_kind_of_brother)
                print(f"Your {what_kind_of_brother_result} brother hit you so hard! You fell to the ground, almost dead!")
                health = 1
                print(f"You have only 1 health!")
            
            if result == 'choose your adventure':
                print(f"Welcome to 'choose your adventure'. (3 adventures) Here is the storyline of what to do!")
                time.sleep(2)
                first_adventure = input("Do you want to murder your next door man? (yes, no)  ")
                options_for_adventure = ['yes', 'no']
                random_result_of_options_for_adventure = random.choice(options_for_adventure)
                if first_adventure == random_result_of_options_for_adventure:
                    print(f"Okay! You earned $1000 for doing the following action.")
                    money += 1000
                else:
                    print(f"NOPE!!! Wrong move, the man slipped into your underwear and blasted you! (you lost health)")
                    health -= random.randint(15, 30)
                    print(f"You have {health} health left!")
                second_adventure = input("Where do you want to return to: (backyard, porch)  ")
                options_for_adventure2 = ['backyard', 'porch']
                random_option_for_adventure_result2 = random.choice(options_for_adventure2)
                if second_adventure == random_option_for_adventure_result2:
                    print(f"Great choice, you escaped from the situation of the murder! You earn 0.1 credits.")
                    game_credits += 0.1
                else:
                    print(f"Wrong location, the police saw you and accused you because you are up past curfew")
                    second_adventure_escape = input("(run, stay)  ")
                    if second_adventure_escape == 'run':
                        print(f"You ran away successfully, but got caught by another group of policemen!")
                        print(f"You lost $150,000 for a fine for being late after curfew and escaping policemen.")
                        money -= 150_000
                    else:
                        print(f"You chose to stay! You stayed in jail for 5 years but finally got released.")
                        print(f"You lost 50 health!")
                        health -= 50
                third_adventure = input("Do you go inside? (yes, no)  ")
                options_for_adventure = ['yes', 'no']
                random_result_of_options_for_adventure = random.choice(options_for_adventure)
                if third_adventure == random_result_of_options_for_adventure:
                    print(f"You went inside successfully to your house and won! (See your stats for updated rewards).")
                    money += random.randint(1000, 10000)
                    health += random.randint(10, 20)
                    game_credits += round(random.uniform(0, 0.5), 2)
                else:
                    print(f"You realized that you went inside another random ghost house! A random skeleton killed you!")
                    print(f"GAME OVER!!! -- You died")
                    break

            if result == 'multiplication':
                print(f"Solve a multiplication problem to earn money!!!")
                multiplication_difficulty = input("(easy, medium, hard)  ")
                if multiplication_difficulty == 'hard':
                    factor1 = random.uniform(1, 10000)
                    factor2 = random.uniform(1, 10000)
                    answer_to_multiplication_question = round(factor1 * factor2, 2)
                    multiplication_question = float(input(f"What is {factor1} * {factor2}?  Round to nearest hundreth:  "))
                    if multiplication_question != answer_to_multiplication_question:
                        print(f"No, the right answer is {answer_to_multiplication_question}. Sorry, you lost $1000.")
                        money -= 1000
                    else:
                        print(f"Correct! You earned $10000!")
                        money += 10000
                elif multiplication_difficulty == 'medium':
                    factor1 = random.uniform(1, 100)
                    factor2 = random.uniform(1, 100)
                    answer_to_multiplication_question = round(factor1 * factor2, 2)
                    multiplication_question = float(input(f"What is {factor1} * {factor2}?  Round to nearest hundreth:  "))
                    if multiplication_question != answer_to_multiplication_question:
                        print(f"No, the right answer is {answer_to_multiplication_question}. Sorry, you lost $500.")
                        money -= 500
                    else:
                        print(f"Correct! You earned $5000!")
                        money += 5000
                elif multiplication_difficulty == 'easy':
                    factor1 = random.randint(1, 100)
                    factor2 = random.randint(1, 100)
                    answer_to_multiplication_question = round(factor1 * factor2, 2)
                    multiplication_question = float(input(f"What is {factor1} * {factor2}?  Round to nearest hundreth:  "))
                    if multiplication_question != answer_to_multiplication_question:
                        print(f"No, the right answer is {answer_to_multiplication_question}. Sorry, you lost $100.")
                        money -= 100
                    else:
                        print(f"Correct! You earned $750!")
                        money += 750
            
            if result == 'division':
                print(f"Solve a division problem to earn money!!!")
                multiplication_difficulty = input("(easy, medium, hard)  ")
                if multiplication_difficulty == 'hard':
                    factor1 = random.uniform(1, 10000)
                    factor2 = random.uniform(1, 10000)
                    answer_to_division_question = round(factor1 / factor2, 2)
                    division_question = float(input(f"What is {factor1} / {factor2}? Round to nearest hundredth.  "))
                    if division_question != answer_to_division_question:
                        print(f"No, the right answer is {answer_to_division_question}. Sorry, you lost $1000.")
                        money -= 1000
                    else:
                        print(f"Correct! You earned $10000!")
                        money += 10000
                elif multiplication_difficulty == 'medium':
                    factor1 = random.uniform(1, 100)
                    factor2 = random.uniform(1, 100)
                    answer_to_division_question = round(factor1 / factor2, 2)
                    division_question = float(input(f"What is {factor1} / {factor2}? Round to nearest hundredth.  "))
                    if division_question != answer_to_division_question:
                        print(f"No, the right answer is {answer_to_division_question}. Sorry, you lost $500.")
                        money -= 500
                    else:
                        print(f"Correct! You earned $5000!")
                        money += 5000
                elif multiplication_difficulty == 'easy':
                    factor1 = random.randint(1, 100)
                    factor2 = random.randint(1, 100)
                    answer_to_division_question = round(factor1 / factor2, 2)
                    division_question = float(input(f"What is {factor1} / {factor2}? Round to nearest hundredth.  "))
                    if division_question != answer_to_division_question:
                        print(f"No, the right answer is {answer_to_division_question}. Sorry, you lost $100.")
                        money -= 100
                    else:
                        print(f"Correct! You earned $750!")
                        money += 750

            if result == 'merry':
                print(f"You felt merry! You got $1300 and 3 health!")
                health += 3
                money += 1300
                print(f"You have ${money} and {health} health!")
            
            if result == 'credit holder':
                print(f"WELCOME TO THE CREDIT HOLDER VAULT!")
                the_credit_vault_get_money = input("Do you want to sneak up and steal credits? (yes, no)  ")
                random_option_for_stealing_credits_from_vault = ['successfully made it', 'got caught by a monster',
                                                                 'got bit by a monster', 'did not got anything', 'fell']
                the_option_for_stealing_credits_from_vault = random.choice(random_option_for_stealing_credits_from_vault)
                if the_credit_vault_get_money == 'no':
                    print(f"Ok! Have a nice day.")
                    health -= random.randint(1, 5)
                else:
                    if the_option_for_stealing_credits_from_vault == 'fell':
                        print(f"You fell down!!! You got lucky someone saved you. Otherwise you could have died!")
                        health_after_falling = random.randint(1, 5)
                        health = health_after_falling
                        print(f"You have {health} health left!")
                    elif the_option_for_stealing_credits_from_vault == 'did not got anything':
                        print(f"You made the wise move of not getting anything!")
                    elif the_option_for_stealing_credits_from_vault == 'successfully made it':
                        credits_recieved_from_the_vault = round(random.uniform(0.75, 1.5), 2)
                        game_credits = game_credits + credits_recieved_from_the_vault
                        print(f"You successfully made it! You got {credits_recieved_from_the_vault} credits!")
                    elif the_option_for_stealing_credits_from_vault == 'got bit by a monster':
                        health -= random.randint(10, 50)
                        print(f"You got bit by a monster! You lost some health, and you have {health} health left!")
                    else:
                        print(f"You got caught by a monster! You were able to escape successfully but lost LITTLE money!")
                        money -= random.randint(10, 1000)
                        print(f"You have ${money} left!")
                    
            if result == 'loser':
                print(f"Eminem and his friends hijacked you and called you loser! You lost some health and money.")
                money -= random.randint(10, 2000)
                health -= random.randint(1, 15)
                print(f"You have ${money} and {health} health!")
            
            if result == 'log':
                print(f"Stepped on a log on your favorite shoes!")
                money -= 5000
                print(f"You lost $5000")
            
            if result == 'safety':
                print(f"You got into the safety patrol! You saved many lives and you are a good person")
                print(f"You got $2500")
                money += 2500
                if has_job == True:
                    safety_raise = round(random.uniform(1, 2), 2)
                    print(f"Your salary got increased by {safety_raise}!")
                    salary = salary * safety_raise
                    print(f"Your salary is now: ${salary}!")
            
            if result == 'earn money yes':
                random_earn_money = random.randint(1000, 5000)
                print(f"You earned ${random_earn_money}")
                money = money + random_earn_money
                print(f"You have ${money}")
            
            if result == 'lose money no':
                random_lose_money = random.randint(500, 2500)
                print(f"You lost ${random_lose_money}")
                money = money - random_lose_money
                print(f"You have ${money}")
            
            if result == 'risky trade':
                risky_enter_trade = input("Do you want to do a risky trade? (yes, no)  ")
                if risky_enter_trade == 'no':
                    if gender == 'male':
                        wording_for_risky_trade_enter_risk = 'man'
                    else:
                        wording_for_risky_trade_enter_risk = 'woman'
                    print(f"Ok, have a nice life! Here is something risky for you, young {wording_for_risky_trade_enter_risk} You lose money (lots):")
                    money -= random.randint(1, 10_000)
                else:
                    money_risky_trade_amount = random.randint(1, 1_000_000)
                    credits_risky_trade_amount = round(random.uniform(0, 2), 1)
                    health_risky_trade_amount = random.randint(-50, 10)
                    what_you_want_for_risk_trade = input("What do you want? (money, credits)  ")
                    if what_you_want_for_risk_trade == 'money':
                        print(f"You get ${money_risky_trade_amount}! You give {credits_risky_trade_amount}!")
                        money = money + money_risky_trade_amount
                        game_credits = game_credits - credits_risky_trade_amount
                        print(f"You have ${money} and {game_credits} credits")
                        if money <= 0:
                            print(f"GAME OVER -- You lost the risky trade! Ran out of money. LOSE ALL HEALTH")
                            health = 0
                        if game_credits <= 0:
                            print(f"GAME OVER -- You lost the risky trade! Ran out of credits. LOSE ALL HEALTH")
                            health = 0
                        print(f"You got {health_risky_trade_amount} health!")
                        health = health + health_risky_trade_amount
                    elif what_you_want_for_risk_trade == 'credits':
                        print(f"You get {credits_risky_trade_amount}! You give ${money_risky_trade_amount}!")
                        money = money - money_risky_trade_amount
                        game_credits = game_credits + credits_risky_trade_amount
                        print(f"You have ${money} and {game_credits} credits")
                        if money <= 0:
                            print(f"GAME OVER -- You lost the risky trade! Ran out of money. LOSE ALL HEALTH")
                            health = 0
                        if game_credits <= 0:
                            print(f"GAME OVER -- You lost the risky trade! Ran out of credits. LOSE ALL HEALTH")
                            health = 0
                        print(f"You got {health_risky_trade_amount} health!")
                        health = health + health_risky_trade_amount
                    else:
                        print(f"FOLLOW DIRECTIONS!!! YOU LOST SO MUCH STUFF! See stats for updates...")
                        money -= random.randint(1, 1_500_000)
                        health -= random.randint(25, 70)

            if result == 'best friend':
                print(f"You get a best friend! Cool!")
                best_friend_health = random.randint(10, 20)
                money += random.randint(10, 100)
                print(f"YES!!! You got {best_friend_health} health from your BEST friend! You also got some money!")
            
            if result == 'eminem':
                print(f"You were watching rap music, eminem!")
                health -= 1
                print(f"You have {health} health left!")
            
            if result == 'sofa':
                print(f"You want a sofa!")
                time.sleep(1)
                what_sofa = int(input("How much money you want to spend for your sofa? $"))
                if what_sofa <= 100:
                    money = money - what_sofa
                    print(f"Nice try! You get no sofa...")
                elif what_sofa <= 500:
                    money = money - what_sofa
                    print(f"You have a okay sofa!")
                    health += 10
                    game_credits += 0.1
                elif what_sofa <= 1000:
                    money = money - what_sofa
                    print(f"You have a good sofa!")
                    health += 20
                    game_credits += 0.5
                elif what_sofa <= 10000:
                    money = money - what_sofa
                    print(f"You have a nice sofa!")
                    health += 100
                    game_credits += 0.5
                else:
                    money = money - what_sofa
                    print(f"You have a AWESOME sofa!")
                    health += 200
                    game_credits += 0.75
            
            if result == 'story mode':
                print(f"Do you want to enter the story mode for fun? {time.sleep(1)} \n\nThis game has inapropriate content!!!")
                enter_story_mode = input("Do you want to do it? (yes, no)  ")
                if enter_story_mode == 'no':
                    print(f"Ok, have a nice life!")
                    health -= random.randint(1, 10)
                    print(f"You have {health} health left!")
                else:
                    print(f"If you win, you get a random big money amount!!!")
                    def dfhjsksfjsdfh3i3u2tr38oiasdfhu34qofoqew8fq2f3u8alfjewuf832quofl32io8rfr3489crynfiouwndsuioqj8nrdhiouasyr47rwo(anything):
                        """
                        Play the secret story mode game right now when you call the function. 
                        Please be aware this may have inappropriate content. Hope you enjoy the story mode! This is interactive!
                        Enter anything inside the parenthesis to start the game just to avoid robots!
                        """
                        
                        print(f"You entered '{anything}'... Lets start the game NOW!!! ")
                        message = input("\n\n\n\n\n\nHOW THE FUCK U FOUND THIS PIECE??!!: ")
                        if message != "IDK":
                            print("That's it you nigger ass bitch, its over!!! (fucking asshole)")
                            print("Game Over")
                        else:
                            name = input("Ohhh, my bad for underestimating your DUMBNESS, guess you are??? (your name): ")
                            print(f"Hello, {name.title()}...")
                            print("You do not belong here bitch!!!: ")
                            magic_word = input("If you say my MAGIC word, I shall reward you with $100000, if you fail, YOU DIE BITCH!!!: ")
                            
                            
                            
                            if magic_word == "dick":
                                print(f"Ok {name.title()}, I guess your aren't a nigger-ass dick! Your a skinny bitch cock! Here is ur $100000 and get outa here before I kill u!!!!!!!")
                                yes = input("Say 'yes' if you understand!: ")
                                if yes != "yes":
                                    print("YOU SHALL DIE FOR DISRESPECTING ME!!!!!!")
                                    print("Game Over")
                                else:
                                    print("Ok, you win, here is an extra $500000 and you shall be my royal servent!!!")
                                    print("Before, Here is some tests to qualify. Many failed!")
                                    q1 = input("What is 1+1?: ")
                                    q1 = int(q1)
                                    if q1 == 2:
                                        print("Ok, you are correct! That was easy!")
                                        q2 = input("What kind of button will NEVER unbutton???: ")
                                        if q2 == "belly button":
                                            print("You are correct, you are ready for the LAST challenge!")
                                            
                                            
                                            q3 = input("Will you fight me?: ")
                                            if q3 != "yes":
                                                print("YOU SHALL BE SQUASHED AND RETURN TO THE HUMAN WORLD ASSHOLE! ur lucky i spared u")
                                                die = input("You understand: ")
                                                if die == "yes":
                                                    print("YOU RETURNED TO THE HUMAN WORLD empty handed!!!")
                                                    print("You Lost 50%")
                                                else:
                                                    print("YOU WILL DIE FOPR DISRESPECTING ME FUCKING NIGGER!!!")
                                                    print("Game Over")
                                            else:
                                                duel = input("Ok choose your stratergy, (offence OR defence): ")
                                                if duel != "defence":
                                                    print("You lost the fight, the monster defended that attack and thrown you!!!")
                                                    print("Game Over")
                                                else:
                                                    print("Ok, you survived the attack by 1% !!! The monster is frustrated")
                                                    print("The monster attacked you and now you are almost nearly dying! You find a potion and drank it! You are feeling better.")
                                                    duel_2 = input("Choose your next stratergy: ")
                                                    if duel_2 != "defence":
                                                        print("You lost the fight, the monster defended that attack and thrown you!!!")
                                                        print("Game Over")
                                                    else:
                                                        print("You survived less than 1%. You find a potion but it is on the other side!")
                                                        chance = input("Will you get the potion? ('yes' or 'no'): ")
                                                        if chance != "yes":
                                                            print("The monster came to you and did a BIG BLOW and you died")
                                                            print("Game Over")
                                                        else:
                                                            print("You ran and drank the potion succesfully! You also gained some extra strength")
                                                            duel_3 = input("Choose your next stratergy: ")
                                                            
                                                            if duel_3 != "offence":
                                                                print("You are DEAD, you tried to defend the monster's attack, but your were not prepared and died!")
                                                                print("Game Over")
                                                            
                                                            else:
                                                                print("You punched the monster so hard, the monster collapsed and died! You Won the Fight!")
                                                                print("Now You have lots of money!!! (over 10 million dollars)")
                                                                
                                                                
                                                                q4 = input("Do you want to return to the human world? ('yes' or 'no'): ")
                                                                if q4 == "yes":
                                                                    print("You went back to human world, got a good wife (Laksha), good job, good finance including houses and cars, and you have a very pleasant life")
                                                                    print("Besides, you and your wife (Laksha) kissed for the first time!!!")
                                                                    breakup = input("You want to break up with Laksha? ('yes' or 'no'): ")
                                                                    if breakup == "yes":
                                                                        print("Laksha left you the next day after you told her 'I want to break up with you'")
                                                                        print("After a couple of weeks, you felt guilty and tried to make up with her")
                                                                        print("Laksha did not want to marry you again!")
                                                                        print("You felt really sad and died out of sadness!")
                                                                        print("Game Over")
                                                                    else:
                                                                        print("Your life was at peace. Your life is very easy since you are rich!")
                                                                        print(f"{name.title()} and Laksha had many pleasant memories together!")
                                                                        print("\n\n\nIn summary, you had a happy life!")
                                                                        print("You Won")
                                                                        play_again = input("You want to play 'PART 2'?")
                                                                        if play_again == "yes":
                                                                            print("The game is about to start!")
                                                                   
                                                                            print("\n\n\n\n\n\nMeanwhile, you and your wife are enjoying the view.")
                                                                            print("You are enjoying your time of your life!")
                                                                            print("Then, you went inside to get a refill of coffee.")
                                                                            print("Then, when you came back outside, Laksha is gone")
                                                                            wife = "laksha"
                                                                            tcasewife = wife.title()
                                                                            first_reaction = input("What will you do? ('search nearby' or 'call the cops'): ")
                                                                            if first_reaction == "search nearby":
                                                                                print("You tried, but some random person scared your life out of existence!")
                                                                                print("He choked you until you died!")
                                                                                print("Game Over")
                                                                            elif first_reaction == "call the cops":
                                                                                print("You managed to get into your house and called the cops to help you find your wife")
                                                                                print(f"You are wondering if {tcasewife} is ok and safe. Is she actually coming back? Is this a prank?")
                                                                                second_option = input("choose an option, 'Hopes she comes back later' or 'call the cops'?: ")
                                                                                if second_option == "Hopes she comes back later":
                                                                                    print("You ignored her absence, hoping she'll come back.")
                                                                                    print(f"The next day, you heard news that {tcasewife} is dead!")
                                                                                    print("You got a heart attack at the sudden news and you died.")
                                                                                    print("Game Over")
                                                                                else:
                                                                                    print("You called the cops on her absence.")
                                                                                    print("You are in a deep panic and you counted the numbers 1-20.")
                                                                                    current_number = 1
                                                                                    while current_number <= 20:
                                                                                        print(current_number)
                                                                                        current_number += 1
                                                                                    print("The cops asked you to come to the station tomorrow.")
                                                                                    print("The next day, you are at the police station")
                                                                                    print("The cops are asking you questions...")
                                                                                    cop_q1 = input("What is your first name in title case form: ")
                                                                                    if cop_q1 == name.title():
                                                                                        print("Ok, lets proceed")
                                                                                        age = input("So, what year are you born? Current year is 2023 (full form)(example is 2023): ")
                                                                                        age = int(age)
                                                                                        if age <= 2005:
                                                                                            print("Ok, you are ready to take action!")
                                                                                            print("Lets find your wife.")
                                                                                            cop_q2 = input("What is your wife full name in title case form: ")
                                                                                            if cop_q2 == wife.title():
                                                                                                print("Yes! I think I found her!")
                                                                                                print("I rescued from the kidnap that Ethan did. Ethan is the kidnapper. He is a very famous one. We caught him and we arrested him. Sadly, you can't talk to him because it's a rule.")
                                                                                                print("So yeah, but I found your wife. She is waiting for you at home. We are sending her home after 1 day.")
                                                                                                cop_q3 = input("So please can you leave. This is a very serious question ('yes' or 'no'): ")
                                                                                                if cop_q3 == 'yes':
                                                                                                    print(f"Thank you {name.title()}")
                                                                                                    print("After that, you went home and waited for one day")
                                                                                                    print(f"The next day you met with your wife, {tcasewife}")
                                                                                                    print(f"{name.title()} and {wife.title()} went out for celebration. They had so much moments and celebrations today!")
                                                                                                    the2nd_last_question = input("Your wife asked you if you can quit your job. Reply your answer: ('yes' or 'no') ")
                                                                                                    if the2nd_last_question != "yes":
                                                                                                        print(f"Your wife, {wife.title()} is a bit sad, but understood. This worked for everybody.")
                                                                                                        last_question = input("Your wife asked you how many hours per day will you work. reply your answer in numeric form: ")
                                                                                                        last_question = int(last_question)
                                                                                                        if last_question <= 8:
                                                                                                            print("Your wife is fine with that.")
                                                                                                            print("She excitment for the adventures they will face in the future.")
                                                                                                            print(f"{name} and {tcasewife}, lived happily ever after!!!")
                                                                                                            print("\n\n\nYou Won")
                                                                                                            part_3 = input("Do you want to play part 3??? (yes,no)  ")
                                                                                                            if part_3 == "no":
                                                                                                                print("That's ok, have a nice day!")
                                                                                                            else:
                                                                                                                print(f"The game is about to start, {name.title()}")
                                                                                                                print("Here are the rules: ")
                                                                                                                print("1. When you lose, you will not have a sign called 'game over', you will not have anything!")
                                                                                                                print("2. When you lose, you automatically die. (even though you didn't mention it)")
                                                                                                                print(f"\n\n\n\n\n\n\n\n\n\n\n\nThe monster from 'part 1' kidnapped you again when you are chilling with {tcasewife}")
                                                                                                                print("Now continuing to the present...")
                                                                                                                starter = input("Hello, do you want to continue?  ")
                                                                                                                starter2 = input(f"LAST CHANCE!!!, do you want to continue?, {name.title()}  ")
                                                                                                                if starter2 == "no":
                                                                                                                    print("Welp, I guess YOUR DONE!!!")
                                                                                                                else:
                                                                                                                    print("Hello, I promise I won't say any cuss words!!!")
                                                                                                                    print("I heard you want to unlock the secret vault...")
                                                                                                                    print("Ok, to unlock the secret vault, answer some locked questions")
                                                                                                                    q1 = input("What is 342879398234 + 234903249039 * 473284923 ?   ")
                                                                                                                    q1 = int(q1)
                                                                                                                    if q1 != 111176166476752337231:
                                                                                                                        print(f"WOW, you think you can open the vault by not answering the simple question?, {name.title()}")
                                                                                                                        print("Your dumb. You can never open the vault.")
                                                                                                                    else:
                                                                                                                        you_sure = input("You sure that is the answer? (yes, no) ")
                                                                                                                        if you_sure == "no":
                                                                                                                            print(f"Haha, this is the answer {name.title()}. You need confidence to access this vault.")
                                                                                                                        else:
                                                                                                                            print("Ok... your correct")
                                                                                                                            print("next question.....")
                                                                                                                            q2 = input("What kind of button will never unbutton? (all lowercase letters)  ")
                                                                                                                            if q2 == "belly button":
                                                                                                                                print(f"Yes... you are kinda smart!, {name.title()}")
                                                                                                                                print("Next question!")
                                                                                                                                q3 = input("What can a child make, but not see? (enter answer in lowercase form) ")
                                                                                                                                if q3 != "noise":
                                                                                                                                    print("Your completely wrong. You need smarts and a good fashioned brain to enter this vault")
                                                                                                                                else:
                                                                                                                                    print("Ok, your pretty good!")
                                                                                                                                    print("Last question: ")
                                                                                                                                    q4 = input(f"What is the most longest word in titlecase form?, {name.title()}  ")
                                                                                                                                    if q4 == "Pneumonoultramicroscopicsilicovolcanoconiosis":
                                                                                                                                        print("Great Job! Your qualified into the vault... maybe?  ")
                                                                                                                                        q4_5 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ndu u want t enter no vault? ")
                                                                                                                                        if q4_5 == "yes":
                                                                                                                                            print("Ha, that is a trick question or...")
                                                                                                                                            print(f"Maybe you don't want to go. I guess goodbye, {name.title()}!")
                                                                                                                                        else:
                                                                                                                                            print("Ok fine. you. want. to. go. to vault. hmm")
                                                                                                                                            print("If you want I will give you 10 thousand cents and leave. Is that ok? ")
                                                                                                                                            q4_7 = input("IS THAT FINE WITH YOU???!?!?!? ")
                                                                                                                                            if q4_7 != "no":
                                                                                                                                                print("Good. take it and leave. Don't ever come to me again. (you got scammed)")
                                                                                                                                            else:
                                                                                                                                                print(f"Ugh your stubborn as a donkey, {name.title()}!!! If you want to go inside, answer some bonus questions!")
                                                                                                                                                q5 = input("What is the question you cannot say yes to? (lowercase form with question mark) ")
                                                                                                                                                if q5 == "are you asleep?":
                                                                                                                                                    print("Ugh, your kinda smart. gettin on my nerves.")
                                                                                                                                                    print("Fine then. Next question")
                                                                                                                                                    q6 = input("What does DNA stand for??? (title case form) ")
                                                                                                                                                    if q6 == "Deoxyribonucleic Acid":
                                                                                                                                                        print("OH MY GOD, YOU ARE INCREDABLY SMART!!!")
                                                                                                                                                        print(f"{name.title()}, you may actually win!!! ")
                                                                                                                                                        q7 = input("Do we all have the same DNA??? (lowercase form) ")
                                                                                                                                                        if q7 == "no":
                                                                                                                                                            print("Obviously you will get it correct, NERD!!!")
                                                                                                                                                            print("Ok next question...")
                                                                                                                                                            q8 = input("What is the name of the person who Taylor Swift is dating. 2023??? (title case)  ")
                                                                                                                                                            if q8 != "Travis Kelce":
                                                                                                                                                                print(f"You need to learn social events and keep track to enter this vault, {name.title()}.")
                                                                                                                                                            else:
                                                                                                                                                                print("Hmmmm, you actually aren't that much of a nerd. Nice... i guess")
                                                                                                                                                                q9 = input("Along with that question, who is Taylor Swift's ex-boyfriend first name in title case form???  ")
                                                                                                                                                                if q9 == "Joe":
                                                                                                                                                                    print("Correct")
                                                                                                                                                                    print("I guess you have your last question!!!")
                                                                                                                                                                    print("If you fail, you are DONE. ")
                                                                                                                                                                    q10 = input(f"Who is the most popular NBA player in 2024???, {name.title()} (uppercase form) ")
                                                                                                                                                                    if q10 == "LEBRON JAMES":
                                                                                                                                                                        print("Wow, you sure know a lot. I'm really sorry for doubting you")
                                                                                                                                                                        print("You may enter the vault.")
                                                                                                                                                                        print(" **You entered the vault** ")
                                                                                                                                                                        print("Choose a chest to open and leave")
                                                                                                                                                                        last_question = input(f"What chest will you open, {name.title()}? (1, 2, 3)  ")
                                                                                                                                                                        last_question = int(last_question)
                                                                                                                                                                        if last_question == 1:
                                                                                                                                                                            print("Nice, you got $10000 and 50 diamonds!!!")
                                                                                                                                                                            print("You got the 2nd best reward")
                                                                                                                                                                            print("You lost 75%")
                                                                                                                                                                        elif last_question == 2:
                                                                                                                                                                            print("Great, you got $1000")
                                                                                                                                                                            print("You got the last best reward")
                                                                                                                                                                            print("You lost 50%")
                                                                                                                                                                        elif last_question == 3:
                                                                                                                                                                            print("Awesome, you got $1000000 and 100 diamonds.")
                                                                                                                                                                            print("You got the best reward and WON THE GAME!!!")
                                                                                                                                                                        else:
                                                                                                                                                                            print("Sorry, your answer is out of range or invalid syntax>>>")
                                                                                                                                                                        print(f"Congrats for entering the vault, {name.title()}. Unless you entered the wrong output, I hope you enjoyed the reward.")
                                                                                                                                                                        print("NOW GET OUT OF HERE BEFORE I GET MAD!!!")
                                                                                                                                                                        print(f"You ran away and felt happy you entered the vault with a happy face. You finally had fun with {wife.title()}")
                                                                                                                                                                    else:
                                                                                                                                                                        print(f"You need to know about entertainment like sports to enter this secret vault, {name.title()}. I could only give you $100 for your participation and effort")
                                                                                                                                                                        
                                                                                                                                                                else:
                                                                                                                                                                    print("Come on, learn a bit more. GET OUT OF HERE.")
                                                                                                                                                                    
                                                                                                                                                        else:
                                                                                                                                                            print(f"HOW THE HELL YOU GOT THAT WRONG, {name.title()}.")
                                                                                                                                                    else:
                                                                                                                                                        print("Finally, you got something wrong. Learn science to access this vault. I will not give you anything and get out of my sight!")

                                                                                                                                                else:
                                                                                                                                                    print("Haha you failed. Goodbye.")
                                                                                                                                    else:
                                                                                                                                        print("Your wrong, pay attention to directions")
                                                                                                                                        print("You need ELA and academic knowledge to qualify into this vault.")
                                                                                                                            else:
                                                                                                                                print("NOPE!!! Wrong answer. You need a sense of humor to enter this vault")
                                                                                                                                print("Make sure you write your answer in all lowercase form!!!")

                                                                                                        
                                                                                                        else:
                                                                                                            print("Your wife says she will leave you now for working too much")
                                                                                                            print(f"You miss {tcasewife} so much, you died!")
                                                                                                            print("Game Over")
                                                                                                    else:
                                                                                                        print("Your wife is happy.")
                                                                                                        print("After a few days, the cops took away your house")
                                                                                                        print("You and Laksha are really sad and you both commit suicide")
                                                                                                        print("Game Over")
                                                                                                else:
                                                                                                    print("Do NOT DESRESPECT ME. You are under arrest.")
                                                                                                    print("You died after one week of prison")
                                                                                                    print("Game Over")
                                                                                            else:
                                                                                                print("Sorry, I did not heard of her!")
                                                                                                print("Please wait about 4-5 years because we have some other cases to do.")
                                                                                                print(f"After the cop stated that, you felt really upset and died because you couldn't bear the loss of your wife, {tcasewife}")
                                                                                                print("Game Over")
                                                                                        else:
                                                                                            print("Sorry, you cannot take action. Please contact a valid 18 year old!")   
                                                                                            print("After the cop stated that, you got very upset and lived a miserable life.")
                                                                                            print("You Lost 50%")
                                                                                    else:
                                                                                        print(f"You are wrong, liar!!!! I saw your name tag just before and your name is {name.title()}")
                                                                                        print("You are a fucking liar. I will not help a liar. Go home!!!")
                                                                                        print("After the cop said that, you fell down, got a heart attack and died.")
                                                                                        print("Game Over")
                                                                            else:
                                                                                print("Sorry, that is not a valid answer.")
                                                                        else:
                                                                            print(f"We got it {name.title()}, You won the game! Hope you enjoy your day!")
                                                                else:
                                                                    print("You lived there for a couple of days, enjoying the food there!")
                                                                    print("Suddenly, a huge storm came. The storm rushed down your palace and burned it!")
                                                                    print("You died in the accident!")
                                                                    print("Game Over")
                                        
                                        else:
                                            print("That is a huge disrespect cock dick! You are surely a fucking asshole. You shall be in thew dungeons for the rest of ur life, DICK!!!")
                                            print("You Lost 50%")
                                    else:
                                        take = input("You do not DESERVE to be my servent BITCH. You are very dumb. I will take that money!: ")
                                        if take == "ok":
                                            print("Ok, I will spare your life, but LEAVE ASSHOLE!!!!")
                                            print("You Lost 50%")
                                        else:
                                            print("YOU DISRESPECTED ME????!!?!?!??! YOU WILL DIE BITCH-ASS!!!")
                                            print("Game Over")
                            else:
                                print("PREPARE TO DIE, fucking ass nigger dick bitch cock!!! YOU WILL LEAVE THIS WORLD!!!")
                                print("Game Over")
                    dfhjsksfjsdfh3i3u2tr38oiasdfhu34qofoqew8fq2f3u8alfjewuf832quofl32io8rfr3489crynfiouwndsuioqj8nrdhiouasyr47rwo('anything')
                    msg_for_money = input("You want money? (yes, no)  ")
                    if msg_for_money == 'yes':
                        game_participation_award = random.randint(-50000, 100_000)
                        money = money + game_participation_award
                        print(f"You earned ${game_participation_award}!")
                    else:
                        print(f"Ok, have a nice day!")
                    
            if result == 'school':
                do_you_want_to_go_to_school = input("Do you want to go to school to increase salary for $100,000? (yes, no)  ")
                if do_you_want_to_go_to_school == 'yes':
                    print(f"Lets see if you can go to school...")
                    time.sleep(15)
                    if has_job == True:
                        print(f"You want to go back to school and increase your salary? ($100,000)")
                        if money >= 100_000:
                            print(f"You went back to school and paid $100,000! Lets see your salary increase for your work.")
                            money -= 100000
                            time.sleep(3)
                            increased_salary_amount = round(random.uniform(1, 3), 2)
                            salary = salary * increased_salary_amount
                            print(f"Your salary is now ${salary} per day!")
                        else:
                            print(f"You don't have enough money to go back to school!")
                    else:
                        print(f"Sorry, you got rejected to go to school because no job application(s) or degree.")
                else:
                    print(f"Ok, enjoy your life!")

            if result == 'get money':
                if has_wife == True:
                    want_money = input("u want monei? ")
                    print(f"Either 'yes' or 'no', you are participating in this because your wife/husband forced you!")
                    print(f"Guess my 2-digit number password to earn money. The less attempts you take to win, the more money you get!")
                    two_digit_password = random.randint(10, 99)
                    attempts_for_success = 0
                    can_guess = True
                    time.sleep(2)
                    while can_guess:
                        guess_digit = input("Guess the number: ")
                        guess_digit = int(guess_digit)
                        attempts_for_success += 1
                        if guess_digit == two_digit_password:
                            print(f"You win!")
                            print(f"It took you {attempts_for_success} attempts to win.")
                            if attempts_for_success <= 1:
                                if game_difficulty == 'hardcore':
                                    guess_money = 2_500_000
                                elif game_difficulty == 'hard':
                                    guess_money = 3_000_000
                                elif game_difficulty == 'medium':
                                    guess_money = 4_000_000
                                elif game_difficulty == 'easy':
                                    guess_money = 5_000_000
                            elif attempts_for_success <= 5:
                                if game_difficulty == 'easy':
                                    guess_money = 2_500_000
                                else:
                                    game_difficulty = 1_500_000
                            elif attempts_for_success <= 10:
                                if game_difficulty == 'easy':
                                    guess_money = 1_000_000
                                elif game_difficulty == 'medium':
                                    guess_money = 1_000_000
                                else:
                                    guess_money = 875_000
                            elif attempts_for_success <= 15:
                                guess_money = 750_000
                            elif attempts_for_success <= 30:
                                if game_difficulty == 'easy':
                                    guess_money = 500_000
                                elif game_difficulty == 'medium':
                                    guess_money = 100_000
                                elif game_difficulty == 'hard':
                                    guess_money = 25_000
                                elif game_difficulty == 'hardcore':
                                    guess_money = 5000
                            elif attempts_for_success <= 40:
                                guess_money = 1000
                            elif attempts_for_success <= 50:
                                if game_difficulty == 'easy':
                                    guess_money = 0
                                else:
                                    guess_money = -5000
                            elif attempts_for_success <= 65:
                                if game_difficulty == 'hardcore':
                                    guess_money = -100_000
                                else:
                                    guess_money = -10000
                            elif attempts_for_success <= 80:
                                if game_difficulty == 'hardcore':
                                    guess_money = -500_000
                                else:
                                    guess_money = -100_000
                            else:
                                if game_difficulty == 'hardcore':
                                    guess_money = -5_000_000
                                elif game_difficulty == 'hard':
                                    guess_money = -4_000_000
                                elif game_difficulty == 'medium':
                                    guess_money = -2_500_000
                                elif game_difficulty == 'easy':
                                    guess_money = -1_500_000
                            print(f"You got ${guess_money}!")
                            money = money + guess_money
                            print(f"You now have ${money}.")
                            can_guess = False
                        else:
                            print(f"Wrong, guess again! {attempts_for_success} attempts so far!")
                else:
                    want_money = input("u want monei? (yes, no) ")
                    if want_money == 'no':
                        print(f"Ok! Have a nice day.")
                    else:
                        print(f"Guess my 2-digit number password to earn money. The less attempts you take to win, the more money you get!")
                        two_digit_password = random.randint(10, 99)
                        attempts_for_success = 0
                        can_guess = True
                        time.sleep(2)
                        while can_guess:
                            guess_digit = input("Guess the number: ")
                            guess_digit = int(guess_digit)
                            attempts_for_success += 1
                            if guess_digit == two_digit_password:
                                print(f"You win!")
                                print(f"It took you {attempts_for_success} attempts to win.")
                                if attempts_for_success <= 1:
                                    if game_difficulty == 'hardcore':
                                        guess_money = 2_500_000
                                    elif game_difficulty == 'hard':
                                        guess_money = 3_000_000
                                    elif game_difficulty == 'medium':
                                        guess_money = 4_000_000
                                    elif game_difficulty == 'easy':
                                        guess_money = 5_000_000
                                elif attempts_for_success <= 5:
                                    if game_difficulty == 'easy':
                                        guess_money = 2_500_000
                                    else:
                                        game_difficulty = 1_500_000
                                elif attempts_for_success <= 10:
                                    if game_difficulty == 'easy':
                                        guess_money = 1_000_000
                                    elif game_difficulty == 'medium':
                                        guess_money = 1_000_000
                                    else:
                                        guess_money = 875_000
                                elif attempts_for_success <= 15:
                                    guess_money = 750_000
                                elif attempts_for_success <= 30:
                                    if game_difficulty == 'easy':
                                        guess_money = 500_000
                                    elif game_difficulty == 'medium':
                                        guess_money = 100_000
                                    elif game_difficulty == 'hard':
                                        guess_money = 25_000
                                    elif game_difficulty == 'hardcore':
                                        guess_money = 5000
                                elif attempts_for_success <= 40:
                                    guess_money = 1000
                                elif attempts_for_success <= 50:
                                    if game_difficulty == 'easy':
                                        guess_money = 0
                                    else:
                                        guess_money = -5000
                                elif attempts_for_success <= 65:
                                    if game_difficulty == 'hardcore':
                                        guess_money = -100_000
                                    else:
                                        guess_money = -10000
                                elif attempts_for_success <= 80:
                                    if game_difficulty == 'hardcore':
                                        guess_money = -500_000
                                    else:
                                        guess_money = -100_000
                                else:
                                    if game_difficulty == 'hardcore':
                                        guess_money = -5_000_000
                                    elif game_difficulty == 'hard':
                                        guess_money = -4_000_000
                                    elif game_difficulty == 'medium':
                                        guess_money = -2_500_000
                                    elif game_difficulty == 'easy':
                                        guess_money = -1_500_000
                                print(f"You got ${guess_money}!")
                                money = money + guess_money
                                print(f"You now have ${money}.")
                                can_guess = False
                            else:
                                print(f"Wrong, guess again! {attempts_for_success} attempts so far!")
        if welcome_message == 'gamble':
            actions_count += 1
            if game_difficulty == 'hardcore':
                health = health - random.randint(5, 10)
            else:
                health = health - random.randint(1, 5)
            print(f"You currently have {health} health.")
            # Gambling logic
            gamble_choice = input("Choose your gambling option (slot, roulette, blackjack): ").lower()
            if gamble_choice == 'slot':
                # Slot machine logic
                bet_amount = int(input("Enter the amount you want to bet: "))
                if bet_amount > money:
                    print("You don't have enough money to place that bet.")
                else:
                    money -= bet_amount
                    symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
                    result = [random.choice(symbols) for _ in range(3)]
                    print(f"Slot machine result: {' - '.join(result)}")
                    if all(symbol == result[0] for symbol in result):
                        winnings = bet_amount * 3  # You win triple the bet amount for a matching set
                        money += winnings
                        print(f"You won {winnings} dollars!")
                        money = money + winnings
                    else:
                        lost_amount = bet_amount
                        print(f"Sorry, you lost {lost_amount} dollars.")
                        money = money - lost_amount
            elif gamble_choice == 'roulette':
                # Roulette logic
                bet_amount = int(input("Enter the amount you want to bet: "))
                if bet_amount > money:
                    print("You don't have enough money to place that bet.")
                else:
                    money -= bet_amount
                    color_choice = input("Choose your color (red, black): ").lower()
                    if color_choice not in ['red', 'black']:
                        print("Invalid color choice. Please choose red or black.")
                    else:
                        result_color = random.choice(['red', 'black'])
                        print(f"Roulette result: {result_color}")
                        if color_choice == result_color:
                            winnings = bet_amount * 2  # You win double the bet amount for a correct color
                            money += winnings
                            print(f"You won {winnings} dollars!")
                            money = money + winnings
                        else:
                            lost_amount = bet_amount
                            print(f"Sorry, you lost {lost_amount} dollars.")
                            money = money - lost_amount
            elif gamble_choice == 'blackjack':
                # Blackjack logic
                bet_amount = int(input("Enter the amount you want to bet: "))  # Define bet_amount for blackjack
                player_hand = [random.randint(1, 11), random.randint(1, 11)]
                dealer_hand = [random.randint(1, 11), random.randint(1, 11)]
                print(f"Your hand: {player_hand}")
                print(f"Dealer's hand: {dealer_hand[0]}")
                while sum(player_hand) < 21:
                    action = input("Do you want to hit or stand? ").lower()
                    if action == 'hit':
                        player_hand.append(random.randint(1, 11))
                        print(f"Your hand: {player_hand}")
                    elif action == 'stand':
                        break
                    else:
                        print("Invalid action. Please choose hit or stand.")
                while sum(dealer_hand) < 17:
                    dealer_hand.append(random.randint(1, 11))
                print(f"Your final hand: {player_hand}")
                print(f"Dealer's final hand: {dealer_hand}")
                if sum(player_hand) > 21 or (sum(dealer_hand) <= 21 and sum(dealer_hand) >= sum(player_hand)):
                    lost_amount = bet_amount
                    print(f"Sorry, you lost {lost_amount} dollars.")
                    money = money - lost_amount
                else:
                    winnings = bet_amount * 2  # You win double the bet amount for winning the round
                    money += winnings
                    print(f"Congratulations! You won {winnings} dollars!")
                    money = money + winnings
            else:
                print("Invalid gambling option. Please choose slot, roulette, or blackjack.")
            print(f"You currently have ${money}.")
        
        if welcome_message == 'very hard math test':
            if game_difficulty == 'hardcore':
                health -= 25
            else:
                health -= random.randint(15, 25)
            print(f"You have {health} health left.")
            msg_for_math_enter = input("Do you want to enter the HARD math challenge to earn rewards? [harder than the action one] (yes, no):  ")
            if msg_for_math_enter == 'no':
                print(f"Ok, so long!")
                money -= random.randint(100, 2000)
                print(f"You have ${money} left.")
            else:
                actions_count += 1
                print("Great! If you lose, you lose money, every time you survive a round, you get credits.")
                print("When you win, you get money!")
                print("Here is round 1...")
                num1 = random.randint(1, 100000000)
                num2 = random.randint(1, 100000000)
                correct_answer = num1 + num2

                user_answer = int(input(f"What is {num1} + {num2}? "))
                if user_answer == correct_answer:
                    print(f"Great! You gained 0.05 credits.")
                    game_credits += 0.05
                    print(f"Lets start round 2...")
                    num1 = random.randint(100000, 100000000)
                    num2 = random.randint(100000, 100000000)
                    correct_answer = num1 - num2
                    user_answer = float(input(f"What is {num1} - {num2}? "))
                    if user_answer == correct_answer:
                        print(f"Great you gained 0.05 credits.")
                        game_credits += 0.05
                        print(f"Lets start round 3...")
                        num1 = random.randint(1, 100000)
                        num2 = random.randint(1, 100000)
                        correct_answer = num1 * num2
                        user_answer = int(input(f"What is {num1} * {num2}? "))
                        if user_answer == correct_answer:
                            print(f"Great, you gained 0.05 credits.")
                            game_credits += 0.05
                            print(f"Wow... Lets start round 4!")
                            num1 = random.randint(1, 100000)
                            num2 = random.randint(1, 100000)
                            correct_answer = round(num1 / num2, 2)
                            user_answer = float(input(f"What is {num1} ÷ {num2}? Round to nearest hundreth if nessesary! "))
                            if user_answer == correct_answer:
                                print("Great! You earned 0.05 credits.")
                                game_credits += 0.05
                                print(f"Lets start round 5... THE FINAL ROUND!!!")
                                num1 = random.uniform(100, 1000)
                                num2 = random.uniform(100, 1000)
                                num3 = random.uniform(10, 1000)
                                operator = random.choice(['+', '*', '/', '-'])
                                operator2 = random.choice(['+', '*', '/', '-'])
                                expression = f"{num1} {operator} {num2} {operator2} {num3}"
                                correct_answer = round(eval(expression), 2)
                                user_answer = float(input(f"What is {expression}? Round to nearest hundreth if nessesary! "))
                                if user_answer == correct_answer:
                                    print(f"Nice! You get 0.10 credits.")
                                    print(f"YOU DID IT!!! You get money, health, and much more. See your stats for updates.")
                                    game_credits += 0.05
                                    if game_difficulty == 'medium':
                                        health += 15
                                        money += 1_500_000
                                        game_credits += 0.01
                                    elif game_difficulty == 'easy':
                                        health += 20
                                        money += 1_500_000
                                        game_credits += 0.05
                                    elif game_difficulty == 'hard':
                                        health += 10
                                        money += 1_000_000
                                    else:
                                        health += 5
                                        money += 750_000
                                    
                                    if game_difficulty != 'hardcore':
                                        more_money_for_math_win = random.randint(1000, 100000)
                                        money = money + more_money_for_math_win
                                    
                                    bonusROUND = input("Do you want to enter the bonus rounds for more (less) money? [yes, no]  ")
                                    if bonusROUND == 'yes':
                                        print("Here comes round 6 out of 10...")
                                        num1 = random.uniform(10, 100)
                                        num2 = random.uniform(10, 100)
                                        num3 = random.uniform(10, 100)
                                        num4 = random.uniform(10, 100)
                                        operator = random.choice(['+', '*', '/', '-'])
                                        operator2 = random.choice(['+', '*', '/', '-'])
                                        operator3 = random.choice(['+', '*', '/', '-'])
                                        expression = f"{num1} {operator} {num2} {operator2} {num3} {operator3} {num4}"
                                        correct_answer = round(eval(expression), 2)
                                        user_answer = float(input(f"What is {expression}? Round to nearest hundreth if nessesary! "))
                                        if user_answer == correct_answer:
                                            print(f"Here is your 0.01 credits!")
                                            game_credits += 0.01
                                            print(f"Great! Lets continue to round 7...")
                                            num1 = random.uniform(100, 1000)
                                            num2 = random.uniform(100, 1000)
                                            num3 = random.uniform(100, 1000)
                                            operator = random.choice(['+', '*', '/', '-'])
                                            operator2 = random.choice(['+', '*', '/', '-'])
                                            expression = f"{num1} {operator} {num2} {operator2} {num3}"
                                            correct_answer = round(eval(expression), 2)
                                            user_answer = float(input(f"What is {expression}? Round to nearest hundreth if nessesary! "))
                                            if user_answer == correct_answer:
                                                print(f"Right! Your on track, and here is your 0.02 credits.")
                                                game_credits += 0.02
                                                print(f"Here goes round 8...")
                                                num1 = random.uniform(100, 1000)
                                                num2 = random.uniform(250, 1000)
                                                num3 = random.uniform(500, 1000)
                                                operator = random.choice(['+', '*', '/', '-'])
                                                operator2 = random.choice(['+', '*', '/', '-'])
                                                expression = f"{num1} {operator} {num2} {operator2} {num3}"
                                                correct_answer = round(eval(expression), 2)
                                                user_answer = float(input(f"What is {expression}? Round to nearest hundreth if nessesary! "))
                                                if user_answer == correct_answer:
                                                    print(f"Correct! Lets move on to line 9, round 9...")
                                                    print(f"You earn 0.02 credits!")
                                                    game_credits += 0.02
                                                    num1 = random.uniform(1, 9.25)
                                                    num2 = random.uniform(1, 9.25)
                                                    correct_answer = round(num1 ** num2, 2)
                                                    user_answer = float(input(f"What is {num1} ^ {num2}? Round to nearest hundreth if nessesary! "))
                                                    if user_answer == correct_answer:
                                                        print(f"Correct! Lets move on to THE FINAL ROUND, 10!")
                                                        game_credits += 0.02
                                                        print(f"You earned 0.02 credits!")
                                                        number_for_root_square = random.uniform(10, 100_000)
                                                        correct_answer = round(math.sqrt(number_for_root_square), 2)
                                                        user_answer = float(input(f"What is the square root of {number_for_root_square}? Round to nearest hundreth if nessesary! "))
                                                        if user_answer == correct_answer:
                                                            print(f"Nice! You get 0.05 credits.")
                                                            print(f"YOU DID IT!!! You get money, health, and much more. See your stats for updates.")
                                                            game_credits += 0.05
                                                            if game_difficulty == 'medium':
                                                                health += 15
                                                                money += 2_500_000
                                                                game_credits += 0.01
                                                            elif game_difficulty == 'easy':
                                                                health += 20
                                                                money += 3_500_000
                                                                game_credits += 0.05
                                                            elif game_difficulty == 'hard':
                                                                health += 10
                                                                money += 2_000_000
                                                            else:
                                                                health += 5
                                                                money += 1_750_000
                                                        else:
                                                            print(f"Wrong! Answer is {correct_answer}.")
                                                            loss_money_for_math = random.randint(900_000, 1_000_000)
                                                            money = money - loss_money_for_math
                                                            print(f"You lost ${loss_money_for_math}!")
                                                    else:
                                                        print(f"Wrong! Answer is {correct_answer}.")
                                                        loss_money_for_math = random.randint(750_000, 900_000)
                                                        money = money - loss_money_for_math
                                                        print(f"You lost ${loss_money_for_math}!")
                                                else:
                                                    print(f"Wrong! Answer is {correct_answer}.")
                                                    loss_money_for_math = random.randint(250000, 750000)
                                                    money = money - loss_money_for_math
                                                    print(f"You lost ${loss_money_for_math}!")
                                            
                                            else:
                                                print(f"Wrong! Answer is {correct_answer}.")
                                                loss_money_for_math = random.randint(100000, 750000)
                                                money = money - loss_money_for_math
                                                print(f"You lost ${loss_money_for_math}!")   
                                            
                                        else:
                                            print(f"Wrong! Answer is {correct_answer}.")
                                            loss_money_for_math = random.randint(100000, 500000)
                                            money = money - loss_money_for_math
                                            print(f"You lost ${loss_money_for_math}!")
                                    else:
                                        print(f"Ok, Have a nice day!")
                                else:
                                    loss_money_for_math = random.randint(100000, 500000)
                                    print(f"OH NO!!! You lost ${loss_money_for_math}")
                                    print(f"The correct answer is {correct_answer}!")
                                    money = money - loss_money_for_math
                                
                            else:
                                loss_money_for_math = random.randint(50000, 100000)
                                print(f"OH NO!!! You lost ${loss_money_for_math}.")
                                print(f"The correct answer is {correct_answer}!")
                                money = money - loss_money_for_math
                        else:
                            loss_money_for_math = random.randint(20000, 50000)
                            print(f"OH NO!!! You lost ${loss_money_for_math}.")
                            print(f"The correct answer is {correct_answer}!")
                            money = money - loss_money_for_math
                    else:
                        print("OH NO!!! You lost $20000")
                        print(f"The correct answer is {correct_answer}!")
                        money -= 20000
                else:
                    print(f"OH NO!!! You MAY lose $5000")
                    print(f"The correct answer is {correct_answer}!")
                    if game_difficulty != 'easy':
                        money -= 5000

        if welcome_message == 'wife/husband':
            if has_wife == True:
                print(f"You already have a wife/husband!")
            else:
                actions_count += 1
                health -= random.randint(10, 15)
                print(f"You have {health} health left.")
                wife_possibilities = ['yes', 'no']
                if_you_got_wife = random.choices(wife_possibilities, weights=[0.10, 0.90])[0]
                if if_you_got_wife == 'yes':
                    has_wife = True
                    if gender == 'male':
                        lover_names = ['amelia', 'angelina', 'olivia', 'ella', 'ellie', 'samira', 'emma', 'charlotte', 'ava', 'emily',
                                        'abigail', 'harper', 'evelyn', 'rylie', 'sophia', 'clara', 'chloe', 'natalie', 'mia', 'summer']
                    else:
                        lover_names = [
                        "Liam", "Noah", "Oliver", "Elijah", "William",
                        "James", "Benjamin", "Lucas", "Henry", "Alexander",
                        "Mason", "Ethan", "Logan", "Jackson", "Aiden",
                        "Sebastian", "Caleb", "Matthew", "Samuel", "David"
                        ]
                    ywn = random.choice(lover_names)
                    print(f"You got a wife/husband, her/his name is {ywn.title()}.")
                else:
                    print("Sorry, you didn't have any luck finding a lover!")
        
        if welcome_message == 'secret wheel_fortune23 gameisTRUE':
            actions_count += 1
            if game_difficulty == 'hardcore':
                health -= random.randint(150, 200)
            else:
                health -= random.randint(100, 150)
            print(f"You have {health} health left!")
            words = [
                "APPLE",
                "BOOK",
                "CANDLE",
                "DOG",
                "ELEPHANT",
                "FLOWER",
                "GUITAR",
                "HAPPINESS",
                "ICICLE",
                "JUNGLE",
                "KITE",
                "LAUGHTER",
                "MOUNTAIN",
                "NECKLACE",
                "OCEAN",
                "PINEAPPLE",
                "QUARTER",
                "RIVER",
                "SUNSHINE",
                "TIGER",
                "UMBRELLA",
                "VIOLIN",
                "WATERFALL",
                "XYLOPHONE",
                "YELLOW",
                "ZEBRA",
                "FIREWORKS",
                "JOURNEY",
                "SNOWFLAKE",
                "MOONLIGHT",
                "WISDOM",
                "DOLPHIN",
                "MYSTERY",
                "SYMPHONY",
                "WILDERNESS",
                "BUTTERFLY",
                "CLOCKWORK",
                "DREAM",
                "FANTASY",
                "GLACIER",
                "HORIZON",
                "LANTERN",
                "MEADOW",
                "NOVEL",
                "PARADISE",
                "QUEST",
                "SPARKLE"
                "BICYCLE",
                "CHOCOLATE",
                "DINOSAUR",
                "EXPLORER",
                "FIREPLACE",
                "GALAXY",
                "HARMONY",
                "INSPIRATION",
                "JOURNAL",
                "KANGAROO",
                "LANTERN",
                "MARATHON",
                "NOSTALGIA",
                "OASIS",
                "PARACHUTE",
                "QUEST",
                "RECIPE",
                "SUNFLOWER",
                "TREASURE",
                "UNICORN",
                "VOLCANO",
                "WILDFLOWER",
                "XANADU",
                "YESTERDAY",
                "ZEPPELIN",
                "AFRICAN",
                "BLOSSOM",
                "COASTAL",
                "DELIGHT",
                "ECLIPSE",
                "FREEDOM",
                "GALAXY",
                "HORIZON",
                "ILLUMINATE",
                "JUBILANT",
                "KALEIDOSCOPE",
                "LUMINOUS",
                "MAGICAL",
                "NURTURING",
                "OBLIVION",
                "PRECIOUS",
                "QUIETUDE",
                "RADIANCE",
                "SERENITY",
                "TRANQUILITY",
                "UTOPIA",
                "VELVET"
                "AMBER",
                "BREEZE",
                "CASCADE",
                "DREAMY",
                "ENCHANT",
                "FLUTTER",
                "GLOW",
                "HARMONY",
                "IGNITE",
                "JUBILANT",
                "KINETIC",
                "LULLABY",
                "MELODY",
                "NIRVANA",
                "OPULENT",
                "PLEASANT",
                "QUILL",
                "RADIANT",
                "SUBLIME",
                "TRIUMPH",
                "UNISON",
                "VIBRANT",
                "WONDER",
                "XYLOPHONE",
                "ZENITH",
                "ALABASTER",
                "BRILLIANT",
                "CASCADING",
                "DELICATE",
                "ELEGANT",
                "FANTASY",
                "GALLANT",
                "HORIZON",
                "ILLUMINATE",
                "JASMINE",
                "KALEIDOSCOPE",
                "LUMINOUS",
                "MAGICAL",
                "NEBULA",
                "OBLIVION",
                "PLEASURE",
                "QUEST",
                "RADIANCE",
                "SERENE",
                "TRANQUIL",
                "UTOPIA",
                "VELVET",
                "WHISPER",
                "AMETHYST",
                "BLISS",
                "CHARM",
                "DAZZLE",
                "ETHEREAL",
                "FABLE",
                "GRACE",
                "HALO",
                "IRIDESCENCE",
                "JOURNEY",
                "KEYNOTE",
                "LUMBER",
                "MIRAGE",
                "NOBLE",
                "ONYX",
                "PASTURE",
                "QUAGMIRE",
                "RUSTIC",
                "SCARLET",
                "TRANSCEND",
                "UPLIFT",
                "VELOCITY",
                "WILLOW",
                "XANADU",
                "YONDER",
                "ZEPHYR",
                "ADEPT",
                "BLISSFUL",
                "CHERISH",
                "DIVINE",
                "ETERNAL",
                "FABULOUS",
                "GENTLE",
                "HALCYON",
                "ILLUMINATE",
                "JUBILEE",
                "KISS",
                "LUXURIANT",
                "MELLOW",
                "NOURISH",
                "OPAL",
                "PURITY",
                "QUIESCENT",
                "RUSTLE",
                "SERENADE",
                "TRIUMPHANT",
                "UTOPIAN",
                "VIVID",
                "WANDER",
                "XOXO",
                "YEARNING",
                "ZEST"
                "ADVENTURE",
                "CLEVER",
                "CURIOUS",
                "DELIGHT",
                "DISCOVER",
                "EXCITING",
                "FRIENDSHIP",
                "GIGGLE",
                "IMAGINE",
                "JOURNEY",
                "LUCKY",
                "MYSTERY",
                "PLAYFUL",
                "SILLY",
                "SURPRISE",
                "TREASURE",
                "WONDERFUL",
                "BRAVE",
                "CHEERFUL",
                "COZY",
                "DAZZLING",
                "DELICIOUS",
                "ENCHANT",
                "FANTASTIC",
                "GENTLE",
                "HARMONY",
                "INVENT",
                "JOYFUL",
                "KINDNESS",
                "LIVELY",
                "MAGIC",
                "MARVEL",
                "NATURE",
                "OPTIMISTIC",
                "RADIANT",
                "SUNNY",
                "TALENT",
                "VIBRANT",
                "WHIMSICAL",
                "ADORABLE",
                "BALANCE",
                "CELEBRATE",
                "DANCE",
                "EFFORT",
                "EXPLORE",
                "FRIENDSHIP",
                "GENEROUS",
                "HEALTHY",
                "INSPIRE",
                "KNOWLEDGE",
                "LAUGHTER",
                "MOTIVATE",
                "NURTURE",
                "ORGANIZE",
                "POLITE",
                "QUEST",
                "RESPECT",
                "SMILE",
                "TEAMWORK",
                "UNDERSTANDING",
                "VALUE",
                "WISDOM",
                "YUMMY",
                "ZEAL",
                "ASTONISH",
                "BLOSSOM",
                "CLEVER",
                "DELIGHTFUL",
                "ENERGETIC",
                "FASCINATE",
                "GLORIOUS",
                "HEARTWARMING",
                "INVENTIVE",
                "JUBILANT",
                "KEEN",
                "LUMINOUS",
                "MAGNIFICENT",
                "NOBLE",
                "OUTSTANDING",
                "PLEASANT",
                "QUEST",
                "RADIANT",
                "SPECTACULAR",
                "THRILLING",
                "UNIQUE",
                "VIVID",
                "WHOLESOME",
                "YOUTHFUL",
                "ADVENTUROUS",
                "BRIGHT",
                "CHERISH",
                "CREATIVE",
                "DETERMINED",
                "EAGER",
                "FASCINATING",
                "GENUINE",
                "HAPPY",
                "IMAGINATIVE",
                "JOYOUS",
                "KINDHEARTED",
                "LIVELY",
                "MINDFUL",
                "NURTURING",
                "OPTIMISTIC",
                "PLAYFUL",
                "QUIRKY",
                "RADIANT",
                "SPIRITED",
                "THOUGHTFUL",
                "UPLIFTING",
                "VIVACIOUS",
                "WHOLESOME",
                "YOUTHFUL",
                "ZEALOUS",
                "AFFECTIONATE",
                "BRILLIANT",
                "CARING",
                "DILIGENT",
                "ENERGETIC",
                "FRIENDLY",
                "GENEROUS",
                "HONEST",
                "INQUISITIVE",
                "JOVIAL",
                "KIND",
                "LOVING",
                "MODEST",
                "NEIGHBORLY",
                "OPEN-MINDED",
                "PATIENT",
                "RESPONSIBLE",
                "SUPPORTIVE",
                "TALENTED",
                "UNDERSTANDING",
                "VALIANT",
                "WARMHEARTED",
                "XTRAORDINARY",  # Creatively using 'X' for extra fun!
                "YOUTHFUL",
                "ZESTY"
            ]
            selected_word = random.choice(words)
            guessed_letters = []
            max_attempts = 12
            
            print(f"Welcome to your favorite game!")
            time.sleep(1)
            print("Wheel.", end=" ")
            time.sleep(1)
            print("Of.", end=" ")
            time.sleep(1)
            print("Fortune!")
            time.sleep(1)
            while max_attempts > 0:
                print("\nAttempts left:", max_attempts)

                display_word = ""
                for letter in selected_word:
                    if letter in guessed_letters:
                        display_word += letter
                    else:
                        display_word += "_"
                print(" ".join(display_word))

                guess = input("Enter a letter: ").upper()

                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a valid single letter.")
                    continue

                if guess in guessed_letters:
                    print("You've already guessed that letter. Try again.")
                    continue

                guessed_letters.append(guess)

                if guess not in selected_word:
                    max_attempts -= 1
                    print("Incorrect guess!")

                if set(selected_word) <= set(guessed_letters):
                    print("\nCongratulations! You guessed the word:", selected_word)
                    money_amounts_for_wheel_of_fortune = [40000, 75000, 100000]
                    the_money_amount_for_wheel_of_fortune = random.choices(money_amounts_for_wheel_of_fortune, 
                                                                        weights=[0.90, 0.095, 0.005])[0]
                    money = money + the_money_amount_for_wheel_of_fortune
                    print(f"You get ${the_money_amount_for_wheel_of_fortune}\nNow you have ${money}!")
                    break

            if max_attempts == 0:
                print("\nSorry, you ran out of attempts. The word was:", selected_word)
        
        if welcome_message == 'lottery':
            actions_count += 1
            if game_difficulty == 'hardcore':
                health -= random.randint(20, 50)
            else:
                health -= random.randint(5, 20)
            print(f"You have {health} health!")
            what_lottery = input(f"You pick three kinds of lotteries... (easy, medium, hard)  ")
            
            if what_lottery == 'easy':
                def generate_lottery_numbers():
                    """Generate a list of 3 random numbers between 1 and 5."""
                    return random.sample(range(1, 6), 3)

                def buy_lottery_ticket():
                    """Allow the user to buy a lottery ticket."""
                    print("Welcome to the Easier Lottery! Good luck!")
                    input("Press Enter to buy a lottery ticket...")
                    return generate_lottery_numbers()

                def check_lottery_results(ticket_numbers, winning_numbers):
                    """Check if the ticket has won."""
                    matched_numbers = set(ticket_numbers).intersection(winning_numbers)
                    return len(matched_numbers)

                def run_lottery():
                    """Run the lottery."""
                    while True:
                        global health
                        health -= random.randint(5, 10)
                        lottery_ticket = random.randint(5, 10)
                        print(f"Ticket: ${lottery_ticket}")
                        global money
                        money = money - lottery_ticket
                        print(f"You have ${money} and {health} health")
                        winning_numbers = generate_lottery_numbers()
                        user_ticket = buy_lottery_ticket()

                        print("\nWinning Numbers:", winning_numbers)
                        matched_count = check_lottery_results(user_ticket, winning_numbers)

                        print("\nYou matched", matched_count, "number(s)!")
                        if matched_count == 3:
                            print("Congratulations! You won the jackpot!")
                            money_or_raise = input("Do you want money or a salary raise? (money, raise)   ")
                            if money_or_raise == 'money':
                                easy_lottery_total = random.randint(10_000, 25_000)
                                print(f"You got ${easy_lottery_total}")
                                money = money + easy_lottery_total
                                print(f"You now have ${money}")
                                global game_credits
                                game_credits += 0.25
                            else:
                                global has_job
                                if has_job:
                                    raise_salary = round(random.uniform(1, 2.5), 2)
                                    print(f"Raised salary:  {raise_salary}")
                                    global salary
                                    salary = salary * raise_salary
                                    print(f"Your salary is now ${salary}")
                                else:
                                    print(f"You don't have a job!")
                        else:
                            print("Better luck next time.")

                        play_again = input("\nDo you want to play again? (Enter 'quit' to exit): ").lower()
                        if play_again == 'quit':
                            break

                if __name__ == "__main__":
                    run_lottery()
            
            elif what_lottery == 'medium':
                def generate_lottery_numbers():
                    """Generate a list of 4 random numbers between 1 and 10."""
                    return random.sample(range(1, 11), 4)

                def buy_lottery_ticket():
                    """Allow the user to buy a lottery ticket."""
                    print("Welcome to the Lottery! Good luck!")
                    input("Press Enter to buy a lottery ticket...")
                    return generate_lottery_numbers()

                def check_lottery_results(ticket_numbers, winning_numbers):
                    """Check if the ticket has won."""
                    matched_numbers = set(ticket_numbers).intersection(winning_numbers)
                    return len(matched_numbers)

                def run_lottery():
                    """Run the lottery."""
                    while True:
                        global health
                        health -= random.randint(5, 10)
                        lottery_ticket = random.randint(5, 10)
                        print(f"Ticket: ${lottery_ticket}")
                        global money
                        money = money - lottery_ticket
                        print(f"You have ${money} and {health} health")
                        winning_numbers = generate_lottery_numbers()
                        user_ticket = buy_lottery_ticket()

                        print("\nWinning Numbers:", winning_numbers)
                        matched_count = check_lottery_results(user_ticket, winning_numbers)

                        print("\nYou matched", matched_count, "number(s)!")
                        if matched_count == 4:
                            print("Congratulations! You won the jackpot!")
                            money_or_raise = input("Do you want money or a salary raise? (money, raise)   ")
                            if money_or_raise == 'money':
                                easy_lottery_total = random.randint(100_000, 500_000)
                                print(f"You got ${easy_lottery_total}")
                                money = money + easy_lottery_total
                                print(f"You now have ${money}")
                                global game_credits
                                game_credits += 0.5
                            else:
                                global has_job
                                if has_job:
                                    raise_salary = round(random.uniform(2, 5), 2)
                                    print(f"Raised salary:  {raise_salary}")
                                    global salary
                                    salary = salary * raise_salary
                                    print(f"Your salary is now ${salary}")
                                else:
                                    print(f"You don't have a job!")
                        else:
                            print("Better luck next time.")

                        play_again = input("\nDo you want to play again? (Enter 'quit' to exit): ").lower()
                        if play_again == 'quit':
                            break

                if __name__ == "__main__":
                    run_lottery()
            
            elif what_lottery == 'hard':
                def generate_lottery_numbers():
                    """Generate a list of 6 random numbers between 1 and 49."""
                    return random.sample(range(1, 50), 6)

                def buy_lottery_ticket():
                    """Allow the user to buy a lottery ticket."""
                    print("Welcome to the Lottery! Good luck!")
                    input("Press Enter to buy a lottery ticket...")
                    return generate_lottery_numbers()

                def check_lottery_results(ticket_numbers, winning_numbers):
                    """Check if the ticket has won."""
                    matched_numbers = set(ticket_numbers).intersection(winning_numbers)
                    return len(matched_numbers)

                def run_lottery():
                    """Run the lottery."""
                    while True:
                        global health
                        health -= random.randint(5, 10)
                        lottery_ticket = random.randint(5, 10)
                        print(f"Ticket: ${lottery_ticket}")
                        global money
                        money = money - lottery_ticket
                        print(f"You have ${money} and {health} health")
                        winning_numbers = generate_lottery_numbers()
                        user_ticket = buy_lottery_ticket()

                        print("\nWinning Numbers:", winning_numbers)
                        matched_count = check_lottery_results(user_ticket, winning_numbers)

                        print("\nYou matched", matched_count, "number(s)!")
                        if matched_count == 6:
                            print("Congratulations! You won the jackpot!")
                            money_or_raise = input("Do you want money or a salary raise? (money, raise)   ")
                            if money_or_raise == 'money':
                                easy_lottery_total = random.randint(1_000_000, 5_000_000)
                                print(f"You got ${easy_lottery_total}")
                                money = money + easy_lottery_total
                                print(f"You now have ${money}")
                                global game_credits
                                game_credits += 1
                            else:
                                global has_job
                                if has_job:
                                    raise_salary = round(random.uniform(5, 10), 2)
                                    print(f"Raised salary:  {raise_salary}")
                                    global salary
                                    salary = salary * raise_salary
                                    print(f"Your salary is now ${salary}")
                                else:
                                    print(f"You don't have a job!")
                        else:
                            print("Better luck next time.")
                        
                        play_again = input("\nDo you want to play again? (Enter 'quit' to exit): ").lower()
                        if play_again == 'quit':
                            break

                if __name__ == "__main__":
                    run_lottery()
            else:
                print("Wrong input!")
        
        if welcome_message == 'education':
            if game_difficulty == 'hardcore':
                health -= random.randint(75, 150)
            else:
                health -= random.randint(50, 100)
            print(f"You have {health} health left!")
            if has_job == False:
                if game_difficulty == 'easy':
                    print(f"Ok, lets see if you can build back your education [guarenteed]! ($500,000)")
                    college_education = 500_000
                elif game_difficulty == 'medium':
                    print(f"Ok, lets see if you can build back your education [guarenteed]! ($600,000)")
                    college_education = 600_000
                else:
                    print(f"Ok, lets see if you can build back your education [guarenteed]! ($750,000)")
                    college_education = 750_000
                if money > college_education:
                    pay_for_second_education = input(f"Do you want to pay for your education? (yes, no)  ")
                    if pay_for_second_education == 'yes':
                        time.sleep(5)
                        print(f"Ok... {time.sleep(3)} You paid for your education!")
                        money -= 750_000
                        print(f"You graduated from college successfully!")
                        print(f"Lets see your jobs...")
                        time.sleep(1.5)
                        jobs_for_college = ['doctor', 'scientist', 'buisnessman', 'lawyer', 'software engineer', 'teacher',
                                'video game designer', 'vet', 'fashion designer', 'secret agent']
                        your_job = random.choice(jobs_for_college)
                        has_job = True
                        print(f"Your job is: {your_job} (you work for 8 hours)")
                        print(f"Calculating salary per day:")
                        time.sleep(2.5)
                        if your_job == 'doctor':
                            salary = random.randint(800, 900)
                        if your_job == 'scientist':
                            salary = random.randint(300, 400)
                        if your_job == 'buisnessman':
                            salary = random.randint(320, 420)
                        if your_job == 'lawyer':
                            salary = random.randint(500, 600)
                        if your_job == 'software engineer':
                            salary = random.randint(560, 660)
                        if your_job == 'teacher':
                            salary = random.randint(280, 380)
                        if your_job == 'video game designer':
                            salary = random.randint(600, 700)
                        if your_job == 'vet':
                            salary = random.randint(640, 740)
                        if your_job == 'fashion designer':
                            salary = random.randint(250, 350)
                        if your_job == 'secret agent':
                            salary = random.randint(310, 410)
                        print(f"Your salary is ${salary} per day!")
                    else:
                        print(f"Ok, have a good life!")
                else:
                    print(f"Sorry, you don't have enough money to educate yourself!")
            else:
                print(f"You already graduated from college or did career life! Lets see if we can upgrade our salary!")
                time.sleep(1.5)
                do_you_want_to_go_to_school = input("Do you want to go to school to increase salary for $250,000? (yes, no)  ")
                if do_you_want_to_go_to_school == 'yes':
                    print(f"Lets see if you can go to school...")
                    time.sleep(15)
                    if has_job == True:
                        print(f"You want to go back to school and increase your salary? ($250,000)")
                        if money > 250_000:
                            print(f"You went back to school and paid $250,000! Lets see your salary increase for your work.")
                            money -= 100000
                            time.sleep(3)
                            increased_salary_amount = round(random.uniform(1, 3), 2)
                            salary = salary * increased_salary_amount
                            print(f"Your salary is now ${salary} per day!")
                        else:
                            print(f"You don't have enough money to go back to school!")
                    else:
                        print(f"Sorry, you got rejected to go to school because no job application(s) or degree.")
                else:
                    print(f"Ok, enjoy your life!")
            
        
        if welcome_message == 'doctor':
            if doctor_attempts < 3:
                actions_count += 1
                which_doctor = input("Which doctor you want to go to? (successful, good, bad) ")
                if which_doctor == 'BESTdoctorEVERinWORLD':
                    if game_difficulty != 'easy':
                        print(f"Sorry, this secret doctor is disabled in this game mode!")
                    else:
                        print(f"secret...")
                        time.sleep(1.5)
                        print(f"doctor...")
                        time.sleep(1.5)
                        doctors_money_amount = random.randint(1_000_000, 2_000_000)
                        see_amount = input(f"This is the amount you pay: ${doctors_money_amount}. Is that ok with you? (yes, no)")
                        if see_amount == 'yes':
                            money = money - doctors_money_amount
                            health_gained_by_doctor = random.randint(10, 150)
                            health = health + health_gained_by_doctor
                            print(f"You gained {health_gained_by_doctor} health from the doctor.")
                            if game_credits > 2:
                                extra_health = random.randint(1, 15)
                                health = health + extra_health
                                print("I like your trust by credits! Here is some more health included from your package."
                                    f"You got {extra_health} health more!")
                if which_doctor == 'successful':
                    if game_difficulty == 'hardcore':
                        print("This doctor disabled in hardcore mode! Pick a different kind of doctor.")
                    else:
                        doctors_money_amount = random.randint(10000, 100000)
                        see_amount = input(f"This is the amount you pay: ${doctors_money_amount}. Is that ok with you? (yes, no)")
                        if see_amount == 'yes':
                            money = money - doctors_money_amount
                            health_gained_by_doctor = random.randint(-5, 60)
                            health = health + health_gained_by_doctor
                            print(f"You gained {health_gained_by_doctor} health from the doctor.")
                            if game_credits > 2:
                                extra_health = random.randint(1, 10)
                                health = health + extra_health
                                print("I like your trust by credits! Here is some more health included from your package."
                                    f"You got {extra_health} health more!")
                elif which_doctor == 'good':
                        doctors_money_amount = random.randint(1000, 10000)
                        see_amount = input(f"This is the amount you pay: ${doctors_money_amount}. Is that ok with you? (yes, no)")
                        if see_amount == 'yes':
                            money = money - doctors_money_amount
                            health_gained_by_doctor = random.randint(-15, 45)
                            health = health + health_gained_by_doctor
                            print(f"You gained {health_gained_by_doctor} health from the doctor.")
                            if game_credits > 2:
                                extra_health = random.randint(1, 5)
                                health = health + extra_health
                                print("I like your trust by credits! Here is some more health included from your package."
                                    f"You got {extra_health} health more!")           
                elif which_doctor == 'bad':
                        doctors_money_amount = random.randint(100, 1000)
                        see_amount = input(f"This is the amount you pay: ${doctors_money_amount}. Is that ok with you? (yes, no)")
                        if see_amount == 'yes':
                            money = money - doctors_money_amount
                            health_gained_by_doctor = random.randint(-30, 20)
                            health = health + health_gained_by_doctor
                            print(f"You gained {health_gained_by_doctor} health from the doctor.")
                            if game_credits > 2:
                                extra_health = random.randint(0, 2)
                                health = health + extra_health
                                print("I like your trust by credits! Here is some more health included from your package."
                                    f"You got {extra_health} health more!")
                elif which_doctor == 'terrible':
                        doctors_money_amount = random.randint(10, 100)
                        see_amount = input(f"This is the amount you pay: ${doctors_money_amount}. Is that ok with you? (yes, no)")
                        if see_amount == 'yes':
                            money = money - doctors_money_amount
                            health_gained_by_doctor = random.randint(-50, 20)
                            health = health + health_gained_by_doctor
                            print(f"You gained {health_gained_by_doctor} health from the doctor.")
                if has_wife == True:
                    print(f"You get extra money since you have a wife!")
                    money = money + random.randint(100, 10000)
                print(f"You have ${money} left and {health} health!")
                if game_difficulty != 'easy':
                    doctor_attempts += 1
                else:
                    doctor_attempts += 0.5
            else:
                print("You have max doctor attempts in this game.")


        # Check if the player has performed 5 actions
        if has_job == True:
            if actions_count % 5 == 0:
                money = money + salary
                print(f"You earned ${salary} as your salary per day!")
                if game_difficulty == 'easy':
                    credit_salary = 0.1
                elif game_difficulty == 'medium':
                    credit_salary = 0.05
                elif game_difficulty == 'hard':
                    credit_salary = 0.025
                elif game_difficulty == 'hardcore':
                    credit_salary = 0.01
                game_credits = game_credits + credit_salary
                print(f"You earned {credit_salary} credits too!")
                print(f"You have ${money} and {game_credits} credits!")
        
        # Bouns salary every 12 rounds!
        if has_job == True:
            if actions_count % 12 == 0:
                bonus_salary = salary * 10
                money = money + bonus_salary
                print(f"You earned ${bonus_salary} as your BOUNS salary!")
                if game_difficulty == 'easy':
                    credit_salary = 0.15
                elif game_difficulty == 'medium':
                    credit_salary = 0.1
                elif game_difficulty == 'hard':
                    credit_salary = 0.05
                elif game_difficulty == 'hardcore':
                    credit_salary = 0.01
                game_credits = game_credits + credit_salary
                print(f"You earned {credit_salary} credits too!")
                print(f"You have ${money} and {game_credits} credits!")

        if game_difficulty == 'easy':
            if money >= 2_500_000:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    
            if game_credits >= 2.5:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    

        elif game_difficulty == 'medium':
            if money >= 5_000_000:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    
            if game_credits >= 3:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    

        elif game_difficulty == 'hard':
            if money >= 7_500_000:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    
            if game_credits >= 3.5:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    
        
        elif game_difficulty == 'hardcore':
            if money >= 10_000_000:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    
            if game_credits >= 4:
                if has_loan == False:
                    print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                    break
                else:
                    print(f"Even if you have money or credits, you can't win because you are on dept!")
                    
except Exception as e:
    print(f"GAME OVER (Error occured): {e}")

finally:
    print("Remember to enter good/right information!")