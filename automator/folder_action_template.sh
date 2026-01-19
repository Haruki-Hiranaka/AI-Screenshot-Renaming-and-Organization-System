PYTHON="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"

export GEMINI_API_KEY_FOR_AI_SCREENSHOT_RENAMING_SYSTEM="YOUR_API_KEY"

REPO="$HOME/Desktop/AI Screenshot Renaming and Organization System"
RENAMER="$REPO/scripts/ai_rename.py"

for file in "$@"
do
  DATE=$(date -r "$file" +"%Y_%m_%d")
  DEST="$HOME/Desktop/スクリーンショット/$DATE"
  mkdir -p "$DEST"

  BASENAME=$(basename "$file")
  MOVED_FILE="$DEST/$BASENAME"

  mv "$file" "$MOVED_FILE"

  "$PYTHON" "$RENAMER" "$MOVED_FILE"
done
