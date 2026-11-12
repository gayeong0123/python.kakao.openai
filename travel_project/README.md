# 국내 여행 추천 프로그램

## 1. 프로젝트 소개

이 프로젝트는 사용자가 입력한 지역과 여행 스타일을 바탕으로 국내 여행 코스를 추천하는 프로그램입니다.

카카오 Local API를 사용해 실제 장소 정보를 검색하고, OpenAI API를 사용해 여행 일정을 생성합니다.

## 2. 주요 기능

- 여행 지역 입력
- 여행 스타일 입력
- 카카오 Local API를 이용한 장소 검색
- 검색 결과 중복 제거
- OpenAI API를 이용한 여행 일정 추천
- API 키가 없을 경우 간단 추천 결과 출력

## 3. 사용 기술

- Python
- Kakao Local API
- OpenAI API
- requests
- python-dotenv

## 4. 파일 구조

```text
travel_project/
├─ travel_planner.py
├─ kakao_api.py
├─ llm_recommender.py
├─ config.py
├─ requirements.txt
├─ README.md
├─ .env.example
└─ .gitignore