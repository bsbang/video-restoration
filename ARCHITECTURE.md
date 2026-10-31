# Zero-Touch Git-Ops Autonomous Development Constitution

본 프로젝트(video-restoration)는 사람이 코드를 터미널에 복사·붙여넣기하거나 에이전트 UI에 프롬프트를 수동 입력하지 않는 **'완전 무개입 자율 개발 루프'**로 운영된다.

## 1. 3대 절대 원칙 (Non-Negotiable)
1. **Zero Manual Copy-Paste**: 사용자는 텔레그램 또는 대화창을 통해 "목표(Goal)"만 선언한다.
2. **Git-Ops Asynchronous Bus**: GitHub 저장소가 비동기 작업 큐 역할을 수행한다.
   - 기획자(Jarvis/텔레그램): `TASK.md` 및 `sprint_state.json` (QUEUED) 생성 후 Push
   - 실행자(Antigravity): Push 감지 -> 환경 구축 -> 자율 코딩 -> pytest 통과 -> Push (COMPLETED)
   - 모니터(Telegram Daemon): 상태 변경 감지 -> 결과물(`outputs/comparison.png`) 텔레그램 자동 전송
3. **Session Immortality**: 세션이나 메모리가 휘발되어도 `ARCHITECTURE.md`와 `sprint_state.json`을 단일 진실 공급원으로 삼아 즉시 원래 방향성을 100% 복원한다.

## 2. 작업 계약 규약 (Contract)
- **명세 파일**: `TASK.md` (목표, 가중치 다운로드 URL, 구현 파일 경로, 검증 명령어 포함)
- **상태 관리**: `sprint_state.json` (QUEUED -> IN_PROGRESS -> COMPLETED)
- **검증 기준**: `pytest tests/` 무조건 Pass + `scripts/demo.py` 정상 종료
