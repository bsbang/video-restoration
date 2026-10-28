# SRS (요구사항 명세서) - video-restoration

## 1. 개요
- 목표: OpenCV and FFmpeg based vintage camcorder video restoration and upscaling pipeline

## 2. 기능 요구사항 (Functional Requirements)
- **FR-01 (코어 엔진 및 UI)**: 핵심 데이터 구조, 화면 렌더링 및 기본 레이아웃 구현
- **FR-02 (핵심 인터랙션 및 로직)**: 사용자 입력 처리, 상태 전이, 게임/비즈니스 규칙 및 점수/상태 기록(localStorage 등)
- **FR-03 (편의 기능 및 모바일/사운드)**: 반응형 터치/키보드 조작, 효과음 또는 예외 처리 및 리셋 기능