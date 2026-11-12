import requests
from config import KAKAO_REST_API_KEY

KAKAO_KEYWORD_URL = "https://dapi.kakao.com/v2/local/search/keyword.json"


def search_places(query, size=5):
    """
    카카오 Local API를 사용해 장소를 검색하는 함수
    """
    if not KAKAO_REST_API_KEY:
        print("오류: KAKAO_REST_API_KEY가 설정되어 있지 않습니다.")
        return []

    headers = {
        "Authorization": f"KakaoAK {KAKAO_REST_API_KEY}"
    }

    params = {
        "query": query,
        "size": size
    }

    response = requests.get(KAKAO_KEYWORD_URL, headers=headers, params=params)

    if response.status_code != 200:
        print("카카오 API 호출 실패")
        print("상태 코드:", response.status_code)
        print("응답:", response.text)
        return []

    data = response.json()
    documents = data.get("documents", [])

    places = []

    for doc in documents:
        places.append({
            "name": doc.get("place_name", ""),
            "address": doc.get("road_address_name") or doc.get("address_name", ""),
            "category": doc.get("category_name", ""),
            "url": doc.get("place_url", ""),
            "x": doc.get("x", ""),
            "y": doc.get("y", "")
        })

    return places


def collect_places(region, style):
    """
    지역과 여행 스타일을 바탕으로 여러 검색어를 만들고,
    검색 결과를 모아 중복 제거 후 반환하는 함수
    """
    style_keywords = {
        "자연": ["자연 명소", "공원", "둘레길"],
        "역사": ["역사 유적", "박물관", "궁"],
        "맛집": ["맛집", "카페", "전통시장"],
        "가족": ["가볼만한 곳", "테마파크", "체험"],
        "힐링": ["산책로", "수목원", "한적한 카페"]
    }

    keywords = style_keywords.get(style, ["가볼만한 곳"])
    all_places = []
    seen = set()

    for keyword in keywords:
        query = f"{region} {keyword}"
        places = search_places(query)

        for place in places:
            key = (place["name"], place["address"])

            if key not in seen:
                seen.add(key)
                all_places.append(place)

    return all_places