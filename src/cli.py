# -*- coding: utf-8 -*-
"""
Command Line Interface for video restoration pipeline.
"""

import argparse
import sys
from video_restoration.pipeline import process_video

def main():
    parser = argparse.ArgumentParser(
        description="OpenCV and NumPy based vintage camcorder video restoration pipeline."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to input video file.")
    parser.add_argument("-o", "--output", required=True, help="Path to output restored video file.")
    parser.add_argument("--no-deinterlace", action="store_true", help="Disable deinterlacing.")
    parser.add_argument("--field", default="top", choices=["top", "bottom"], help="Deinterlacing field ('top' or 'bottom').")
    parser.add_argument("--no-denoise", action="store_true", help="Disable denoising.")
    parser.add_argument("--h-val", type=float, default=10.0, help="Denoising filter strength.")
    parser.add_argument("--no-clahe", action="store_true", help="Disable CLAHE contrast enhancement.")
    parser.add_argument("--clip-limit", type=float, default=2.0, help="CLAHE clip limit.")
    parser.add_argument("--tile-size", type=int, default=8, help="CLAHE tile grid size (N x N).")

    args = parser.parse_args()

    try:
        print(f"Starting video restoration on {args.input}...")
        stats = process_video(
            input_path=args.input,
            output_path=args.output,
            deinterlace=not args.no_deinterlace,
            field=args.field,
            denoise=not args.no_denoise,
            h_val=args.h_val,
            clahe=not args.no_clahe,
            clip_limit=args.clip_limit,
            tile_grid_size=(args.tile_size, args.tile_size)
        )
        print("Restoration completed successfully!")
        print(f"Output saved to: {stats['output_path']}")
        print(f"Processed {stats['total_frames']} frames at {stats['fps']} FPS ({stats['width']}x{stats['height']}).")
    except Exception as e:
        print(f"Error during video restoration: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
