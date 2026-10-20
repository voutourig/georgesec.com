# georgesec.com

Personal site of George Voutouris. Built with [Hugo](https://gohugo.io) and the
[Terminal](https://github.com/panr/hugo-theme-terminal) theme (MIT licence, fetched into `themes/terminal` at a pinned commit),
with a custom `whoami` home page. Deployed to GitHub Pages by `.github/workflows/hugo.yml`.

## Run it locally

```bash
git clone https://github.com/panr/hugo-theme-terminal.git themes/terminal
git -C themes/terminal checkout 8ef994c0e0303861b1204d1248541af06c9bfea6
hugo server -D        # http://localhost:1313, -D also shows drafts
hugo --minify         # production build into public/
```

## Add an article

```bash
hugo new articles/my-article-name.md
```

This creates `content/articles/my-article-name.md` from `archetypes/articles.md`. Then:

1. Set the `title`, a short `description` (used on the home page, the list and in link previews) and `tags`.
2. Write the article in Markdown below the front matter.
3. Change `draft: true` to `draft: false` when it is ready, then commit and push to `main`.

To include images, make the article a folder instead:

```bash
hugo new articles/my-article-name/index.md
```

and put the images next to `index.md`, then use `![alt text](image.png)`.

The three newest articles appear on the home page automatically.

## Add a project

```bash
hugo new projects/my-project.md
```

Fill in `description`, `tags` and `repo` (the GitHub link). Set `featured: true` to show it under
Featured projects on the home page. If nothing is featured, the newest projects are shown.

## Where things live

| Path | What it is |
| --- | --- |
| `layouts/index.html` | Home page with the `whoami` terminal |
| `layouts/partials/header.html` | Header: the ASCII banner is the logo (large on home, compact on inner pages) plus the nav menu |
| `content/about.md` | About page |
| `layouts/partials/head.html` | SEO, Open Graph and favicon tags |
| `assets/css-site/site.css`, `static/terminal.css` | Custom styles and colours |
| `static/CNAME` | Custom domain for GitHub Pages |
| `_build/assets.py` | Regenerates favicons and `og-image.png` (uses the banner partial, so run `banner.py` first) |
| `_build/banner.py` | Regenerates `layouts/partials/banner.html` (ASCII banner, figlet font ANSI Shadow, needs pyfiglet) and `layouts/partials/info.html` (the `=[ georgesec v2026 ]` block) |
| `static/fonts/banner-dejavu-mono.woff2` | Tiny DejaVu Sans Mono subset (block and box characters only) so the banner renders the same everywhere |

## Binary assets

The images and fonts (`static/*.png` and `static/fonts/*.woff2`) are stored
base64-encoded under `.github/binary-assets/`, mirroring their real paths. The deploy workflow decodes them
into place before running Hugo. The real files are also fine to commit directly; if you do, delete the
matching `.b64` copy.
