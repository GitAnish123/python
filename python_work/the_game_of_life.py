try:
    """
    Money is very important in this game, you need 5 million to win the game. For health, it is lost for anything you do.
    Regardless if good or bad, at the beginning of every thing you do, you will lose at least 1 healh. If you have no health,
    you lose as if you lost all money, you lose. Try to win 5 million dollars by the least amount of actions.
    Only few/some actions will include health loss. Some will only include money loss. ADDITIONALLY, you can earn credits.
    You earn credits ONLY when if you shop for stuff and do a business. BEWARE it costs many health point loss. 
    When you earn 4 credits, you win. So watch out for those three things: health, money, and credits.
    """

    import random, time

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
            jobs_for_college = ['doctor', 'scientist', 'buisnessman', 'lawyer', 'software engineer']
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
            print(f"Your salary is ${salary} per day!")
    if which_path == 'career':
        print(f"You picked career path!")
        jobs_for_college = ['artist', 'police officer', 'athlete', 'salesperson', 'teacher']
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
        if your_job == 'teacher':
            salary = random.randint(130, 180)
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
        health = random.randint(120, 250)
        game_credits = 0.2

    # Set a limit for doctor attempts. First make the value to 0.
    doctor_attempts = 0

    # Set a limit for shop attempts. First make value to 0.
    shop_attempts = 0

    # Flag if you have a wife
    has_wife = False

    # Every 5 turns, you earn your salary. Count every action.
    actions_count = 0

    print(f"You start with ${money}")
    print(f"You start with {health} health.")
    print(f"You start with {game_credits} credits.")
    print(f"You currently have 3 doctor attempts. You used 0 doctor attempts.")

    while True:
        welcome_message = input(f"Welcome to your life! What do you want to do?\nEnter 'quit' to quit: ")
        discount_attempts = 0

        if welcome_message == 'quit':
            print(f"Thanks for playing, {name}!")
            break
        
        if money <= 0:
            print(f"{name}, GAME OVER: YOU RAN OUT OF MONEY")
            break
        
        if health <= 0:
            print(f"{name}, GAME OVER: YOU HAVE NO HEALTH")
            break

        if which_path == 'college':
            if paid_for_college == False:
                if money > 500_000:
                    print(f"You have enough to pay for your college funds!")
                    money -= 500_000
                    print(f"You have ${money} left.")
                    paid_for_college = True

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
                    health -= random.randint(25,50)
                elif game_difficulty == 'easy':
                    health -= random.randint(15,25)
                else: 
                    health -= random.randint(20,40)
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
                        'poo', 'get money']
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
                "What is the smallest bone in the human body?": "Stapes (in the ear)",
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
                "What is the smallest bone in the human body?": "Stapes (in the ear)",
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

            if result == 'poo':
                print(f"You went poo!")
                health += 1
                print(f"You have {health} health!")
            
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
        
        if welcome_message == 'hard math test':
            if game_difficulty == 'hardcore':
                health -= 25
            else:
                health -= random.randint(15, 25)
            print(f"You have {health} health left.")
            msg_for_math_enter = input("Do you want to enter the HARD math challenge to earn rewards? (yes, no):  ")
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
                health -= random.randint(75, 150)
            else:
                health -= random.randint(75, 100)
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
                print(display_word)

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
        
        if welcome_message == 'doctor':
            if doctor_attempts < 3:
                actions_count += 1
                which_doctor = input("Which doctor you want to go to? (successful, good, bad) ")
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
        
        
        # Increment the action count every turn.
        actions_count += 1

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
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                break
            if game_credits >= 2.5:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                break

        elif game_difficulty == 'medium':
            if money >= 5_000_000:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                break
            if game_credits >= 3:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                break

        elif game_difficulty == 'hard':
            if money >= 7_500_000:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                break
            if game_credits >= 3.5:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                break
        
        elif game_difficulty == 'hardcore':
            if money >= 10_000_000:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH MONEY!")
                break
            if game_credits >= 4:
                print("YOU WIN THE GAME!!! YOU HAVE ENOUGH CREDITS!")
                break
except Exception as e:
    print(f"GAME OVER (Error occured): {e}")
finally:
    print("Remember to enter good/right information!")