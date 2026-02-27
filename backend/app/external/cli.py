import click
from .extract import run_all_extracts
from .transform import run_all_transforms
from .load import run_all_loads

def register_etl_cli(app):
    @app.cli.command("etl")
    @click.option("--step", type=click.Choice(["extract", "transform", "load", "all"]), default="all")
    def etl_external_apis(step):
        if step in ("extract", "all"):
            run_all_extracts()
        if step in ("transform", "all"):
            run_all_transforms()
        if step in ("load", "all"):
            run_all_loads()