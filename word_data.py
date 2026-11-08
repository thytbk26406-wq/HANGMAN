
import random


# ==============================
# LEVEL 1: EASY
# ==============================

word_list_easy = [
    "APPLE", "TIGER", "ORANGE", "HOUSE", "WATER",
    "MUSIC", "HAPPY", "TABLE", "CHAIR", "PHONE"
]

hint_list_easy = [
    "Fruit",       # APPLE
    "Animal",      # TIGER
    "Color",       # ORANGE
    "Place",       # HOUSE
    "Drink",       # WATER
    "Entertainment",  # MUSIC
    "Feeling",     # HAPPY
    "Furniture",   # TABLE
    "Furniture",   # CHAIR
    "Technology"  # PHONE
]


# ==============================
# LEVEL 2: MEDIUM
# ==============================

word_list_medium = [
    "APPLE", "TIGER", "ORANGE", "PLANET", "SCHOOL",
    "BRIDGE", "WINDOW", "GARDEN", "MONKEY", "JOURNEY"
]

hint_list_medium = [
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


# ==============================
# LEVEL 3: HARD
# ==============================

word_list_hard = [
    "COMPUTER", "ELEPHANT", "MOUNTAIN", "HOSPITAL", "NOTEBOOK",
    "BUTTERFLY", "WATERFALL", "IMPORTANT", "ADVENTURE", "KNOWLEDGE"
]

hint_list_hard = [
    "Technology",  # COMPUTER
    "Animal",      # ELEPHANT
    "Nature",      # MOUNTAIN
    "Place",       # HOSPITAL
    "Object",      # NOTEBOOK
    "Animal",      # BUTTERFLY
    "Nature",      # WATERFALL
    "Adjective",   # IMPORTANT
    "Experience",  # ADVENTURE
    "Knowledge"    # KNOWLEDGE
]


# ==============================
# HÀM LẤY TỪ NGẪU NHIÊN
# ==============================

def random_word(level):

    # Kiểm tra cấp độ Easy
    if level == "Easy":
        word_list = word_list_easy
        hint_list = hint_list_easy

    # Kiểm tra cấp độ Medium
    elif level == "Medium":
        word_list = word_list_medium
        hint_list = hint_list_medium

    # Kiểm tra cấp độ Hard
    elif level == "Hard":
        word_list = word_list_hard
        hint_list = hint_list_hard

    # Nếu cấp độ không hợp lệ
    else:
        return None, None

    # Chọn vị trí ngẫu nhiên
    index = random.randint(0, len(word_list) - 1)

    # Trả về từ và gợi ý tương ứng
    return word_list[index], hint_list[index]
