class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        self.health

Hero = Character(10, 3)
Goblin = Character(6, 2)
Zombie = Character(Hero.power + 1, 5)

while Hero.alive() and Goblin.alive():
    print("You have %d health and %d power." % (Hero.health, Hero.power))
    print("The goblin has %d health and %d power." % (Goblin.health, Goblin.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()
    if user_input == "1":
        # Hero attacks goblin
        Goblin.health -= Hero.power
        print("You do %d damage to the goblin." % Hero.power)
        if Goblin.health <= 0:
            print("The goblin is dead.")
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)

    if Goblin.health > 0:
        # Goblin attacks hero
        Hero.health -= Goblin.power
        print("The goblin does %d damage to you." % Goblin.power)
        if Hero.health <= 0:
            print("You are dead.")

print("A zombie appears!<oh, no!>")

while Hero.alive() and Zombie.alive():
    print("You have %d health left." %(Hero.health))
    print("What do you want to do?")
    print("1. fight zombie")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()
    if user_input == "1":
        print("Zombie is unaffected!")
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Zombie stumbles closer!")
    else:
        print("Invalid input %r" % user_input)
    Zombie.attack(Hero)
    if Hero.health <= 0:
        print("You are dead!")
        break

