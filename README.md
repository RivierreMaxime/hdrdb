# hdrdb

Site de base de données de films réalisé avec Django dans le cadre de la licence professionnelle informatique à l'université d'Orléans.

### Installation

En premier lieu, cloner ce repository :

```bash
git clone git@github.com:baptistehardy/hdrdb.git hdrdb
cd hdrdb
```

##### Environnement virtuel et paquets requis

- Créer un environnement virtuel (*venv*) et le lancer :
```bash
python3 -m venv [nom du venv]
source [nom du venv]/bin/activate
```

- Installer Django et autres paquets requis :
```bash
pip install -r requirements.txt
```

##### Serveur web Django

- Une fois l'installation terminée, entrer la commande suivante :
```bash
./manage.py runserver
```

Le serveur est alors lancé et le site web est disponible en ouvrant un navigateur web à l'adresse [127.0.0.1:8000](http://127.0.0.1:8000).


### Contributions

This repository is **not** open to contributions as it is a group project made as part of our course.

### dev

```bash
git checkout dev    //aller à la branche 'dev'
git remote -v       //affiche l'origin
git remote add "lien vers le repo"
git add .
git commit -m "commit message"
git push origin dev
```

#### Mise à jour du fork par rapport au master

```bash
git remote add upstream git@github.com:baptistehardy/hdrdb.git
git fetch upstream
git checkout master
git rebase upstream/master
```
