ĐỀ TÀI TÓM TẮT VĂN BẢN TIẾNG VIỆT THEO PHƯƠNG PHÁP TRÍCH XUẤT (Extractive summarization)

# Khái niệm tóm tắt trích xuất:
Tóm tắt trích xuất (extractive summarization) là quá trình tổng hợp thông tin từ một văn bản nguồn để tạo ra một bản tóm tắt mới, trong đó chỉ các đoạn văn bản quan trọng nhất được chọn lọc và sắp xếp lại mà không có sự thay đổi nội dung. Phương pháp này giữ nguyên các câu và đoạn văn bản từ nguồn gốc và tạo ra một tóm tắt bằng cách chọn những đoạn văn bản quan trọng nhất. Các hệ thống tóm tắt trích xuất thường sử dụng các kỹ thuật xử lý ngôn ngữ tự nhiên và máy học để xác định đoạn văn bản quan trọng. Các thuật toán có thể đánh giá mức độ quan trọng của mỗi câu dựa trên các yếu tố như tần suất xuất hiện của từ khóa, độ quan trọng của câu trong ngữ cảnh, hoặc sự tương đồng giữa các câu. Tóm tắt trích xuất thường được ứng dụng trong các ứng dụng như tổng hợp tin tức, tóm tắt nội dung bài báo, hoặc rút gọn thông tin từ các văn bản dài để giúp người đọc tiết kiệm thời gian. Tuy nhiên, một số hạn chế của phương pháp này có thể bao gồm việc mất mát thông tin quan trọng nếu các đoạn văn bản quan trọng không được chọn lựa đúng, và sự không linh hoạt trong việc tạo ra một tóm tắt có cấu trúc và ngôn ngữ tự nhiên.

# Sử dụng python 3.11.7
- download: https://www.python.org/downloads/release/python-3117/

# Thư viện sử dụng:
- underthesea
- nltk

# Trong đề tài này tập trung vào tóm tắt văn bản sử dụng ngôn ngữ tiếng việt.
- Văn bản: Văn bản đầu vào có thể chọn bất kỳ
- Tiền xử lý văn bản: Tại bước này, đề tài thực hiện quá trình tiền xử lý chuyển toàn bộ văn bản sang chữ viết thường, xóa các dấu và ký hiệu không cần thiết và xóa các khoảng trống.
- Tách câu trong văn bản: Sau khi đã có được văn bản tiền xử lý thì đề tài thực hiện quá trình tách các câu trong đoạn văn bản và tạo thành danh sách câu.
- Ghép từ có nghĩa: Khi đã có danh sách các câu đề tài tiến hành ghép các từ có nghĩa lại với nhau.
- Xây dựng đoạn tóm tắt: Sau khi đã hoàn thiện được các khâu chuẩn bị trước đó, đề tài thực hiện quá trình xây dựng lại đoạn tóm tắt dựa trên phương pháp tính điểm các câu, sau đó thực hiện trích xuất câu có điểm cao nhất để đưa ra kết quả tóm tắt.

# Chạy thử nghiệm:
- python main.py
