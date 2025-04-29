#Employee perfromance evaluation

def evaluate_employee(communication,punctuality,productivity,teamwork):
    score = 0

#Scoring communication
    if communication.lower() == 'excellent':
        score += 3
    elif communication.lower() == 'good':
        score += 2
    elif communication.lower() == 'average':
        score += 1

#Scoring punctuality

    if punctuality.lower() == 'always on time':
        score += 3
    elif punctuality.lower() == 'usually on time':
        score += 2
    elif punctuality.lower() == 'sometimes late':
        score += 1

#Scoring teamwork

    if teamwork.lower() == 'excellent':
        score += 3
    elif teamwork.lower() == 'good':
        score += 2
    elif teamwork.lower() == 'average':
        score += 1

#Final evaluation
    if score >= 10:
        return "Excellent"
    elif score >= 7:
        return "Good"
    elif score >= 5:
        return "Average"
    else:
        return "Needs Improvement"
    
#Example usage 
print("Enter employee evaluation inputs:")
comm = input("Communication (Excellent/Good/Average): ")
punct = input("Punctuality (Always on time/Usually on time/Someimes late): ")
prod = input("Productivity (High/Medium/Low): ")
team = input("Teamwork (Excellent/Good/Average): ")

result = evaluate_employee(comm,punct,prod,team)
print(f"\nEmployee Performance : {result}")

