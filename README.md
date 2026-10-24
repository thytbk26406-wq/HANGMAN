# HANGMAN – Trò chơi đoán từ

Bài tập nhóm môn Tư duy lập trình: lập trình game Hangman bằng Python và PyQt6 + Qt Designer.

## Chức năng hiện có

- Trang chủ với 2 nút **Đăng ký** và **Đăng nhập**.
- **Đăng ký**: nhập tên đăng nhập, mật khẩu và xác nhận lại mật khẩu. Mật khẩu phải có ít nhất 8 ký tự, 1 chữ cái in hoa, 1 số, 1 ký tự đặc biệt.
- **Đăng nhập**: đúng tên đăng nhập và mật khẩu đã đăng ký thì chuyển sang trang tiếp theo (phần game đang được phát triển).
- Hiện thông báo lỗi màu đỏ khi nhập sai, nút con mắt để hiện/ẩn mật khẩu, nút mũi tên để quay lại.

## Cách chạy

```bash
pip install PyQt6
python main.py
```

Các file `main.py`, `welcome.ui`, `login.ui`, `register.ui` và ảnh logo phải nằm cùng một thư mục.
