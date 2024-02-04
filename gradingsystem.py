#calcute average and grant grade
def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(average_score):
    if 70 <= average_score <= 100:
        return 'A'
    elif 60 <= average_score < 69:
        return 'B'
    elif 50 <= average_score < 59:
        return 'C'
    elif 40 <= average_score < 49:
        return 'D'
    elif 0 <= average_score < 39:
        return 'Fail'

def main():
    subject1 = get_valid_score("Enter score for subject 1: ")
    subject2 = get_valid_score("Enter score for subject 2: ")
    subject3 = get_valid_score("Enter score for subject 3: ")

    average_score = (subject1 + subject2 + subject3) / 3

    print(f"Average Score: {average_score:.2f}")
    grade = calculate_grade(average_score)
    print(f"Grade: {grade}")
main()
