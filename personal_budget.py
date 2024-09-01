import re
#Task 1
class BudgetCategory:
    def __init__(self, category, allocated_budget):
        self.__category = category
        self.__allocated_budget = allocated_budget
#Task 2
    def get_category(self):
        return self.__category
    
    def set_category(self, new_category):
        self.__category = new_category

    def get_budget(self):
        return self.__allocated_budget
    
    def set_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
            print(f"New allocated budget: ${self.__allocated_budget}")
        else:
            print(f"{new_budget} is not a positive number.")
#Task 3
    def add_expenses(self, amount):
        new_budget = self.__allocated_budget - amount
        print(f"${amount} removed from budget.")
        self.set_budget(new_budget)
        

#Task 4:
    def display_category_summary(self):
        print(f"Current Budget: ${self.__allocated_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expenses(100)
food_category.display_category_summary()

