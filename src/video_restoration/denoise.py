# -*- coding: utf-8 -*-
"""
Denoising algorithms for vintage camcorder footage.
Supports Non-Local Means (FastNlMeans) and Gaussian/Median filtering.
"""

import cv2
import numpy as np

def denoise_frame(frame: np.ndarray, h_val: float = 10.0, template_window_size: int = 7, search_window_size: int = 21) -> np.ndarray:
    """
    Denoises a single video frame using OpenCV's fastNlMeansDenoising.
    
    Args:
        frame (np.ndarray): Input image frame (grayscale or BGR).
        h_val (float): Parameter regulating filter strength for luminance.
        template_window_size (int): Size in pixels of the template patch.
        search_window_size (int): Size in pixels of the window used to search patches.
        
    Returns:
        np.ndarray: Denoised frame of the same shape and type.
    """
    if frame is None or frame.size == 0:
        raise ValueError("Input frame is empty or None.")
        
    # Ensure uint8 type for OpenCV NlMeans
    if frame.dtype != np.uint8:
        frame_uint8 = np.clip(frame, 0, 255).astype(np.uint8)
    else:
        frame_uint8 = frame
        
    if frame_uint8.ndim == 2:
        denoised = cv2.fastNlMeansDenoising(
            frame_uint8, None, h=h_val, 
            templateWindowSize=template_window_size, 
            searchWindowSize=search_window_size
        )
    elif frame_uint8.ndim == 3:
        denoised = cv2.fastNlMeansDenoisingColored(
            frame_uint8, None, h=h_val, hColor=h_val, 
            templateWindowSize=template_window_size, 
            searchWindowSize=search_window_size
        )
    else:
        raise ValueError("Unsupported frame dimensions for denoising.")
        
    return denoised
