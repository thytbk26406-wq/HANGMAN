import random

# Level 1 - Easy: từ 3-4 ký tự
word_list = ["DOG", "TEA", "CAKE", "PEAR", "BIKE", "PINK", "SUIT", "BED", "EAR", "JULY"]
hint_list = ["animal", "drink", "food", "fruit", "vehicle", "color", "clothes", "sleep", "body", "month"]

# Danh sách từ vựng Level 2
word_list = [
    "APPLE", "TIGER", "ORANGE", "PLANET", "SCHOOL",
    "BRIDGE", "WINDOW", "GARDEN", "MONKEY", "JOURNEY"
]

# Gợi ý theo nhóm phân loại của từ
hint_list = [
    "Fruit",       # APPLE
    "Animal",      # TIGER
    "Color",       # ORANGE
    "Space",       # PLANET
    "Place",       # SCHOOL
    "Structure",   # BRIDGE
    "Object",      # WINDOW
    "Place",       # GARDEN
    "Animal",      # MONKEY
    "Travel"       # JOURNEY
]


# Hàm lấy từ ngẫu nhiên của Level 1 (từ nhánh lv1)
def random_word():
    i = random.randint(0, len(word_list) - 1)
    return word_list[i], hint_list[i]
