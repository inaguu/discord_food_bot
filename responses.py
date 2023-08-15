def get_response(message):
    p_message = message.lower()

    if p_message.find('!add') > -1:
        add_food = p_message.replace('!add', '').split()
        add_food = ' '.join(map(str, add_food))

        return f"***{add_food.capitalize()}*** has been added to the list."

    if p_message.find('!list') > -1:
        return "The list contains:"

    if p_message == '!help':
        return '`This is a help message`'

    if p_message == '!pick':
        return "We got"

    return None
