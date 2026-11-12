from openai import OpenAI
from config import OPENAI_API_KEY


def create_travel_plan(region, style, days, places):
    """
    OpenAI API를 사용해 여행 일정을 생성하는 함수
    """

    if not places:
        return "추천할 장소가 없습니다."

    if not OPENAI_API_KEY:
        return create_simple_plan(region, style, days, places)

    client = OpenAI(api_key=OPENAI_API_KEY)

    place_text = ""

    for idx, place in enumerate(places, start=1):
        place_text += f"{idx}. {place['name']} - {place['address']} - {place['category']}\n"

    prompt = f"""
너는 국내 여행 일정을 추천하는 여행 플래너야.

사용자 조건:
- 지역: {region}
- 여행 스타일: {style}
- 여행 기간: {days}일

아래 장소 후보만 사용해서 여행 코스를 추천해줘.

장소 후보:
{place_text}

출력 형식:
1. 추천 여행 코스
2. 장소별 추천 이유
3. 간단한 이동 순서
4. 여행 팁

주의:
- 장소 후보에 없는 장소는 새로 만들지 마.
- 너무 길지 않게 작성해줘.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "너는 국내 여행 추천을 도와주는 친절한 여행 플래너야."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def create_travel_plan(region, style, days, places):
    """
    OpenAI API 키가 없을 때 사용하는 간단 추천 함수
    """
    result = f"\n[{region} {style} 여행 추천 코스]\n"
    result += f"여행 기간: {days}일\n\n"

    for idx, place in enumerate(places[:5], start=1):
        result += f"{idx}. {place['name']}\n"
        result += f"   주소: {place['address']}\n"
        result += f"   분류: {place['category']}\n"
        result += f"   링크: {place['url']}\n\n"

    result += "위 장소들을 순서대로 방문하는 코스를 추천합니다."

    return result