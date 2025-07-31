questions=[
    {
        "prompt": "What's the capital of India ?",
        "options":["A. Paris","B. London","C. New Delhi","D. Mumbai"],
        "answer": "C"
            
    },
    {
        "prompt": "What language is primarily spoken in India ?",
        "options":["A. Tamil","B. Hindhi","C. Telugu","D. English"],
        "answer": "B"
        
    },
    {
        "prompt": "What is the smallest prime number ?",
        "options":["A. 2","B. 1","C. 0","D. 5"],
        "answer": "A"
    },
    {
        "prompt": "Who is the author of the song mocking bird ?",
        "options":["A. Taylor","B. Ed sheeran","C. olivia","D. Eminem"],
        "answer": "D"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer(A,B,C or D): ").upper()
        if answer == question["answer"]:
            print("Correct Answer Dude ! \n")
            score+=1
        else:
            print("Wrong answer ! The correct answer was ", question["answer"],"\n")
    print(f"You got {score} out of {len(questions)} questions correct. ")
            
run_quiz(questions)