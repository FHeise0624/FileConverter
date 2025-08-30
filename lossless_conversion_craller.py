import os
import subprocess

VIDEO_EXTENSIONS = (
    '.mkv', '.avi', '.mov', '.mp4', '.flv', '.wmv', '.ts', '.m2ts', '.mts'
)

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
        # Check for crf=0 with ffprobe is tricky; assume not lossless if h264
        # So treat h264 as lossy unless known otherwise
        return False
    return False

def convert_to_lossless(input_path):
    """Convert video to lossless H.264 (crf 0) and FLAC audio in MKV container"""
    output_path = os.path.splitext(input_path)[0] + '_lossless.mkv'
    print(f"Converting\n  '{input_path}'\nto lossless\n  '{output_path}'")
    cmd = [
        'ffmpeg', '-i', input_path,
        '-c:v', 'libx264', '-preset', 'veryslow', '-crf', '0',
        '-c:a', 'flac',
        output_path
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Conversion finished: {output_path}")
    except subprocess.CalledProcessError:
        print(f"Error converting {input_path}")

def crawl_and_convert(root_dir):
    for dirpath, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(VIDEO_EXTENSIONS):
                full_path = os.path.join(dirpath, file)
                if not is_lossless(full_path):
                    convert_to_lossless(full_path)
                else:
                    print(f"Skipping lossless file: {full_path}")

if __name__ == '__main__':
    media_root = '/media/felix/server'  # Change to your root video directory
    crawl_and_convert(media_root)
