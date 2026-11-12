import argparse
import sys
from datetime import datetime

from kakao_api import search_places
from llm_recommender import create_travel_plan


def parse_date(value):
    """
    날짜 문자열이 YYYY-MM-DD 형식인지 검사하고 date 객체로 변환하는 함수
    예: 2025-08-20
    """
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(
            "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력하세요. 예: 2025-08-20"
        )


def main():
    parser = argparse.ArgumentParser(
        description="국내 여행지 추천 및 일정 생성 프로그램"
    )

    parser.add_argument(
        "--region",
        required=True,
        help="여행 지역을 입력하세요. 예: 서울, 부산, 제주"
    )

    parser.add_argument(
        "--start",
        required=True,
        type=parse_date,
        help="여행 시작일을 입력하세요. 형식: YYYY-MM-DD"
    )

    parser.add_argument(
        "--end",
        required=True,
        type=parse_date,
        help="여행 종료일을 입력하세요. 형식: YYYY-MM-DD"
    )

    args = parser.parse_args()

    # 시작일이 종료일보다 늦으면 에러 처리
    if args.start > args.end:
        parser.error("시작일은 종료일보다 늦을 수 없습니다.")

    region = args.region
    start_date = args.start.strftime("%Y-%m-%d")
    end_date = args.end.strftime("%Y-%m-%d")

    print("===================================")
    print("국내 여행 일정 생성 프로그램")
    print("===================================")
    print(f"여행 지역: {region}")
    print(f"여행 기간: {start_date} ~ {end_date}")
    print()

    # 카카오 API로 장소 검색
    try:
        print("[1단계] 카카오 API로 관광지를 검색하는 중...")
        places = search_places(f"{region} 관광지")
    except Exception as e:
        print("[오류] 카카오 API 호출 중 문제가 발생했습니다.")
        print(e)
        sys.exit(1)

    if not places:
        print("[오류] 검색된 장소가 없습니다.")
        print("지역명을 다시 확인해 주세요.")
        sys.exit(1)

    print(f"[완료] 장소 {len(places)}개를 찾았습니다.")
    print()

    # LLM으로 여행 일정 생성
    try:
        print("[2단계] AI가 여행 일정을 생성하는 중...")
        travel_plan = create_travel_plan(
            region,
            start_date,
            end_date,
            places
        )
    except Exception as e:
        print("[오류] AI 여행 일정 생성 중 문제가 발생했습니다.")
        print(e)
        sys.exit(1)

    print()
    print("===================================")
    print("추천 여행 일정")
    print("===================================")
    print(travel_plan)


if __name__ == "__main__":
    main()