# YCP 포트폴리오

전북대학교 IT지능정보공학과 YCP의 개인 소개 웹사이트입니다. [Hugo](https://gohugo.io/)와 [Hugo Coder](https://github.com/luizdepra/hugo-coder) 테마로 만들었고, GitHub Actions로 GitHub Pages에 자동 배포합니다.

- 공개 사이트: <https://parkyechan2979.github.io/portfolio/>
- 소개 페이지: <https://parkyechan2979.github.io/portfolio/about/>
- 활동 페이지: <https://parkyechan2979.github.io/portfolio/projects/>
- 배포 기록: <https://github.com/ParkYeChan2979/portfolio/actions>

## 폴더 구조와 수정할 파일

| 경로 | 역할 |
| --- | --- |
| `site/hugo.toml` | 사이트 설정: 제목, 작성자, 소개 문구(`info`), 메뉴, GitHub 링크, 아바타, 사용자 CSS/JS 지정 |
| `site/content/about.md` | 소개 페이지 (관심 분야, 학습 목표, 역량) |
| `site/content/projects.md` | 활동 페이지 (대표 활동의 기간·목적·역할·과정·산출물·배운 점) |
| `site/static/images/` | 아바타·파비콘 이미지 |
| `site/assets/css/custom.css` | 직접 추가한 스타일 (키보드 초점, 모바일 메뉴, 긴 텍스트·이미지 대응) |
| `site/assets/js/custom.js` | 직접 추가한 스크립트 (모바일 메뉴 Enter 키 조작) |
| `site/layouts/_partials/` | 테마 원본을 덮어쓰는 템플릿 (아바타 alt, 메뉴·다크 모드 버튼 접근성, 아이콘 참조) |
| `site/themes/template/` | Hugo Coder 테마 원본 (직접 수정하지 않음) |
| `site/pages.json` | 배포용 설정 (baseURL 등). 수업 제공 스크립트가 생성. 직접 수정하지 않음 |
| `.github/workflows/hugo-pages.yml` | GitHub Actions 배포 워크플로 (Hugo 버전 지정) |
| `.github/pages_build.py` | 워크플로가 실행하는 빌드 스크립트 (수업 제공 스크립트 사본) |
| 루트의 `layouts/`, `assets/`, `exampleSite/` 등 | 처음 받은 테마 ZIP 원본. 빌드에는 `site/` 폴더만 사용 |

## 필요한 도구와 버전

| 도구 | 버전 | 용도 |
| --- | --- | --- |
| Git | 2.x (작성 환경 2.56.0) | 저장소 clone, 커밋, push |
| Python | 3.9 이상 (작성 환경 3.13.5, Actions 3.12) | `.github/pages_build.py` 빌드 스크립트 실행 |
| Hugo **extended** | **0.167.0** | 사이트 빌드 (테마 SCSS 변환에 extended 판 필요) |

- 테마는 `site/themes/template/`에 포함되어 있습니다. 따라서 git submodule이나 npm 설치가 필요 없습니다.
- GitHub Actions는 위 버전의 Hugo를 워크플로(`.github/workflows/hugo-pages.yml`의 `HUGO_VERSION`)에서 자동으로 설치합니다.

### Hugo 설치 (로컬에서 확인할 때만 필요)

1. <https://github.com/gohugoio/hugo/releases/tag/v0.167.0>에서 운영체제에 맞는 **extended** 파일을 받습니다. Windows는 `hugo_extended_0.167.0_windows-amd64.zip`입니다.
2. 압축을 풀고 `hugo.exe`가 있는 폴더를 PATH에 추가합니다.
3. `hugo version`을 실행해 `v0.167.0 ... +extended`가 나오는지 확인합니다.

## 로컬에서 빌드·확인하는 방법

```bash
git clone https://github.com/ParkYeChan2979/portfolio.git
cd portfolio
```

**① 미리보기 서버** (수정하면서 바로 확인)

```bash
cd site
hugo server --config hugo.toml,pages.json --baseURL http://localhost:1313/portfolio/
```

브라우저에서 <http://localhost:1313/portfolio/>를 엽니다. 종료는 `Ctrl + C`입니다.

**② 배포와 같은 방식으로 빌드** (저장소 루트에서 실행)

```bash
python .github/pages_build.py --build
```

GitHub Actions와 같은 스크립트입니다. 결과는 `public/` 폴더에 생성되고, `public/index.html`이 홈 페이지입니다. `public/`은 `.gitignore`로 제외되어 커밋되지 않습니다.

## 내용 수정과 재배포 방법

1. 위 표의 파일을 수정합니다. 예: 소개 글은 `site/content/about.md`, 메뉴는 `site/hugo.toml`의 `[[languages.ko.menu.main]]`
2. (선택) 로컬 미리보기 서버로 결과를 확인합니다.
3. `main` 브랜치에 커밋하고 push합니다.
   ```bash
   git add site/content/about.md
   git commit -m "콘텐츠: 소개 페이지 학습 목표 수정"
   git push origin main
   ```
4. GitHub 저장소의 **Actions** 탭(<https://github.com/ParkYeChan2979/portfolio/actions>)에서 방금 push한 커밋의 **Deploy Hugo to GitHub Pages** 실행을 확인합니다. `build`와 `deploy` 작업이 모두 초록색 체크면 성공입니다(보통 1~2분).
5. 공개 사이트(<https://parkyechan2979.github.io/portfolio/>)를 새로고침해 변경 내용이 반영됐는지 확인합니다. 이전 화면이 보이면 `Ctrl + Shift + R`로 캐시 없이 새로고침합니다.

> GitHub 저장소 **Settings → Pages → Build and deployment → Source**는 **GitHub Actions**로 설정되어 있어야 합니다.

## 배포 결과 점검 방법

```bash
python tools/check_site.py
```

공개 사이트의 홈·소개·활동·404 페이지를 내려받아 다음을 자동으로 확인합니다. 문제가 없으면 `== PROBLEMS: 0`을 출력하고 종료 코드 0을 반환합니다.

- 링크, CSS, JS, 이미지의 응답 코드(200)
- `#앵커` 대상이 실제로 있는지
- `<html lang="ko">`, 제목 구조, 이미지 alt
- `localhost`, `file://`, `http://` 흔적이 남았는지

화면 폭(1440·768·390px), 키보드(Tab·Enter) 조작, 200% 확대는 크롬 개발자도구 기기 모드로 직접 확인합니다.

## 출처와 이용 조건

### 외부 자료

| 자료 | 사용 위치 | 원본 | 이용 조건 |
| --- | --- | --- | --- |
| Hugo Coder 테마 (Luiz F. A. de Prá) | `site/themes/template/`, 루트의 테마 원본 파일 | <https://github.com/luizdepra/hugo-coder> | MIT License: [`LICENSE.md`](LICENSE.md) 유지, 사이트 하단 "Powered by Hugo & Coder" 표기 유지 |
| Font Awesome Free 6 (Fonticons, Inc.) | 테마에 포함된 아이콘 글꼴 `site/themes/template/static/fonts/` | <https://fontawesome.com> | 아이콘 CC BY 4.0, 글꼴 SIL OFL 1.1: [`static/fonts/LICENSE.txt`](static/fonts/LICENSE.txt) 유지 |
| normalize.css 8.0.1 | 테마 `assets/scss/css/normalize.css` | <https://github.com/necolas/normalize.css> | MIT (파일 머리말에 고지 유지) |
| DOMPurify 2.4.1 | 테마 `assets/js/purify.min.js` | <https://github.com/cure53/DOMPurify> | Apache 2.0 / MPL 2.0 (파일 머리말에 고지 유지) |
| Hugo | 사이트 생성 도구 | <https://gohugo.io> | Apache 2.0 |
| 배포 준비 스크립트 `prepare_github_pages.py` 3.1 | 루트 `prepare_github_pages.py`, `.github/pages_build.py`, `.github/workflows/hugo-pages.yml`, `site/pages.json`, `.github-pages.json` | 초급프로젝트 수업 제공 | 수업 과제용 |
| 생활코딩 WEB 강의 예제 (egoing) | 활동 페이지에서 **링크로만** 소개 (코드는 이 저장소에 포함하지 않음) | <https://github.com/web-n/web2_javascript> | 원저작자 저장소 링크로 출처 표기 |

### 직접 제작과 AI 활용 구분

| 자료 | 구분 | 설명 |
| --- | --- | --- |
| `site/static/images/avatar.jpg` | 직접 촬영 + AI 도움 편집 | 본인이 촬영한 행사 사진입니다. 화이트보드의 타인 이메일 지우기, 정사각형 자르기, EXIF 제거는 AI(Claude)가 만든 Python(Pillow) 명령으로 처리했습니다. |
| `site/static/images/favicon.svg`, `favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png` | AI 도움 제작 | 테마 데모 로고 대신 쓰려고 'Y' 글자 아이콘을 AI(Claude)가 SVG와 Pillow 코드로 만들었습니다. 색상(#1565c0)은 사이트 링크 색과 맞췄습니다. |
| `site/static/images/projects/portfolio-home-1440.jpg` | 직접 제작 화면 캡처 | 이 사이트 홈 화면을 크롬 headless로 캡처한 이미지입니다. |
| `site/content/about.md`, `site/content/projects.md` | 직접 작성 + AI 문장 정리 | 내용(관심 분야, 목표, 활동 사실)은 본인이 제공했고, AI(Claude)가 문장을 정리했습니다. 본인이 사실 여부를 확인했습니다. |
| `site/hugo.toml` 수정 내용 | 직접 설정 + AI 도움 | 이름, 메뉴, 링크 등 값은 본인이 정했고, AI 도움으로 반영했습니다. |
| `site/assets/css/custom.css`, `site/assets/js/custom.js`, `site/layouts/_partials/**` | AI 도움 작성 + 본인 검증 | 접근성·반응형 문제를 점검해 AI(Claude)가 수정 코드를 제안했습니다. 본인이 배포 사이트에서 동작을 확인했습니다. |
| `README.md` | AI 도움 작성 + 본인 검토 | |

AI 도구: Anthropic Claude (Claude Code, 모델 Claude Opus 5.5), 사용일 2026-11-06. 상세 사용 기록은 과제 보고서에 정리했습니다.
