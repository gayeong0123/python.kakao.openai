from kakao_api import collect_places
from llm_recommender import create_travel_plan


def get_user_input():
    """
    사용자에게 여행 정보를 입력받는 함수
    """
    print("=== 국내 여행 추천 프로그램 ===")

    region = input("여행할 지역을 입력하세요 예: 서울, 부산, 제주: ").strip()
    style = input("여행 스타일을 입력하세요 예: 자연, 역사, 맛집, 가족, 힐링: ").strip()
    days_input = input("여행 기간을 입력하세요 예: 1, 2, 3: ").strip()

    if not region:
        region = "서울"

    if not style:
        style = "자연"

    try:
        days = int(days_input)
    except ValueError:
        days = 1

    return region, style, days


def print_places(places):
    """
    카카오 API로 검색된 장소 후보를 출력하는 함수
    """
    print("\n=== 검색된 장소 후보 ===")

    if not places:
        print("검색된 장소가 없습니다.")
        return

    for idx, place in enumerate(places, start=1):
        print(f"{idx}. {place['name']}")
        print(f"   주소: {place['address']}")
        print(f"   분류: {place['category']}")
        print(f"   링크: {place['url']}")


def main():
    region, style, days = get_user_input()

    places = collect_places(region, style)

    print_places(places)

    print("\n=== AI 여행 일정 추천 ===")
    plan = create_travel_plan(region, style, days, places)
    print(plan)


if __name__ == "__main__":
    main()