# Pinecone CRUD 정리

Pinecone은 **임베딩 벡터를 저장하고, 질문과 의미가 비슷한 데이터를 검색하는 벡터 데이터베이스**이다.

쉽게 기억하면:

**문장 → 임베딩(숫자) → Pinecone 저장 → 질문 임베딩 → 비슷한 문서 검색**

---

## 0. Pinecone 연결

`.env`에 저장한 API Key를 불러와 Pinecone에 연결한다.

```python
import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index("quickstart-index")
```

> API Key는 코드에 직접 작성하지 않고 `.env`에 저장한다.

---

## 1. Create — 데이터 저장

Pinecone에서는 데이터를 저장할 때 `upsert()`를 사용한다.

```python
vectors = [
    {
        "id": "doc1",
        "values": embedding1,
        "metadata": {
            "text": "Pinecone은 벡터 데이터베이스입니다.",
            "category": "tech"
        }
    },
    {
        "id": "doc2",
        "values": embedding2,
        "metadata": {
            "text": "Pinecone은 임베딩 벡터를 저장하고 유사한 정보를 검색하는 서비스입니다.",
            "category": "tech"
        }
    }
]

index.upsert(
    vectors=vectors,
    namespace="example-namespace"
)
```

### 쉽게 기억

**Upsert = Update + Insert**

- 없는 ID → 새로 저장
- 같은 ID → 기존 데이터 덮어쓰기

---

## 2. Read — 데이터 검색

### 유사한 문서 검색 `query()`

질문도 임베딩 벡터로 만든 뒤 Pinecone에서 가장 비슷한 데이터를 찾는다.

```python
result = index.query(
    vector=question_vector,
    top_k=2,
    include_metadata=True,
    namespace="example-namespace"
)

for match in result.matches:
    print(match.id, match.score, match.metadata["text"])
```

예시 결과:

```text
doc2 → 0.6642
doc1 → 0.4800
```

점수가 높을수록 질문과 의미가 더 비슷하다.

### 특정 ID 조회 `fetch()`

```python
result = index.fetch(
    ids=["doc1", "doc2"],
    namespace="example-namespace"
)

print(result)
```

`query` = **비슷한 것 찾아줘**

`fetch` = **이 ID 가져와**

---

## 3. Update — 데이터 수정

특정 ID의 metadata 등을 수정할 수 있다.

```python
index.update(
    id="doc1",
    set_metadata={
        "text": "Pinecone은 클라우드 벡터 데이터베이스입니다.",
        "category": "tech"
    },
    namespace="example-namespace"
)
```

또는 같은 `id`로 다시 `upsert()`하면 기존 데이터를 덮어쓸 수 있다.

---

## 4. Delete — 데이터 삭제

### 특정 데이터 삭제

```python
index.delete(
    ids=["doc1"],
    namespace="example-namespace"
)
```

### Namespace 데이터 전체 삭제

```python
index.delete(
    delete_all=True,
    namespace="example-namespace"
)
```

---

# 핵심 암기

| CRUD | Pinecone | 의미 |
|---|---|---|
| Create | `upsert()` | 저장 |
| Read | `query()` / `fetch()` | 검색 / 조회 |
| Update | `update()` / `upsert()` | 수정 |
| Delete | `delete()` | 삭제 |

## RAG에서 제일 중요한 부분 ⭐

우리가 오늘 한 실습은:

**문서 → 임베딩 → Pinecone 저장 → 질문 임베딩 → `query()` → 관련 문서 검색**

이 중 `query()`로 관련 문서를 찾는 과정이  
**RAG의 Retrieval(검색)** 부분이다.

> 쉽게 기억: **Pinecone = AI가 답변하기 전에 참고자료를 찾아주는 벡터 창고**