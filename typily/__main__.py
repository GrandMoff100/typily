import astpretty
import ast
import click

from typily.validator import ModuleValidator


@click.command()
@click.argument("file", type=click.File("r"))
@click.option("--show-ast", is_flag=True, help="Print the AST.")
def main(file, show_ast: bool):
    """
    This is a simple program that takes a file and prints out the AST of the file.
    """
    tree = ast.parse(file.read())
    if show_ast:
        astpretty.pprint(tree, show_offsets=False)
    ModuleValidator(tree).validate()


if __name__ == "__main__":
    main()
