# FileConverter **v1.0.0 Pre-release** [![Release](https://img.shields.io/github/v/release?include_prereleases=FHeise0624/FileConverter)](https://github.com/FHeise0624/FileConverter/releases/latest)

FileConverter scans directories recursively and converts video files to **H.264 lossless** for optimal **Jellyfin** streaming. Uses FFmpeg while preserving original quality.

**Current status**: Python + FFmpeg subprocess. Optimized for Windows/Linux media servers.

**🚨 PRE-RELEASE NOTICE**: Edit `media_root` path (line ~70) before first run. v1.1.0 adds config file.

## ✨ Features
- Recursively crawls video files (MKV, AVI, MOV, MP4, etc.)
- Detects existing lossless H.264 files (skips redundant work)
- Converts to **H.264 CRF 0 + FLAC** in MKV container
- Compatible with Jellyfin, Plex, streaming servers

## 📋 Requirements
- Python 3.8+
- FFmpeg in PATH (`winget install Gyan.FFmpeg` / `apt install ffmpeg`)
- ffprobe (included with FFmpeg)


## 🛣️ Roadmap
| Version | Feature | Status |
|---------|---------|--------|
| **v1.0.0** | Python base (pre-release) | ✅ [Download](https://github.com/FHeise0624/FileConverter/releases/tag/v1.0.0) |
| **v1.1.0** | Parallel processing + config file | 📋 Planned | 
| **v2.0.0** | **C++ (5x faster)** | 📋 Planned |
| **v2.1.0** | GUI | 📋 Planned |


## 🚀 Quick Start

### Option 1. Download Pre-release
[![Download v1.0.0](https://github.com/FHeise0624/FileConverter/releases/latest/download/fileconverter.py)]() 👈

### Option 2: Git Clone
1.  Git Clone
```
git clone https://github.com/FHeise0624/FileConverter.git
cd FileConverter
```

**Both options require the next step**  

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
* **Slow conversion:** Use a faster preset (```medium``` 3-5x faster) or upgrade the hardware. You can alternatively use a more powerful device in your network with access to the media drive of your server for the conversion.

### Pro tip for Jellyfin users:
Point your library at the ```_lossless``` output files for maximum compatibility across devices (Raspberry Pi, TVs, mobile).

## 📄 License
MIT License - see LICENSE © Felix Heise

