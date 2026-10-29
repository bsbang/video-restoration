# -*- coding: utf-8 -*-
"""
VHS Chroma Bleed removal module.
"""

import cv2
import numpy as np

def remove_chroma_bleed(frame: np.ndarray, ksize: int = 5) -> np.ndarray:
    """
    Remove VHS chroma bleed by blurring or shifting color channels in YUV/YCrCb color space.
    
    Args:
        frame (np.ndarray): Input BGR frame.
        ksize (int): Kernel size for smoothing chroma channels.
        
    Returns:
        np.ndarray: Frame with reduced chroma bleeding.
    """
    if frame is None or frame.size == 0:
        raise ValueError("Input frame is empty or None.")
        
    if len(frame.shape) == 2 or frame.shape[2] == 1:
        # Grayscale, no chroma channels
        return frame.copy()

    # Convert to YCrCb
    ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)

    # Apply blur or sharpening to Cr and Cb to reduce bleed/smearing
    # Alternatively, median filtering or bilateral filtering on Cr/Cb
    if ksize % 2 == 0:
        ksize += 1

    cr_cleaned = cv2.bilateralFilter(cr, d=ksize, sigmaColor=50, sigmaSpace=50)
    cb_cleaned = cv2.bilateralFilter(cb, d=ksize, sigmaColor=50, sigmaSpace=50)

    merged = cv2.merge([y, cr_cleaned, cb_cleaned])
    output = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)
    return output
