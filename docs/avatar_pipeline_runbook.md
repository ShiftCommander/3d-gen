# Avatar 3D Pipeline Runbook

Pipeline choice is documented in [avatar_pipeline_decision.md](avatar_pipeline_decision.md).

There is no local generation script in this repo — generation runs on Colab or Kaggle via
Hunyuan3D, then the delivery bundle is downloaded and reviewed locally.

## 1) Run Hunyuan3D on Colab or Kaggle

- Colab: open [colab_hunyuan3d_avatar.ipynb](../notebooks/colab_hunyuan3d_avatar.ipynb)
  and follow [colab_hunyuan3d_quickstart_avatar.md](colab_hunyuan3d_quickstart_avatar.md).
- Kaggle: open [kaggle_hunyuan3d_avatar_embedded.ipynb](../notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb)
  and follow [kaggle_quickstart_avatar.md](kaggle_quickstart_avatar.md).

Both notebooks:
- generate the shape with `Hunyuan3D-2mini`
- attempt the texture with `Hunyuan3D-Paint`
- fail on purpose if `texture_status != PASS`, so an untextured mesh never gets mistaken for a
  finished delivery
- produce a downloadable `*_hunyuan_delivery.zip`

## 2) Review the downloaded bundle locally

```bash
python3 scripts/review_avatar_delivery.py --bundle "/path/to/avatar-man-1_hunyuan_delivery.zip"
```

## 3) Optional: Blender cleanup, UV, bake

If you need a manual cleanup/bake pass on the downloaded GLB and Blender is in PATH:

```bash
blender -b -P scripts/blender_cleanup_bake.py -- \
  --input-glb /path/to/avatar-man-1_final_raw.glb \
  --out-glb /path/to/avatar-man-1_final.glb \
  --tex-dir /path/to/textures \
  --texture-size 2048
```

## 4) Validation checklist

- Shape: no major limb/pose artifacts.
- Texture: seams not obvious in medium shot.
- PBR response: cloth/leather/skin roughness separation looks plausible.
- Face fidelity: recognizable in front and 3/4 view.
- Final GLB opens without errors in Blender and web GLB viewers.
