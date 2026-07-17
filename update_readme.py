import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

how_to_use = """
## How to Use It (The Easiest Way)

As a user, the easiest way to generate a 3D avatar is by leveraging cloud notebooks (so you don't need an expensive local GPU). Here is the step-by-step process:

1. **Generate the Avatar in the Cloud:**
   - Open either the [Google Colab notebook](notebooks/colab_hunyuan3d_avatar.ipynb) or the [Kaggle notebook](notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb) in your browser.
   - Upload a single reference photo of yourself and follow the notebook's simple execution steps.
   - Wait for it to complete. The notebook runs on free cloud GPUs and will output a `.zip` delivery bundle (e.g. `avatar-man-1_delivery.zip`).
   - Download this generated `.zip` bundle to your local computer.

2. **Review the Generated Avatar Locally:**
   - Once the `.zip` is on your machine, you can quickly review its contents (quality assurance boards, turntable preview, GLB files) using the local review script without needing any heavy software:
     ```bash
     python3 scripts/review_avatar_delivery.py --bundle "/path/to/avatar_hunyuan_delivery.zip"
     ```
   - *Optional:* If you wish to manually clean up or bake the final textures, and you have Blender installed locally, use the provided cleanup script:
     ```bash
     blender -b -P scripts/blender_cleanup_bake.py -- --input-glb /path/to/avatar_final_raw.glb --out-glb /path/to/avatar_final.glb --tex-dir /path/to/textures --texture-size 2048
     ```
"""

content = content.replace("---", f"---\n{how_to_use}")

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
