# -*- coding: utf-8 -*-
"""
Deinterlacing algorithms for video restoration.
Supports bob deinterlacing (spatial interpolation) and weaving.
"""

import numpy as np

def bob_deinterlace(frame: np.ndarray, field: str = 'top') -> np.ndarray:
    """
    Bob deinterlacing: interpolates missing lines from adjacent lines within the same field.
    
    Args:
        frame (np.ndarray): Input 2D (grayscale) or 3D (color) image array.
        field (str): 'top' or 'bottom' field to keep/interpolate from.
        
    Returns:
        np.ndarray: Deinterlaced frame with the same shape as input.
    """
    if frame is None or frame.size == 0:
        raise ValueError("Input frame is empty or None.")
        
    out = frame.copy()
    h = out.shape[0]
    
    if field == 'top':
        # Top field is on even rows (0, 2, 4, ...). Interpolate odd rows (1, 3, 5, ...)
        start_row = 1
    elif field == 'bottom':
        # Bottom field is on odd rows (1, 3, 5, ...). Interpolate even rows (0, 2, 4, ...)
        start_row = 0
    else:
        raise ValueError("Field must be either 'top' or 'bottom'.")
        
    for r in range(start_row, h, 2):
        if r == 0:
            out[0] = out[1] if h > 1 else out[0]
        elif r == h - 1:
            out[r] = out[r - 1]
        else:
            if out.ndim == 3:
                out[r] = (out[r - 1].astype(np.float32) + out[r + 1].astype(np.float32)) / 2.0
                out[r] = np.clip(out[r], 0, 255).astype(out.dtype)
            else:
                out[r] = (out[r - 1].astype(np.float32) + out[r + 1].astype(np.float32)) / 2.0
                out[r] = np.clip(out[r], 0, 255).astype(out.dtype)
                
    return out
