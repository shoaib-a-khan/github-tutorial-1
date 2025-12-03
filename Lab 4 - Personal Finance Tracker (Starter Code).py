# -*- coding: utf-8 -*-
"""
PERSONAL FINANCE TRACKER - STARTER CODE
Student Name: [Your Name]
Date: [Current Date]

Complete the TODO sections in each part below.
Work through Parts 1-4 sequentially.

INSTRUCTIONS:
1. Complete each PART in order
2. Test each part before moving to the next
3. Uncomment the test lines at the bottom to test
4. Focus on DICTIONARY operations
"""

# =============================================================================
# PART 1: THE FOUNDATION - MODELING A TRANSACTION
# =============================================================================

def part1():
    """
    TODO: Complete this function to create and display a single transaction dictionary.
    """
    print("=== Part 1: Single Transaction ===")
    
    # TODO: Get user input for transaction details
    # You need to ask for: date, description, amount, category
    
    # TODO: Create a transaction dictionary with the above values
    # Use these exact keys: 'date', 'description', 'amount', 'category'
    transaction = {
        # Add key-value pairs here
    }
    
    # TODO: Print the transaction dictionary
    print("\nYour transaction:", transaction)


# =============================================================================
# PART 2: TRACKING MULTIPLE TRANSACTIONS
# =============================================================================

def part2():
    """
    TODO: Complete this function to manage a list of transaction dictionaries.
    """
    print("\n=== Part 2: Transaction Log ===")
    
    # Create an empty list to store transactions
    transaction_log = []
    
    # TODO: Create a while loop that allows entering multiple transactions
    while True:
        print(f"\n--- Transaction #{len(transaction_log) + 1} ---")
        
        # TODO: Get transaction details (you can reuse code from Part 1)
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        
        # Convert amount to float (this part is done for you)
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue
            
        category = input("Enter category: ")
        
        # Create transaction dictionary (done for you)
        transaction = {
            'date': date,
            'description': description,
            'amount': amount,
            'category': category
        }
        
        # TODO: Add the transaction to transaction_log list
        
        # TODO: Ask if user wants to continue and break if they say 'no'
        continue_choice = input("\nWould you like to enter another transaction? (yes/no): ")
        # Add your break condition here
    
    # TODO: Print the entire transaction log
    print("\n--- Your Transaction Log ---")
    # Print each transaction here
    
    # TODO: Print total number of transactions
    # Hint: Use len(transaction_log)


# =============================================================================
# PART 3: GAINING INSIGHTS WITH FUNCTIONS
# =============================================================================

def get_total_spending(transactions):
    """
    Calculate the total amount spent across all transactions.
    
    Args:
        transactions: List of transaction dictionaries
    
    Returns:
        float: Total amount spent
    
    TODO: Implement this function
    """
    total = 0.0
    # TODO: Loop through transactions and sum all 'amount' values
    # Hint: Use a for loop to go through each transaction dictionary
    return total


def get_spending_by_category(transactions):
    """
    Calculate total spending for each category.
    
    Args:
        transactions: List of transaction dictionaries
    
    Returns:
        dict: Dictionary with categories as keys and total amounts as values
    
    TODO: Implement this function - FOCUS ON DICTIONARY OPERATIONS!
    """
    category_totals = {}
    
    # TODO: For each transaction in transactions:
    #   1. Get the category from the transaction dictionary
    #   2. Check if category is already a key in category_totals
    #   3. If not, add it with the transaction amount as value
    #   4. If yes, add the transaction amount to the existing value
    
    return category_totals


def print_summary(transactions):
    """
    Print a formatted financial summary.
    
    TODO: Call the functions above and print results in a nice format
    """
    print("\n--- Financial Summary ---")
    
    # TODO: Call get_total_spending and print the result
    # Format: "Total Spending: $X.XX"
    
    # TODO: Call get_spending_by_category and print each category
    # Format: "  CategoryName: $X.XX" for each category


def test_part3():
    """
    Test function for Part 3 - you can use this to test your functions
    """
    # Sample data for testing
    test_transactions = [
        {'date': '2023-10-26', 'description': 'Groceries', 'amount': 65.4, 'category': 'Food'},
        {'date': '2023-10-25', 'description': 'Movie', 'amount': 15.0, 'category': 'Entertainment'},
        {'date': '2023-10-24', 'description': 'Restaurant', 'amount': 35.0, 'category': 'Food'}
    ]
    
    print("\n=== Part 3: Testing Functions ===")
    print("Test transactions:", test_transactions)
    
    # Test get_total_spending
    total = get_total_spending(test_transactions)
    print(f"Total spending: ${total:.2f}")
    
    # Test get_spending_by_category
    by_category = get_spending_by_category(test_transactions)
    print("Spending by category:", by_category)
    
    # Test print_summary
    print_summary(test_transactions)


