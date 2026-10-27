# Danh sách lưu điểm của 5 ván gần nhất
scores_easy = []
scores_medium = []
scores_hard = []

# Hàm 1: Tính điểm sau mỗi ván
def tinh_diem(level, so_lan_sai, thang):
    if thang == False:
        return 0
    if level == "Easy":
        diem = 200 - so_lan_sai * 10
    elif level == "Medium":
        diem = 200 - so_lan_sai * 15
    elif level == "Hard":
        diem = 200 - so_lan_sai * 20
    else:
        return 0
    return max(0, diem) #nếu điểm ra âm thì sẽ trả về 0

# Hàm 2: Lưu điểm và tìm điểm cao nhất

def luu_diem(level, diem=None):
    if level == "Easy":
        scores = scores_easy
    elif level == "Medium":
        scores = scores_medium
    elif level == "Hard":
        scores = scores_hard
    else:
        return 0
    if diem is not None: #nếu có điểm trả về thì phải lưu điểm
        scores.append(diem)
    if len(scores) == 0:
        return 0
    return max(scores)
       
# Hàm 3: Tính điểm và lưu điểm sau một ván
def ket_thuc_van(level, so_lan_sai, thang):
    diem = tinh_diem(level, so_lan_sai, thang)
    diem_cao_nhat = luu_diem(level, diem)
    return diem_cao_nhat