<h1 align= "center">원티드 프리온보딩 프론트엔드 코스 선발과제</h1>

구현방법,이유 어려웠던점,해결방법

:black_small_square: Toggle
:black_small_square: Modal
:black_small_square: Tab
:black_small_square: Tag
:black_small_square: AutoComplete
:black_small_square: ClicktoText
### :white_check_mark: Toggle
~~~
on,off 를 state로 관리 (true,false)
state 값에 따라 추가로 class를 부여, 다른 css적용
on 일 때 css : background-color,토글의 동그라미 부분의 margin-left를 변경,transition을 통해 애니메이션 효과 적용

동그라미 부분을 수평으로 이동시키는 방법에 대해 고민하다
영역의 크기를 계산하여 좌우 반전된 배치를 갖는 margin값과 transition을 통해 해결

~~~





### :white_check_mark: Modal


### :white_check_mark: Tab


### :white_check_mark: AutoComplete
~~~

최근 검색목록을 배열로 만들어 state로 관리
최근 검색목록을 <option>요소로 담는  <datalist>를 <input>과 연결

Enter키가 눌리면 사용자의 입력을 최근검색어 state에 추가


<option>요소를 미리 담아둔 <datalist>에  


~~~
### :white_check_mark: ClicktoText
~~~
이름과 나이를 state로 관리하는 Controlled Component 
1.<input/>에서 onBlur 이벤트 발생 시  handleBlur 함수 실행 
2.<input/>의 id와 일치하는 state를 업데이트 

<input/>에서 포커싱이 벗어날 때 state가 업데이트 되는것을 파악,  
React 공식문서를 통해 onBlur 이벤트를 새롭게 알게되어 적용

~~~

### :computer: demo
~~~
1. npm install
2. npm start
~~~

### :house: URL
https://hustlekang-pre-onboarding-course.netlify.app/


