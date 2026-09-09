### 코드 흐름

1. `item_id`를 입력받는다.
2. `item_id`가 `items_db`에 존재하는지 확인한다.
3. 없으면 `HTTPException`으로 404 오류를 반환한다.
4. 있으면 `items_db.pop(item_id)`로 데이터를 삭제한다.
5. 삭제된 데이터를 응답으로 반환한다.

### pop()

`items_db.pop(item_id)`

- 해당 `item_id`의 데이터를 가져온다.
- 가져오면서 동시에 `items_db`에서 삭제한다.

### Swagger 실습

1. POST로 `블루베리` 생성
2. 생성된 `item_id = 4` 확인
3. DELETE `/items/{item_id}` 실행
4. `item_id`에 `4` 입력
5. Execute
6. 응답 코드 `200` 확인
7. `"삭제 완료"`와 삭제된 블루베리 데이터 확인
8. GET `/items/`를 다시 실행해서 블루베리가 사라졌는지 확인

## CRUD 정리

- GET → 조회
- POST → 생성
- PUT → 수정
- DELETE → 삭제

## CRUD는 왜 필요한가?

CRUD는 데이터를 다루는 가장 기본적인 4가지 기능이다.

- **Create (POST)** → 데이터 생성
- **Read (GET)** → 데이터 조회
- **Update (PUT)** → 데이터 수정
- **Delete (DELETE)** → 데이터 삭제

### 왜 필요한가?

대부분의 서비스는 데이터를 **만들고, 조회하고, 수정하고, 삭제하는 과정**으로 이루어져 있기 때문이다.

예: 쇼핑몰 상품 관리

- POST → 새로운 상품 등록
- GET → 상품 목록 조회
- PUT → 상품 가격 수정
- DELETE → 상품 삭제

### 어디에 쓰이나?

- 회원 관리
- 게시판
- 쇼핑몰
- 일정 관리
- DB 데이터 관리
- API 서버
- AI Agent의 외부 서비스 연동

### AI Agent에서는?

Agent가 사용자의 요청에 따라 실제 데이터를 처리할 때 CRUD API를 사용할 수 있다.

예:

`"내 일정 보여줘"` → GET  
`"내일 회의 추가해줘"` → POST  
`"회의 시간을 3시로 바꿔줘"` → PUT  
`"회의 취소해줘"` → DELETE  

**CRUD = 데이터를 생성·조회·수정·삭제하는 서비스의 기본 구조**