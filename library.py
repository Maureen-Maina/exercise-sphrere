# python function
def calculate_fine():
    ID = int(input("Enter your bookID: "))
    dueDate = int(input("Enter your dueDate: "))
    returnDate = int(input("Enter the return date: "))
    
    days_overdue = returnDate - dueDate
    print("Days overdue:", days_overdue)
    
    if days_overdue <= 7:
        fine = 20 * days_overdue 
        print("Fine:", fine)
        
    elif days_overdue >= 8 and days_overdue <= 14:
        fine = 50 * days_overdue 
        print("Fine:", fine)
        
    elif days_overdue > 15:
        fine = 100 * days_overdue 
        print("Fine:", fine)

calculate_fine()
    
