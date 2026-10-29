# -*- coding: utf-8 -*-
"""
Side-by-side comparison module for original and restored frames.
"""

import cv2
import numpy as np

def create_side_by_side(orig: np.ndarray, restored: np.ndarray, 
                          label_orig: str = "Original", 
                          label_restored: str = "Restored",
                          separator_width: int = 10) -> np.ndarray:
    """
    Create a side-by-side comparison image of original and restored frames with labels.
    
    Args:
        orig (np.ndarray): Original BGR or grayscale frame.
        restored (np.ndarray): Restored BGR or grayscale frame.
        label_orig (str): Text label for original frame.
        label_restored (str): Text label for restored frame.
        separator_width (int): Width of separator space between images.
        
    Returns:
        np.ndarray: Combined side-by-side image.
    """
    if orig is None or orig.size == 0 or restored is None or restored.size == 0:
        raise ValueError("Input frames cannot be empty or None.")

    # Ensure same height
    h_orig, w_orig = orig.shape[:2]
    h_rest, w_rest = restored.shape[:2]

    if h_orig != h_rest or w_orig != w_rest:
        restored = cv2.resize(restored, (w_orig, h_orig))

    # Handle grayscale vs color channel mismatch
    if len(orig.shape) == 2 and len(restored.shape) == 3:
        orig = cv2.cvtColor(orig, cv2.COLOR_GRAY2BGR)
    elif len(orig.shape) == 3 and len(restored.shape) == 2:
        restored = cv2.cvtColor(restored, cv2.COLOR_GRAY2BGR)

    h, w = orig.shape[:2]
    separator = np.zeros((h, separator_width, 3), dtype=np.uint8) + 50 # Gray separator

    combined = np.hstack((orig, separator, restored))

    # Add text labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = max(0.5, h / 500.0)
    thickness = max(1, int(h / 200.0))
    
    cv2.putText(combined, label_orig, (20, 30), font, font_scale, (0, 255, 255), thickness, cv2.LINE_AA)
    cv2.putText(combined, label_restored, (w + separator_width + 20, 30), font, font_scale, (0, 255, 255), thickness, cv2.LINE_AA)

    return combined
