import os
import subprocess
import config
from multiprocessing import Pool
from tqdm import tqdm


def get_video_codec(file_path):
    """Get the video codec of the file using ffprobe"""
    cmd = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=codec_name',
        '-of', 'default=noprint_wrappers=1:nokey=1', file_path
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def is_lossless(file_path):
    """Check if video codec is lossless libx264 with crf 0 or ffv1"""
    codec = get_video_codec(file_path)
    if codec is None:
        return False
    if codec == 'ffv1':
        return True
    if codec == 'h264':
        # Treats h264 as lossy unless known otherwise
        return False
    return False

def convert_to_lossless(input_path):
    """Convert video to lossless H.264 (crf 0) and FLAC audio in MKV container"""
    output_path = os.path.splitext(input_path)[0] + '_lossless.mkv'
    print(f"Converting\n  '{input_path}'\nto lossless\n  '{output_path}'")
    cmd = [
        'ffmpeg', '-i', input_path,
        '-c:v', 'libx264', '-preset', config.CONVERSION_SPEED, '-crf', '0',
        '-c:a', 'flac',
        output_path
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Conversion finished: {output_path}")
    except subprocess.CalledProcessError:
        print(f"Error converting {input_path}")

def process_video(full_path):
    """Worker function for multiprocessing - process single video"""
    output_path = os.path.splitext(full_path)[0] + '_lossless.mkv'

    if os.path.exists(output_path):
        print(f"Exists already, skipping {output_path}")
        return

    if not is_lossless(full_path):
        convert_to_lossless(full_path)
    else:
        print(f"Skipping lossless file: {full_path}")

def crawl_and_convert(root_dir):
    """Scanns through directory-structure and starts converison process"""
    video_files = []
    print(f"Scanning {root_dir} for video files...")
    for dirpath, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(config.VIDEO_EXTENSIONS):
                full_path = os.path.join(dirpath, file)
                video_files.append(full_path)

    print(f"{len(video_files)} videos found.")

    if not video_files:
        print("No video files found.")
        return

    max_workers =  min(len(video_files), config.MAX_WORKERS or ((os.cpu_count() or 4) // 2)) #half CPU cores
    print(f"Starting parallel conversion using {max_workers} workers...")

    with Pool(processes=max_workers) as pool:
        list(tqdm(pool.imap(process_video, video_files),
                  total=len(video_files),
                  desc="Converting Videos"))

    print("🎉 All conversions completed!")


if __name__ == '__main__':
    crawl_and_convert(config.MEDIA_ROOT)
