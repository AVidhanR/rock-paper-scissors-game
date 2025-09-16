import random
import os

# ASCII Art for each choice
ROCK_ART = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def clearScreen():
    """Clear the terminal screen for better display"""
    os.system('cls' if os.name == 'nt' else 'clear')

def displayGameTitle():
    """Display the game title with decorative border"""
    print("=" * 60)
    print("🗿  📄  ✂️   ROCK PAPER SCISSORS GAME   🗿  📄  ✂️")
    print("=" * 60)

def displayGameRules():
    """Display the rules of the game"""
    print("\n🎮 GAME RULES:")
    print("   🗿 Rock vs 📄 Paper → Paper wins")
    print("   🗿 Rock vs ✂️ Scissors → Rock wins")
    print("   📄 Paper vs ✂️ Scissors → Scissors wins")
    print("=" * 60)

def getChoiceArt(choiceNumber):
    """Return ASCII art for the given choice number"""
    if choiceNumber == 1:
        return ROCK_ART
    elif choiceNumber == 2:
        return PAPER_ART
    else:
        return SCISSORS_ART

def getChoiceName(choiceNumber):
    """Return the name of the choice based on the number"""
    if choiceNumber == 1:
        return "Rock"
    elif choiceNumber == 2:
        return "Paper"
    else:
        return "Scissors"

def getChoiceEmoji(choiceNumber):
    """Return emoji for the choice"""
    if choiceNumber == 1:
        return "🗿"
    elif choiceNumber == 2:
        return "📄"
    else:
        return "✂️"

def getUserChoice():
    """Get and validate user input"""
    print("\n🎯 Make your choice:")
    print("   1. 🗿 Rock")
    print("   2. 📄 Paper")
    print("   3. ✂️ Scissors")
    
    while True:
        try:
            userChoice = int(input("\n👤 Your turn (1-3): "))
            if 1 <= userChoice <= 3:
                return userChoice
            else:
                print("❌ Please enter a valid choice (1, 2, or 3)")
        except ValueError:
            print("❌ Please enter a valid number (1, 2, or 3)")

def getComputerChoice(userChoice):
    """Generate computer choice (different from user choice for more interesting gameplay)"""
    computerChoice = random.randint(1, 3)
    # Allow same choice for fair gameplay
    return computerChoice

def displayChoices(userChoice, computerChoice):
    """Display both choices with ASCII art side by side"""
    userChoiceName = getChoiceName(userChoice)
    computerChoiceName = getChoiceName(computerChoice)
    userEmoji = getChoiceEmoji(userChoice)
    computerEmoji = getChoiceEmoji(computerChoice)
    
    print(f"\n👤 You chose: {userEmoji} {userChoiceName}")
    print(getChoiceArt(userChoice))
    
    print("⚡ VS ⚡")
    
    print(f"🤖 Computer chose: {computerEmoji} {computerChoiceName}")
    print(getChoiceArt(computerChoice))

def determineWinner(userChoice, computerChoice):
    """Determine the winner based on game rules"""
    if userChoice == computerChoice:
        return "tie"
    
    # Check winning conditions
    if ((userChoice == 1 and computerChoice == 3) or    # Rock beats Scissors
        (userChoice == 2 and computerChoice == 1) or    # Paper beats Rock
        (userChoice == 3 and computerChoice == 2)):     # Scissors beats Paper
        return "user"
    else:
        return "computer"

def displayResult(winner, userChoice, computerChoice):
    """Display the game result with visual flair"""
    print("=" * 60)
    
    if winner == "tie":
        print("🤝 IT'S A TIE! 🤝")
        print("   Great minds think alike!")
    elif winner == "user":
        print("🎉 YOU WIN! 🎉")
        winnerChoice = getChoiceName(userChoice)
        loserChoice = getChoiceName(computerChoice)
        print(f"   {getChoiceEmoji(userChoice)} {winnerChoice} beats {getChoiceEmoji(computerChoice)} {loserChoice}!")
    else:
        print("🤖 COMPUTER WINS! 🤖")
        winnerChoice = getChoiceName(computerChoice)
        loserChoice = getChoiceName(userChoice)
        print(f"   {getChoiceEmoji(computerChoice)} {winnerChoice} beats {getChoiceEmoji(userChoice)} {loserChoice}!")
    
    print("=" * 60)

def playAgain():
    """Ask if the user wants to play again"""
    while True:
        playAgainChoice = input("\n🔄 Do you want to play again? (Y/N): ").strip().upper()
        if playAgainChoice in ['Y', 'YES']:
            return True
        elif playAgainChoice in ['N', 'NO']:
            return False
        else:
            print("❌ Please enter Y for Yes or N for No")

def main():
    """Main game loop"""
    clearScreen()
    displayGameTitle()
    displayGameRules()
    
    gameCount = 0
    userWins = 0
    computerWins = 0
    ties = 0
    
    while True:
        gameCount += 1
        print(f"\n🎮 ROUND {gameCount}")
        print("-" * 30)
        
        # Get user choice
        userChoice = getUserChoice()
        
        # Get computer choice
        computerChoice = getComputerChoice(userChoice)
        
        # Display choices
        displayChoices(userChoice, computerChoice)
        
        # Determine winner
        winner = determineWinner(userChoice, computerChoice)
        
        # Update score
        if winner == "user":
            userWins += 1
        elif winner == "computer":
            computerWins += 1
        else:
            ties += 1
        
        # Display result
        displayResult(winner, userChoice, computerChoice)
        
        # Display score
        print(f"\n📊 SCORE: You {userWins} | Computer {computerWins} | Ties {ties}")
        
        # Ask to play again
        if not playAgain():
            break
        
        clearScreen()
        displayGameTitle()
    
    # Final message
    print("\n" + "=" * 60)
    print("🙏 THANKS FOR PLAYING! 🙏")
    print(f"📈 Final Score: You {userWins} | Computer {computerWins} | Ties {ties}")
    
    if userWins > computerWins:
        print("🏆 You are the overall winner! Congratulations! 🏆")
    elif computerWins > userWins:
        print("🤖 Computer wins overall! Better luck next time! 🤖")
    else:
        print("🤝 It's a tie overall! You're evenly matched! 🤝")
    
    print("=" * 60)

if __name__ == "__main__":
    main()