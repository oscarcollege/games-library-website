import os

def fill_template(template, games_list):
    output = ''
    for game_name in games_list:
        image_src = f'games/{game_name}/1.jpg'
        with open(f'games/{game_name}/desc.txt', 'r') as file:
            description = file.read()
        price = description.split('\n')[0]
        filled_template = template.replace('{{Image Src}}', image_src)
        filled_template = filled_template.replace('{{Name}}', game_name)
        filled_template = filled_template.replace('{{Price}}', price)
        output += filled_template
    return output

game_folders_list = os.listdir('games')

outputs = []
lists = ['wishlist.txt', 'popular.txt', 'friends play.txt', 'recommended.txt']

for game_list in lists:
    with open('partials/Games_List_Template.html', 'r') as file:
        template = file.read()

    with open(f'game lists/{game_list}', 'r') as file:
        games_list = file.read().split('\n')

    outputs.append(fill_template(template, games_list))

with open('partials/build.html', 'r') as file:
    build_template = file.read()

filled_template = build_template.replace('{{Wishlist}}', outputs[0])
filled_template = filled_template.replace('{{Popular Games List}}', outputs[1])
filled_template = filled_template.replace('{{Friends Played}}', outputs[2])
filled_template = filled_template.replace('{{Recommended}}', outputs[3])

with open('index.html', 'w') as file:
    file.write(filled_template)
