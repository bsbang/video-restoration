# -*- coding: utf-8 -*-
"""
Unit tests for color_noise and comparison modules.
"""

import pytest
import numpy as np
import cv2
from video_restoration.color_noise import remove_chroma_bleed
from video_restoration.comparison import create_side_by_side

def test_remove_chroma_bleed():
    frame = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    cleaned = remove_chroma_bleed(frame, ksize=5)
    assert cleaned.shape == frame.shape

    # Grayscale frame should return as is or handled gracefully
    gray_frame = np.random.randint(0, 256, (64, 64), dtype=np.uint8)
    gray_cleaned = remove_chroma_bleed(gray_frame)
    assert gray_cleaned.shape == gray_frame.shape

    with pytest.raises(ValueError):
        remove_chroma_bleed(np.array([]))

def test_create_side_by_side():
    orig = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    restored = np.random.randint(0, 256, (64, 64, 3), dtype=np.uint8)
    
    sbs = create_side_by_side(orig, restored, label_orig="Original", label_restored="Restored")
    assert sbs.shape == (64, 128 + 10, 3) # width expanded by 128 + separator 10

    # Size mismatch handling (should resize)
    other = np.random.randint(0, 256, (32, 32, 3), dtype=np.uint8)
    sbs_resized = create_side_by_side(orig, other)
    assert sbs_resized.shape[0] == 64

    with pytest.raises(ValueError):
        create_side_by_side(np.array([]), restored)
