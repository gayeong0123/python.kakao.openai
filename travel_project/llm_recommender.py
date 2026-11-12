from datetime import datetime
from openai import OpenAI
from config import OPENAI_API_KEY


def calculate_days(start_date, end_date):
    """
    시작일과 종료일 문자열(YYYY-MM-DD)을 받아 총 여행 일수를 계산하는 함수
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        return (end - start).days + 1
    except ValueError:
        return None


def create_simple_plan(region, start_date, end_date, places):
    """
    OpenAI API 키가 없거나 API 호출에 실패했을 때 사용하는 간단 추천 함수
    """
    days = calculate_days(start_date, end_date)

    result = f"\n[{region} 여행 추천 코스]\n"
    if days:
        result += f"여행 기간: {start_date} ~ {end_date} ({days}일)\n\n"
    else:
        result += f"여행 기간: {start_date} ~ {end_date}\n\n"

    for idx, place in enumerate(places[:5], start=1):
        result += f"{idx}. {place.get('name', '이름 정보 없음')}\n"
        result += f"   주소: {place.get('address', '주소 정보 없음')}\n"
        result += f"   분류: {place.get('category', '분류 정보 없음')}\n"
        result += f"   링크: {place.get('url', '링크 정보 없음')}\n\n"

    result += "추천 순서: 위 장소를 1번부터 차례대로 방문하는 코스를 추천합니다.\n"
    result += "여행 팁: 이동 시간을 고려해 오전/오후 일정을 나누어 계획하면 좋습니다."

    return result


def create_travel_plan(region, start_date, end_date, places):
    """
    OpenAI API를 사용해 여행 일정을 생성하는 함수
    """
    if not places:
        return "추천할 장소가 없습니다."

    days = calculate_days(start_date, end_date)
    days_text = f"{days}일" if days else "일정 계산 불가"

    if not OPENAI_API_KEY:
        return create_simple_plan(region, start_date, end_date, places)

    client = OpenAI(api_key=OPENAI_API_KEY)

    place_text = ""
    for idx, place in enumerate(places, start=1):
        place_text += (
            f"{idx}. {place.get('name', '이름 정보 없음')} - "
            f"{place.get('address', '주소 정보 없음')} - "
            f"{place.get('category', '분류 정보 없음')}\n"
        )

    prompt = f"""
너는 국내 여행 일정을 추천하는 여행 플래너야.

사용자 조건:
- 지역: {region}
- 여행 기간: {start_date} ~ {end_date} ({days_text})

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
- 한국어로 작성해줘.
"""

    try:
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

    except Exception:
        return create_simple_plan(region, start_date, end_date, places)