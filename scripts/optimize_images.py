import os
import sys
from PIL import Image
import glob

def optimize_images(target_dir, max_size=1600, quality=85):
    """
    Resizes and optimizes all .jpg images in the specified directory.
    """
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    # Support both .jpg and .jpeg
    files = glob.glob(os.path.join(target_dir, "*.jpg")) + glob.glob(os.path.join(target_dir, "*.jpeg"))
    
    if not files:
        print(f"No JPEG files found in {target_dir}")
        return

    print(f"Optimizing {len(files)} images in {target_dir}...")

    for file_path in files:
        try:
            with Image.open(file_path) as img:
                original_size = os.path.getsize(file_path)
                
                # Check if resize is needed
                if img.width > max_size or img.height > max_size:
                    img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                # Save optimized (strips EXIF by default when not explicitly saved)
                img.save(file_path, "JPEG", quality=quality, optimize=True)
                
                new_size = os.path.getsize(file_path)
                reduction = (original_size - new_size) / original_size * 100 if original_size > 0 else 0
                print(f"Optimized {os.path.basename(file_path)}: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB ({reduction:.1f}% reduction)")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/optimize_images.py <directory_path> [max_size] [quality]")
        print("Example: python3 scripts/optimize_images.py static/img/mein-neuer-ordner 1600 85")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
    qual = int(sys.argv[3]) if len(sys.argv) > 3 else 85
    
    optimize_images(dir_path, size, qual)
