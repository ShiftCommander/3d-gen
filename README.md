# Avatar 3D Pipeline

Photo-to-textured-GLB avatar generation, plus HeyGen avatar identity files for video avatars.

*[Lire en français](README_fr.md)*

---

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


## What's Here

This repo has two independent pieces:

1. **3D avatar generation** — turn a single reference photo into a textured 3D avatar (`.glb`),
   using [Hunyuan3D](https://github.com/Tencent/Hunyuan3D-2) run on free Colab/Kaggle GPUs.
2. **HeyGen avatar identity files** — reference docs (`AVATAR-*.md`) describing photo-based video
   avatars created in HeyGen, for use with the HeyGen API (group ID, voice, look ID).

There is no local GPU pipeline in this repo — generation happens on Colab or Kaggle, then the
delivery bundle is downloaded and reviewed locally.

## 3D Avatar Generation

Start with [docs/avatar_pipeline_decision.md](docs/avatar_pipeline_decision.md) for the pipeline
choice, then [docs/avatar_pipeline_runbook.md](docs/avatar_pipeline_runbook.md) for the full flow.

- **Colab**: [notebooks/colab_hunyuan3d_avatar.ipynb](notebooks/colab_hunyuan3d_avatar.ipynb) —
  see [docs/colab_hunyuan3d_quickstart_avatar.md](docs/colab_hunyuan3d_quickstart_avatar.md)
- **Kaggle**: [notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb](notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb) —
  see [docs/kaggle_quickstart_avatar.md](docs/kaggle_quickstart_avatar.md)

Both notebooks generate the shape with `Hunyuan3D-2mini`, attempt the texture with
`Hunyuan3D-Paint`, and fail on purpose if the texture pass doesn't pass QA — so a bare mesh never
gets mistaken for a finished delivery.

Once you've downloaded a delivery bundle, review it locally:

```bash
python3 scripts/review_avatar_delivery.py --bundle "/path/to/avatar_hunyuan_delivery.zip"
```

Optional manual cleanup/bake pass (requires Blender in `PATH`):

```bash
blender -b -P scripts/blender_cleanup_bake.py -- \
  --input-glb /path/to/avatar_final_raw.glb \
  --out-glb /path/to/avatar_final.glb \
  --tex-dir /path/to/textures \
  --texture-size 2048
```

## HeyGen Avatar Identity Files

`AVATAR-ISABELLE.md` and `AVATAR-LAURENT.md` at the repo root document photo-based HeyGen video
avatars (appearance, voice, `group_id`/`look_id`). `look_id` values are ephemeral — always resolve
them fresh from `group_id` at runtime rather than hardcoding them.

## License

MIT — see [LICENSE](LICENSE). This repo was originally forked from
[microsoft/TRELLIS](https://github.com/microsoft/TRELLIS); the TRELLIS 3D generation engine has
since been removed in favor of the Hunyuan3D-based pipeline above.
