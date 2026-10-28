# Jonas Mikhaeil — academic website

The static website for https://jonasmikhaeil.github.io/. The public files live directly at the repository root. No build tools, Jekyll, external fonts, or JavaScript dependencies are needed. `.nojekyll` tells GitHub Pages to serve the static files directly.

## Preview locally

Double-click `preview.command` on a Mac with Python 3 installed, or run:

```sh
python3 preview.py
```

Open http://127.0.0.1:8766/. Keep the terminal running, refresh after edits, and press Control-C to stop. This port is separate from the earlier preview on port 8765. The preview serves only the public website files and binds only to this computer.

## Edit

- `index.html`: introduction, research, teaching, and contact details.
- `styles.css`: typography, layout, colors, and the photograph crop.
- `images/jonas-mikhaeil-talk.jpg`: original photograph.
- `files/JonasMikhaeil_CV.pdf`: downloadable CV.
- `files/JonasMikhaeil_IntroductionToStatistics_Notes.pdf`: downloadable lecture notes.

The PDFs are independent copies. After editing an original document, replace its corresponding PDF here, retaining the filename. Update the lecture-note date and page count in `index.html` when needed.

## Publish

Use the existing `master` branch. The GitHub Pages publishing source should be **Deploy from a branch → master → /(root)** in the repository's **Settings → Pages**. Do not select `/docs`; this repository serves the website from its root.

For future edits, review and commit the changes, then push:

```sh
git add -A
git commit -m "Update academic website"
git push origin master
```

A push to the configured publishing branch updates the public site. Check the deployment in GitHub's Actions tab, then open https://jonasmikhaeil.github.io/ and check the photo, navigation, CV, lecture notes, and paper links. GitHub says publishing can take up to ten minutes.

Keep `.nojekyll` in the repository. Do not add application documents, review reports, backup archives, or source folders for the CV and lecture notes.

[GitHub Pages publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
