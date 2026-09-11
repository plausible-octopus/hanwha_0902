import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model="gpt-5.6-luna",
        input="연결 테스트입니다. OK라고만 답해줘."
    )

    print("✅ OpenAI API 연결 성공")
    print(response.output_text)

except Exception as e:
    print("❌ 연결 실패")
    print(e)