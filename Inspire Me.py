import random

# List of motivational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The best way to predict the future is to create it. - Peter Drucker",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

def generate_quote():
    """Generate and display a random quote."""
    print("\nHere's a motivational quote for you:")
    print(random.choice(quotes))

# Main program loop
while True:
    generate_quote()
    again = input("\nDo you want another quote? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the motivational quote generator!")
        break
