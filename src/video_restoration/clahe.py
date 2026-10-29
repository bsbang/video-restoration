# -*- coding: utf-8 -*-
"""
CLAHE (Contrast Limited Adaptive Histogram Equalization) contrast enhancement.
"""

import cv2
import numpy as np

def apply_clahe(frame: np.ndarray, clip_limit: float = 2.0, tile_grid_size: tuple = (8, 8)) -> np.ndarray:
    """
    Applies CLAHE contrast enhancement to an image frame.
    For color images, CLAHE is applied to the L channel in LAB color space.
    
    Args:
        frame (np.ndarray): Input image frame (grayscale or BGR).
        clip_limit (float): Threshold for contrast limiting.
        tile_grid_size (tuple): Size of grid for histogram equalization.
        
    Returns:
        np.ndarray: Enhanced frame of the same shape and type.
    """
    if frame is None or frame.size == 0:
        raise ValueError("Input frame is empty or None.")
        
    if frame.dtype != np.uint8:
        frame_uint8 = np.clip(frame, 0, 255).astype(np.uint8)
    else:
        frame_uint8 = frame
        
    clahe_obj = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    
    if frame_uint8.ndim == 2:
        enhanced = clahe_obj.apply(frame_uint8)
    elif frame_uint8.ndim == 3:
        # Convert BGR to LAB
        lab = cv2.cvtColor(frame_uint8, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l_enhanced = clahe_obj.apply(l)
        lab_enhanced = cv2.merge((l_enhanced, a, b))
        enhanced = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)
    else:
        raise ValueError("Unsupported frame dimensions for CLAHE.")
        
    return enhanced
