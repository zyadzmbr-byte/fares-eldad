import os
import re
import shutil

src_dir = r"c:\webs\محمد رزق"
dst_dir = os.path.join(src_dir, "ا", "محمد رزق")

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

def remove_ai_words(text):
    words = [r"AI\b", r"ChatGPT\b", r"الذكاء\s*الاصطناعي", r"bot\b", r"OpenAI\b", r"Claude\b", r"Gemini\b", r"AI-generated\b", r"الذكاء\b"]
    for w in words:
        text = re.sub(w, "", text, flags=re.IGNORECASE)
    return text

def remove_html_comments(text):
    return re.sub(r'<!--[\s\S]*?-->', '', text)

def remove_js_css_comments(text):
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    text = re.sub(r'//.*', '', text)
    return text

def remove_python_comments(text):
    text = re.sub(r'#.*', '', text)
    text = re.sub(r'\"\"\"[\s\S]*?\"\"\"', '', text)
    text = re.sub(r"\'\'\'[\s\S]*?\'\'\'", '', text)
    return text

def read_file_content(filepath):
    encodings = ['utf-8', 'utf-16', 'windows-1256', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            pass
    return ""

html_files = []
js_files = []
css_files = []
py_files = []
other_important_files = []

for f in os.listdir(src_dir):
    path = os.path.join(src_dir, f)
    if not os.path.isfile(path) or f == 'processor.py':
        continue
    if f.endswith('.html'):
        html_files.append(f)
    elif f.endswith('.js'):
        js_files.append(f)
    elif f.endswith('.css'):
        css_files.append(f)
    elif f.endswith('.py'):
        py_files.append(f)
    elif f.endswith(('.jpg', '.jpeg', '.png', '.svg', '.gif')):
        other_important_files.append(f)

# HTML
combined_html = ""
for f in html_files:
    content = read_file_content(os.path.join(src_dir, f))
    content = remove_html_comments(content)
    content = remove_ai_words(content)
    combined_html += content + "\n\n"
if combined_html:
    with open(os.path.join(dst_dir, "index.html"), 'w', encoding='utf-8') as f:
        f.write(combined_html)

# JS
combined_js = ""
for f in js_files:
    content = read_file_content(os.path.join(src_dir, f))
    content = remove_js_css_comments(content)
    content = remove_ai_words(content)
    combined_js += content + "\n\n"
if combined_js:
    with open(os.path.join(dst_dir, "script.js"), 'w', encoding='utf-8') as f:
        f.write(combined_js)

# CSS
combined_css = ""
for f in css_files:
    content = read_file_content(os.path.join(src_dir, f))
    content = remove_js_css_comments(content)
    content = remove_ai_words(content)
    combined_css += content + "\n\n"
if combined_css:
    with open(os.path.join(dst_dir, "style.css"), 'w', encoding='utf-8') as f:
        f.write(combined_css)

# Python
combined_py = ""
for f in py_files:
    content = read_file_content(os.path.join(src_dir, f))
    content = remove_python_comments(content)
    content = remove_ai_words(content)
    combined_py += content + "\n\n"
if combined_py:
    with open(os.path.join(dst_dir, "main.py"), 'w', encoding='utf-8') as f:
        f.write(combined_py)

# Other files
for f in other_important_files:
    shutil.copy2(os.path.join(src_dir, f), os.path.join(dst_dir, f))
