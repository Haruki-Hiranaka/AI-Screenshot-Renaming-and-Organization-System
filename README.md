# AI Screenshot Renaming and Organization System (SnapSense)

A macOS automation that organizes screenshots into date-based folders and renames them semantically using Gemini Vision (gemini-2.5-flash).

## Features
- Automatically moves screenshots into `~/Desktop/スクリーンショット/YYYY_MM_DD/`
- Renames files based on screenshot content (Japanese, searchable)
- Free-tier compatible (Gemini 2.5 Flash)

## Requirements
- macOS (Automator)
- Python 3.10+
- Gemini API Key (Google AI Studio)

## Install
1) Clone this repo
2) Install dependencies:
   - `pip3 install -r requirements.txt`
3) Set your API key (recommended):
   - `export GEMINI_API_KEY_FOR_AI_SCREENSHOT_RENAMING_SYSTEM="YOUR_KEY"`
4) Create a Folder Action in Automator and paste:
   - `automator/folder_action_template.sh`

## Notes
- Do not commit API keys. Keep secrets local.
