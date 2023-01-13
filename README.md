# Helios ros

Dossier présent sur l'ordi embarqué dans catkin_ws/src

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
