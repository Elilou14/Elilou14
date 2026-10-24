# Mise en ligne du profil (5 minutes)

1. **Crée le repo spécial** : sur GitHub, nouveau repository nommé **exactement comme ton identifiant** (ex. `exoliance` si ton profil est github.com/exoliance), public, sans README.
2. **Personnalise** : ouvre `build.py`, modifie le bloc `CONFIG` (identifiant, email, site, LinkedIn, stack, réalisations), puis lance :
   ```bash
   python3 build.py
   ```
   Tout est régénéré : `README.md`, les 16 visuels de `assets/` (sombre + clair) et le workflow.
3. **Envoie les fichiers** à la racine du repo : `README.md`, `assets/`, `.github/workflows/snake.yml` (et `build.py` si tu veux pouvoir régénérer plus tard).
   ```bash
   git init && git add . && git commit -m "Profil Exoliance"
   git branch -M main
   git remote add origin https://github.com/TON_ID/TON_ID.git
   git push -u origin main
   ```
4. **Active l'animation des contributions** : onglet *Actions* du repo → « Animation des contributions » → *Run workflow*. Elle crée la branche `output` et se met ensuite à jour toute seule deux fois par jour.
   Si l'action échoue avec une erreur de droits : *Settings → Actions → General → Workflow permissions → Read and write*.

## Bon à savoir
- Les visuels suivent automatiquement le thème clair/sombre du visiteur.
- Les animations sont du SVG pur (CSS + SMIL) : aucun service externe, aucun JavaScript, rien ne peut tomber en panne.
- GitHub met parfois les images en cache quelques minutes après un push : fais Ctrl+F5.
- Pour retirer le serpent : `"snake": False` dans `CONFIG`, puis supprime `.github/workflows/snake.yml`.
- Les couleurs sont dans `PALETTES` (lime `#B8FF3C` / cyan `#3CE3FF` en sombre).
