# Project Progress & Autonomous Loop Tasks

- [x] Phase 0: 프로젝트 구조 및 의존성 설정 (`pyproject.toml`, 디렉토리 레이아웃)
- [x] Phase 1: `video_restoration/` 내 YADIF 스타일 보간 디인터레이싱, 가우시안/바이래터럴 노이즈 제거, CLAHE 명암비 개선 및 PSNR/SSIM 품질 측정 함수 구현
- [x] Phase 2: `cli.py`를 통한 명령줄 인터페이스 구현 및 전체 파이프라인 통합
- [ ] Phase 3: `tests/` 단위 테스트 작성, CI 워크플로우 설정 및 README.md 작성
- [ ] Phase 4: VHS 크로마 블리드(YUV 색차 채널 블러/보정) 제거 필터 추가 및 원본/복원본 Side-by-Side 비교 이미지 저장 기능 구현
