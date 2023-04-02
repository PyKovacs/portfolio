from flask import Flask, render_template, abort
from typing import List, Dict
import json
import os


app = Flask(__name__)

with open("./portfolio/projects.json", "r") as projects_file:
    projects: List[Dict[str, str | List[str]]] = json.load(projects_file)

slug_to_project = {project["slug"]: project for project in projects}

def create_app():
    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])

    @app.errorhandler(404)
    def page404(error):
        return render_template("404.html"), 404


create_app()
