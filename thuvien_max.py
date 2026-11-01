# Dữ liệu mẫu để test
# Sau này thay bằng danh sách của nhóm
scores_easy = [7, 9, 6, 10, 8]
scores_medium = [5, 7, 8, 6]
scores_hard = [3, 5, 7, 4]


def diem_cao_nhat(scores):
    if len(scores) == 0:
        return 0
    return max(scores)


def lay_diem_3_level():
    easy = diem_cao_nhat(scores_easy)
    medium = diem_cao_nhat(scores_medium)
    hard = diem_cao_nhat(scores_hard)

    return easy, medium, hard