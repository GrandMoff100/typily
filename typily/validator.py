"""Module for validating the type compatibility node by node."""
import ast
from typing import Type

from typily.compatibility import Operation


class Validator:
    """Abstract class for validating a node."""

    def __new__(cls, node: ast.AST) -> "Validator":
        for child in Validator.__subclasses__():
            if isinstance(node, child.node_type):
                return super().__new__(child)
        raise TypeError(f"No validator found for {node.__class__.__name__}.")

    def __init__(self, node: ast.AST) -> None:
        self.node = node

    def __init_subclass__(cls, node_type: Type[ast.AST]) -> None:
        cls.node_type = node_type

    def validate(self) -> None:
        """Check the object type compatibilities for a node type."""
        raise NotImplementedError()

    def get_type(self) -> Type:
        """Get the type of resulting object."""
        raise NotImplementedError()


class ModuleValidator(Validator, node_type=ast.Module):
    """Class for validating Module nodes"""

    def validate(self) -> None:
        for child in self.node.body:
            Validator(child).validate()

    def get_type(self) -> Type:
        pass


class ConstantValidator(Validator, node_type=ast.Constant):
    """Class for validating constant nodes."""

    def validate(self) -> None:
        pass

    def get_type(self) -> Type:
        return type(self.node.value)


class ExpressionValidator(Validator, node_type=ast.Expr):
    """Class for validating expression nodes."""

    def validate(self) -> None:
        Validator(self.node.value).validate()

    def get_type(self) -> Type:
        return Validator(self.node.value).get_type()


class BinOpValidator(Validator, node_type=ast.BinOp):
    """Class for validating binary operation nodes."""

    def validate(self) -> None:
        pass

    def get_type(self) -> Type:
        return Operation(self.node.op).result(
            Validator(self.node.left).get_type(),
            Validator(self.node.right).get_type(),
        )
