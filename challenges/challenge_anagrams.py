def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    if len(first_string) == len(second_string):
        return True
    if first_string == "" or second_string == "":
        return False
