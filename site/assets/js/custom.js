// 모바일 메뉴 체크박스: 기본 키(Space) 외에 Enter로도 메뉴를 열고 닫을 수 있게 함
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('menu-toggle');
  if (!toggle) return;
  toggle.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      toggle.click();
    }
  });
});
