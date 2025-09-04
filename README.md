# Hackathon
SkipAIlh propose "skoazell slide"
Moteur de création de matériel pédagogique (diapos) dans une langue sous-dotée (breton).


## Vendre le système

### Motivation:

- Aide à l'enseignement d'une langue sous-dotée <graph 1> (généré sur ELG dasboard, 04/09/2025)
- Augmenter le corpus disponible par récupération de texte de qualité (avec consentement explicite)
- Faciliter les contributions Wikipédia en breton

### Déontologie (D'abord ne pas nuire)
- Désirabilité des outils numériques établie (Plan de réappropriation des langues de Bretagne 2024-2027; avalisé par le Conseil culturel de Bretagne; 2 décembre 2023)
- Réduction d'écart numérique entre langues en bilinguisme (présupposé d'acculturation à l'outil > bas impact sur les usages culturels)
- Pas de pollution linguistique: l'outil s'adresse explicitement aux enseignant.es brittophones
- Pas de concurrence avec nos utilisateurs: hors circuit de financement public (Région, Département)
- Soutien dev, promotion sociale et maintien pressenti > fond de dotation Breizh Niverel, dans le cadre de leur réponse BPI France

### Explication du système (Comment ça marche ?)

- Ce que fait le système maintenant ?
- Les applications possibles (Enrichir wikipedia):
    - Utiliser l'outil/ la démo pour produire des données pour enrichir les corpus.

### Roadmap (Futures perspectives - Fonctionalités)

- Filtration
- Slides données par qqn d'autres
- Templating des slides:
    - Méta Rêquetes pour faire des slides.

## Lancer l'interface (Gradio)

Prérequis: Python 3.10+.

1. Installer les dépendances: `uv sync`
2. Démarrer l'app: `uv run main.py`
3. Ouvrir l'URL locale affichée pour utiliser l'éditeur de diapositives.

Fonctions clés:
- Panneau gauche: liste des slides, bouton ➕ pour ajouter, bouton «Save All» pour télécharger une archive `.zip` de toutes les diapositives.
- Panneau droit: champs «Title» et «Content (Markdown)», aperçu en direct, «Save» pour mémoriser la diapositive sélectionnée, «Download» pour exporter la diapositive courante en `.md`.

### Charger des données JSON

Utiliser le champ «Load JSON» pour importer un fichier `.json` au format:

```json
{"query": "Breizh", "md_text": "## HERE THE MARKDOWN TEXT", "Metadata": {"source": "..."}}
```

- `query` → titre de la diapositive
- `md_text` → contenu Markdown
- `Metadata` (optionnel) est stocké avec la diapositive et inclus dans `slides.json` lors de «Save All».

Le chargeur accepte aussi une liste de tels objets.
