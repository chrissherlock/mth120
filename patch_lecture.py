#!/usr/bin/env python3
"""Usage: python3 patch_lecture.py week1-lecture3.html
Writes week1-lecture3.patched.html with the telescope widget swapped in.
Keep telescoping-sum-widget.html in the same folder as this script."""
import sys, os, re
src = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
w = open(os.path.join(here, 'telescoping-sum-widget.html'), encoding='utf-8').read()
css = w.split('/* ===== Widget styles (scoped under .ct) ===== */')[1].split('</style>')[0]
html = w[w.index('<div class="ct" id="ct">'):w.rindex('</script>') + len('</script>')]

page = open(src, encoding='utf-8').read()

start = page.find('<!-- VISUAL CANCELLATION DIAGRAM -->')
end = page.find('2. Computing Famous Sums with Telescoping Magic')
if start < 0 or end < 0:
    sys.exit('Could not find the old diagram block - is this the Lecture 3 file?')
end = page.rfind('<h3', start, end)          # start of the next section heading
if page.count('ct-row') or 'class="ct"' in page:
    sys.exit('Widget already present - nothing changed.')

block = ('<!-- INTERACTIVE: COLLAPSING POCKET TELESCOPE -->\n'
         '            <div style="margin: 1.75rem 0;">\n' + html + '\n            </div>\n\n            ')
page = page[:start] + block + page[end:]

i = page.rfind('</style>')
page = page[:i] + '\n        /* ===== Telescope widget ===== */' + css + '    ' + page[i:]

out = re.sub(r'\.html$', '', src) + '.patched.html'
open(out, 'w', encoding='utf-8').write(page)
print('Wrote', out)
