import random
from word_data import word_list, hint_list


class HangmanLogic:
    def __init__(self):
        self.score = 0
        self.lives = 6
        self.secret_word = ""
        self.hint = ""
        self.guessed_letters = []
        self.remaining_indices = []

    def reset_game(self):
        """Khởi tạo danh sách chỉ số từ vựng và đặt lại điểm số"""
        self.remaining_indices = []
        for i in range(len(word_list)):
            self.remaining_indices.append(i)
        self.score = 0

    def prepare_next_word(self):
        """Chọn ngẫu nhiên một từ mới. Trả về False nếu đã chơi hết danh sách từ"""
        if len(self.remaining_indices) == 0:
            return False

        random_pos = random.randint(0, len(self.remaining_indices) - 1)
        chosen_index = self.remaining_indices.pop(random_pos)
        self.secret_word = word_list[chosen_index]
        self.hint = hint_list[chosen_index]

        self.lives = 6
        self.guessed_letters = []
        return True

    def get_display_text(self):
        """Tạo chuỗi ký tự hiển thị (chữ đã đoán hoặc dấu _)"""
        display_text = ""
        for i in range(len(self.secret_word)):
            char = self.secret_word[i]
            if char in self.guessed_letters:
                display_text += char
            else:
                display_text += "_"

            if i < len(self.secret_word) - 1:
                display_text += " "
        return display_text

    def process_guess(self, letter):
        """
        Xử lý khi người chơi chọn một chữ cái.
        Trả về tuple: (is_correct, is_win)
        """
        if letter in self.secret_word:
            self.guessed_letters.append(letter)

            # Kiểm tra xem đã đoán hết các chữ cái chưa
            is_win = True
            for char in self.secret_word:
                if char not in self.guessed_letters:
                    is_win = False
                    break

            if is_win:
                self.score += 1

            return True, is_win
        else:
            self.lives -= 1
            return False, False

    def get_wrong_count(self):
        """Tính số lần đoán sai (từ 1 đến 6)"""
        return 6 - self.lives

    def get_total_words(self):
        return len(word_list)

    def get_current_round(self):
        return len(word_list) - len(self.remaining_indices)