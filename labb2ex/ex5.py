def get_char(string, position):
    if position > (len(string) - 1):
        return 'Invalid position.'
    else:
        return string[position]