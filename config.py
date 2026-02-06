"""Configuration file for fileconverter.py"""
VIDEO_EXTENSIONS = (
    '.mkv', '.avi', '.mov', '.mp4', '.flv', '.wmv', '.ts', '.m2ts', '.mts'
)
MEDIA_ROOT = '/media/user/server'  # Change to your root video directory
CONVERSION_SPEED = 'veryslow' # or 'slow', 'medium', for faster encoding