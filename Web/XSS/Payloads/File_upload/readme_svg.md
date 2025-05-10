# XSS Image Upload - Test

## Objectif
Tester les différentes combinaisons de **Content-Type** pour identifier celles qui déclenchent l'exécution d'un payload XSS via l'upload de fichier image (par exemple, pour un champ de profil/avatar).

### Tableau de tests

| Test # | File Extension        | Content-Type              | Payload Exécuté ? | Affichage (img/iframe/other) | Remarques                                   |
|--------|-----------------------|---------------------------|--------------------|-------------------------------|---------------------------------------------|
| 1      | test.svg              | image/svg+xml             | Oui                | Inline ou via `<iframe>`      | Cas nominal pour SVG                        |
| 2      | test.svg              | image/jpeg                | Oui (parfois)      | Inline ou via `<iframe>`      | MIME sniffing permet l'exécution du payload |
| 3      | test.svg              | image/png                 | Oui (parfois)      | Inline ou via `<iframe>`      | Même comportement que pour JPEG             |
| 4      | test.svg              | application/octet-stream  | Oui (parfois)      | Inline ou via `<iframe>`      | Format générique qui peut être accepté      |
| 5      | test.svg              | text/plain                | Oui                | Inline ou via `<iframe>`      | Peut contourner certains filtres            |
| 6      | test.jpg (SVG inside) | image/jpeg                | Oui (parfois)      | Inline ou via `<iframe>`      | SVG camouflé sous extension `.jpg`          |
| 7      | test.png (SVG inside) | image/png                 | Oui (parfois)      | Inline ou via `<iframe>`      | SVG camouflé sous extension `.png`          |

### Payload recommandé pour les tests

#### Payload simple avec `onload` :

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert('XSS')"/>
```
