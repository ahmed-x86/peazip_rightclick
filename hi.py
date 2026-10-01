import subprocess
import os

def get_modified_files():
    # نستخدم --porcelain لأنها تعطي مسارات الملفات بشكل نظيف جداً
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    files = []
    
    for line in result.stdout.splitlines():
        if line.strip():
            # تجاهل أول 3 حروف (والتي تمثل حالة الملف مثل M أو ??) وخذ المسار
            file_path = line[3:]
            files.append(file_path)
            
    return files

def main():
    files = get_modified_files()
    
    if not files:
        print("لا توجد ملفات معدلة أو جديدة لعمل Commit لها.")
        return

    print(f"تم العثور على {len(files)} ملفات. جاري الحلب... 🚀")

    for file in files:
        # استخراج اسم الملف فقط ليكون عنوان الـ commit شكله نظيف
        file_name = os.path.basename(file)
        commit_message = f"Update {file_name}"
        
        print(f"-> Committing: {file_name}")
        
        # 1. Git Add
        subprocess.run(['git', 'add', file])
        
        # 2. Git Commit
        subprocess.run(['git', 'commit', '-m', commit_message], stdout=subprocess.DEVNULL)

    # 3. Git Push (مرة واحدة في النهاية)
    print("\nجاري رفع كل الـ Commits مرة واحدة (git push)...")
    subprocess.run(['git', 'push'])
    
    print("\n✅ تمت العملية بنجاح! تم تفخيخ عداد الـ Commits.")

if __name__ == '__main__':
    main()