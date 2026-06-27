<div align="center">
  <img src="assets/logo.webp" width="100%" alt="TRELLIS Logo">

  <h1>Structured 3D Latents<br>for Scalable and Versatile 3D Generation</h1>

  <p>
    <a href="https://arxiv.org/abs/2412.01506"><img src="https://img.shields.io/badge/arXiv-Paper-red?logo=arxiv&logoColor=white" alt="arXiv"></a>
    <a href="https://microsoft.github.io/TRELLIS/"><img src="https://img.shields.io/badge/Project_Page-Website-green?logo=googlechrome&logoColor=white" alt="Project Page"></a>
    <a href="https://huggingface.co/spaces/Microsoft/TRELLIS"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live_Demo-blue" alt="Hugging Face Demo"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  </p>

  <p>
    <img src="assets/teaser.png" width="100%" alt="Teaser Image">
  </p>
</div>

<span style="font-size: 16px; font-weight: 600;">T</span><span style="font-size: 12px; font-weight: 700;">RELLIS</span> est un grand modèle de génération d'assets 3D. Il prend en entrée des prompts textuels ou visuels (images) et génère des assets 3D de haute qualité dans divers formats, tels que les Champs de Radiance (Radiance Fields), les Gaussiennes 3D (3D Gaussians) et les maillages (meshes). La pierre angulaire de <span style="font-size: 16px; font-weight: 600;">T</span><span style="font-size: 12px; font-weight: 700;">RELLIS</span> est une représentation unifiée de latents structurés (<span style="font-size: 16px; font-weight: 600;">SL</span><span style="font-size: 12px; font-weight: 700;">AT</span>) qui permet un décodage vers différents formats de sortie, associée à des Transformers "Rectified Flow" spécialement conçus pour <span style="font-size: 16px; font-weight: 600;">SL</span><span style="font-size: 12px; font-weight: 700;">AT</span> en tant que puissants backbones.

Nous fournissons des modèles pré-entraînés à grande échelle comprenant jusqu'à 2 milliards de paramètres, entraînés sur un vaste ensemble de données de 500 000 objets 3D divers. <span style="font-size: 16px; font-weight: 600;">T</span><span style="font-size: 12px; font-weight: 700;">RELLIS</span> surpasse considérablement les méthodes existantes, y compris les plus récentes à des échelles similaires, et présente une sélection flexible du format de sortie ainsi que des capacités d'édition 3D locale qui n'étaient pas offertes par les modèles précédents.

