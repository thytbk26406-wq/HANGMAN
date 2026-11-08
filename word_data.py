
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
# LEVEL 1 (nhánh lv1) - test.py dùng word_list, hint_list
# ==============================

word_list = ["DOG", "TEA", "CAKE", "PEAR", "BIKE", "PINK", "SUIT", "BED", "EAR", "JULY"]
hint_list = ["animal", "drink", "food", "fruit", "vehicle", "color", "clothes", "sleep", "body", "month"]


# ==============================
# HÀM LẤY TỪ NGẪU NHIÊN
# ==============================

def random_word(level=None):

    # Không truyền level -> dùng danh sách Level 1 (giữ cách dùng của nhánh lv1)
    if level is None:
        word_list_chon = word_list
        hint_list_chon = hint_list

    # Kiểm tra cấp độ Easy
    elif level == "Easy":
        word_list_chon = word_list_easy
        hint_list_chon = hint_list_easy

    # Kiểm tra cấp độ Medium
    elif level == "Medium":
        word_list_chon = word_list_medium
        hint_list_chon = hint_list_medium

    # Kiểm tra cấp độ Hard
    elif level == "Hard":
        word_list_chon = word_list_hard
        hint_list_chon = hint_list_hard

    # Nếu cấp độ không hợp lệ
    else:
        return None, None

    # Chọn vị trí ngẫu nhiên
    index = random.randint(0, len(word_list_chon) - 1)

    # Trả về từ và gợi ý tương ứng
    return word_list_chon[index], hint_list_chon[index]
