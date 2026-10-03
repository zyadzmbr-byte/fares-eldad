import os

path = r'c:\webs\محمد رزق'
files = [f for f in os.listdir(path) if f.endswith('.html') or f.endswith('.js')]

for file in files:
    file_path = os.path.join(path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # Titles
    content = content.replace('منصة محمد حسني التعلمية', 'منصة التبيان التعليمية')
    content = content.replace('منصة محمد حسني', 'منصة التبيان التعليمية')
    content = content.replace('حصون', 'منصة التبيان التعليمية')
    
    # Subtitles
    content = content.replace('حاصل على لسانس اداب وتربية', 'ر') # Temp remove
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated {file}")
