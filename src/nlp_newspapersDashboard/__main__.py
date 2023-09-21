"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """NLP Newspapers Dashboard."""


if __name__ == "__main__":
    main(prog_name="nlp-newspapersDashboard")  # pragma: no cover
