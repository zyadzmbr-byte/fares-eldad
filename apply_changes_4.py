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

    # 1. Platform Name Replacement
    content = re.sub(r'(منصة )?التبيان( التعليمية)?', 'منصة فارس الضاد التعليمية', content)
    # Just in case "فارس الضاد التعليمية التعليمية" was created
    content = content.replace("منصة فارس الضاد التعليمية التعليمية", "منصة فارس الضاد التعليمية")
    content = content.replace("منصة منصة", "منصة")

    # 2. Teacher Name Replacement
    content = re.sub(r'(أستاذ |أ\.\s*|د\.\s*|دكتورة |دكتور |استاذ )?محمد رزق', 'استاذ عماد سعدون', content)
    
    # 3. Images Replacement
    content = content.replace("img_hero_man.jpg", "hero.5.jpg")
    content = content.replace("img_logo.jpg", "logo.5.jpg")

    # 4. WhatsApp Number
    content = content.replace("201111382747", "201098858663")
    content = content.replace("01111382747", "01098858663")

    # 5. Cloudinary Upload Preset
    content = content.replace("'yxii0trt'", "'fares eddad'")
    content = content.replace('"yxii0trt"', '"fares eddad"')

    # 6. Firebase Config
    if 'const firebaseConfig' in content and 'apiKey:' in content:
        new_config = """const firebaseConfig = {
  apiKey: "AIzaSyBRys4lNgZ64RoJBlC9NW-scfO2m-59bcY",
  authDomain: "fares-eldad.firebaseapp.com",
  projectId: "fares-eldad",
  storageBucket: "fares-eldad.firebasestorage.app",
  messagingSenderId: "576584552167",
  appId: "1:576584552167:web:961e3a8d388b3ca38b9c42"
};"""
        content = re.sub(r'const\s+firebaseConfig\s*=\s*\{[^}]+\};', new_config, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding=encoding_used) as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html') or file.endswith('.js'):
            process_file(os.path.join(root, file))

print("Done processing files.")
