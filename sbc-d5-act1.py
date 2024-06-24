l = []

while len(l) < 5:
    user = int(input("Choose a number: "))
    l.append(user)
    
print(l)

while True:
    action = input("Add, Delete, or Done? ").lower()
    
    if action == "add":
        add_num = int(input("Enter a number to add: "))
        l.append(add_num)
        if len(l) > 5:
            l.pop(0)  # Delete the first element
            l.pop()   # Delete the last element
    elif action == "delete":
        if len(l) > 0:
            del_num = int(input("Enter the index of the number to delete (0 to {}): ".format(len(l)-1)))
            if del_num >= 0 and del_num < len(l):
                l.pop(del_num)
            else:
                print("Invalid index. Please try again.")
        else:
            print("The list is empty. Nothing to delete.")
    elif action == "done":
        break
    else:
        print("Invalid action. Please choose 'Add', 'Delete', or 'Done'.")

print("Updated list:", l) 