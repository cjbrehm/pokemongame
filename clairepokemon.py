# This is Claire's pokemon game 
import random 

name = input("What is your name? ")

class Trainer:
    pokedex = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        self.pokedex.append(pokemon)


player = Trainer(name)

class Pokemon:
    def __init__(self, name, element, weakness, attacks):
        self.name = name 
        self.element = element
        self.weakness = weakness
        self.attacks = attacks
        self.health = 10

charmander = Pokemon(
    name = 'Charmander',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}]
)

squirtle = Pokemon(
    name = 'Squirtle',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}]
)

bulbasaur = Pokemon(
    name = 'Bulbasaur',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}]
)

flareon = Pokemon(
    name = 'Flareon',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}]
)

vaporeon = Pokemon(
    name = 'Vaporeon',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}]
)

leafeon = Pokemon(
    name = 'Leafeon',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}]
)

ivysaur = Pokemon(
    name = 'Ivysaur',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}]
)

venusaur = Pokemon(
    name = 'Venusaur',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}]
)

wartortle = Pokemon(
    name = 'Wartortle',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}]
)

blastoise = Pokemon(
    name = 'Blastoise',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}]
)

charmeleon = Pokemon(
    name = 'Charmeleon',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}]
)

ponyta = Pokemon(
    name = 'Ponyta',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}]
)

wild_pokemons = [charmander, squirtle, bulbasaur, flareon, vaporeon, leafeon, ivysaur, venusaur, wartortle, blastoise, charmeleon, ponyta]


index = int(input("Choose a random pokemon by selecting a number 0 through 12: "))
pokemon = wild_pokemons.pop(index)
player.add_pokemon(pokemon)
for pokemon in player.pokedex:
    print(pokemon.name)


#print('These pokemon are still wild:', wild_pokemons)
#print(player.pokedex)

def catch_battle():
    #opponent = wild_pokemons.pop(random.choice(pokemon.name))
    opponent = random.choice(wild_pokemons)
    print(f"You've encountered a wild {opponent.name}!")
    return opponent

def main_menu():
    action_taken = input("\n What would you like to do? "
        "\n - Catch Pokemon"
        "\n - Quit"
        "\n > ")
    if 'catch' in action_taken.lower():
        opponent = catch_battle()
        return opponent
    elif action_taken.lower() == "quit":
        print(f"Thanks for playing, {player.name}!")

def find_pokemon(your_poke_name):
    print(your_poke_name)
    for pokemon in player.pokedex:
        if pokemon.name.lower() == your_poke_name:
            return pokemon
        # else:
        #     pass
        

def choose_battle_poke():
    print("Which pokemon do you want to use? ")
    for pokemon in player.pokedex:
       print(pokemon.name)
    your_poke = (input('> '))
    print(f"Go get 'em {your_poke}! ")
    your_poke = find_pokemon(your_poke)
    return your_poke


def run_pokemon():
    opponent.health = 10
    print("You got away safely.")
    main_menu()

















def fight_pokemon(players_pokemon, opponent):
    pokemon_health = players_pokemon.health
    opponent_health = opponent.health
    # hit = random.randint(1,3)
    turn = players_pokemon
    winner = None

    while winner is None:
        if  turn == players_pokemon:
            print("Which attack do you want to use? ")
            for i in players_pokemon.attacks:
                print(i, players_pokemon.attacks[name,type])
            print("> ")
            opponent_health = opponent_health - random.randint(1,3)
            print(f"You attacked {opponent.name} with ! Their health is now {opponent_health}.")
            turn = opponent
        else:
            pokemon_health = pokemon_health - random.randint(1,3)
            print(f"{opponent.name} attacked you! {players_pokemon.name}'s health is now {pokemon_health}")
            turn = players_pokemon
        
        if opponent_health <= 0:
            winner = players_pokemon.name
        elif pokemon_health <= 0:
            winner = opponent.name
    print(f"The winner is {winner}!")





















opponent = main_menu()
players_pokemon = choose_battle_poke()
battle_action_taken = input("\n Battle Menu: "
    "\n - Fight"
    "\n - Switch Pokemon"
    "\n - Run"
    "\n > ")
if 'fight' in battle_action_taken.lower():
    fight_pokemon(players_pokemon, opponent)
elif 'switch' in battle_action_taken.lower():
    choose_battle_poke()
elif 'run' in battle_action_taken.lower():
    run_pokemon()




# make pokemon list a dictionary 
# take out functions that aren't used in 