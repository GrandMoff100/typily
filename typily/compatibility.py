"""Module for checking compatibility of AST nodes."""

import ast
from typing import Type


class Operation:
    """
    Class for checking operation compatibility of AST nodes.
    """

    def __new__(cls, operation: ast.AST) -> 'Operation':
        for subcls in cls.__subclasses__():
            if subcls.op == operation:
                return super().__new__(subcls)
        raise TypeError(f'No operation found for {operation}.')

    def __init_subclass__(cls, op: ast.AST) -> None:
        cls.op = op

    def result(self, left: Type, right: Type) -> Type:
        """
        Check if the operation is compatible with the given types and return the resulting type.
        """
        raise NotImplementedError()


class Add(Operation, op=ast.Add):
    """
    Class for checking addition compatibility of AST nodes.
    """

    def result(self, left: Type, right: Type) -> Type:
        pass
