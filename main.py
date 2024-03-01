import re
import nltk
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from underthesea import word_tokenize as vt_word_tokenize

# Tải dữ liệu cần thiết cho việc tách câu (nếu chưa tải)
nltk.download('punkt')

text_file = "D:\\SonThai-Learning-Master\\VN-Text-Summarization\\copus_original.txt"

### Tiền xử lý văn bản
def XL_noidung_original(noidung):
    # Mở file để đọc
    with open(noidung, 'r', encoding='utf-8') as file:
        # Đọc nội dung từ file
        content = file.read()
        
    # Chuyển đổi sang chữ thường
    output = content.lower()  
    # Đổi các ký tự xuống dòng thành chấm câu
    output = output.replace('\n', '. ')  
    # Loại bỏ đi các khoảng trắng thừa
    output = output.strip()  
    # Xử lý dấu câu trùng lặp
    output = re.sub(r'([.!?])\1+', r'\1', output)  
    # Xóa ký tự không cần thiết
    output = re.sub(r'[\"\'‘’“”`‛‟«»„‹›「」『』()〝〞〟〰]', '', output)  
    return output

### Tiền xử lý tách văn bản thành câu
def tach_van_ban_thanh_cau(van_ban):
    return sent_tokenize(van_ban)

### Tiền xử lý ghép từ có nghĩa
def tien_xu_ly_ghep_tu_co_nghia(van_ban):
    return vt_word_tokenize(van_ban, format="text")

### Tính điểm cho từng câu
def tinh_diem_cau(cac_cau, tan_so_tu):
    diem_cau = {}
    for i, cau in enumerate(cac_cau):
        tu_ca_i = vt_word_tokenize(cau, format="text").split()  # Sử dụng thư viện Underthesea để tách từ
        diem_cau[i] = sum(tan_so_tu[tu] for tu in tu_ca_i)
    return diem_cau

### Tạo tóm tắt
def tao_tom_tat(cac_cau, so_cau_tom_tat=3):
    # Tính tần số xuất hiện của từng từ
    tan_so_tu = Counter(' '.join(cac_cau).split())
    # Tính điểm cho từng câu
    diem_cau = tinh_diem_cau(cac_cau, tan_so_tu)
    # Chọn các câu có điểm cao nhất
    cac_cau_tom_tat = sorted(diem_cau.keys(), key=lambda i: diem_cau[i], reverse=True)[:so_cau_tom_tat]
    # Sắp xếp lại các câu theo thứ tự xuất hiện ban đầu
    cac_cau_tom_tat.sort()
    # Gộp các câu đã chọn để tạo tóm tắt
    tom_tat = ' '.join(cac_cau[i] for i in cac_cau_tom_tat)
    return tom_tat

#Tiền xử lý thêm sau khi tóm tắt để có đoạn văn bản đẹp
def XL_output(kq_tomtat):
    formatted_text = kq_tomtat.replace("_", " ")
    formatted_text = re.sub(r'\s*([,\.])', r'\1', formatted_text)
    return formatted_text

# Tiền xử lý văn bản
ketquaXL = XL_noidung_original(text_file)
print("Kết quả tiền xử lý văn bản:\n", ketquaXL, "\n")

# Ghép từ có nghĩa
ketquaXL_gheptu = tien_xu_ly_ghep_tu_co_nghia(ketquaXL)
print("Kết quả tiền xử lý ghép từ có nghĩa:\n", ketquaXL_gheptu, "\n")

# Tách câu
ketquaXL_tachcau = tach_van_ban_thanh_cau(ketquaXL_gheptu)
print("Kết quả tiền xử lý tách câu:\n", ketquaXL_tachcau, "\n")

# kết quả tóm tắt với số lượng câu mong muốn, ở đây đang để là 5 câu.
tom_tat = XL_output(tao_tom_tat(ketquaXL_tachcau, 5))
print("Tóm tắt:\n", tom_tat)


