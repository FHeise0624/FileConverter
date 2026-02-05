# FileConverter [![Release](https://img.shields.io/github/v/release/FHeise0624/FileConverter)](https://github.com/FHeise0624/FileConverter/releases/latest) [![Downloads](https://img.shields.io/github/downloads/FHeise0624/FileConverter/total)](https://github.com/FHeise0624/FileConverter/releases)

FileConverter scans a directory recursively and converts video files to H.264 (lossless) for optimal Jellyfin streaming compatibility. It uses FFmpeg to ensure broad client support while preserving original quality.

## Current status: 
Python implementation using FFmpeg subprocess calls. Optimised for Windows/Linux media servers.

## Features
* Recursively crawls directories for video files (MKV, AVI, MOV, MP4, etc.)
* Detects existing lossless H.264 files to skip redundant conversions
* Converts to lossless H.264 (CRF 0) + FLAC audio in MKV container
*Compatible with Jellyfin, Plex, and most streaming servers

## Requirements
* Python 3.8+
* FFmpeg installed and accessible in PATH (Windows: WinGet Gyan.FFmpeg, Linux: apt install ffmpeg)
* ffprobe (included with FFmpeg)


## 🛣️ Roadmap (Releases)

| Version | Feature | Status |
|---------|---------|--------|
| **v1.0.0** | Python base version | ✅ [Released](https://github.com/FHeise0624/FileConverter/releases/tag/v1.0.0) |
| **v1.1.0** | Parallel processing | 🔄 Preparing |
| **v2.0.0** | **C++ Rewrite** (5x faster) | 🏗️ In development |
| **v2.1.0** | GUI + Config file | 📋 Planned |


## 🚀 Quick Start

### Option 1: Direct Download (recommended)
[![Download latest](https://github.com/FHeise0624/FileConverter/releases/latest/download/fileconverter.zip)]() 👈 **Just download and run**

### Option 2: Git Clone
1.  Git Clone
```
git clone https://github.com/FHeise0624/FileConverter.git
cd FileConverter
```

2. Edit the media path (line ~70):

```
media_root = '/media/user/server'  # Your Jellyfin video directory
```

3. Run:

```
python fileconverter.py
```

Example output: 
```
Converting
  '/media/movies/Action.mkv'
to lossless
  '/media/movies/Action_lossless.mkv'
Conversion finished: /media/movies/Action_lossless.mkv
Skipping lossless file: /media/movies/AlreadyGood.mkv
```

## Technical Details
| Input Formats | Output | Codec Settings |
|---------------|--------|-------------------|
| MKV, AVI, MOV | MKV | H.264 CRF 0 (lossless) |
| MP4, FLV, WMV | MKV | FLAC Audio |

**Lossless check:** Uses ```ffprobe``` to detect FFV1 or skip existing H.264 files.


## Troubleshooting

* **FFmpeg not found:** Add FFmpeg to PATH or set full paths in code
* **Permission errors:** Run as administrator or check directory permissions
* **Slow conversion:** Use a faster preset (```medium```) or upgrade the hardware. You can alternatively use a more powerful device in your network with access to the media drive of your server for the conversion.

### Pro tip for Jellyfin users:
Point your library at the ```_lossless``` output files for maximum compatibility across devices (Raspberry Pi, TVs, mobile).

## 📄 License

[![License](https://img.shields.io/github/license/FHeise0624/FileConverter)](LICENSE)  
MIT License - see [LICENSE](LICENSE) © Felix Heise

