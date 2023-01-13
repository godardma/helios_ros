# Helios ros

Dossier présent sur l'ordi embarqué dans catkin_ws/src

## Connexion en ssh au helios

Se connecter au reseau munu_ubnt, puis dans un terminal :

```bash
ssh s100@10.43.20.223
#mot de passe : s100
```

## Utilisation

Ouvrir le port du recepteur GNSS et envoyer les corrections rtk dans un terminal:

```bash
narval_supply_control.py -e usbl
send-rtk-corrections
```

Dans le __name__=="__main__" du fichier suivi_chemin.py, compléter les listes latitudes et longitudes avec celles des waypoints

Dans un autre terminal :

```bash
roscore
```

Dans un dernier terminal :

```bash
ros launch s100 demarrage.launch
# Hors de l'eau pour ne pas utiliser les moteurs :
ros launch s100 sans_moteur.launch
```
