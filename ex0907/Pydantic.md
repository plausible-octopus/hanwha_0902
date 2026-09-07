### 2. 실전: 기본값, Optional, 중첩 모델

Field()
| None
기본값
Nested Model
복잡한 JSON 데이터 검증


age: int = Field(ge=0, le=150)
age >= 0, age <= 150


### 3. API 요청 → 검증 → 데이터 변환

Pydantic의 역할은 비즈니스 로직에 들어가기 전에 데이터가 올바른지 검사하는 것

**model_dump()는 Python dict로 변환** 하고,
**model_dump_json()은 JSON 문자열로 변환**


|단계 | 배운 것 | 핵심
|---|---|---|
|1 | BaseModel | 타입 검증
|2 | Field, Nested Model | 복잡한 데이터 검증
|3 | API 데이터 모델링 | 실무에서 검증 + 변환