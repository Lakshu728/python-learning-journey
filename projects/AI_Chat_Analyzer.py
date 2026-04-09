# smart AI Chat Analyzer
chat_history = []

def analyze_message(message):
      """ Analyze user message and return category & response."""
      message=message.lower()
      refund_keywords = {"refund", "return", "money back"}
      late_keywords = {"late", "delay", "not delivered"}
      thanks_keywords = {"thank you", "thanks", "good"}
      
      #category detection
      for word in refund_keywords:
          if word in message:
              return "Refund Request", "Your refund request is being processed."
          
      for word in late_keywords:
          if word in message:
              return "Delivery Issue", "Sorry for the delay, we will check your ordeer."
      
      for word in thanks_keywords:
          if word in message:
              return "Positive Feedback", "Thank You for your feedback!"
          
      return "Unkown", "Sorry, I didn't understand. Please try again."
  
  
def save_chat(message, category):
    ''' Save chat history in list'''
    chat_history.append((message, category))

def show_history():
    '''Display Chat history'''
    if not chat_history:
        print("No chat history found.")
    else:
        print("\n----Chat History-----")
        for i, data in enumerate(chat_history, start=1):
            print(f"{i}. Message: {data[0]} | category: {data[1]}")
            
def ai_score(message):
    ''' Simple AI sentiment score'''
    message = message.lower()
    
    positive_words = {"good", "thank", "great"}
    negative_words = {"bad", "late", "refund", "problem"}
    
    score = 0
    
    for word in positive_words:
        if word in message:
            score += 1
          
    for word in negative_words:
        if word in message:
            score -= 1
    return score

def retry():
    '''Recursion for retry system''' 
    choice = input("Do you want to try again? (yes/no): ").lower()
    if choice == "yes":
        run_chat()
    elif choice == "no":
        print("Thank you for using AI chat Analyzer!")  
    else :
        print("Invalid input!")
        retry() # recursion
        
def run_chat(): 
    '''Main Chat function'''
    message = input("\nEnter your message: ")
    
    category, response = analyze_message(message)
    
    print(f"\nCategory: {category}")
    print(f"Response: {response}")
    
    score = ai_score(message)
    print(f"AI Score: {score}")                                      
         
    save_chat(message, category)
    
    retry()
    
# Main Menu
while True:
    print("\n------ AI Chat Analyzer------") 
    print("1. Start Chat")
    print("2. View Chat History")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            run_chat()
            
        case 2:
            show_history()
            
        case 3:
            print("Exiting Program....") 
            break
                  
        case _:
            print("Invalid choice!")          