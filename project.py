import time
import random

print("Welcome to the quiz")
time.sleep(2)
print("you are directing towards the registration page")
time.sleep(3)
fullname=input("Enter your full name: ")
phone_number=int(input("Enter your phone number: "))
username=input("enter your username: ")
password=input("enter your password: ")
time.sleep(2)
print("your directing to the login page")
login_username=input("Enter your username: ")  
login_password=input("enter your password: ")
if(login_username==username and login_password==password):
    
      questions = {
    'General Knowledge': [
        {"question": "Who was the first President of India?", "options": ["A) Dr. Rajendra Prasad", "B) Sarvepalli Radhakrishnan", "C) Zakir Husain", "D) V. V. Giri"], "answer": "A"},
        {"question": "Which is the smallest state in India by area?", "options": ["A) Kerala", "B) Goa", "C) Sikkim", "D) Nagaland"], "answer": "B"},
        {"question": "Which is the official language of the Indian state of Karnataka?", "options": ["A) Telugu", "B) Kannada", "C) Tamil", "D) Malayalam"], "answer": "B"},
        {"question": "Who is the founder of the Maurya Empire in India?", "options": ["A) Chandragupta Maurya", "B) Ashoka", "C) Bindusara", "D) Harsha"], "answer": "A"},
        {"question": "In which year was the Indian Constitution adopted?", "options": ["A) 1947", "B) 1949", "C) 1950", "D) 1952"], "answer": "C"},
        {"question": "Which of the following cities is known as the 'City of Joy'?", "options": ["A) Kolkata", "B) Mumbai", "C) Delhi", "D) Chennai"], "answer": "A"},
        {"question": "Which state in India is known for the Sun Temple at Konark?", "options": ["A) Odisha", "B) Bihar", "C) Rajasthan", "D) Gujarat"], "answer": "A"},
        {"question": "Who is the current Chief Justice of India (as of 2024)?", "options": ["A) D.Y. Chandrachud", "B) N.V. Ramana", "C) Sharad Arvind Bobde", "D) Ranjan Gogoi"], "answer": "A"},
        {"question": "Which festival is celebrated in Punjab as a harvest festival?", "options": ["A) Holi", "B) Baisakhi", "C) Diwali", "D) Onam"], "answer": "B"},
        {"question": "Which of the following is the largest desert in India?", "options": ["A) Thar Desert", "B) Rann of Kutch", "C) Ladakh", "D) Deccan Plateau"], "answer": "A"},
        {"question": "Who is the author of the famous book 'Discovery of India'?", "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Sardar Vallabhbhai Patel", "D) B.R. Ambedkar"], "answer": "A"},
        {"question": "Which Indian state is known as the 'Land of Five Rivers'?", "options": ["A) Punjab", "B) Haryana", "C) Rajasthan", "D) Uttar Pradesh"], "answer": "A"},
        {"question": "Which city is home to the Golden Temple?", "options": ["A) New Delhi", "B) Chandigarh", "C) Amritsar", "D) Patiala"], "answer": "C"},
        {"question": "Which Mughal emperor built the Taj Mahal?", "options": ["A) Akbar", "B) Shah Jahan", "C) Aurangzeb", "D) Humayun"], "answer": "B"},
        {"question": "Which freedom fighter gave the slogan 'Inquilab Zindabad'?", "options": ["A) Bhagat Singh", "B) Subhash Chandra Bose", "C) Jawaharlal Nehru", "D) Mahatma Gandhi"], "answer": "A"},
        {"question": "Which of the following is the national tree of India?", "options": ["A) Neem", "B) Peepal", "C) Banyan", "D) Mango"], "answer": "C"},
        {"question": "Who was the first woman Chief Minister of an Indian state?", "options": ["A) Sucheta Kriplani", "B) Indira Gandhi", "C) Sarojini Naidu", "D) Pratibha Patil"], "answer": "A"},
        {"question": "Which state is known for the Kathakali dance form?", "options": ["A) Tamil Nadu", "B) Kerala", "C) Andhra Pradesh", "D) Karnataka"], "answer": "B"},
        {"question": "Who is known as the 'Iron Man of India'?", "options": ["A) Sardar Vallabhbhai Patel", "B) Lal Bahadur Shastri", "C) Bal Gangadhar Tilak", "D) B.R. Ambedkar"], "answer": "A"},
        {"question": "Which Indian city is known as the 'City of Lakes'?", "options": ["A) Udaipur", "B) Bhopal", "C) Jaipur", "D) Srinagar"], "answer": "A"},
        {"question": "Which state in India has the longest coastline?", "options": ["A) Gujarat", "B) Maharashtra", "C) Tamil Nadu", "D) Kerala"], "answer": "A"},
        {"question": "Who was the first Indian to win the Nobel Prize?", "options": ["A) C.V. Raman", "B) Rabindranath Tagore", "C) Amartya Sen", "D) Kailash Satyarthi"], "answer": "B"},
        {"question": "What is the currency of India?", "options": ["A) Dollar", "B) Rupee", "C) Yen", "D) Pound"], "answer": "B"},
        {"question": "Which city is the capital of Andhra Pradesh (as of 2024)?", "options": ["A) Amaravati", "B) Visakhapatnam", "C) Vijayawada", "D) Tirupati"], "answer": "A"},
        {"question": "Which Indian state is famous for the classical dance form Bharatnatyam?", "options": ["A) Kerala", "B) Tamil Nadu", "C) Karnataka", "D) Andhra Pradesh"], "answer": "B"}
    ],

    'Technology': [
        {"question": "Which company is India's largest IT services provider?", "options": ["A) Infosys", "B) Wipro", "C) TCS", "D) HCL"], "answer": "C"},
        {"question": "What is the name of India's indigenous operating system?", "options": ["A) BharatOS", "B) IndOS", "C) HindOS", "D) IndiaOS"], "answer": "A"},
        {"question": "In which year did ISRO launch its first satellite, Aryabhata?", "options": ["A) 1972", "B) 1975", "C) 1980", "D) 1984"], "answer": "B"},
        {"question": "Which Indian scientist is known as the 'Missile Man of India'?", "options": ["A) Dr. A.P.J. Abdul Kalam", "B) Homi Bhabha", "C) Vikram Sarabhai", "D) Satish Dhawan"], "answer": "A"},
        {"question": "What is the full form of UPI in India’s digital payment system?", "options": ["A) Unified Payments Interface", "B) Universal Payment Identity", "C) Unified Personal Interface", "D) Unified Process Infrastructure"], "answer": "A"},
        {"question": "Which Indian company developed the Aakash tablet?", "options": ["A) Infosys", "B) Reliance", "C) DataWind", "D) HCL"], "answer": "C"},
        {"question": "Which of the following is a major IT park in India?", "options": ["A) Hinjewadi", "B) Electronic City", "C) Cybercity", "D) All of the above"], "answer": "D"},
        {"question": "Who is the CEO of Google as of 2024?", "options": ["A) Satya Nadella", "B) Sundar Pichai", "C) Shantanu Narayen", "D) Parag Agrawal"], "answer": "B"},
        {"question": "Which Indian mobile brand was the first to develop a 5G smartphone?", "options": ["A) Micromax", "B) Intex", "C) Karbonn", "D) Reliance Jio"], "answer": "D"},
        {"question": "Which is the highest civilian award given for contributions to science and technology in India?", "options": ["A) Padma Shri", "B) Padma Bhushan", "C) Shanti Swarup Bhatnagar Prize", "D) Padma Vibhushan"], "answer": "C"},
        {"question": "Which of the following organizations is responsible for India's defense research?", "options": ["A) ISRO", "B) DRDO", "C) HAL", "D) BHEL"], "answer": "B"},
        {"question": "Which of these was India's first nuclear reactor?", "options": ["A) Cirus", "B) Apsara", "C) Dhruva", "D) Pokhran"], "answer": "B"},
        {"question": "Which company built India's first supercomputer?", "options": ["A) C-DAC", "B) ISRO", "C) Infosys", "D) TCS"], "answer": "A"},
        {"question": "Which of the following is an AI research institute in India?", "options": ["A) IISc", "B) AIIMS", "C) IIT Madras AI Lab", "D) CSIR"], "answer": "C"},
        {"question": "In which city is India's Silicon Valley located?", "options": ["A) Hyderabad", "B) Pune", "C) Bengaluru", "D) Chennai"], "answer": "C"},
        {"question": "Which Indian IT firm acquired Capco, a global management and technology consultancy?", "options": ["A) Infosys", "B) TCS", "C) Wipro", "D) Cognizant"], "answer": "C"},
        {"question": "Who is credited with developing India's first indigenous computer?", "options": ["A) Dr. Vijay Bhatkar", "B) Ratan Tata", "C) A.P.J. Abdul Kalam", "D) Homi Bhabha"], "answer": "A"},
        {"question": "Which Indian state houses the most IT parks?", "options": ["A) Karnataka", "B) Maharashtra", "C) Tamil Nadu", "D) Telangana"], "answer": "A"},
        {"question": "Which of these is India’s main space research organization?", "options": ["A) ISRO", "B) NASA", "C) DRDO", "D) C-DAC"], "answer": "A"},
        {"question": "Which Indian e-commerce platform launched the 'Big Billion Days' sale?", "options": ["A) Amazon", "B) Flipkart", "C) Snapdeal", "D) Myntra"], "answer": "B"},
        {"question": "Which Indian scientist co-discovered the Raman Effect?", "options": ["A) C.V. Raman", "B) S. Chandrasekhar", "C) Homi Bhabha", "D) A.P.J. Abdul Kalam"], "answer": "A"},
        {"question": "Which tech giant partnered with the Indian government to provide free Wi-Fi at railway stations?", "options": ["A) Microsoft", "B) Apple", "C) Google", "D) Facebook"], "answer": "C"},
        {"question": "Which of these companies is known for AI-based conversational bots in India?", "options": ["A) Haptik", "B) Niki.ai", "C) Yellow.ai", "D) All of the above"], "answer": "D"},
        {"question": "Who was the first Indian to become the CEO of a major global tech company?", "options": ["A) Sundar Pichai", "B) Satya Nadella", "C) Shantanu Narayen", "D) Arvind Krishna"], "answer": "B"},
        {"question": "Which Indian state declared 'K-Tech Innovation Hub' to boost technology startups?", "options": ["A) Maharashtra", "B) Karnataka", "C) Tamil Nadu", "D) Telangana"], "answer": "B"}
    ],

    'Sports': [
        {"question": "Who is the first Indian to win an individual Olympic gold medal?", "options": ["A) Abhinav Bindra", "B) Neeraj Chopra", "C) P.T. Usha", "D) Rajyavardhan Singh Rathore"], "answer": "A"},
        {"question": "Who won the first Cricket World Cup for India in 1983?", "options": ["A) Sachin Tendulkar", "B) Kapil Dev", "C) Sunil Gavaskar", "D) Rahul Dravid"], "answer": "B"},
        {"question": "Which Indian footballer holds the record for most international goals?", "options": ["A) Sunil Chhetri", "B) Bhaichung Bhutia", "C) Gurpreet Singh Sandhu", "D) Jeje Lalpekhlua"], "answer": "A"},
        {"question": "Who is known as the 'Flying Sikh' of India?", "options": ["A) Milkha Singh", "B) P.T. Usha", "C) Abhinav Bindra", "D) Sushil Kumar"], "answer": "A"},
        {"question": "Which Indian cricketer was known as the 'Little Master'?", "options": ["A) Sunil Gavaskar", "B) Sachin Tendulkar", "C) Virender Sehwag", "D) Rahul Dravid"], "answer": "A"},
        {"question": "Who was the first Indian woman to win a medal at the Olympics?", "options": ["A) P.T. Usha", "B) Saina Nehwal", "C) Karnam Malleswari", "D) Mary Kom"], "answer": "C"},
        {"question": "Which sport is associated with the Davis Cup?", "options": ["A) Football", "B) Tennis", "C) Badminton", "D) Hockey"], "answer": "B"},
        {"question": "Who is the first Indian woman to win a gold medal at the Asian Games?", "options": ["A) P.T. Usha", "B) Hima Das", "C) Mary Kom", "D) Karnam Malleswari"], "answer": "A"},
        {"question": "Which team has won the most IPL titles?", "options": ["A) Mumbai Indians", "B) Chennai Super Kings", "C) Kolkata Knight Riders", "D) Royal Challengers Bangalore"], "answer": "A"},
        {"question": "Who is the first Indian to win the All England Badminton Championship?", "options": ["A) Pullela Gopichand", "B) Saina Nehwal", "C) Prakash Padukone", "D) P.V. Sindhu"], "answer": "C"},
        {"question": "Who is the first Indian woman to win silver in Olympics for badminton?", "options": ["A) P.V. Sindhu", "B) Saina Nehwal", "C) Jwala Gutta", "D) Ashwini Ponnappa"], "answer": "A"},
        {"question": "Which country did India defeat in the 2011 Cricket World Cup final?", "options": ["A) Australia", "B) Sri Lanka", "C) Pakistan", "D) England"], "answer": "B"},
        {"question": "Who was the captain of India's first Olympic gold medal-winning hockey team?", "options": ["A) Dhanraj Pillay", "B) Dhyan Chand", "C) Balbir Singh", "D) Roop Singh"], "answer": "B"},
        {"question": "In which year did India host its first Cricket World Cup?", "options": ["A) 1983", "B) 1987", "C) 1996", "D) 2011"], "answer": "B"},
        {"question": "Which Indian athlete won a gold medal in the javelin throw at the 2020 Tokyo Olympics?", "options": ["A) Abhinav Bindra", "B) Bajrang Punia", "C) Neeraj Chopra", "D) Ravi Kumar Dahiya"], "answer": "C"},
        {"question": "Which Indian sportsperson is the brand ambassador of the 'Khelo India' initiative?", "options": ["A) P.V. Sindhu", "B) Neeraj Chopra", "C) Mary Kom", "D) Hima Das"], "answer": "B"},
        {"question": "Which stadium in India is the largest by seating capacity?", "options": ["A) Wankhede Stadium", "B) Eden Gardens", "C) Narendra Modi Stadium", "D) M. Chinnaswamy Stadium"], "answer": "C"},
        {"question": "Who is India's first Formula 1 driver?", "options": ["A) Narain Karthikeyan", "B) Karun Chandhok", "C) Arjun Maini", "D) Jehan Daruvala"], "answer": "A"},
        {"question": "Who is the first Indian tennis player to win a Grand Slam title?", "options": ["A) Leander Paes", "B) Mahesh Bhupathi", "C) Sania Mirza", "D) Rohan Bopanna"], "answer": "A"},
        {"question": "Who won India's first ever Olympic medal in wrestling?", "options": ["A) Yogeshwar Dutt", "B) Sushil Kumar", "C) Bajrang Punia", "D) K.D. Jadhav"], "answer": "D"},
        {"question": "Who was the first Indian cricketer to hit six sixes in an over?", "options": ["A) Yuvraj Singh", "B) Virender Sehwag", "C) Sachin Tendulkar", "D) MS Dhoni"], "answer": "A"},
        {"question": "Who is the first Indian Paralympian to win two gold medals in a single edition of the Paralympics?", "options": ["A) Devendra Jhajharia", "B) Mariyappan Thangavelu", "C) Deepa Malik", "D) Varun Singh Bhati"], "answer": "A"},
        {"question": "Which sportsperson is nicknamed 'The Wall' in Indian cricket?", "options": ["A) Rahul Dravid", "B) V.V.S. Laxman", "C) Anil Kumble", "D) Sourav Ganguly"], "answer": "A"},
        {"question": "Who is India's first woman chess grandmaster?", "options": ["A) Koneru Humpy", "B) Tania Sachdev", "C) Harika Dronavalli", "D) Subbaraman Vijayalakshmi"], "answer": "D"},
        {"question": "Which country won the inaugural ICC T20 World Cup in 2007?", "options": ["A) India", "B) Pakistan", "C) South Africa", "D) Australia"], "answer": "A"}
    ]
}


def select_domain():
    print("\nSelect a domain for the quiz:")
    print("1. General Knowledge")
    print("2. Technology")
    print("3. Sports")
    choice = input("\nEnter the number of your choice: ")
    
    if choice == '1':
        return 'General Knowledge'
    elif choice == '2':
        return 'Technology'
    elif choice == '3':
        return 'Sports'
    else:
        print("Invalid choice, please try again.")
        return select_domain()

def ask_questions(domain):
    selected_questions = random.sample(questions[domain], 5)
    score = 0

    for i, q in enumerate(selected_questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
    
    return score

def main_quiz():
    while True:
        domain = select_domain()
        print(f"\nYou selected: {domain}")

        score = ask_questions(domain)
        print(f"\nYour score: {score}/5")

        retry = input("\nDo you want to take another test? (yes/no): ").lower()
        if retry != 'yes':
            print("Thank you for playing the quiz!")
            break

if __name__ == "__main__":
    main_quiz()

  

