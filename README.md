## 1.개발환경
<hr>
<br>
- 언어 python(3.8.2), html5, django-html, css3, 8.0.30 for macos12.4 on x86_64 (Homebrew)<br>
- 서버 (배포이전)<br>
- FRAMEWORK - django(4.1.3)<br>
- DB pymysql(1.0.2)<br>

## 2.이 레파지토리의 목적
<hr>
<br>
django를 좀 더 심화로 활용하며, 데이터를 관리자모드로 잘 관리 할 수 있는가? 확인을 목적으로 합니다.


## 3.포트폴리오 설명
<hr>
<br>
db에 등록되어있는 정보가 3개에 한해서 메인 페이지에 노출이 되는 구조입니다.<br><br>
sub_page - posts에는 db에 등록되어있는 모든 post에 대해서 노출이 되는 영역 입니다.<br>
해당 post로 들어가게 되면 db에 등록할 당시에 언제 만들어진 것이며, 누가 만든 것이며, 제목, 내용 및 태그가 확인 가능합니다.<br>
누적 코멘트를 확인할 수 있으며 코멘트 작성이 가능합니다.<br>
Read Later를 클릭하게 되면 "Stored Posts"에 해당 post가 임시로 누적이 됩니다.<br><br>
Posts에서 Read Later를 눌렀던 post를 Stored Posts에서 확인이 가능하며, 내용을 확인 후 "Remove from ~~~" 버튼을 누르면 임시로 저장되었던 내용이 삭제되게 됩니다.
물론 posts의 원본 데이터에는 영향이 없습니다.



writted in 6/Dec/2022