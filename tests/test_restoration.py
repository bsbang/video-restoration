# -*- coding: utf-8 -*-
"""
Unit tests for video_restoration modules.
"""

import pytest
import numpy as np
import cv2
from video_restoration.deinterlace import bob_deinterlace
from video_restoration.denoise import denoise_frame
from video_restoration.clahe import apply_clahe
from video_restoration.metrics import calculate_psnr, calculate_ssim

def test_bob_deinterlace():
    # Create synthetic frame (100x100, 3 channels)
    frame = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    deinterlaced_top = bob_deinterlace(frame, field='top')
    deinterlaced_bottom = bob_deinterlace(frame, field='bottom')
    
    assert deinterlaced_top.shape == frame.shape
    assert deinterlaced_bottom.shape == frame.shape

    # Grayscale test
    gray_frame = np.random.randint(0, 256, (50, 50), dtype=np.uint8)
    gray_out = bob_deinterlace(gray_frame, field='top')
    assert gray_out.shape == gray_frame.shape

    # Invalid field test
    with pytest.raises(ValueError):
        bob_deinterlace(frame, field='invalid')

    # Empty frame test
    with pytest.raises(ValueError):
        bob_deinterlace(np.array([]))

def test_denoise_frame():
    frame = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    denoised = denoise_frame(frame, h_val=5.0)
    assert denoised.shape == frame.shape

    gray_frame = np.random.randint(0, 256, (64, 64), dtype=np.uint8)
    gray_denoised = denoise_frame(gray_frame, h_val=5.0)
    assert gray_denoised.shape == gray_frame.shape

    with pytest.raises(ValueError):
        denoise_frame(np.array([]))

def test_apply_clahe():
    frame = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    enhanced = apply_clahe(frame, clip_limit=2.0)
    assert enhanced.shape == frame.shape

    gray_frame = np.random.randint(0, 256, (64, 64), dtype=np.uint8)
    gray_enhanced = apply_clahe(gray_frame, clip_limit=2.0)
    assert gray_enhanced.shape == gray_frame.shape

    with pytest.raises(ValueError):
        apply_clahe(np.array([]))

def test_metrics():
    orig = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    restored = orig.copy()
    
    psnr_val = calculate_psnr(orig, restored)
    ssim_val = calculate_ssim(orig, restored)
    
    # Identical images should have very high PSNR (> 90 or inf) and SSIM of 1.0
    assert ssim_val == pytest.approx(1.0, rel=1e-2)
    assert psnr_val > 50.0

    # Shape mismatch test
    other = np.random.randint(0, 256, (32, 32, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        calculate_psnr(orig, other)
    with pytest.raises(ValueError):
        calculate_ssim(orig, other)
