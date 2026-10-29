# -*- coding: utf-8 -*-
"""
Video restoration pipeline combining deinterlacing, denoising, and CLAHE.
"""

import cv2
import numpy as np
from .deinterlace import bob_deinterlace
from .denoise import denoise_frame
from .clahe import apply_clahe

def process_video(
    input_path: str,
    output_path: str,
    deinterlace: bool = True,
    field: str = 'top',
    denoise: bool = True,
    h_val: float = 10.0,
    clahe: bool = True,
    clip_limit: float = 2.0,
    tile_grid_size: tuple = (8, 8)
) -> dict:
    """
    Processes an entire video file through the restoration pipeline.
    
    Args:
        input_path (str): Path to input video file.
        output_path (str): Path to save restored video file.
        deinterlace (bool): Whether to apply bob deinterlacing.
        field (str): Field to keep ('top' or 'bottom').
        denoise (bool): Whether to apply denoising.
        h_val (float): Denoising filter strength.
        clahe (bool): Whether to apply CLAHE contrast enhancement.
        clip_limit (float): CLAHE clip limit.
        tile_grid_size (tuple): CLAHE tile grid size.
        
    Returns:
        dict: Processing summary statistics (total_frames, fps, resolution, etc.)
    """
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise IOError(f"Could not open input video: {input_path}")
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30.0 # fallback
        
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not out.isOpened():
        cap.release()
        raise IOError(f"Could not open video writer for output: {output_path}")
        
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        processed = frame
        if deinterlace:
            processed = bob_deinterlace(processed, field=field)
        if denoise:
            processed = denoise_frame(processed, h_val=h_val)
        if clahe:
            processed = apply_clahe(processed, clip_limit=clip_limit, tile_grid_size=tile_grid_size)
            
        out.write(processed)
        frame_count += 1
        
    cap.release()
    out.release()
    
    return {
        "input_path": input_path,
        "output_path": output_path,
        "total_frames": frame_count,
        "fps": fps,
        "width": width,
        "height": height
    }
