import random


QUIZ_QUESTIONS = [
    ("What is the capital of Japan?", ["Seoul", "Tokyo", "Beijing", "Bangkok"], 2),
    ("Which is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], 4),
    ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], 3),
    ("Which country is home to the Great Pyramid of Giza?", ["Mexico", "Egypt", "Greece", "India"], 2),
    ("What is the currency of Japan?", ["Won", "Yuan", "Yen", "Ringgit"], 3),
    ("Which is the largest hot desert in the world?", ["Gobi", "Sahara", "Kalahari", "Mojave"], 2),
    ("Mount Everest is part of which mountain range?", ["Andes", "Alps", "Himalayas", "Rockies"], 3),
    ("What is the capital of Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], 2),
    ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "Thailand", "South Korea"], 2),
    ("Which is the smallest continent by land area?", ["Europe", "Australia", "Antarctica", "South America"], 2),
    ("What is the capital of Italy?", ["Venice", "Milan", "Rome", "Naples"], 3),
    ("The Amazon rainforest is primarily located on which continent?", ["Africa", "Asia", "South America", "Europe"], 3),
    ("Which river flows through London?", ["Seine", "Thames", "Danube", "Tiber"], 2),
    ("What is the capital of South Korea?", ["Busan", "Seoul", "Incheon", "Jeju"], 2),
    ("Which country has a maple leaf on its national flag?", ["Canada", "Denmark", "Austria", "Switzerland"], 1),
    ("What is the capital of Spain?", ["Barcelona", "Lisbon", "Madrid", "Seville"], 3),
    ("Which is the largest country in the world by land area?", ["China", "Canada", "Russia", "United States"], 3),
    ("Which sea lies between Europe and Africa?", ["Caribbean Sea", "Mediterranean Sea", "Baltic Sea", "Arabian Sea"], 2),
    ("What is the capital of Nepal?", ["Pokhara", "Kathmandu", "Thimphu", "Dhaka"], 2),
    ("Which is the highest waterfall in the world?", ["Niagara Falls", "Angel Falls", "Victoria Falls", "Iguazu Falls"], 2),
    ("What is the chemical symbol for gold?", ["Ag", "Go", "Au", "Gd"], 3),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Mercury"], 2),
    ("What gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], 3),
    ("What is the closest star to Earth?", ["Sirius", "The Sun", "Proxima Centauri", "Polaris"], 2),
    ("How many bones are there in the typical adult human body?", ["186", "206", "226", "246"], 2),
    ("What is the hardest naturally occurring substance?", ["Quartz", "Iron", "Diamond", "Granite"], 3),
    ("Which organ pumps blood around the human body?", ["Lungs", "Liver", "Heart", "Kidneys"], 3),
    ("What is the chemical formula for water?", ["CO2", "H2O", "O2", "NaCl"], 2),
    ("Which planet is the largest in our solar system?", ["Saturn", "Earth", "Jupiter", "Neptune"], 3),
    ("What force keeps planets in orbit around the Sun?", ["Magnetism", "Friction", "Gravity", "Electricity"], 3),
    ("Which part of a plant usually absorbs water from the soil?", ["Flower", "Leaf", "Root", "Stem"], 3),
    ("What is the center of an atom called?", ["Electron", "Nucleus", "Molecule", "Proton"], 2),
    ("Which vitamin can the human body produce with sunlight exposure?", ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], 4),
    ("At what temperature does water boil at sea level in Celsius?", ["50", "75", "100", "125"], 3),
    ("Which blood cells help the body fight infections?", ["Red blood cells", "White blood cells", "Platelets", "Plasma"], 2),
    ("What is the process by which plants make food using sunlight?", ["Respiration", "Photosynthesis", "Fermentation", "Digestion"], 2),
    ("Which is the fastest land animal?", ["Lion", "Cheetah", "Horse", "Leopard"], 2),
    ("What is the main gas in Earth's atmosphere?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], 3),
    ("Which instrument is used to measure temperature?", ["Barometer", "Thermometer", "Hygrometer", "Altimeter"], 2),
    ("How many chambers does a human heart have?", ["Two", "Three", "Four", "Five"], 3),
    ("Which is the largest mammal in the world?", ["African elephant", "Blue whale", "Giraffe", "Orca"], 2),
    ("Who was the first Mughal emperor in India?", ["Akbar", "Babur", "Humayun", "Shah Jahan"], 2),
    ("Who founded the Maurya Empire?", ["Ashoka", "Chandragupta Maurya", "Harsha", "Bindusara"], 2),
    ("In which year did India gain independence?", ["1942", "1945", "1947", "1950"], 3),
    ("Who wrote India's national anthem, Jana Gana Mana?", ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Subhas Chandra Bose"], 2),
    ("Who was the first person to walk on the Moon?", ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], 3),
    ("Which ancient civilization built Machu Picchu?", ["Maya", "Aztec", "Inca", "Roman"], 3),
    ("Who was known as the Iron Man of India?", ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "B. R. Ambedkar", "Lal Bahadur Shastri"], 2),
    ("The ancient Olympic Games began in which country?", ["Italy", "Greece", "Egypt", "Turkey"], 2),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", ["Amelia Earhart", "Valentina Tereshkova", "Bessie Coleman", "Sally Ride"], 1),
    ("Which monument was built by Shah Jahan in memory of Mumtaz Mahal?", ["Red Fort", "Qutub Minar", "Taj Mahal", "India Gate"], 3),
    ("Who wrote the play Romeo and Juliet?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], 2),
    ("Who wrote the Harry Potter book series?", ["C. S. Lewis", "J. R. R. Tolkien", "J. K. Rowling", "Roald Dahl"], 3),
    ("Which detective was created by author Arthur Conan Doyle?", ["Hercule Poirot", "Sherlock Holmes", "Miss Marple", "Philip Marlowe"], 2),
    ("Who wrote the novel The Jungle Book?", ["Rudyard Kipling", "George Orwell", "A. A. Milne", "Lewis Carroll"], 1),
    ("What is the name of the fictional land in The Lord of the Rings?", ["Narnia", "Westeros", "Middle-earth", "Neverland"], 3),
    ("Which instrument has 88 keys on a standard version?", ["Violin", "Piano", "Flute", "Harp"], 2),
    ("Which Indian classical dance form originated in Kerala?", ["Kathak", "Bharatanatyam", "Kathakali", "Odissi"], 3),
    ("Which artist painted the Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"], 3),
    ("Which language has the most native speakers worldwide?", ["English", "Spanish", "Mandarin Chinese", "Arabic"], 3),
    ("What is the name of the cowboy in the Toy Story films?", ["Buzz Lightyear", "Woody", "Rex", "Andy"], 2),
    ("Which Indian festival is widely known as the Festival of Lights?", ["Holi", "Diwali", "Pongal", "Onam"], 2),
    ("Which sport is played at Wimbledon?", ["Golf", "Cricket", "Tennis", "Rugby"], 3),
    ("How many players from one team are on the field in a football (soccer) match?", ["9", "10", "11", "12"], 3),
    ("In cricket, how many runs are scored when the ball crosses the boundary without bouncing?", ["Four", "Five", "Six", "Seven"], 3),
    ("Which country won the men's FIFA World Cup in 2022?", ["France", "Brazil", "Argentina", "Germany"], 3),
    ("How many rings are on the Olympic symbol?", ["Four", "Five", "Six", "Seven"], 2),
    ("Which sport uses a shuttlecock?", ["Squash", "Badminton", "Table tennis", "Tennis"], 2),
    ("In which sport would you perform a slam dunk?", ["Volleyball", "Basketball", "Baseball", "Handball"], 2),
    ("Which chess piece moves in an L-shape?", ["Bishop", "Rook", "Knight", "Pawn"], 3),
    ("How many players are on court for one volleyball team during play?", ["Five", "Six", "Seven", "Eight"], 2),
    ("The Tour de France is a major event in which sport?", ["Marathon running", "Cycling", "Motor racing", "Skiing"], 2),
    ("Which country is traditionally associated with sumo wrestling?", ["China", "Japan", "Mongolia", "Thailand"], 2),
    ("What is the maximum score with a single dart in standard darts?", ["20", "40", "50", "60"], 4),
    ("Which Indian cricketer is popularly known as the 'Master Blaster'?", ["Rahul Dravid", "Kapil Dev", "Sachin Tendulkar", "Virat Kohli"], 3),
    ("Which sport is associated with the Stanley Cup?", ["Basketball", "Ice hockey", "Baseball", "American football"], 2),
    ("How many points is a free throw worth in basketball?", ["One", "Two", "Three", "Four"], 1),
    ("What is the term for zero in tennis scoring?", ["Nil", "Love", "Blank", "Deuce"], 2),
    ("Which country hosted the 2016 Summer Olympics?", ["China", "Brazil", "United Kingdom", "Japan"], 2),
    ("What does CPU stand for?", ["Central Processing Unit", "Computer Power Utility", "Core Program Upload", "Central Program User"], 1),
    ("Which company created the Windows operating system?", ["Apple", "Google", "Microsoft", "IBM"], 3),
    ("What does 'www' stand for in a website address?", ["World Wide Web", "Web World Window", "Wide Web Works", "World Web Wire"], 1),
    ("Which device is used to connect a computer to a network wirelessly?", ["Scanner", "Wi-Fi router", "Printer", "Projector"], 2),
    ("What is the primary language used to structure web pages?", ["HTML", "SQL", "Python", "C++"], 1),
    ("Which of these is a type of computer memory that is volatile?", ["ROM", "SSD", "RAM", "Hard drive"], 3),
    ("What does GPS stand for?", ["Global Positioning System", "General Place Service", "Geographic Program Signal", "Global Path Setup"], 1),
    ("Which company developed the Android operating system?", ["Microsoft", "Google", "Nokia", "Sony"], 2),
    ("What is the common name for an image made of pixels?", ["Vector graphic", "Raster image", "Blueprint", "Database"], 2),
    ("Which key is commonly used to refresh a webpage on a Windows computer?", ["F1", "F5", "F8", "F12"], 2),
    ("What does a URL identify?", ["A web resource address", "A computer's processor", "A file's size", "A Wi-Fi password"], 1),
    ("Which Indian city is known as the Pink City?", ["Jaipur", "Jodhpur", "Udaipur", "Bhopal"], 1),
    ("What is the national animal of India?", ["Asiatic lion", "Bengal tiger", "Elephant", "Leopard"], 2),
    ("Which is the largest Indian state by area?", ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Uttar Pradesh"], 3),
    ("What is the capital of the Indian state of Maharashtra?", ["Pune", "Nagpur", "Mumbai", "Nashik"], 3),
    ("Which Indian city is often called the Silicon Valley of India?", ["Hyderabad", "Chennai", "Bengaluru", "Pune"], 3),
    ("Which river is considered the longest river in India?", ["Yamuna", "Godavari", "Ganga", "Narmada"], 3),
    ("What is the national flower of India?", ["Rose", "Lotus", "Jasmine", "Marigold"], 2),
    ("Which Indian state is famous for the backwaters of Alleppey?", ["Goa", "Kerala", "Tamil Nadu", "Karnataka"], 2),
    ("Who was the first President of India?", ["Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "Zakir Husain", "V. V. Giri"], 1),
    ("Which Indian space mission successfully landed near the Moon's south polar region in 2023?", ["Mangalyaan", "Chandrayaan-2", "Chandrayaan-3", "Aditya-L1"], 3),
]


def rock_paper_scissors():
    print("\nWelcome to Rock Paper Scissors!")
    print("1. Rock\n2. Paper\n3. Scissors")
    while True:
        try:
            target = int(input("Enter how many points are needed to win: "))
            if target > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    user_score = computer_score = 0
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while user_score < target and computer_score < target:
        try:
            user = int(input("\nChoose 1, 2, or 3: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if user not in choices:
            print("Invalid choice. Choose 1, 2, or 3.")
            continue

        computer = random.randint(1, 3)
        print("You chose:", choices[user])
        print("Computer chose:", choices[computer])
        if user == computer:
            print("Match Draw!")
        elif (user, computer) in ((1, 3), (2, 1), (3, 2)):
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")
        print(f"Score — You: {user_score} | Computer: {computer_score}")

    print("Congratulations! You reached the target first." if user_score == target
          else "Computer reached the target first. Better luck next time!")


def quiz_game():
    print("\n" + "=" * 55)
    print("                 RD GENERAL KNOWLEDGE QUIZ")
    print("=" * 55)
    name = input("Enter your name: ").strip() or "Player"
    print(f"\nHello, {name}! Each round has 10 random questions from a bank of {len(QUIZ_QUESTIONS)}.")
    print("Scoring: +10 for a correct answer | -5 for an incorrect answer")
    questions = random.sample(QUIZ_QUESTIONS, min(10, len(QUIZ_QUESTIONS)))
    score = 0
    for number, (question, options, answer) in enumerate(questions, start=1):
        print(f"\n{'-' * 55}\nQUESTION {number}/10: {question}")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("Please choose an option from 1 to 4.")
            except ValueError:
                print("Invalid input. Enter a number from 1 to 4.")
        if choice == answer:
            score += 10
            print(f"Correct! Score: {score}")
        else:
            score -= 5
            print(f"Incorrect. The correct answer was: {options[answer - 1]}. Score: {score}")

    print(f"\n{'=' * 55}\nQUIZ COMPLETE | {name}'s final score: {score}/100")
    if score >= 80:
        print("You played really well! Excellent knowledge.")
    elif score >= 50:
        print("You played well, but you can learn more.")
    elif score >= 20:
        print("Come back again and try to improve your general knowledge.")
    else:
        print("Keep practising and try again!")
    print(f"Thank you, {name}, for playing the game.")


def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number from 1 to 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not 1 <= guess <= 100:
            print("Your number must be between 1 and 100.")
            continue
        attempts += 1
        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number:
            print("Your number is smaller. Try again!")
        else:
            print("Your number is greater. Try again!")


def find_movie_game():
    print("\nWelcome to Find the Movie Name!")
    print("Find these 5 Bollywood movie names in the letter grid.")
    print("Type the movie names in CAPITAL LETTERS.")
    print("Movies are hidden horizontally in the grid.\n")
    grid = [
        list("XANIMALYZQ"),
        list("ABCDONPQRS"),
        list("ROYXYZABCD"),
        list("LMNISHQXYZ"),
        list("ABMULKQRST"),
        list("QWERTYUIOP"),
        list("ASDFGHJKLZ"),
        list("ZXCVBNMASD"),
        list("POIUYTREWQ"),
        list("LKJHGFDSAM"),
    ]
    for row in grid:
        print("  ".join(row))
    movies = {"DON", "ROY", "ANIMAL", "ISHQ", "MULK"}
    found = set()
    while len(found) < len(movies):
        answer = input("\nEnter a movie name (or Q to quit): ").strip().upper()
        if answer == "Q":
            break
        if answer not in movies:
            print("Wrong answer! Try again, or enter Q to quit.")
        elif answer in found:
            print("You already found that movie. Try another one.")
        else:
            found.add(answer)
            print(f"Correct! You found {len(found)} out of 5 movies.")
    if found == movies:
        print("Congratulations! You found all five movie names.")
    else:
        print(f"Game ended. You found {len(found)} out of 5 movies.")


def main():
    print("=" * 55)
    print("       Welcome to Single Player RD Gaming Zone")
    print("=" * 55)
    games = {
        1: rock_paper_scissors,
        2: quiz_game,
        3: number_guessing_game,
        4: find_movie_game,
    }
    while True:
        print("\nChoose a game:")
        print("1. Rock Paper Scissors")
        print("2. Quiz Game")
        print("3. Number Guessing Game")
        print("4. Find the Movie Name")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue
        if choice == 5:
            print("Thanks for playing RD Gaming Zone. See you next time!")
            return
        game = games.get(choice)
        if game is None:
            print("Wrong input. Please choose between 1 and 5.")
            continue
        game()
        while True:
            play_again = input("\nWould you like to play another game? (y/n): ").strip().lower()
            if play_again in ("y", "yes"):
                break
            if play_again in ("n", "no"):
                print("Thanks for playing RD Gaming Zone. See you next time!")
                return
            print("Please enter y/yes or n/no.")


if __name__ == "__main__":
    main()
