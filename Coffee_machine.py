class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def supply(self):
        print("\nThe coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.beans} of coffee_beans\n"
              f"{self.cups} of disposable cups\n"
              f"${self.money} of money\n")

    def check(self, r_water, r_milk, r_beans, r_cups, r_money):
        if self.water < r_water:
            print("Sorry, not enough water!")
        elif self.water < r_milk:
            print("Sorry, not enough milk!")
        elif self.water < r_beans:
            print("Sorry, not enough coffee beans!")
        elif self.water < r_cups:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resource, making you a coffee!")
            self.water -= r_water
            self.milk -= r_milk
            self.beans -= r_beans
            self.cups -= r_cups
            self.money += r_money

    def buy_coffee(self):
        coffee_type = input("What do you want to buy? 1 - espresso, "
                            "2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee_type == "back":
            return
        elif coffee_type == "1":
            self.check(250, 0, 16, 1, 4)
        elif coffee_type == "2":
            self.check(350, 75, 20, 1, 7)
        elif coffee_type == "3":
            self.check(200, 100, 12, 1, 6)

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans "
                                "do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee "
                               "do you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def action(self):
        while True:
            buyer_action = input("Write action (buy, fill, take, remaining, exit):\n")
            if buyer_action == "buy":
                self.buy_coffee()
            elif buyer_action == "fill":
                self.fill()
            elif buyer_action == "take":
                self.take()
            elif buyer_action == "remaining":
                self.supply()
            elif buyer_action == "exit":
                break
            else:
                print(f"Command '{buyer_action}' not found")


# Initial state of the coffee machine
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
# ask the client what he wants to do
coffee_machine.action()
