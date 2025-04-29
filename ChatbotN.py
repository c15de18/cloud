def chatbot():
    print("🍕 Welcome to QuickPizza Bot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if 'order' in user_input and 'pizza' in user_input:
            print("Bot: Great! What size would you like? (small, medium, large)")
        elif any(size in user_input for size in ['small', 'medium', 'large']):
            print(f"Bot: {user_input.capitalize()} pizza selected. Would you like any toppings? (cheese, pepperoni, mushrooms)")
        elif any(topping in user_input for topping in ['cheese', 'pepperoni', 'mushrooms']):
            print("Bot: Awesome choice! Your pizza is being prepared. Anything else?")
        elif 'price' in user_input or 'cost' in user_input:
            print("Bot: Prices - Small: $5, Medium: $8, Large: $12. Toppings are $1 each.")
        elif 'no' in user_input or 'nothing' in user_input:
            print("Bot: Thanks for ordering! Have a delicious day! 🍕")
        elif 'exit' in user_input:
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: I'm sorry, I didn't understand that. Can you rephrase?")

chatbot()
