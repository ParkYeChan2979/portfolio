"""공개 사이트 자동 점검 스크립트 (Python 3.9+, 표준 라이브러리만 사용)

확인 항목: 페이지·링크·CSS/JS/이미지 응답 코드, 앵커 대상 존재, html lang,
제목(h1~h6) 구조, 이미지 alt, localhost·file·http 흔적, 빈 링크(# 등).

사용법:  python tools/check_site.py [사이트 주소]
기본 주소: https://parkyechan2979.github.io/portfolio/
"""
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

BASE = (sys.argv[1] if len(sys.argv) > 1 else 'https://parkyechan2979.github.io/portfolio/').rstrip('/') + '/'
PAGES = ['', 'about/', 'projects/', '404.html']
UA = {'User-Agent': 'site-check/1.0'}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.assets, self.imgs, self.heads, self.lang, self.ids = [], [], [], [], None, set()
        self._h = None

    def handle_starttag(self, tag, a):
        a = dict(a)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'a':
            self.links.append((a.get('href'), a.get('aria-label')))
        if tag in ('link',) and a.get('href') and a.get('rel') in ('stylesheet', 'icon', 'apple-touch-icon', 'mask-icon', 'manifest'):
            self.assets.append(a['href'])
        if tag == 'script' and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'img':
            self.imgs.append((a.get('src'), a.get('alt')))
            self.assets.append(a.get('src'))
        if re.fullmatch(r'h[1-6]', tag):
            self.heads.append(tag)


def status(url):
    try:
        req = urllib.request.Request(url, headers=UA, method='GET')
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return str(e), b''


problems = []
checked = {}
for page in PAGES:
    url = BASE + page
    code, body = status(url)
    html = body.decode('utf-8', 'replace')
    p = P()
    p.feed(html)
    print(f'\n== {url} -> {code}')
    print('  lang =', p.lang, '| headings =', ' '.join(p.heads), '| h1 count =', p.heads.count('h1'))
    for bad in ('localhost', '127.0.0.1', 'file://', 'C:\\', 'C:/', 'http://'):
        for m in re.finditer(re.escape(bad), html):
            ctx = html[max(0, m.start() - 60):m.end() + 60].replace('\n', ' ')
            if bad == 'http://' and ('www.w3.org' in ctx):
                continue
            problems.append(f'{url}: "{bad}" found: ...{ctx}...')
    for src, alt in p.imgs:
        print('  img', src, 'alt=', repr(alt))
        if alt is None:
            problems.append(f'{url}: img without alt {src}')
    for href, label in p.links:
        if href is None or href.strip() in ('', '#'):
            problems.append(f'{url}: empty link href={href!r} label={label!r}')
            continue
        if href.startswith(('mailto:', 'tel:')):
            continue
        full = urllib.parse.urljoin(url, href)
        frag = urllib.parse.urlparse(full).fragment
        target = full.split('#')[0]
        if target not in checked:
            checked[target] = status(target)
        c, b = checked[target]
        note = ''
        if frag:
            tp = P()
            tp.feed(b.decode('utf-8', 'replace'))
            if urllib.parse.unquote(frag) not in tp.ids:
                note = '  <-- ANCHOR MISSING'
                problems.append(f'{url}: anchor #{frag} missing in {target}')
        print(f'  link {c} {href}{note}')
        if c != 200:
            problems.append(f'{url}: link {href} -> {c}')
    for a in p.assets:
        full = urllib.parse.urljoin(url, a)
        if full not in checked:
            checked[full] = status(full)
        c = checked[full][0]
        print(f'  asset {c} {a}')
        if c != 200:
            problems.append(f'{url}: asset {a} -> {c}')

print('\n== PROBLEMS:', len(problems))
for x in problems:
    print(' -', x)
sys.exit(1 if problems else 0)
