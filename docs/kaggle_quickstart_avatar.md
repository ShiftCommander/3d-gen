# Kaggle Quickstart (Avatar 3D)

## But
Produire un bundle `.zip` contenant un GLB 3D depuis `avatar-man-1.png`.

Le chemin Kaggle est Hunyuan3D, car il est plus leger que TRELLIS (retire de ce repo) sur GPU T4 et gere mieux la generation shape + texture.

## Hunyuan3D embedded
Utilise [kaggle_hunyuan3d_avatar_embedded.ipynb](</Users/tim/Code environments/TRELLIS/notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb>).

Ce notebook embarque directement `assets/custom/avatar-man-1.png`, donc il ne depend pas d'un upload d'image Kaggle. Il telecharge le repo Hunyuan3D au runtime, installe les dependances, genere la forme avec `Hunyuan3D-2mini`, puis tente la texture avec `Hunyuan3D-Paint`.

Reglages Kaggle:
1. `Accelerator: GPU`
2. `Internet: ON`
3. `Run All`

Sortie attendue:
```bash
/kaggle/working/outputs/avatar-man-1-hunyuan/avatar-man-1_hunyuan_delivery.zip
```

Le notebook echoue volontairement si `texture_status != PASS`, afin de ne pas confondre un mesh non texture avec une livraison complete.

## Récupérer

Après téléchargement sur le Mac, vérifie le bundle:
```bash
python3 scripts/review_avatar_delivery.py --bundle "/chemin/vers/avatar-man-1_hunyuan_delivery.zip"
```
