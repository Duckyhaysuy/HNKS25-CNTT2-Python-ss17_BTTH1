
raw_logs = []
processed_logs = []

def clean_raw_logs(raw_text):
    table = str.maketrans("", "", "!@#$")
    clean_text = raw_text.translate(table)
    log_list = clean_text.split(";")
    return [log.strip() for log in log_list if log.strip() != ""]

def load_logs():
    global raw_logs
    print("\n--- NẠP DỮ LIỆU LOG ---")
    input_logs = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
    raw_logs = clean_raw_logs(input_logs)
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

def filter_danger_logs():
    global processed_logs
    print("\n--- LỌC CẢNH BÁO ---")

    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    processed_logs = [log for log in raw_logs if "error" in log.lower() or "critical" in log.lower()]

    if len(processed_logs) == 0:
        print("Không tìm thấy cảnh báo nguy hiểm.")
        return

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

    for log in processed_logs:
        print("-", log)

def mask_ip(ip):
    parts = ip.split(".")

    if len(parts) == 4:
        parts[2] = "*"
        parts[3] = "*"

    return ".".join(parts)

def encrypt_ip_logs():
    print("\n--- MÃ HÓA IP ---")

    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    if len(processed_logs) == 0:
        print("Chưa có log nguy hiểm để mã hóa.")
        return

    safe_logs = []

    for log in processed_logs:
        words = log.split()
        new_words = []

        for word in words:
            if "." in word:
                new_words.append(mask_ip(word))
            else:
                new_words.append(word)

        safe_logs.append(" ".join(new_words))

    print("Báo cáo log an toàn:")

    for i in range(len(safe_logs)):
        print(f"{i+1}. {safe_logs[i]}")

def display_menu():
    print("\n============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao")
    print("3. Mã hóa địa chỉ IP")
    print("4. Đóng hệ thống")
    print("=================================================")

while True:
    display_menu()
    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        load_logs()

    elif choice == "2":
        filter_danger_logs()

    elif choice == "3":
        encrypt_ip_logs()

    elif choice == "4":
        print("Đã đóng hệ thống phân tích log.")
        break

    else:
        print("Lựa chọn không hợp lệ!")

