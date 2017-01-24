def alphabet_position(letter):
    al="abcdefghijklmnopqrstuvwxyz"
    if letter.upper()==letter:
        return al.index(letter.lower())
    else:
        return al.index(letter)


def rotate_character(char, rot):
    rot=int(rot)
    al="abcdefghijklmnopqrstuvwxyz"
    if char in al:
        return al[(alphabet_position(char)+rot)%26]
    elif char.lower() in al:
        return al[(alphabet_position(char)+rot)%26].upper()
    return char


def encrypt(text, rot):
    al="abcdefghijklmnopqrstuvwxyz"
    encrypted=""
    for i in text:
        encrypted=encrypted+rotate_character(i, rot)
    return encrypted
