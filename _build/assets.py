# Renders favicon PNGs and the Open Graph image (static/og-image.png) with Playwright.
# The OG image reuses the header banner (layouts/partials/banner.html) with the red to purple gradient.
# Run with /workspace/.venv/bin/python after _build/banner.py.
import pathlib, re
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parent.parent
svg=(root/'static/favicon.svg').read_text()
fira=(root/'themes/terminal/static/fonts/FiraCode-Latin.woff2').as_uri()
bfont=(root/'static/fonts/banner-dejavu-mono.woff2').as_uri()
banner=re.search(r'<pre class="banner"[^>]*>(.*?)</pre>',(root/'layouts/partials/banner.html').read_text(),re.S).group(1)
og=f'''<html><head><style>@font-face{{font-family:Fira;src:url({fira})}}@font-face{{font-family:B;src:url({bfont})}}
body{{margin:0;width:1200px;height:630px;background:#0b0a10;font-family:Fira,monospace;color:#d6d6de;display:flex;align-items:center;justify-content:center}}
.t{{width:1080px;border:2px solid #ff3346;background:#07070b;box-shadow:0 0 60px rgba(179,102,255,.22),0 0 30px rgba(255,51,70,.2)}}
.b{{display:flex;gap:12px;padding:14px 22px;border-bottom:1px solid rgba(255,51,70,.45);background:#131119;align-items:center}}
.d{{width:16px;height:16px;border-radius:50%}}.b span{{margin-left:14px;opacity:.6;font-size:20px}}
.c{{padding:34px 46px 38px}}
.bn{{margin:0 0 22px;font-family:B,monospace;font-size:20.5px;line-height:1;white-space:pre;background:linear-gradient(90deg,#ff3346,#b366ff);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 10px rgba(255,51,70,.35))}}
.i{{font-size:24px;line-height:1.5;white-space:pre}}.ip{{color:#ff3346;font-weight:bold}}.it{{color:#22d3ee}}
.w{{margin-top:22px;font-size:27px;line-height:1.4}}.s{{opacity:.9}}.w b{{color:#fff}}.u{{margin-top:12px;font-size:24px;color:#22d3ee}}.cur{{color:#ff3346}}
</style></head><body><div class="t"><div class="b"><i class="d" style="background:#ff5f56"></i><i class="d" style="background:#ffbd2e"></i><i class="d" style="background:#27c93f"></i><span>georgesec console</span></div>
<div class="c"><pre class="bn">{banner}</pre>
<div class="i"><span class="ip">       =[ </span><span class="it">georgesec v2026</span>
<span class="ip">+ -- --=[ </span><span class="it">detection engineering | penetration testing</span></div>
<div class="w"><span class="ip">georgesec &gt;</span> whoami<br><b>George Voutouris</b><br><span class="s">Detection Engineer &amp; Penetration Tester</span></div>
<div class="u">georgesec.com <span class="cur">&#9608;</span></div></div></div></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch()
    for size,name in [(32,'favicon-32.png'),(180,'apple-touch-icon.png'),(192,'favicon.png')]:
        pg=b.new_page(viewport={'width':size,'height':size})
        pg.set_content(f'<html><body style="margin:0;background:transparent">{svg.replace("<svg ",f"<svg width={size} height={size} ")}</body></html>')
        pg.screenshot(path=str(root/'static'/name),omit_background=True); pg.close()
    pg=b.new_page(viewport={'width':1200,'height':630})
    pg.set_content(og); pg.wait_for_timeout(400)
    print('og content', pg.evaluate('()=>{const t=document.querySelector(".t").getBoundingClientRect();const n=document.querySelector(".bn");return {top:t.top,bottom:t.bottom,bnW:n.scrollWidth,cW:n.clientWidth}}'))
    pg.screenshot(path=str(root/'static/og-image.png')); b.close()
print('ok')
