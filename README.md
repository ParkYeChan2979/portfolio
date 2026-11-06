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
