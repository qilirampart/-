from __future__ import annotations

import shutil
import sys
from pathlib import Path


def _resolve_resource_root() -> Path:
    if getattr(sys, "frozen", False):
        meipass = getattr(sys, "_MEIPASS", "")
        if meipass:
            return Path(meipass)
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parents[2]


def _resolve_app_root(resource_root: Path) -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return resource_root


RESOURCE_ROOT = _resolve_resource_root()
APP_ROOT = _resolve_app_root(RESOURCE_ROOT)
PROJECT_ROOT = APP_ROOT
IS_PACKAGED_BUILD = bool(getattr(sys, "frozen", False))
APP_NAME = "帧析"
APP_ORGANIZATION = "Zhenxi"

ASSETS_DIR = RESOURCE_ROOT / "assets"
DOCS_DIR = RESOURCE_ROOT / "docs"
BUNDLED_RUNTIME_DIR = RESOURCE_ROOT / "runtime"
APP_ICON_PATH = ASSETS_DIR / "app-icon.svg"
USER_GUIDE_PATH = DOCS_DIR / "user-guide.md"

RUNTIME_DIR = APP_ROOT / "runtime"
OCR_MODEL_DIR = RUNTIME_DIR / "models"
OCR_DET_MODEL_DIR = OCR_MODEL_DIR / "text_detection"
OCR_REC_MODEL_DIR = OCR_MODEL_DIR / "text_recognition"
OCR_CLS_MODEL_DIR = OCR_MODEL_DIR / "textline_orientation"
FFMPEG_DIR = RUNTIME_DIR / "ffmpeg"

OUTPUT_DIR = APP_ROOT / "output"
SCREENSHOT_DIR = OUTPUT_DIR / "screenshots"
DOWNLOAD_DIR = OUTPUT_DIR / "downloads"
EXTRACTED_AUDIO_DIR = OUTPUT_DIR / "audio"
TRANSCRIPT_DIR = OUTPUT_DIR / "transcripts"
LOG_DIR = OUTPUT_DIR / "logs"

API_CONFIG_PATH = RUNTIME_DIR / "api_config.json"
DOWNLOADER_CONFIG_PATH = RUNTIME_DIR / "downloader_config.json"
TENCENT_ASR_CONFIG_PATH = RUNTIME_DIR / "tencent_asr_config.json"
API_CONFIG_EXAMPLE_PATH = BUNDLED_RUNTIME_DIR / "api_config.example.json"
DOWNLOADER_CONFIG_EXAMPLE_PATH = BUNDLED_RUNTIME_DIR / "downloader_config.example.json"
TENCENT_ASR_CONFIG_EXAMPLE_PATH = BUNDLED_RUNTIME_DIR / "tencent_asr_config.example.json"

ASR_DIRECT_UPLOAD_LIMIT_BYTES = 5 * 1024 * 1024
ASR_AUDIO_CHUNK_SECONDS = 10 * 60

SUPPORTED_VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".flv",
    ".wmv",
    ".m4v",
}

SUPPORTED_IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".bmp",
}

DEFAULT_STATIC_CANDIDATE_FRAME_COUNT = 5
AVAILABLE_SCROLL_INTERVALS = (2, 3)
DEFAULT_SCROLL_INTERVAL_SECONDS = 2

PREVIEW_RATIO_PRESETS = ("原始", "9:16", "16:9", "1:1", "3:4", "4:3")
DEFAULT_PREVIEW_RATIO = "原始"
DEFAULT_PREVIEW_CANVAS_RATIO = 9 / 16
PREVIEW_MIN_WIDTH = 320
PREVIEW_MIN_HEIGHT = 320
PREVIEW_PLAYER_MIN_HEIGHT = 300
PREVIEW_PLAYER_PREFERRED_HEIGHT = 480
PREVIEW_PLAYER_PADDING = 20
WINDOW_MIN_WIDTH = 1400
WINDOW_MIN_HEIGHT = 860


def ensure_app_directories() -> None:
    for directory in (
        RUNTIME_DIR,
        OUTPUT_DIR,
        SCREENSHOT_DIR,
        DOWNLOAD_DIR,
        EXTRACTED_AUDIO_DIR,
        TRANSCRIPT_DIR,
        LOG_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    _ensure_runtime_scaffold()


def _ensure_runtime_scaffold() -> None:
    bundled_items = (
        (API_CONFIG_EXAMPLE_PATH, RUNTIME_DIR / "api_config.example.json"),
        (DOWNLOADER_CONFIG_EXAMPLE_PATH, RUNTIME_DIR / "downloader_config.example.json"),
        (TENCENT_ASR_CONFIG_EXAMPLE_PATH, RUNTIME_DIR / "tencent_asr_config.example.json"),
    )
    for source_path, target_path in bundled_items:
        if source_path.exists() and not target_path.exists():
            shutil.copy2(source_path, target_path)
