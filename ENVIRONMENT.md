# Video Restoration 개발 환경 명세서

## 1. 런타임 환경
- **플랫폼**: Google Cloud Shell (Debian x86_64 Linux)
- **언어**: Python 3.10+
- **주요 라이브러리**: OpenCV (Headless), PyTorch (CPU Inference), Real-ESRGAN, Basicsr, Pytest
- **제어 인터페이스**: Telegram Bot (12-Button Remote Control Panel)

## 2. 텔레그램 원격 제어 인터페이스 연동 규약
- `/status`: `sprint_state.json` 읽기 및 스프린트 진행 현황 보고
- `/run`: `scripts/demo.py` 비동기 실행 후 `outputs/*.png` 결과 사진 채팅방 회신
- `/test`: `pytest tests/` 실행 후 통과/실패 요약 리포트 전송
- `/approve`: 현재 스프린트 승인 완료 기록 (`approved: true`)
- `/git`: 최근 커밋 3건 및 미커밋 변경 사항(`git status -s`) 확인
- `/sys`: Cloud Shell 메모리(RAM), 디스크 가용량, CPU 부하 실시간 점검
- `/clean`: `__pycache__` 및 pytest 캐시 안전 삭제

## 3. 실행 가이드
- **단위 테스트**: `pytest tests/`
- **데모 파이프라인**: `python3 scripts/demo.py`
- **웹 UI 목업**: `streamlit run app.py --server.port 8501`
