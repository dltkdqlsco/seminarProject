# 1. Python 3.10 기반 이미지 사용
FROM python:3.10-slim

# 2. 작업 디렉터리 생성 및 이동
WORKDIR /app

# 3. 현재 디렉터리의 모든 파일 복사
COPY . /app

# 4. 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. Flask 환경 변수 설정 (프로덕션에서는 적절히 조정)
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# 6. 컨테이너 외부에서 접근 가능한 포트 설정
EXPOSE 8080

# 7. Flask 앱 실행
CMD ["flask", "run"]
