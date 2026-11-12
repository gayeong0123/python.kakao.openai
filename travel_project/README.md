국내 여행 추천 프로그램

LLM과 카카오 로컬 API를 활용해 국내 여행지를 추천하는 Python 기반 CLI 프로그램입니다.
사용자가 지역, 여행 시작일, 여행 종료일을 입력하면 해당 조건에 맞는 여행지를 추천하고, 관련 장소 정보를 함께 제공합니다.

프로젝트 소개

이 프로젝트는 사용자의 여행 조건을 바탕으로 국내 여행 계획을 도와주는 프로그램입니다.
LLM을 활용해 여행 추천 문장을 생성하고, 카카오 로컬 API를 이용해 실제 장소 검색 결과를 함께 제공합니다.

주요 기능
사용자가 입력한 지역과 여행 날짜를 기반으로 여행 추천
날짜 형식 검증 기능 제공
카카오 로컬 API를 활용한 장소 검색
환경변수(.env) 기반 API 키 관리
CLI(Command Line Interface) 방식으로 간단하게 실행 가능
기술 스택
Python
argparse
requests
python-dotenv
Kakao Local API
LLM API
프로젝트 구조
bash
travel_project/
├── travel_planner.py
├── llm_recommender.py
├── kakao_api.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

파일 설명
travel_planner.py

프로그램의 메인 실행 파일입니다.
사용자 입력을 받고, 날짜를 검증한 뒤 여행 추천 로직을 실행합니다.

llm_recommender.py

LLM을 활용해 여행 추천 문장을 생성하는 파일입니다.

kakao_api.py

카카오 로컬 API를 호출하여 장소 검색 결과를 가져오는 파일입니다.

config.py

환경변수에서 API 키를 불러오는 설정 파일입니다.

requirements.txt

프로젝트 실행에 필요한 Python 라이브러리 목록입니다.

.env.example

환경변수 파일 예시입니다.
실제 실행 시에는 .env 파일을 만들어 API 키를 입력해야 합니다.

설치 방법
1. 저장소 클론
bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름

2. 가상환경 생성 및 활성화

Windows

bash
python -m venv venv
venv\Scripts\activate


macOS / Linux

bash
python3 -m venv venv
source venv/bin/activate

3. 필요한 라이브러리 설치
bash
pip install -r requirements.txt

환경변수 설정

프로젝트 루트 폴더에 .env 파일을 생성한 뒤, 필요한 API 키를 입력합니다.

예시:

env
KAKAO_REST_API_KEY=your_kakao_rest_api_key
LLM_API_KEY=your_llm_api_key


LLM_API_KEY 이름은 실제 코드에서 사용하는 환경변수 이름에 맞춰 작성하세요.

실행 방법

기본 실행 형식은 아래와 같습니다.

bash
python travel_planner.py --region 지역명 --start YYYY-MM-DD --end YYYY-MM-DD

실행 예시
bash
python travel_planner.py --region 부산 --start 2025-08-01 --end 2025-08-03

동작 과정
사용자가 지역, 시작일, 종료일을 입력합니다.
프로그램이 날짜 형식을 검증합니다.
카카오 로컬 API를 통해 해당 지역의 장소 정보를 검색합니다.
LLM이 여행 추천 문장을 생성합니다.
최종 추천 결과를 사용자에게 출력합니다.
날짜 입력 규칙

날짜 형식은 반드시 YYYY-MM-DD 형식이어야 합니다.

시작일이 종료일보다 늦으면 안 됩니다.

예시:

올바른 입력: 2025-08-01
잘못된 입력: 2025/08/01
잘못된 입력: 08-01-2025
requirements.txt 예시
txt
requests
python-dotenv


실제 사용 중인 라이브러리가 더 있다면 pip freeze > requirements.txt 또는 직접 확인 후 반영하세요.

.gitignore 예시
gitignore
venv/
__pycache__/
.env
*.pyc

실행 결과 예시
bash
[여행 추천 결과]
지역: 부산
여행 기간: 2025-08-01 ~ 2025-08-03

추천 여행지:
- 해운대
- 감천문화마을
- 광안리

추천 일정:
부산의 대표 명소를 중심으로 2박 3일 여행을 즐길 수 있습니다.
바다 풍경, 먹거리, 산책 코스를 함께 경험할 수 있는 일정입니다.


실제 출력 결과는 코드 구현 방식과 LLM 응답에 따라 달라질 수 있습니다.

문제 해결
1. .env 파일을 읽지 못하는 경우
.env 파일이 프로젝트 루트 폴더에 있는지 확인
python-dotenv가 설치되어 있는지 확인
bash
pip install python-dotenv

2. 카카오 API 호출 시 403 오류가 발생하는 경우
Kakao Developers에서 REST API 키가 올바른지 확인
카카오 로컬 API 사용 권한이 활성화되어 있는지 확인
요청 헤더 형식이 올바른지 확인
3. 모듈이 없다고 나오는 경우

필요한 라이브러리를 다시 설치합니다.

bash
pip install -r requirements.txt

4. 날짜 오류가 발생하는 경우
날짜 형식이 YYYY-MM-DD인지 확인
시작일과 종료일 순서를 확인
향후 개선 방향
추천 정확도 향상을 위한 프롬프트 개선
관광지 외 맛집, 숙소 추천 기능 추가
웹 서비스 형태로 확장
사용자 선호도 기반 맞춤 추천 기능 추가
느낀 점

이 프로젝트를 통해 다음 내용을 학습할 수 있습니다.

Python CLI 프로그램 구성 방법
환경변수 관리 방법
외부 API 연동 방법
LLM을 활용한 추천 시스템 기본 구조
Git과 GitHub를 활용한 프로젝트 관리
라이선스

이 프로젝트는 학습 및 개인 포트폴리오 용도로 제작되었습니다.
