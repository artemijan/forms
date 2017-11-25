"""Bootstrap the application for web serving."""

from backend.app import create_app
from backend.config import CONFIG

app = create_app(config=CONFIG['dev'])

if __name__ == "__main__":
    host, port = ('localhost', 3535)
    app.run(host=host, port=port)
