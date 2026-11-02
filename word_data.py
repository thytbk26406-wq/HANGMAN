import word_data
word_list = ["DOG", "TEA", "CAKE", "PEAR", "BIKE","PINK", "SUIT", "BED", "EAR", "JULY"]
hint_list = ["animal", "drink", "food", "fruit", "vehicle","color", "clothes", "sleep", "body", "month"]
def random_word():
    i = word_data.randint(0, len(word_list) - 1)
    word = word_list[i]
    hint = hint_list[i]
    return word, hint

