import shutil
from pathlib import Path

TRAIN_DIR = Path("./Raw")
VAL_DIR = Path("./data/val_hr_tif")
VAL_DIR.mkdir(parents=True, exist_ok=True)

all_tifs = sorted(list(TRAIN_DIR.glob("*.tif")) +
                  list(TRAIN_DIR.glob("*.tiff")))
print("Found in TRAIN_DIR:", len(all_tifs))

if len(all_tifs) == 0:
    print("No TIFFs found in TRAIN_DIR.")
else:
    # Keep at least 1 image for validation
    val_count = max(1, int(round(len(all_tifs) * 0.2)))
    val_files = all_tifs[-val_count:]

    for src in val_files:
        dst = VAL_DIR / src.name
        if not dst.exists():
            shutil.copy2(src, dst)

    print("Copied to VAL_DIR:", len(val_files))
