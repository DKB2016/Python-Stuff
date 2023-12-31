#
##
#

def main():
    
    shopping_list = ["milk", "pasta", "eggs", "cheese", "spam", "bread", "rice"]
    
    item_to_find = "spam"
    found_at = None
    
    for index in range(len(shopping_list)):
        if shopping_list[index] == item_to_find:
            found_at = index
            break
        
    print("Item found at index: " + str(index))
        
if __name__ == "__main__":
    main()