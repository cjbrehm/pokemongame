# This is Claire's pokemon game 
import random 
import sys

#create the Trainer class which handles the pokedex and trainer's name
class Trainer:
    pokedex = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        self.pokedex.append(pokemon)

# create the Pokemon class which handles each pokemon and their attributes
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
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}],
)

squirtle = Pokemon(
    name = 'Squirtle',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}],
)

bulbasaur = Pokemon(
    name = 'Bulbasaur',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}],   
)

flareon = Pokemon(
    name = 'Flareon',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}], 
)

vaporeon = Pokemon(
    name = 'Vaporeon',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}],
)

leafeon = Pokemon(
    name = 'Leafeon',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}], 
)

ivysaur = Pokemon(
    name = 'Ivysaur',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}], 
)

venusaur = Pokemon(
    name = 'Venusaur',
    element = 'grass',
    weakness = 'fire',
    attacks = [{'name': 'vine whip', 'type': 'grass'}, {'name': 'tackle', 'type': 'normal'}],
)

wartortle = Pokemon(
    name = 'Wartortle',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}], 
)

blastoise = Pokemon(
    name = 'Blastoise',
    element = 'water',
    weakness = 'grass',
    attacks = [{'name': 'water gun', 'type': 'water'}, {'name': 'tackle', 'type': 'normal'}],   
)

charmeleon = Pokemon(
    name = 'Charmeleon',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}],  
)

ponyta = Pokemon(
    name = 'Ponyta',
    element = 'fire',
    weakness = 'water',
    attacks = [{'name': 'ember', 'type': 'fire'}, {'name': 'tackle', 'type': 'normal'}],  
)

#The list of pokemon, which are all wild at the start of the game
wild_pokemons = [charmander, squirtle, bulbasaur, flareon, vaporeon, leafeon, ivysaur, venusaur, wartortle, blastoise, charmeleon, ponyta]

#allows the chosen pokemon to be found by the game as the input is a string not a number
def find_pokemon(your_poke_input: str) -> Pokemon:
    print(your_poke_input)
    for pokemon in player.pokedex:
        if pokemon.name.lower() == your_poke_input:
            return pokemon


# the battle between two pokemon

def battle():
    winner = None
    opponent = random.choice(wild_pokemons)
    def choose_battle_poke():
        print("Which pokemon do you want to use? ")
        for pokemon in player.pokedex:
            print(pokemon.name)

    def main_menu():
        nonlocal winner
        if winner is None:
            action_taken = input("\n What would you like to do? "
                "\n - Catch Pokemon"
                "\n - Quit"
                "\n > ")
            
            if 'catch' in action_taken.lower():
                action = 'catch'
                print(f"You've encountered a wild {opponent.name}!")
            elif action_taken.lower() == "quit":
                print(f"Thanks for playing, {player.name}!")
                action = 'quit'
                sys.exit()
            elif action_taken.lower() != "quit" and action_taken.lower() != "catch":
                print('Please respond with one of the options below:')
                main_menu()
        else:
            pass

    #battle functions 

    def battle_action_taken():
        battle_action = input("\n Battle Menu: "
        "\n - Fight"
        "\n - Switch Pokemon"
        "\n - Run"
        "\n > ")
        if 'fight' in battle_action.lower():
            fight_pokemon(players_pokemon, opponent)
        elif 'switch' in battle_action.lower():
            switch_pokemon()
        elif 'run' in battle_action.lower():
            run_pokemon()


    def run_pokemon():
        winner = opponent
        opponent.health = 10
        print("\n You got away safely.")
        main_menu()


    def switch_pokemon():
        print("Which pokemon do you want to use? ")
        for pokemon in player.pokedex:
            print(f"{pokemon.name}: {pokemon.health}")
        your_poke = (input('> '))
        your_poke = find_pokemon(your_poke)
        print(f"Go get 'em {your_poke.name}! ")
        battle_action_taken()


    def fight_pokemon(players_pokemon: Pokemon, opponent):
        nonlocal winner
        pokemon_health = players_pokemon.health
        opponent_health = opponent.health
        hit = random.randint(1, 3)
        turn = players_pokemon
        
        while winner is None:
            if  turn == players_pokemon:
                print("Choose an attack: ")
                for index, pokemon_attack in enumerate(players_pokemon.attacks):
                    print(index, pokemon_attack['name'])
                print("\n If you want to get out of the game: "
                "\n 2. Run")
                input_attack_index = int(input("> "))
                if input_attack_index == 2:
                    winner = opponent.name
                    opponent_health = 10
                    print("You got away safely. ")
                if input_attack_index != 2:
                    selected_attack_dict = players_pokemon.attacks[input_attack_index]
                    opponent_health = opponent_health - random.randint(1,3)
                    if opponent_health <= 0:
                        opponent_health = 0
                    print(f"You attacked {opponent.name} with {selected_attack_dict}! Their health is now {opponent_health}.")
                    turn = opponent
            else:
                pokemon_health = pokemon_health - random.randint(1,3)
                if pokemon_health <= 0:
                    pokemon_health = 0
                print(f"{opponent.name} attacked you! {players_pokemon.name}'s health is now {pokemon_health}.")
                turn = players_pokemon
            
                if opponent_health == 0:              
                    winner = players_pokemon.name
                elif pokemon_health == 0:
                    winner = opponent.name
                if winner is not None:
                    print(f"The winner is {winner}!")
        main_menu()
            

        if winner == players_pokemon.name:
            opponent.health = 10 
            players_pokemon.health = 10
            player.pokedex.append(wild_pokemons.pop(wild_pokemons.index(opponent)))
            print(f"You caught {opponent.name}! ")

        elif winner == opponent.name:
            opponent.health = 10 
            players_pokemon.health = 10
            wild_pokemons.append(player.pokedex.pop(player.pokedex.index(players_pokemon)))


    #call the functions of the battle 
    choose_battle_poke()
    your_poke_input = (input('> '))
    your_poke = find_pokemon(your_poke_input)
    print(f"Go get 'em {your_poke.name}! "
    "\n")
    players_pokemon = your_poke
    main_menu()
    print('\n What would you like to do? ')
    battle_action_taken()
  
    

#the game where the battle function is called
name = input("What is your name? ")
player = Trainer(name)

#how to choose a pokemon from the wild pokemons list
index = int(input("Choose a random pokemon by selecting a number 0 through 12: "))
pokemon = wild_pokemons.pop(index)
player.add_pokemon(pokemon)
for pokemon in player.pokedex:
    print(f'You chose {pokemon.name}! '
    '\n')

#How to identify when the game is over 
while True:
    if len(player.pokedex) == 12:
        print(f"Way to go! You caught all the pokemon. You win! Thanks for playing, {player.name}")
        sys.exit()
    elif len(player.pokedex) == 0:
        print("Oh no, you lost all your pokemon. Game over... ")
        sys.exit()
    else:
        battle()