# =============================================================================
# PART 4: THE COMPLETE APPLICATION
# =============================================================================

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("    Personal Finance Tracker")
    print("="*40)
    print("1. Add a New Transaction")
    print("2. View All Transactions")
    print("3. Show Financial Summary")
    print("4. Filter Transactions by Category")
    print("5. Exit")
    print("="*40)


def add_transaction(transaction_log):
    """
    Add one or more transactions to the log.
    
    TODO: You can adapt your code from Part 2 here
    """
    while True:
        print(f"\n--- Adding Transaction #{len(transaction_log) + 1} ---")
        
        # TODO: Get transaction details from user
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        
        # Input validation for amount (done for you)
        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Please enter a valid number for the amount.")
        
        category = input("Enter category: ")
        
        # TODO: Create transaction dictionary and add to transaction_log
        
        # TODO: Ask if user wants to add another transaction
        # Break the loop if they don't want to continue


def view_transactions(transaction_log):
    """
    Display all transactions in a readable format.
    
    TODO: Print all transactions in a user-friendly way
    """
    if not transaction_log:
        print("No transactions found.")
        return
    
    print(f"\n--- All Transactions ({len(transaction_log)} total) ---")
    # TODO: Loop through transaction_log and print each transaction nicely
    # Format: "1. Date: 2023-10-26 | Description: Groceries | Amount: $65.40 | Category: Food"


def filter_by_category(transaction_log, category):
    """
    Filter transactions by category.
    
    Args:
        transaction_log: List of transaction dictionaries
        category: Category to filter by
    
    Returns:
        list: Filtered transactions
    
    TODO: Implement this function
    """
    filtered = []
    # TODO: Loop through transaction_log and add transactions to 'filtered'
    # if their category matches the input category
    return filtered


def main():
    """
    Main function to run the complete finance tracker application.
    
    TODO: Complete the menu-driven application
    """
    transaction_log = []  # This will store all our transactions
    
    print("Welcome to your Personal Finance Tracker!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # TODO: Call add_transaction function
            pass
            
        elif choice == '2':
            # TODO: Call view_transactions function
            pass
            
        elif choice == '3':
            # TODO: Call print_summary function
            pass
            
        elif choice == '4':
            if not transaction_log:
                print("No transactions to filter.")
                continue
            
            category = input("Enter category to filter by: ")
            filtered = filter_by_category(transaction_log, category)
            
            if filtered:
                print(f"\n--- Transactions in category '{category}' ---")
                for i, transaction in enumerate(filtered, 1):
                    print(f"{i}. {transaction['description']} - ${transaction['amount']:.2f}")
            else:
                print(f"No transactions found in category '{category}'")
        
        elif choice == '5':
            print("Thank you for using Personal Finance Tracker! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-5.")


# =============================================================================
# TESTING AREA
# =============================================================================

def get_sample_data():
    """
    Returns sample transactions for testing purposes.
    """
    return [
        {'date': '2023-10-26', 'description': 'Groceries at Market', 'amount': 65.40, 'category': 'Food'},
        {'date': '2023-10-25', 'description': 'Movie Tickets', 'amount': 15.00, 'category': 'Entertainment'},
        {'date': '2023-10-24', 'description': 'Gas Station', 'amount': 45.50, 'category': 'Transport'},
        {'date': '2023-10-23', 'description': 'Coffee Shop', 'amount': 12.75, 'category': 'Food'},
        {'date': '2023-10-22', 'description': 'Book Store', 'amount': 25.00, 'category': 'Entertainment'}
    ]


if __name__ == "__main__":
    """
    TESTING INSTRUCTIONS:
    Uncomment one line at a time to test each part as you complete it.
    """
    
    # Test Part 1 (Single Transaction)
    # part1()
    
    # Test Part 2 (Multiple Transactions)
    # part2()
    
    # Test Part 3 (Analysis Functions)
    # test_part3()
    
    # Test with sample data
    # print_summary(get_sample_data())
    
    # Run the complete application (Part 4)
    main()