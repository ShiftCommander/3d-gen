import re

with open('README_fr.md', 'r', encoding='utf-8') as f:
    content = f.read()

how_to_use_fr = """
## Comment l'utiliser (La méthode la plus simple)

En tant qu'utilisateur, la façon la plus simple de générer un avatar 3D est d'utiliser des notebooks dans le cloud (pour éviter d'avoir besoin d'un GPU local coûteux). Voici le processus étape par étape :

1. **Générer l'avatar dans le Cloud :**
   - Ouvrez soit le [notebook Google Colab](notebooks/colab_hunyuan3d_avatar.ipynb) soit le [notebook Kaggle](notebooks/kaggle_hunyuan3d_avatar_embedded.ipynb) dans votre navigateur.
   - Uploadez une seule photo de référence de vous-même et suivez les étapes d'exécution simples du notebook.
   - Attendez la fin du processus. Le notebook s'exécute sur des GPU cloud gratuits et produira une archive `.zip` (par exemple `avatar-man-1_delivery.zip`).
   - Téléchargez cette archive `.zip` générée sur votre ordinateur local.

2. **Examiner l'avatar généré localement :**
   - Une fois le `.zip` sur votre machine, vous pouvez rapidement examiner son contenu (planches d'assurance qualité, aperçu rotatif, fichiers GLB) à l'aide du script d'examen local sans avoir besoin d'un logiciel lourd :
     ```bash
     python3 scripts/review_avatar_delivery.py --bundle "/chemin/vers/avatar_hunyuan_delivery.zip"
     ```
   - *Optionnel :* Si vous souhaitez nettoyer ou *bake* manuellement les textures finales, et que Blender est installé localement, utilisez le script de nettoyage fourni :
     ```bash
     blender -b -P scripts/blender_cleanup_bake.py -- --input-glb /chemin/vers/avatar_final_raw.glb --out-glb /chemin/vers/avatar_final.glb --tex-dir /chemin/vers/textures --texture-size 2048
     ```
"""

content = content.replace("---", f"---\n{how_to_use_fr}")

with open('README_fr.md', 'w', encoding='utf-8') as f:
    f.write(content)
