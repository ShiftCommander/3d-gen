# Avatar Pipeline Decision

## Decision
Use Hunyuan3D as the pipeline for the avatar delivery goal: a textured GLB avatar from one image.

TRELLIS has been removed from this repo. There is no local fallback generator anymore — all avatar
3D generation runs on Colab or Kaggle via the Hunyuan3D notebooks.

## Why Hunyuan3D
- The goal is a textured GLB avatar from one image.
- Hunyuan3D is built as a two-stage mesh + texture pipeline.
- Hunyuan3D-2mini is the best default for Colab/Kaggle T4 because it is lighter.
- Hunyuan3D-2.1 PBR is the quality upgrade path, but it needs substantially more VRAM.

## Where To Run It
- `notebooks/colab_hunyuan3d_avatar.ipynb` for Colab.
- `notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb` for Kaggle.

## Practical Order
1. Run Hunyuan3D on Colab or Kaggle T4.
2. If texture generation fails, keep the shape GLB and retry texture on a higher-VRAM runtime.
3. Review the downloaded delivery bundle locally with `scripts/review_avatar_delivery.py`.
