# 검증 캡처 목록

- 대상: 공개 사이트 <https://parkyechan2979.github.io/portfolio/>, 검증 대상 커밋 `eb233a88d4ab862b731f0c684c4e57fc9de7a7f2`
- 브라우저: Google Chrome 156.0.8078.80 (Windows 11 Home 25H2)
- 방법
  - **자동:** Playwright가 설치된 Chrome을 새 프로필(캐시 없음, 로그인 없음)로 조작해 캡처했습니다.
  - **직접:** 본인이 시크릿 창과 개발자도구에서 캡처했습니다.
- 시각: 2026-11-06 KST

| 그림 | 파일 | 내용 | URL | 폭 | 시각 | 방법 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `fig01_home_1440.png` | 홈 화면(데스크톱) | https://parkyechan2979.github.io/portfolio/ | 1440px | 20:19 | 자동 |
| 2 | `fig02_home_390.png` | 홈 화면(모바일) | https://parkyechan2979.github.io/portfolio/ | 390px | 20:18 | 자동 |
| 3 | `fig03_about_1440.png` | 소개 페이지 전체(P71~P73) | https://parkyechan2979.github.io/portfolio/about/ | 1440px | 20:19 | 자동 |
| 4 | `fig04_projects_1440.png` | 활동 페이지 전체(P74~P79) | https://parkyechan2979.github.io/portfolio/projects/ | 1440px | 20:19 | 자동 |
| 5 | `fig05_projects_390.png` | 활동 페이지 모바일, 긴 URL 줄바꿈 | https://parkyechan2979.github.io/portfolio/projects/ | 390px | 20:18 | 자동 |
| 6 | `fig06_menu_open_390.png` | 모바일 메뉴(☰) 펼침 | https://parkyechan2979.github.io/portfolio/ | 390px | 20:18 | 자동 |
| 7 | `fig07_focus_menu_1440.png` | Tab 초점이 "소개" 메뉴에 있는 상태 | https://parkyechan2979.github.io/portfolio/ | 1440px | 20:18 | 자동 |
| 8 | `fig08_focus_menubtn_390.png` | Tab 초점이 ☰ 메뉴 버튼에 있는 상태 | https://parkyechan2979.github.io/portfolio/ | 390px | 20:18 | 자동 |
| 9 | `fig09_focus_darkmode_1440.png` | Tab 초점이 다크 모드 버튼에 있는 상태 | https://parkyechan2979.github.io/portfolio/ | 1440px | 20:18 | 자동 |
| 10 | `fig10_network_1440.png` | Network 탭(Disable cache): 모든 요청 200 | https://parkyechan2979.github.io/portfolio/ | 1440px | 20:58 | 직접 |
| 11 | `fig11_console_1440.png` | Console 탭: 오류 0건 | https://parkyechan2979.github.io/portfolio/ | 1440px | 21:00 | 직접 |
| 14 | `fig14_zoom200_1440.png` | 브라우저 200% 확대 (1440px 창 = CSS 720px, 배율 2) | https://parkyechan2979.github.io/portfolio/ | 1440px | 20:18 | 자동 |

## 로그

- `auto_verify_log.txt`: Chrome·Edge 자동 검증 131개 항목 결과(배포, 경로·자산, 메뉴·링크, 반응형, 키보드)
- `check_site_log.txt`: `tools/check_site.py` 링크·자산 점검 결과(== PROBLEMS: 0)

> 그림 12(Actions 실행 목록)와 그림 13(최종 실행 상세)은 보고서에만 실었습니다. 저장소에 올리면 그 커밋으로 새 실행이 생겨 화면이 최신 상태와 달라지기 때문입니다. 최신 실행은 <https://github.com/ParkYeChan2979/portfolio/actions>에서 확인할 수 있습니다.
