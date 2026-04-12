import glob
import re

html_files = glob.glob('*.html')

block_immobilie = """<li class="sidebar-item">
                    <a href="immobilie.html" class="{cls}"
                        style="display: flex; align-items: center; gap: 0.5rem; justify-content: flex-start;">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon-blue"
                            style="width: 1.25rem; height: 1.25rem;" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                            <polyline points="9 22 9 12 15 12 15 22" />
                        </svg>
                        Immobilie
                    </a>
                </li>"""

block_kapitalanlageimmobilie = """<li class="sidebar-item">
                    <a href="kapitalanlageimmobilie.html" class="{cls}"
                        style="display: flex; align-items: center; gap: 0.5rem; justify-content: flex-start;">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon-blue"
                            style="width: 1.25rem; height: 1.25rem;" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                            <polyline points="9 22 9 12 15 12 15 22" />
                        </svg>
                        Kapitalanlageimmobilie
                    </a>
                </li>"""

# We'll construct a regex to match both li blocks.
# The matching regex should cover from the first <li class="sidebar-item"> that contains "Immobilie" 
# to the end of the second list item containing "Kapitalanlageimmobilie".
regex = re.compile(
    r'<li class="sidebar-item">\s*<a href="[^"]*?" class="sidebar-link(?: active)?"[^>]*>.*?Immobilie\s*</a>\s*</li>\s*<li class="sidebar-item">\s*<a href="[^"]*?" class="sidebar-link(?: active)?"[^>]*>.*?Kapitalanlageimmobilie\s*</a>\s*</li>',
    re.DOTALL
)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    cls_immo = "sidebar-link active" if filepath == "immobilie.html" else "sidebar-link"
    cls_kap = "sidebar-link active" if filepath == "kapitalanlageimmobilie.html" else "sidebar-link"
    
    replacement = block_immobilie.format(cls=cls_immo) + "\n                " + block_kapitalanlageimmobilie.format(cls=cls_kap)
    
    # Check if we find the match
    new_content = regex.sub(replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No match/changes in {filepath}")
