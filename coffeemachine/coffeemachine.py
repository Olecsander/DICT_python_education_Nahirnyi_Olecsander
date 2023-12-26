"""Jacobs: user-friendly device"""

class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = 'choosing an action'


    def remaining(self):
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n"
              f"{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n"
              f"{self.money} of money")


    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk do you want to add:\n> "))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))


    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n> ")
        if choice == 'back':
            return
        enough_resources = True
        if choice == '1':  # Espresso
            enough_resources = self.check_resources(250, 0, 16)
            cost = 4
        elif choice == '2':  # Latte
            enough_resources = self.check_resources(350, 75, 20)
            cost = 7
        elif choice == '3':  # Cappuccino
            enough_resources = self.check_resources(200, 100, 12)
            cost = 6

        if enough_resources:
            print("I have enough resources, making you a coffee!")
            self.money += cost


    def check_resources(self, water_needed, milk_needed, coffee_needed):
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_beans < coffee_needed:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return False
        self.water -= water_needed
        self.milk -= milk_needed
        self.coffee_beans -= coffee_needed
        self.cups -= 1
        return True


    def user_input(self, input_str):
        if self.state == 'choosing an action':
            if input_str == 'buy':
                self.state = 'choosing a type of coffee'
            elif input_str == 'fill':
                self.fill()
            elif input_str == 'take':
                self.take()
            elif input_str == 'remaining':
                self.remaining()
            elif input_str == 'exit':
                exit()
        elif self.state == 'choosing a type of coffee':
            self.buy()
            self.state = 'choosing an action'


def main():
    machine = CoffeeMachine()
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n> ")
        machine.user_input(action)


if __name__ == "__main__":
    main()
