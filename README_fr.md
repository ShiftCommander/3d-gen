# Pipeline Avatar 3D

Génération d'avatars texturés (.glb) à partir d'une photo, plus des fiches d'identité d'avatars
HeyGen pour la vidéo.

*[Read in English](README.md)*

---

## Contenu du dépôt

Ce dépôt contient deux éléments indépendants :

1. **Génération d'avatar 3D** — transformer une photo de référence en avatar 3D texturé (`.glb`),
   via [Hunyuan3D](https://github.com/Tencent/Hunyuan3D-2) exécuté sur les GPU gratuits de
   Colab/Kaggle.
2. **Fiches d'identité d'avatars HeyGen** — documentation de référence (`AVATAR-*.md`) décrivant
   des avatars vidéo HeyGen créés à partir de photos, pour l'API HeyGen (group ID, voix, look ID).

Il n'y a pas de pipeline GPU local dans ce dépôt — la génération se fait sur Colab ou Kaggle, puis
le bundle de livraison est téléchargé et vérifié localement.

## Génération d'avatar 3D

Commencez par [docs/avatar_pipeline_decision.md](docs/avatar_pipeline_decision.md) pour le choix
du pipeline, puis [docs/avatar_pipeline_runbook.md](docs/avatar_pipeline_runbook.md) pour le
déroulé complet.

- **Colab** : [notebooks/colab_hunyuan3d_avatar.ipynb](notebooks/colab_hunyuan3d_avatar.ipynb) —
  voir [docs/colab_hunyuan3d_quickstart_avatar.md](docs/colab_hunyuan3d_quickstart_avatar.md)
- **Kaggle** : [notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb](notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb) —
  voir [docs/kaggle_quickstart_avatar.md](docs/kaggle_quickstart_avatar.md)

Les deux notebooks génèrent la forme avec `Hunyuan3D-2mini`, tentent la texture avec
`Hunyuan3D-Paint`, et échouent volontairement si la texture ne passe pas le contrôle QA — pour
qu'un maillage non texturé ne soit jamais confondu avec une livraison terminée.

Une fois le bundle téléchargé, vérifiez-le localement :

```bash
python3 scripts/review_avatar_delivery.py --bundle "/chemin/vers/avatar_hunyuan_delivery.zip"
```

Passe de nettoyage/bake manuel optionnelle (nécessite Blender dans `PATH`) :

```bash
blender -b -P scripts/blender_cleanup_bake.py -- \
  --input-glb /chemin/vers/avatar_final_raw.glb \
  --out-glb /chemin/vers/avatar_final.glb \
  --tex-dir /chemin/vers/textures \
  --texture-size 2048
```

## Fiches d'identité d'avatars HeyGen

`AVATAR-ISABELLE.md` et `AVATAR-LAURENT.md` à la racine documentent des avatars vidéo HeyGen
basés sur photo (apparence, voix, `group_id`/`look_id`). Les valeurs de `look_id` sont éphémères —
toujours les résoudre fraîchement depuis `group_id` au moment de l'exécution plutôt que de les
coder en dur.

## Licence

MIT — voir [LICENSE](LICENSE). Ce dépôt provient à l'origine d'un fork de
[microsoft/TRELLIS](https://github.com/microsoft/TRELLIS) ; le moteur de génération 3D TRELLIS a
depuis été retiré au profit du pipeline basé sur Hunyuan3D décrit ci-dessus.
