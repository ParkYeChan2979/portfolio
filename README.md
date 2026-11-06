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
