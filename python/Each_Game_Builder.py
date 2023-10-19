import os

with open('partials/Each_Game_Partial.html', 'r') as file:
    template = file.read()

games_list = os.listdir('games')

for game_folder in games_list:
    with open(f'games/{game_folder}/desc.txt', 'r') as file:
        description = file.read()
        price = description.split('\n')[0]
        description = '\n'.join(description.split('\n')[1:])
    name = game_folder

    filled_template = template.replace('{{Name}}', name)
    filled_template = filled_template.replace('{{Price}}', price)
    filled_template = filled_template.replace('{{Description}}', description)

    with open(f'game sites/{name}.html', 'w') as file:
        file.write(filled_template)
