import re
import nltk
nltk.download('punkt')  # Tải dữ liệu cần thiết cho việc tách câu
from underthesea import word_tokenize #thư viện ghép chữ có nghĩa trong câu
from collections import Counter
from nltk.tokenize import sent_tokenize

text_file = "D:\\SonThai-Learning-Master\\VN-Text-Summarization\\copus_original.txt"

### Tiền xử lý văn bản
def XL_noidung_original (noidung):
    # Mở file để đọc
    with open(noidung, 'r', encoding='utf-8') as file:
        # Đọc nội dung từ file
        content = file.read()
    
    output = content.lower() #chuyển đổi sang chữ thường
    output = output.replace('\n', '. ') #Đổi các ký tự xuống dòng thành chấm câu
    output = output.strip() #Loại bỏ đi các khoảng trắng thừa
    output = re.sub(r'([.!?])\1+', r'\1', output) #xử lý dấu câu trùng lặp
    output = re.sub(r'[\"\'‘’“”`‛‟«»„‹›「」『』()〝〞〟〰]', '', output) #xóa ký tự không cần thiết
    return output

### Tiền xử lý tách văn bản thành câu
def tach_van_ban_thanh_cau(van_ban):
    return sent_tokenize(van_ban)


### Tiền xử lý ghép từ có nghĩa
def tien_xu_ly_ghep_tu_co_nghia(van_ban):
    return word_tokenize(van_ban, format="text")


### xử lý file
ketquaXL = XL_noidung_original(text_file)
print("ket qua tien xu ly van ban: \n")
print(ketquaXL)
print("\n")


## ghép từ có nghĩa.
ketquaXL_gheptu = tien_xu_ly_ghep_tu_co_nghia(ketquaXL)
print("ket qua tien xu ly ghep tu co nghia: \n")
print(ketquaXL_gheptu)
print("\n")


## tách câu
ketquaXL_tachcau = tach_van_ban_thanh_cau(ketquaXL_gheptu)
print("ket qua tien xu ly tach cau: \n")
print(ketquaXL_tachcau)
print("\n")









