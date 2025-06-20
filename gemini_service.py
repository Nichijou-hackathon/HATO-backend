from google import genai
import pydantic

class mood(pydantic.BaseModel):
    emotion: str
    color: str

import os
from dotenv import load_dotenv
def gemini_prompt(s: str):
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=key)
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{s} に当てはまる感情を [Joy , Sadness , Anger , Surprise , Fear , Anticipation , Relief , Desapair , Curiousity , Achievement , Confusion , Excitement] のリストの中から1つだけ選択してください. また{s} に当てはまる色をカラーコードで選択してください. 出力はjson形式でお願いします.",
        config={
            "response_mime_type": "application/json",
            "response_schema": mood,
        },
    )
    
    print(r := response.text)
    return r

# test
# gemini_prompt("米津玄師/Lemon")
