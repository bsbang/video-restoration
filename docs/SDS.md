# SDS (상세 설계서) - video-restoration

## 1. 시스템 아키텍처 및 파일 구조
- `video_restoration/`: 코어 파이프라인 모듈 (deinterlace, denoise, clahe, color_noise, metrics, comparison)
- `cli.py`: CLI 인터페이스 엔트리포인트 (Side-by-Side 비교 출력, 이미지 저장 및 필터 옵션 추가)
- `tests/`: 단위 테스트 스위트
- `pyproject.toml` 또는 `setup.py`: 의존성 관리 (OpenCV, NumPy, scikit-image 등)
- `.github/workflows/ci.yml`: CI 및 테스트 자동화 워크플로우
- `README.md`: 프로젝트 설명 및 사용법 가이드