***Consultez notre [Page Projet](https://microsoft.github.io/TRELLIS/) pour plus de vidéos et de démos interactives !***

---

## 📑 Table des matières

- [🌟 Fonctionnalités](#-fonctionnalités)
- [📦 Installation](#-installation)
- [🤖 Modèles pré-entraînés](#-modèles-pré-entraînés)
- [💡 Utilisation](#-utilisation)
- [📚 Jeu de données](#-jeu-de-données)
- [🏋️‍♂️ Entraînement](#️-entraînement)
- [⏩ Mises à jour](#-mises-à-jour)
- [🤝 Contribution et Support](#-contribution-et-support)
- [⚖️ Licence](#️-licence)
- [📜 Citation](#-citation)

---

## 🌟 Fonctionnalités

- **Haute Qualité** : Produit des assets 3D variés de haute qualité avec des détails complexes de forme et de texture.
- **Polyvalence** : Accepte des prompts textuels ou des images et peut générer diverses représentations 3D finales, y compris (mais sans s'y limiter) des *Champs de Radiance (Radiance Fields)*, des *Gaussiennes 3D* et des *maillages*, s'adaptant ainsi à diverses exigences en aval.
- **Édition Flexible** : Permet des modifications faciles des assets 3D générés, comme la génération de variantes du même objet ou l'édition locale de l'asset 3D.

---

## 📦 Installation

### Prérequis
- **Système** : Le code est actuellement testé uniquement sur **Linux**. Pour une configuration Windows, vous pouvez consulter le ticket [#3](https://github.com/microsoft/TRELLIS/issues/3) (non entièrement testé).
- **Matériel** : Un GPU NVIDIA avec au moins 16 Go de mémoire est nécessaire. Le code a été vérifié sur des GPU NVIDIA A100 et A6000.
- **Logiciel** :
  - Le [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) est nécessaire pour compiler certains sous-modules. Le code a été testé avec les versions 11.8 et 12.2 de CUDA.
  - [Conda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) est recommandé pour gérer les dépendances.
  - Python version 3.8 ou supérieure est requis.

### Étapes d'installation
1. Clonez le dépôt :
    ```sh
    git clone --recurse-submodules https://github.com/microsoft/TRELLIS.git
    cd TRELLIS
    ```

2. Installez les dépendances :

    **Avant d'exécuter la commande suivante, voici quelques points à noter :**
    - En ajoutant `--new-env`, un nouvel environnement conda nommé `trellis` sera créé. Si vous souhaitez utiliser un environnement conda existant, veuillez retirer ce paramètre.
    - Par défaut, l'environnement `trellis` utilisera PyTorch 2.4.0 avec CUDA 11.8. Si vous souhaitez utiliser une version différente de CUDA (par exemple, si vous avez installé CUDA Toolkit 12.2 et ne souhaitez pas installer une autre version 11.8 pour la compilation des sous-modules), vous pouvez retirer le paramètre `--new-env` et installer manuellement les dépendances requises. Référez-vous à [PyTorch](https://pytorch.org/get-started/previous-versions/) pour la commande d'installation.
    - Si vous avez installé plusieurs versions du CUDA Toolkit, `PATH` doit être défini sur la bonne version avant d'exécuter la commande. Par exemple, si CUDA Toolkit 11.8 et 12.2 sont installés, vous devez exécuter `export PATH=/usr/local/cuda-11.8/bin:$PATH`.
    - Par défaut, le code utilise le backend `flash-attn` pour l'attention. Pour les GPU qui ne supportent pas `flash-attn` (ex. NVIDIA V100), vous pouvez retirer le paramètre `--flash-attn` pour installer uniquement `xformers` et définir la variable d'environnement `ATTN_BACKEND` à `xformers` avant d'exécuter le code. Voir l'[Exemple Minimal](#exemple-minimal) pour plus de détails.
    - L'installation peut prendre un certain temps en raison du grand nombre de dépendances. Veuillez patienter. Si vous rencontrez des problèmes, vous pouvez essayer d'installer les dépendances une par une, en spécifiant un paramètre à la fois.
    - En cas de problème lors de l'installation, n'hésitez pas à ouvrir un ticket ou à nous contacter.

    Créez un nouvel environnement conda nommé `trellis` et installez les dépendances :
    ```sh
    . ./setup.sh --new-env --basic --xformers --flash-attn --diffoctreerast --spconv --mipgaussian --kaolin --nvdiffrast
    ```
    L'utilisation détaillée de `setup.sh` peut être consultée en exécutant `. ./setup.sh --help` :
    ```sh
    Usage: setup.sh [OPTIONS]
    Options:
        -h, --help              Afficher ce message d'aide
        --new-env               Créer un nouvel environnement conda
        --basic                 Installer les dépendances de base
        --train                 Installer les dépendances d'entraînement
        --xformers              Installer xformers
        --flash-attn            Installer flash-attn
        --diffoctreerast        Installer diffoctreerast
        --spconv                Installer spconv
        --mipgaussian           Installer mip-splatting
        --kaolin                Installer kaolin
        --nvdiffrast            Installer nvdiffrast
        --demo                  Installer toutes les dépendances pour la démo
    ```

---

## 🤖 Modèles pré-entraînés

Nous fournissons les modèles pré-entraînés suivants :

| Modèle | Description | #Paramètres | Téléchargement |
| --- | --- | --- | --- |
| TRELLIS-image-large | Grand modèle image-vers-3D | 1.2B | [Télécharger](https://huggingface.co/microsoft/TRELLIS-image-large) |
| TRELLIS-text-base | Modèle de base texte-vers-3D | 342M | [Télécharger](https://huggingface.co/microsoft/TRELLIS-text-base) |
| TRELLIS-text-large | Grand modèle texte-vers-3D | 1.1B | [Télécharger](https://huggingface.co/microsoft/TRELLIS-text-large) |
| TRELLIS-text-xlarge | Très grand modèle texte-vers-3D | 2.0B | [Télécharger](https://huggingface.co/microsoft/TRELLIS-text-xlarge) |

*Remarque : Il est toujours recommandé d'utiliser la version conditionnée par l'image des modèles pour de meilleures performances.*

*Remarque : Tous les VAE sont inclus dans le dépôt du modèle **TRELLIS-image-large**.*

Les modèles sont hébergés sur Hugging Face. Vous pouvez les charger directement dans le code via leur nom de dépôt :
```python
TrellisImageTo3DPipeline.from_pretrained("microsoft/TRELLIS-image-large")
```

Si vous préférez charger le modèle localement, vous pouvez télécharger les fichiers du modèle via les liens ci-dessus et spécifier le chemin du dossier (la structure des dossiers doit être maintenue) :
```python
TrellisImageTo3DPipeline.from_pretrained("/chemin/vers/TRELLIS-image-large")
```

---

## 💡 Utilisation

### Exemple Minimal

Voici un [exemple](example.py) d'utilisation des modèles pré-entraînés pour la génération d'assets 3D.

```python
import os
# os.environ['ATTN_BACKEND'] = 'xformers'   # Peut être 'flash-attn' ou 'xformers', par défaut 'flash-attn'
os.environ['SPCONV_ALGO'] = 'native'        # Peut être 'native' ou 'auto', par défaut 'auto'.
                                            # 'auto' est plus rapide mais effectuera un benchmark au début.
                                            # Il est recommandé de définir sur 'native' si vous n'exécutez qu'une fois.

import imageio
from PIL import Image
from trellis.pipelines import TrellisImageTo3DPipeline
from trellis.utils import render_utils, postprocessing_utils

# Charger une pipeline depuis un dossier local ou depuis Hugging Face
pipeline = TrellisImageTo3DPipeline.from_pretrained("microsoft/TRELLIS-image-large")
pipeline.cuda()

# Charger une image
image = Image.open("assets/example_image/T.png")

# Exécuter la pipeline
outputs = pipeline.run(
    image,
    seed=1,
    # Paramètres optionnels
    # sparse_structure_sampler_params={
    #     "steps": 12,
    #     "cfg_strength": 7.5,
    # },
    # slat_sampler_params={
    #     "steps": 12,
    #     "cfg_strength": 3,
    # },
)
# outputs est un dictionnaire contenant les assets 3D générés sous différents formats :
# - outputs['gaussian']: liste des Gaussiennes 3D
# - outputs['radiance_field']: liste des Champs de Radiance
# - outputs['mesh']: liste des maillages (meshes)

# Rendre les sorties (vidéos)
video = render_utils.render_video(outputs['gaussian'][0])['color']
imageio.mimsave("sample_gs.mp4", video, fps=30)
video = render_utils.render_video(outputs['radiance_field'][0])['color']
imageio.mimsave("sample_rf.mp4", video, fps=30)
video = render_utils.render_video(outputs['mesh'][0])['normal']
imageio.mimsave("sample_mesh.mp4", video, fps=30)

# Des fichiers GLB peuvent être extraits des sorties
glb = postprocessing_utils.to_glb(
    outputs['gaussian'][0],
    outputs['mesh'][0],
    # Paramètres optionnels
    simplify=0.95,          # Ratio de triangles à supprimer lors de la simplification
    texture_size=1024,      # Taille de la texture utilisée pour le GLB
)
glb.export("sample.glb")

# Sauvegarder les Gaussiennes au format PLY
outputs['gaussian'][0].save_ply("sample.ply")
```

Après avoir exécuté le code, vous obtiendrez les fichiers suivants :
- `sample_gs.mp4` : vidéo montrant la représentation Gaussienne 3D
- `sample_rf.mp4` : vidéo montrant la représentation Champ de Radiance (Radiance Field)
- `sample_mesh.mp4` : vidéo montrant la représentation du maillage
- `sample.glb` : fichier GLB contenant le maillage texturé extrait
- `sample.ply` : fichier PLY contenant la représentation Gaussienne 3D


### Démo Web

[app.py](app.py) fournit une démonstration web simple pour la génération d'assets 3D. Cette démo étant basée sur [Gradio](https://gradio.app/), des dépendances supplémentaires sont requises :
```sh
. ./setup.sh --demo
```

Après avoir installé les dépendances, vous pouvez lancer la démo avec la commande suivante :
```sh
python app.py
```

Vous pourrez ensuite y accéder à l'adresse indiquée dans le terminal.


---

## 📚 Jeu de données

Nous mettons à disposition **TRELLIS-500K**, un jeu de données à grande échelle contenant 500 000 assets 3D sélectionnés à partir de [Objaverse(XL)](https://objaverse.allenai.org/), [ABO](https://amazon-berkeley-objects.s3.amazonaws.com/index.html), [3D-FUTURE](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-future), [HSSD](https://huggingface.co/datasets/hssd/hssd-models), et [Toys4k](https://github.com/rehg-lab/lowshot-shapebias/tree/main/toys4k), filtrés en fonction de leurs scores esthétiques. Veuillez vous référer au [README du jeu de données](DATASET.md) pour plus de détails.


---

## 🏋️‍♂️ Entraînement

Le framework d'entraînement de TRELLIS est organisé pour fournir une approche flexible et modulaire de la création et de l'affinage de modèles de génération 3D à grande échelle. Le code d'entraînement s'articule autour de `train.py` et est structuré en plusieurs répertoires afin de séparer clairement le traitement des données, les composants des modèles, la logique d'entraînement et les utilitaires de visualisation.

### Structure du code

- **train.py** : Point d'entrée principal pour l'entraînement.
- **trellis/datasets** : Chargement et prétraitement des jeux de données.
- **trellis/models** : Différents modèles et leurs composants.
- **trellis/modules** : Modules personnalisés pour divers modèles.
- **trellis/pipelines** : Pipelines d'inférence pour différents modèles.
- **trellis/renderers** : Renders pour différentes représentations 3D.
- **trellis/representations** : Différentes représentations 3D.
- **trellis/trainers** : Logique d'entraînement pour différents modèles.
- **trellis/utils** : Fonctions utilitaires pour l'entraînement et la visualisation.

### Configuration de l'entraînement

1. **Préparer l'environnement :**
   - Assurez-vous que toutes les dépendances d'entraînement sont installées.
   - Utilisez un système Linux avec un GPU NVIDIA (les modèles sont entraînés sur des GPU NVIDIA A100).
   - Pour un entraînement distribué, vérifiez que vos nœuds peuvent communiquer via l'adresse et le port maître désignés.

2. **Préparation du jeu de données :**
   - Organisez votre jeu de données de manière similaire à TRELLIS-500K. Spécifiez le chemin de votre jeu de données à l'aide de l'argument `--data_dir` lors du lancement de l'entraînement.

3. **Fichiers de configuration :**
   - Les hyperparamètres d'entraînement et les architectures de modèles sont définis dans les fichiers de configuration sous le répertoire `configs/`.
   - Exemples de fichiers de configuration :

| Config | Modèle Pré-entraîné | Description |
| --- | --- | --- |
| [`vae/ss_vae_conv3d_16l8_fp16.json`](configs/vae/ss_vae_conv3d_16l8_fp16.json) | [Encoder](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/ss_enc_conv3d_16l8_fp16.safetensors) [Decoder](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/ss_dec_conv3d_16l8_fp16.safetensors) | VAE structure clairsemée (Sparse structure) |
| [`vae/slat_vae_enc_dec_gs_swin8_B_64l8_fp16.json`](configs/vae/slat_vae_enc_dec_gs_swin8_B_64l8_fp16.json) | [Encoder](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/slat_enc_swin8_B_64l8_fp16.safetensors) [Decoder](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/slat_dec_gs_swin8_B_64l8gs32_fp16.safetensors) | SLat VAE avec Décodeur Gaussien |
| [`vae/slat_vae_dec_rf_swin8_B_64l8_fp16.json`](configs/vae/slat_vae_dec_rf_swin8_B_64l8_fp16.json) | [Decoder](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/slat_dec_rf_swin8_B_64l8r16_fp16.safetensors) | Décodeur SLat Champ de Radiance |
| [`vae/slat_vae_dec_mesh_swin8_B_64l8_fp16.json`](configs/vae/slat_vae_dec_mesh_swin8_B_64l8_fp16.json) | [Decoder](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/slat_dec_mesh_swin8_B_64l8m256c_fp16.safetensors) | Décodeur SLat Maillage (Mesh) |
| [`generation/ss_flow_img_dit_L_16l8_fp16.json`](configs/generation/ss_flow_img_dit_L_16l8_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/ss_flow_img_dit_L_16l8_fp16.safetensors) | Modèle de Flow structure clairsemée conditionné par image |
| [`generation/slat_flow_img_dit_L_64l8p2_fp16.json`](configs/generation/slat_flow_img_dit_L_64l8p2_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-image-large/blob/main/ckpts/slat_flow_img_dit_L_64l8p2_fp16.safetensors) | Modèle SLat Flow conditionné par image |
| [`generation/ss_flow_txt_dit_B_16l8_fp16.json`](configs/generation/ss_flow_txt_dit_B_16l8_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-text-base/blob/main/ckpts/ss_flow_txt_dit_B_16l8_fp16.safetensors) | Modèle de Flow structure clairsemée conditionné par texte (Base) |
| [`generation/slat_flow_txt_dit_B_64l8p2_fp16.json`](configs/generation/slat_flow_txt_dit_B_64l8p2_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-text-base/blob/main/ckpts/slat_flow_txt_dit_B_64l8p2_fp16.safetensors) | Modèle SLat Flow conditionné par texte (Base) |
| [`generation/ss_flow_txt_dit_L_16l8_fp16.json`](configs/generation/ss_flow_txt_dit_L_16l8_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-text-large/blob/main/ckpts/ss_flow_txt_dit_L_16l8_fp16.safetensors) | Modèle de Flow structure clairsemée conditionné par texte (Large) |
| [`generation/slat_flow_txt_dit_L_64l8p2_fp16.json`](configs/generation/slat_flow_txt_dit_L_64l8p2_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-text-large/blob/main/ckpts/slat_flow_txt_dit_L_64l8p2_fp16.safetensors) | Modèle SLat Flow conditionné par texte (Large) |
| [`generation/ss_flow_txt_dit_XL_16l8_fp16.json`](configs/generation/ss_flow_txt_dit_XL_16l8_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-text-xlarge/blob/main/ckpts/ss_flow_txt_dit_XL_16l8_fp16.safetensors) | Modèle de Flow structure clairsemée conditionné par texte (Extra-large) |
| [`generation/slat_flow_txt_dit_XL_64l8p2_fp16.json`](configs/generation/slat_flow_txt_dit_XL_64l8p2_fp16.json) | [Denoiser](https://huggingface.co/microsoft/TRELLIS-text-xlarge/blob/main/ckpts/slat_flow_txt_dit_XL_64l8p2_fp16.safetensors) | Modèle SLat Flow conditionné par texte (Extra-large) |


### Options de ligne de commande

Le script d'entraînement peut être exécuté comme suit :
```sh
usage: train.py [-h] --config CONFIG --output_dir OUTPUT_DIR [--load_dir LOAD_DIR] [--ckpt CKPT] [--data_dir DATA_DIR] [--auto_retry AUTO_RETRY] [--tryrun] [--profile] [--num_nodes NUM_NODES] [--node_rank NODE_RANK] [--num_gpus NUM_GPUS] [--master_addr MASTER_ADDR] [--master_port MASTER_PORT]

options:
  -h, --help                    Afficher ce message d'aide
  --config CONFIG               Fichier de configuration de l'expérience
  --output_dir OUTPUT_DIR       Répertoire de sortie
  --load_dir LOAD_DIR           Répertoire de chargement, par défaut identique au répertoire de sortie
  --ckpt CKPT                   Étape du checkpoint pour reprendre l'entraînement, par défaut le dernier
  --data_dir DATA_DIR           Répertoire des données
  --auto_retry AUTO_RETRY       Nombre de tentatives en cas d'erreur
  --tryrun                      Essai sans entraînement (Dry run)
  --profile                     Profiler l'entraînement
  --num_nodes NUM_NODES         Nombre de nœuds
  --node_rank NODE_RANK         Rang du nœud
  --num_gpus NUM_GPUS           Nombre de GPU par nœud, par défaut tous
  --master_addr MASTER_ADDR     Adresse maître pour l'entraînement distribué
  --master_port MASTER_PORT     Port pour l'entraînement distribué
```

### Exemples de commandes d'entraînement

#### Entraînement sur un seul nœud

Pour entraîner un modèle de phase 2 (image-vers-3D) sur une seule machine :
```sh
python train.py \
  --config configs/vae/slat_vae_dec_mesh_swin8_B_64l8_fp16.json \
  --output_dir outputs/slat_vae_dec_mesh_swin8_B_64l8_fp16_1node \
  --data_dir /chemin/vers/votre/dataset1,/chemin/vers/votre/dataset2 \
```
Le script distribuera automatiquement l'entraînement sur tous les GPUs disponibles. Spécifiez le nombre de GPUs avec le flag `--num_gpus` si vous voulez limiter le nombre de GPUs utilisés.

#### Entraînement multi-nœuds

Pour entraîner avec plusieurs GPUs sur plusieurs nœuds (par ex. 2 nœuds) :
```sh
python train.py \
  --config configs/generation/slat_flow_img_dit_L_64l8p2_fp16.json \
  --output_dir outputs/slat_flow_img_dit_L_64l8p2_fp16_2nodes \
  --data_dir /chemin/vers/votre/dataset1,/chemin/vers/votre/dataset2 \
  --num_nodes 2 \
  --node_rank 0 \
  --master_addr $MASTER_ADDR \
  --master_port $MASTER_PORT
```
Veillez à ajuster `node_rank`, `master_addr`, et `master_port` pour chaque nœud de manière adéquate.

#### Reprendre l'entraînement

Par défaut, l'entraînement reprendra à partir du dernier point de contrôle (checkpoint) sauvegardé dans le même répertoire de sortie. Pour spécifier un checkpoint précis à partir duquel reprendre, utilisez les flags `--load_dir` et `--ckpt` :
```sh
python train.py \
  --config configs/generation/slat_flow_img_dit_L_64l8p2_fp16.json \
  --output_dir outputs/slat_flow_img_dit_L_64l8p2_fp16_resume \
  --data_dir /chemin/vers/votre/dataset1,/chemin/vers/votre/dataset2 \
  --load_dir /chemin/vers/votre/checkpoint \
  --ckpt [étape]
```

### Options supplémentaires

- **Auto Retry:** Utilisez le flag `--auto_retry` pour spécifier le nombre de tentatives en cas d'erreurs intermittentes.
- **Dry Run:** Le flag `--tryrun` permet de vérifier votre configuration et votre environnement sans lancer un entraînement complet.
- **Profilage:** Activez le profilage avec le flag `--profile` pour obtenir des informations sur les performances d'entraînement et diagnostiquer les goulots d'étranglement.

Ajustez les chemins de fichiers et les paramètres en fonction de votre configuration expérimentale.

---

## ⏩ Mises à jour

**25/03/2025**
- Publication du code d'entraînement.
- Publication des modèles **TRELLIS-text** et de la génération de variantes d'assets.
  - Des exemples sont fournis dans [example_text.py](example_text.py) et [example_variant.py](example_variant.py).
  - Une démo Gradio est disponible dans [app_text.py](app_text.py).
  - *Remarque : Il est toujours recommandé de générer de la 3D à partir de texte en générant d'abord des images via des modèles texte-vers-image, puis d'utiliser les modèles TRELLIS-image pour la génération 3D. Les modèles conditionnés sur texte sont moins créatifs et détaillés en raison des limites des données d'entraînement.*

**26/12/2024**
- Lancement du jeu de données [**TRELLIS-500K**](https://github.com/microsoft/TRELLIS#-dataset) et des boîtes à outils (toolkits) pour la préparation des données.

**18/12/2024**
- Implémentation du conditionnement multi-images pour le modèle **TRELLIS-image** ([#7](https://github.com/microsoft/TRELLIS/issues/7)). Ceci est basé sur un algorithme sans ajustement (tuning-free), cela peut donc ne pas donner les meilleurs résultats pour toutes les images en entrée.
- Ajout de l'exportation des Gaussiennes dans `app.py` et `example.py` ([#40](https://github.com/microsoft/TRELLIS/issues/40)).

---

## 🤝 Contribution et Support

Nous apprécions grandement les contributions à ce projet ! Que ce soit pour signaler un bug, proposer une nouvelle fonctionnalité, améliorer la documentation ou soumettre une Pull Request, n'hésitez pas.

- Pour des problèmes ou des questions spécifiques, veuillez consulter nos [Issues](https://github.com/microsoft/TRELLIS/issues) existantes ou en ouvrir une nouvelle.
- Pour plus d'informations sur notre code de conduite, veuillez consulter le fichier [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- Pour obtenir de l'aide concernant le support technique, consultez [SUPPORT.md](SUPPORT.md).
- Pour des problèmes liés à la sécurité, veuillez vous reporter à [SECURITY.md](SECURITY.md).

---

## ⚖️ Licence

Les modèles TRELLIS et la majorité du code sont sous licence [MIT](LICENSE). Les sous-modules suivants peuvent avoir des licences différentes :
- [**diffoctreerast**](https://github.com/JeffreyXiang/diffoctreerast) : Nous avons développé un moteur de rendu d'octree différentiable en temps réel basé sur CUDA pour le rendu des champs de radiance dans le cadre de ce projet. Ce moteur est dérivé du projet [diff-gaussian-rasterization](https://github.com/graphdeco-inria/diff-gaussian-rasterization) et est disponible sous la [LICENCE](https://github.com/JeffreyXiang/diffoctreerast/blob/master/LICENSE).
- [**Flexicubes (Modifié)**](https://github.com/MaxtirError/FlexiCubes) : Dans ce projet, nous avons utilisé une version modifiée de [Flexicubes](https://github.com/nv-tlabs/FlexiCubes) pour supporter les attributs de vertex. Cette version modifiée est distribuée sous la [LICENCE](https://github.com/nv-tlabs/FlexiCubes/blob/main/LICENSE.txt).

---

## 📜 Citation

Si vous trouvez ce travail utile, merci d'envisager de citer notre article :

```bibtex
@article{xiang2024structured,
    title   = {Structured 3D Latents for Scalable and Versatile 3D Generation},
    author  = {Xiang, Jianfeng and Lv, Zelong and Xu, Sicheng and Deng, Yu and Wang, Ruicheng and Zhang, Bowen and Chen, Dong and Tong, Xin and Yang, Jiaolong},
    journal = {arXiv preprint arXiv:2412.01506},
    year    = {2024}
}
```
