def main():
    print("=== Daily Task Reminder ===")
    
    task = input("Enter your task: ")
    
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter only 'high', 'medium', or 'low'")
    
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter only 'yes' or 'no'")
    
    print("\n" + "="*40)
    print("REMINDER:")
    
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"⚠️  '{task}' is a HIGH priority task that requires immediate attention today!")
            else:
                print(f"🔴 '{task}' is a HIGH priority task. Focus on this soon.")
        
        case 'medium':
            if time_bound == 'yes':
                print(f"🟡 '{task}' is a MEDIUM priority task with a deadline. Plan to complete it today.")
            else:
                print(f"🟡 '{task}' is a MEDIUM priority task. Schedule time for it this week.")
        
        case 'low':
            if time_bound == 'yes':
                print(f"🟢 '{task}' is a LOW priority task but has a time constraint. Complete when possible.")
            else:
                print(f"🟢 Note: '{task}' is a LOW priority task. Consider completing it when you have free time.")
    
    print("="*40)

if __name__ == "__main__":
    while True:
        main()
        
        while True:
            continue_choice = input("\nWould you like to add another task? (yes/no): ").lower()
            if continue_choice in ['yes', 'no']:
                break
            else:
                print("Please enter only 'yes' or 'no'")
        
        if continue_choice == 'no':
            print("\nThank you for using Daily Task Reminder! Goodbye! 👋")
            break
        else:
            print("\n" + "="*50 + "\n")