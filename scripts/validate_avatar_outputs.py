#!/usr/bin/env python3
"""Validate avatar pipeline outputs for the Hunyuan3D pipeline (current format)."""
import argparse
import json
from pathlib import Path


def must_exist(path: Path, label: str):
    if not path.exists():
        raise FileNotFoundError(f"Missing {label}: {path}")
    if path.is_file() and path.stat().st_size == 0:
        raise RuntimeError(f"Empty {label}: {path}")


def main():
    parser = argparse.ArgumentParser(description="Validate avatar pipeline outputs (Hunyuan3D).")
    parser.add_argument("--out-dir", default="outputs/avatar-man-1")
    args = parser.parse_args()

    out_dir = Path(args.out_dir).resolve()
    manifest = out_dir / "manifest.json"
    raw_glb = out_dir / "avatar-man-1_final_raw.glb"
    final_glb = out_dir / "avatar-man-1_final.glb"
    raw_mp4 = out_dir / "avatar-man-1_turntable_raw.mp4"
    tex_dir = out_dir / "textures"
    tex_base = tex_dir / "baseColor.png"
    tex_normal = tex_dir / "normal.png"
    tex_rough = tex_dir / "roughness.png"
    qa_dir = out_dir / "qa"
    qa_board = qa_dir / "comparison_board.png"
    qa_summary = qa_dir / "qa_summary.json"

    must_exist(out_dir, "output directory")
    must_exist(manifest, "manifest.json")
    must_exist(raw_glb, "raw final GLB")

    with manifest.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Hunyuan3D manifest validation (pipeline/texture_status format)
    if "pipeline" not in data:
        raise RuntimeError("Missing 'pipeline' in manifest (expected Hunyuan3D format).")
    if "seed" not in data and "selected_seed" not in data:
        raise RuntimeError("Missing 'seed' or 'selected_seed' in manifest.")
    if "texture_status" not in data:
        raise RuntimeError("Missing 'texture_status' in manifest.")
    if data.get("texture_status") != "PASS":
        raise RuntimeError(
            f"Texture did not pass QA: texture_status={data.get('texture_status')}"
        )

    # The bundle is only considered complete when texture passes and final GLB exists.
    if final_glb.exists():
        must_exist(final_glb, "final baked GLB")
    else:
        # If texture passed but no final GLB, it is an incomplete delivery.
        raise RuntimeError(
            "Texture status is PASS but final GLB is missing. "
            "Delivery bundle is incomplete (bare mesh, no texture baked)."
        )

    # Raw turntable preview is optional in the Hunyuan3D pipeline (not produced by default).
    if raw_mp4.exists():
        must_exist(raw_mp4, "raw turntable")

    # Textures are required when final GLB exists.
    if tex_base.exists() or tex_normal.exists() or tex_rough.exists():
        must_exist(tex_base, "baseColor texture")
        must_exist(tex_normal, "normal texture")
        must_exist(tex_rough, "roughness texture")

    if qa_dir.exists():
        if qa_board.exists():
            must_exist(qa_board, "QA board")
        if qa_summary.exists():
            must_exist(qa_summary, "QA summary")

    print("Validation OK (Hunyuan3D)")
    print(f"Manifest: {manifest}")
    print(f"Pipeline: {data.get('pipeline')}")
    print(f"Texture status: {data.get('texture_status')}")
    print(f"Raw GLB: {raw_glb}")
    print(f"Final GLB: {final_glb}")
    if raw_mp4.exists():
        print(f"Raw turntable: {raw_mp4}")
    if qa_summary.exists():
        print(f"QA summary: {qa_summary}")


if __name__ == "__main__":
    main()
