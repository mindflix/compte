# compte

- App permettant de gérer l'organisation de la maison et des tâches quotidiennes
- Nécessite Python 3.9, l'app étant basée sur Flask

## Installation

### Cloner le git dans un répertoire :

```console
$ git clone https://github.com/mindflix/compte
```

### Vérifier que Python est bien installé à la version 3.9 :

```console
$ python3 --version
```

### Créer un environnement virtuel :

#### Installation de l'outil

```console
$ pip install virtualenv
```

#### Création de l'environnement (à la racine)

```console
$ virtualenv env
```

Cela permettra de générer un dossier "env" à la racine.

#### Activation de l'environnement

- Pour l'activer :

```console
$ source env/bin/activate
```

- Pour le désactiver :

```console
(env) $ deactivate
```

### Installer les dépendances (avec l'environnement actif !) :

```console
$ pip install -r requirements.txt
```

Cela permettra d'installer les modules requis pour le fonctionnement de l'app, dont Flask.

### Lancement de l'App :

Pour l'instant, l'app est en développement, il faut initialiser 2 paramètres pour la lancer correctement.

#### Initialisation des variables

```console
$ export FLASK_APP=project
$ export FLASK_ENV=development
```

#### Lancer

```console
$ flask run
```
