# -*- coding: utf-8 -*-
"""
Video quality assessment metrics: PSNR and SSIM.
"""

import numpy as np
from skimage.metrics import peak_signal_noise_ratio as skimage_psnr
from skimage.metrics import structural_similarity as skimage_ssim

def calculate_psnr(orig: np.ndarray, restored: np.ndarray) -> float:
    """
    Calculates Peak Signal-to-Noise Ratio (PSNR) between original and restored frames.
    
    Args:
        orig (np.ndarray): Original reference image/frame.
        restored (np.ndarray): Restored image/frame.
        
    Returns:
        float: PSNR value in decibels (dB).
    """
    if orig.shape != restored.shape:
        raise ValueError("Original and restored frames must have the same shape.")
        
    data_range = 255.0 if orig.dtype == np.uint8 or orig.max() > 1.0 else 1.0
    return float(skimage_psnr(orig, restored, data_range=data_range))

def calculate_ssim(orig: np.ndarray, restored: np.ndarray) -> float:
    """
    Calculates Structural Similarity Index (SSIM) between original and restored frames.
    
    Args:
        orig (np.ndarray): Original reference image/frame.
        restored (np.ndarray): Restored image/frame.
        
    Returns:
        float: SSIM value between -1 and 1.
    """
    if orig.shape != restored.shape:
        raise ValueError("Original and restored frames must have the same shape.")
        
    data_range = 255.0 if orig.dtype == np.uint8 or orig.max() > 1.0 else 1.0
    
    # Handle multichannel automatically
    channel_axis = -1 if orig.ndim == 3 else None
    
    return float(skimage_ssim(orig, restored, data_range=data_range, channel_axis=channel_axis))
