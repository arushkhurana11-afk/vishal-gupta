import os
import glob

# Update HTML files
html_files = glob.glob(r'C:\Users\vishal gupta\Downloads\Animated Portfolio\*.html')
for filepath in html_files:
    if 'projects.html' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('<a href=\"#\" class=\"nav-item\">My Work</a>', '<a href=\"projects.html\" class=\"nav-item\">My Work</a>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Updated nav items in html files.')

# Create projects.html
projects_html = '''<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Projects - Vishal Gupta</title>
    <!-- Fonts -->
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
    <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&family=Great+Vibes&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"style.css\">
    <style>
        .projects-container {
            padding: 40px;
            display: flex;
            flex-direction: column;
            gap: 30px;
            width: 100%;
        }
        .project-card {
            background: var(--card-bg);
            border-radius: 30px;
            padding: 40px;
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.1);
            text-decoration: none;
            color: var(--text-main);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            border: 1px solid var(--accent);
        }
        .project-title {
            font-family: var(--font-display);
            font-size: 2.5rem;
            margin: 0;
            color: var(--text-main);
        }
        .project-card:hover .project-title {
            color: var(--accent);
        }
        .project-desc {
            font-size: 1.2rem;
            color: var(--text-muted);
            margin: 0;
        }
    </style>
</head>
<body>

    <div class=\"scroll-container\">
        <div class=\"page-content\">
            <nav class=\"pill-nav\">
                <a href=\"index.html\" class=\"nav-item\">Home</a>
                <a href=\"about.html\" class=\"nav-item\">About</a>
                <a href=\"projects.html\" class=\"nav-item active\">My Work</a>
                <a href=\"contact.html\" class=\"nav-item\">Contact</a>
            </nav>

            <main class=\"hero-card\" style=\"align-items: flex-start; justify-content: flex-start;\">
                <div class=\"projects-container\">
                    <h1 style=\"font-family: var(--font-display); font-size: 3rem; margin: 0 0 20px 0; color: #FFFFFF;\">My Work</h1>
                    <a href=\"https://mouse-tracker-zeta.vercel.app\" target=\"_blank\" class=\"project-card\">
                        <h2 class=\"project-title\">Character following your mouse pointer</h2>
                        <p class=\"project-desc\">Interactive cursor tracking animation</p>
                    </a>
                </div>
            </main>

            <a href=\"#\" class=\"return-to-top\">Return to Top &uarr;</a>
        </div>
    </div>

</body>
</html>
'''

filepath = r'C:\Users\vishal gupta\Downloads\Animated Portfolio\projects.html'
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(projects_html)
print('Created projects.html')
