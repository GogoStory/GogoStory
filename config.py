from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
MEMORY_DIR = BASE_DIR / "memory"

CYRUS_NAME = "Cyrus"
VERSION = "0.1.0"
OFFLINE_MODE = True
TARGET_CONFIDENCE = 0.80

ENABLE_VOICE = True

VOICE_MODEL_DIR = MODEL_DIR / "vosk"

VOICE_SAMPLE_RATE = 16000

VOICE_ENABLED = True

TTS_ENABLED = True

ENABLE_AUTOMATION = True

AUTOMATION_CONFIDENCE_THRESHOLD = 0.80

ALLOWED_AUTOMATION = [
    "open_application",
    "type_text",
    "move_mouse",
    "click_mouse",
    "press_key",
    "hotkey",
]

REQUIRE_CONFIRMATION_FOR_DANGEROUS_ACTIONS = True
