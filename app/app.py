"""
Ponto de entrada sugerido para uma aplicação Flask futura.

Este arquivo está pronto para ser adaptado quando você instalar Flask.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


def create_app():
    """
    Função de fábrica compatível com o padrão Flask.
    Quando Flask estiver instalado, você pode adaptar assim:

    from flask import Flask

    app = Flask(
        __name__,
        template_folder=str(TEMPLATES_DIR),
        static_folder=str(STATIC_DIR),
    )

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
    """

    # Placeholder para futura integração com Flask.
    return {
        "templates_dir": str(TEMPLATES_DIR),
        "static_dir": str(STATIC_DIR),
    }

