# Video Restoration Project State (PROJECT_STATE.md)

## 1. 프로젝트 개요
- **프로젝트명**: `video-restoration`
- **작업 경로**: `~/SecondBrain/01_Projects/video-restoration`
- **원격 저장소 (SSOT)**: `https://github.com/bsbang/video-restoration.git` (`main` 브랜치, 최신 커밋: `2e10fa3`)
- **기술 스택**: Python, OpenCV, Streamlit, Requests (Telegram Bot API), Git/GitHub, Gemini CLI

## 2. 디렉토리 및 파일 아키텍처 (GitHub 동기화 기준)
- **상태 및 자율 루프 제어**:
  - `PROJECT_STATE.md`: 프로젝트 마스터 상태 및 로드맵 정의 문서
  - `jarvis.json`: Antigravity 자율 에이전트 설정 및 오케스트레이션 구성 파일
  - `sprint_state.json`: 스프린트 단계별 진행 상태 및 승인 게이트 추적 데이터
- **코어 백엔드 및 유틸리티**:
  - `src/video_restoration/enhancer.py`: 프레임별 영상 화질 개선 필터 모듈
  - `src/video_restoration/pipeline.py`: 비디오 스트림 처리, 인코딩 및 알림 오케스트레이션 파이프라인
  - `src/utils/telegram.py`: 텔레그램 봇 API 기반 실시간 작업 리포팅 모듈 (시작/오류/완료 알림)
- **실행 스크립트 및 UI/데모**:
  - `scripts/demo.py`: 파이프라인 실행 및 복원 테스트용 데모 스크립트
  - `docs/UI_MOCKUP.html`: 웹 UI 프로토타입 목업 문서
  - `app_prototype.py`: Streamlit 기반 웹 인터페이스 (`0.0.0.0:8501`)
- **결과물 레퍼런스**:
  - `outputs/comparison.png`: 화질 개선 전후 비교 레퍼런스 이미지
  - `outputs/restored_full.png`: 복원 완료된 전체 해상도 샘플 이미지

## 3. 진행 상황 (Sprint Status)
- **Sprint 1 (기획 및 아키텍처 설계)**: 완료 및 텔레그램 승인 완료
- **Sprint 2 (코어 백엔드 파이프라인 및 텔레그램 연동)**:
  - OpenCV 기반 보정 모듈(`enhancer.py`) 및 파이프라인(`pipeline.py`) 구현 완료
  - 텔레그램 알림 모듈(`telegram.py`)과 파이프라인 라이프사이클(시작/에러/완료) 자동 리포팅 연동 완료
  - `scripts/demo.py`를 통한 샘플 복원 및 비교 이미지(`outputs/comparison.png`, `outputs/restored_full.png`) 생성 완료
  - GitHub `main` 브랜치(`2e10fa3`) 커밋 및 동기화 완료

## 4. 핵심 구현 구성요소 및 최신 기술 기획안
- **1단계 기본 보정 파이프라인 (구현 완료)**:
  - **컬러 노이즈 제거**: `cv2.fastNlMeansDenoisingColored` 적용
  - **명암비 개선**: YCrCb 색공간 기반 `CLAHE` (Contrast Limited Adaptive Histogram Equalization) 적용
  - **해상도 업스케일링**: `Bicubic Interpolation` 기반 2배 확대 및 `mp4v` 코덱 인코딩
- **2단계 차세대 AI 화질 개선 확장 기획 (트렌드 반영)**:
  - **딥러닝 초해상도 (AI Super-Resolution)**: 단순 보간법을 넘어 손실된 텍스처와 디테일을 복원하기 위한 `Real-ESRGAN` 등 딥러닝 업스케일링 모델 플러그인 구조 확장
  - **시계열 노이즈 제거 (Temporal Denoising)**: 프레임 간 깜빡임(Flickering) 현상을 억제하고 시간적 일관성을 유지하는 멀티 프레임 디노이징 기법 도입
  - **하이브리드 자율 개발 루프**: `jarvis.json` 및 `sprint_state.json`을 기반으로 텔레그램 승인(`/approve`)과 클라우드/로컬 실행을 연동하는 무중단 자동화 워크플로우 정착

## 5. 일관성 유지 및 드리프트 방지 수칙 (GitOps & Gemini CLI)
- **단일 진실 공급원 (Single Source of Truth)**: 모든 코드와 상태 문서는 GitHub 저장소(`bsbang/video-restoration`)를 유일한 기준으로 삼으며, 임의 롤백이나 스펙 이탈을 금지함.
- **환경 간 동기화**: 클라우드(Cloud Shell/VM)와 로컬 PC 전환 시 반드시 `git pull origin main` 및 `git status`로 무결성을 먼저 검증한 뒤 작업을 진행함.
- **교차 검증**: Gemini CLI를 통해 실제 파일 시스템과 Git 로그를 대조하고, 변경 사항 발생 시 GitHub 커밋 후 Google Drive 및 NotebookLM 문서를 동기화함.

## 6. 향후 과제 (Next Steps - Sprint 3)
- Argon 모델 환경에서 `jarvis.json` 및 `sprint_state.json` 기반 자율 에이전트 루프 엔드투엔드(E2E) 검증
- `scripts/demo.py` 및 Streamlit UI(`docs/UI_MOCKUP.html` 반영) 실전 연동 테스트
- 대용량 비디오 출력물 관리를 위한 `.gitignore` 설정(`outputs/*.mp4` 제외) 및 AI 초해상도 모델 연동 준비
