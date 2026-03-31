import os
import shutil
from datetime import datetime

def run_cleanup():
    base_path = os.getcwd()
    log_folder = os.path.join(base_path, "Logs")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M')
    log_file = os.path.join(log_folder, f"temizlik_{timestamp}.txt")
    
    with open(log_file, "w", encoding="utf-8") as report:
        report.write(f"SISTEM HESABATI | {timestamp}\n" + "="*30 + "\n")
        folders = [os.environ.get('TEMP'), "C:\\Windows\\Temp"]
        total_deleted = 0
        for folder in folders:
            if folder and os.path.exists(folder):
                for item in os.listdir(folder):
                    try:
                        item_path = os.path.join(folder, item)
                        if os.path.isfile(item_path):
                            os.unlink(item_path)
                            total_deleted += 1
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                            total_deleted += 1
                    except:
                        continue
        report.write(f"\nNetice: {total_deleted} fayl silindi.")
    print(f"Temizlik bitdi. Log: Logs/temizlik_{timestamp}.txt")

if __name__ == "__main__":
    run_cleanup()