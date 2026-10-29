# SRS (요구사항 명세서) - video-restoration

## 1. 개요
- 목표: OpenCV and NumPy based vintage camcorder video restoration pipeline with deinterlacing, denoising, CLAHE contrast, VHS color noise removal, side-by-side comparison, PSNR/SSIM metrics, CLI tool, and unit tests

## 2. 기능 요구사항 (Functional Requirements)
- **FR-01 (복원 파이프라인 코어)**: YADIF 스타일 보간 디인터레이싱, 가우시안/바이래터럴 노이즈 제거, CLAHE 명암비 개선 및 VHS 크로마 블리드 제거 알고리즘 구현
- **FR-02 (품질 평가 및 비교, CLI)**: PSNR 및 SSIM 메트릭 측정, 원본/결과물 Side-by-Side 비교 및 이미지 저장, 명령어 기반 인터페이스(CLI) 구현
- **FR-03 (유닛 테스트 및 안정성)**: 핵심 알고리즘 및 파이프라인 단계별 유닛 테스트 작성 및 예외 처리