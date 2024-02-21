# Projet Clubs Sportifs Auvergne-Rhône-Alpes

Ce projet vise à fournir une plateforme complète pour la gestion et l'analyse des données des clubs sportifs de la région Auvergne-Rhône-Alpes. Il est divisé en deux parties principales : l'ETL (Extract, Transform, Load) et le développement web.

## Structure du projet

- **ETL :**
  - `ods_clubs.py` : Script Python pour créer l'ODS (Operational Data Store) des clubs sportifs.
  - `dwh_clubs.py` : Script Python pour créer le DWH (Data Warehouse) des clubs sportifs.

- **Développement Web :**
  - `frontend/` : Contient les fichiers HTML, CSS et JavaScript pour l'interface utilisateur.
  - `backend/` : Contient le code Python du back-end développé avec Django.

## Prérequis

- Python 3.12
- Django
- Pandas
- ...

## Installation

1. Clonez ce dépôt sur votre machine locale :
2. ```bash
git clone https://github.com/votre-utilisateur/nom-du-projet.git
 ```
3. Installez les dépendances Python en exécutant :
```bash
pip install -r requirements.txt
 ```

## Utilisation avec Docker
1. Assurez-vous d'avoir Docker installé sur votre machine.

2. Clonez ce dépôt sur votre machine locale :
git clone https://github.com/votre-utilisateur/nom-du-projet.git
3. Dans le répertoire du projet, construisez l'image Docker en exécutant la commande suivante :
```bash
docker build -t nom-du-projet .
 ```
```bash
docker-compose up
 ```



## Utilisation

1. Pour exécuter l'ETL :
python ods_clubs.py
python dwh_clubs.py


2. Pour lancer le serveur Django :
python manage.py runserver


3. Accédez à l'adresse http://localhost:8000 dans votre navigateur pour utiliser l'application web.

4. La barre de navigation permet de naviguer sur les pages :
- Accueil
- ODS Clubs
- API
- Panel Admin

5. La page d'accueil permet d'afficher certaines données comme
   - le nombre de lignes de l'ODS
   - le nombre de clubs
   - le nombre de fédérations
   - le nombre de lieux
   - 
De plus, le bouton **Mise à jour ODS Clubs** permet de recharger l'ODS et ainsi observer le temps que met le script à **Bulck** les données

## Licence

Ce projet est sous licence MIT.
