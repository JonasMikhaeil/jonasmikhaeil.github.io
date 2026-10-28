#!/usr/bin/env python3
"""Preview the public website files locally without serving repository metadata."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8766


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404, "File not found")
        return None

    def is_public_file(self):
        request_path = unquote(urlsplit(self.path).path)
        if request_path == "/":
            request_path = "/index.html"
        candidate = (SITE / request_path.lstrip("/")).resolve()
        try:
            relative = candidate.relative_to(SITE)
        except ValueError:
            return False
        allowed = relative.as_posix() in {"index.html", "styles.css", ".nojekyll"}
        allowed = allowed or bool(relative.parts and relative.parts[0] in {"files", "images"})
        return allowed and candidate.is_file()

    def do_GET(self):
        if self.is_public_file():
            super().do_GET()
        else:
            self.send_error(404, "File not found")

    def do_HEAD(self):
        if self.is_public_file():
            super().do_HEAD()
        else:
            self.send_error(404, "File not found")


if __name__ == "__main__":
    handler = partial(PreviewHandler, directory=str(SITE))
    try:
        server = ThreadingHTTPServer((HOST, PORT), handler)
    except OSError as error:
        raise SystemExit(
            f"Could not start the preview: {error}\n"
            f"Stop the other preview using port {PORT}, then try again."
        )
    print(f"Local preview: http://{HOST}:{PORT}/", flush=True)
    print("Refresh the browser after edits. Press Control-C to stop.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
