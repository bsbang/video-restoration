#!/usr/bin/env python3
"""video-restoration 프로젝트 전용 검증 데모 스크립트 (표준 규격: outputs/에 결과물 생성)"""
import sys, os, glob, cv2, numpy as np
sys.path.insert(0, os.path.abspath("src"))

os.makedirs("outputs", exist_ok=True)
# 기존 출력물 정리 후 최신 결과물만 남김
for f in glob.glob("outputs/*"):
    if os.path.isfile(f): os.remove(f)

# 입력 인자(업로드된 파일)가 있으면 해당 이미지 사용, 없으면 가상 VHS 샘플 생성
input_file = sys.argv[1] if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else None

if input_file:
    noisy = cv2.imread(input_file)
    clean = None
else:
    h, w = 360, 480
    clean = np.zeros((h, w, 3), dtype=np.uint8)
    cv2.rectangle(clean, (40, 40), (220, 320), (200, 120, 50), -1)
    cv2.circle(clean, (340, 180), 90, (60, 180, 230), -1)
    cv2.putText(clean, 'VHS RESTORE', (80, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
    noisy = clean.copy()
    noise = np.random.normal(0, 25, clean.shape).astype(np.int16)
    noisy = np.clip(noisy.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    noisy[1::2, :] = (noisy[1::2, :] * 0.55).astype(np.uint8)

restored = noisy.copy()
for y in range(1, restored.shape[0]-1, 2):
    restored[y] = ((restored[y-1].astype(np.int16) + restored[y+1].astype(np.int16)) // 2).astype(np.uint8)

ycrcb = cv2.cvtColor(restored, cv2.COLOR_BGR2YCrCb)
y_ch, cr, cb = cv2.split(ycrcb)
y_ch = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(y_ch)
cr = cv2.GaussianBlur(cr, (7, 7), 0)
cb = cv2.GaussianBlur(cb, (7, 7), 0)
restored = cv2.cvtColor(cv2.merge([y_ch, cr, cb]), cv2.COLOR_YCrCb2BGR)
restored = cv2.bilateralFilter(restored, 7, 45, 45)

h, w = noisy.shape[:2]
bar_h = 40
b_bar = np.zeros((h + bar_h, w, 3), dtype=np.uint8); b_bar[bar_h:] = noisy
a_bar = np.zeros((h + bar_h, w, 3), dtype=np.uint8); a_bar[bar_h:] = restored
cv2.putText(b_bar, 'Before', (12, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 255), 2)
cv2.putText(a_bar, 'After', (12, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 255, 100), 2)

comp = np.hstack([b_bar, np.full((h + bar_h, 4, 3), 255, dtype=np.uint8), a_bar])
cv2.imwrite("outputs/comparison.png", comp)
cv2.imwrite("outputs/restored_full.png", restored)

if clean is not None:
    print(f"[데모 검증 완료] 가상 샘플 PSNR 개선: {cv2.PSNR(clean, noisy):.2f} dB -> {cv2.PSNR(clean, restored):.2f} dB")
else:
    print(f"[실전 파일 검증 완료] 입력 해상도: {w}x{h} | 변화도(PSNR): {cv2.PSNR(noisy, restored):.2f} dB")
