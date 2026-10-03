import os
import re

dir_path = r"d:\emad saadoon"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        encoding_used = 'utf-8'
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='utf-16') as f:
                content = f.read()
            encoding_used = 'utf-16'
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='windows-1256') as f:
                content = f.read()
            encoding_used = 'windows-1256'

    original_content = content

    # 1. Fix "منصة منصة"
    content = re.sub(r'منصة\s+منصة', 'منصة', content)
    
    # 2. Fix "التعليمية التعليمية"
    content = re.sub(r'التعليمية\s+التعليمية', 'التعليمية', content)
    
    # 3. Fix "أستاذ استاذ عماد سعدون" or similar in index.html
    # Look for "أستاذ <span ...>استاذ عماد سعدون</span>"
    content = re.sub(r'(أستاذ\s*<span[^>]*>)\s*استاذ', r'\1', content)
    
    # 4. Remove optional phone number sentence
    content = re.sub(r'أو رقم الهاتف \(اختياري للتسجيل\s*الجديد\)', '', content)
    content = content.replace('أدخل الكود أو رقم الهاتف أو اترك الحقل فارغاً', 'أدخل الكود أو اترك الحقل فارغاً')
    content = content.replace('كود الاشتراك أو رقم الهاتف', 'كود الاشتراك')

    if content != original_content:
        with open(filepath, 'w', encoding=encoding_used) as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html') or file.endswith('.js'):
            process_file(os.path.join(root, file))

print("Done fixing files.")
