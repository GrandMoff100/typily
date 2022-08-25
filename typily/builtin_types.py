from typing import Any, Callable, Optional


BUILTINS = {
    object: {
        "__or__": Callable[[Any, Any], Any],
        "__eq__": Callable[[Any, Any], bool],
        "__ne__": Callable[[Any, Any], bool],
        "__lt__": Callable[[Any, Any], bool],
        "__le__": Callable[[Any, Any], bool],
        "__gt__": Callable[[Any, Any], bool],
        "__ge__": Callable[[Any, Any], bool],
        "__ror__": Callable[[Any, Any], Any],
        "__str__": Callable[[Any], str],
        "__dir__" : Callable[[Any], list],
        "__doc__": Optional[str],
        "__new__": Callable[[type], Any],
        "__mro__": Callable[[type], list[type]],
        "__repr__": Callable[[Any], str],
        "__init__": Callable[[Any], None],
        "__dict__": dict[str, Any],
        "__hash__": Callable[[Any], int],
        "__call__": Callable[[Any], Any],
        "__base__": Optional[type],
        "__name__": str,
        "__flags__": int,
        "__class__": object,
        "__bases__": tuple[type, ...],
        "__bool__": Callable[[Any], bool],
    },
    int: {
        "__add__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
            Callable[[int, complex], complex],
        ],
        "__sub__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
            Callable[[int, complex], complex],
        ],
        "__mul__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
            Callable[[int, complex], complex],
        ],
        "__truediv__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
            Callable[[int, complex], complex],
        ],
        "__floordiv__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
        ],
        "__mod__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
        ],
        "__pow__": [
            Callable[[int, int], int],
            Callable[[int, float], float],
            Callable[[int, complex], complex],
        ],
        "__lshift__": [Callable[[int, int], int]],
        "__rshift__": [Callable[[int, int], int]],
        "__and__": [Callable[[int, int], int]],
        "__or__": [Callable[[int, int], int]],
        "__xor__": [Callable[[int, int], int]],
        "__radd__": [
            Callable[[int, int], int],
        ],
        "__rsub__": [
            Callable[[int, int], int],
        ],
        "__rmul__": [
            Callable[[int, int], int],
        ],
        "__rtruediv__": [
            Callable[[int, int], int],
        ],
        "__rfloordiv__": [
            Callable[[int, int], int],
        ],
        "__rmod__": [
            Callable[[int, int], int],
        ],
        "__rpow__": [
            Callable[[int, int], int],
        ],
        "__rlshift__": [
            Callable[[int, int], int],
        ],
        "__rrshift__": [
            Callable[[int, int], int],
        ],
        "__rand__": [
            Callable[[int, int], int],
        ],
        "__ror__": [
            Callable[[int, int], int],
        ],
        "__rxor__": [
            Callable[[int, int], int],
        ],
        "__iat__": [Callable[[int, int], int]],
        "__neg__": [Callable[[int], int]],
        "__pos__": [Callable[[int], int]],
        "__abs__": [Callable[[int], int]],
        "__invert__": [Callable[[int], int]],
        "__lt__": [Callable[[int, int], bool]],
        "__le__": [Callable[[int, int], bool]],
        "__eq__": [Callable[[int, int], bool]],
        "__ne__": [Callable[[int, int], bool]],
        "__gt__": [Callable[[int, int], bool]],
        "__ge__": [Callable[[int, int], bool]],
        "__hash__": [Callable[[int], int]],
        "__index__": [Callable[[int], int]],
        "__trunc__": [Callable[[int], int]],
        "__floor__": [Callable[[int], int]],
        "__ceil__": [Callable[[int], int]],
        "__round__": [Callable[[int], int]],
    },
    float: {
        "__add__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__sub__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__mul__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__truediv__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__floordiv__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__mod__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__pow__": [
            Callable[[float, float], float],
            Callable[[float, complex], complex],
        ],
        "__radd__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__rsub__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__rmul__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__rtruediv__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__rfloordiv__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__rmod__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__rpow__": [
            Callable[[float, int], float],
            Callable[[float, float], float],
        ],
        "__neg__": [Callable[[float], float]],
        "__pos__": [Callable[[float], float]],
        "__abs__": [Callable[[float], float]],
        "__invert__": [Callable[[float], float]],
        "__lt__": [Callable[[float, int], bool], Callable[[float, float], bool]],
        "__le__": [Callable[[float, int], bool], Callable[[float, float], bool]],
        "__eq__": [Callable[[float, int], bool], Callable[[float, float], bool]],
        "__ne__": [Callable[[float, int], bool],Callable[[float, float], bool]],
        "__gt__": [Callable[[float, int], bool], Callable[[float, float], bool]],
        "__ge__": [Callable[[float, int], bool], Callable[[float, float], bool]],
        "__hash__": [Callable[[float], int]],
        "__trunc__": [Callable[[float], int]],
        "__floor__": [Callable[[float], int]],
        "__ceil__": [Callable[[float], int]],
        "__round__": [Callable[[float], int]],
    },
    complex: {
        "__add__": [
            Callable[[complex, complex], complex],
            Callable[[complex, float], complex],
            Callable[[complex, int], complex],
        ],
        "__sub__": [
            Callable[[complex, complex], complex],
            Callable[[complex, float], complex],
            Callable[[complex, int], complex],
        ],
        "__mul__": [
            Callable[[complex, complex], complex],
            Callable[[complex, float], complex],
            Callable[[complex, int], complex],
        ],
        "__truediv__": [
            Callable[[complex, complex], complex],
            Callable[[complex, float], complex],
            Callable[[complex, int], complex],
        ],
        "__floordiv__": [],
        "__mod__": [],
        "__pow__": [
            Callable[[complex, complex], complex],
            Callable[[complex, float], complex],
            Callable[[complex, int], complex],
        ],
        "__radd__": [
            Callable[[complex, int], complex],
            Callable[[complex, float], complex],
        ],
        "__rsub__": [
            Callable[[complex, int], complex],
            Callable[[complex, float], complex],
        ],
        "__rmul__": [
            Callable[[complex, int], complex],
            Callable[[complex, float], complex],
        ],
        "__rtruediv__": [
            Callable[[complex, int], complex],
            Callable[[complex, float], complex],
        ],
        "__rfloordiv__": [],
        "__rmod__": [],
        "__rpow__": [
            Callable[[complex, int], complex],
            Callable[[complex, float], complex],
        ],
        "__neg__": [Callable[[complex], complex]],
        "__pos__": [Callable[[complex], complex]],
        "__abs__": [Callable[[complex], complex]],
        "__invert__": [Callable[[complex], complex]],
        "__lt__": [],
        "__le__": [],
        "__eq__": [
            Callable[[complex, complex], bool],
            Callable[[complex, float], bool],
            Callable[[complex, int], bool],
        ],
        "__ne__": [
            Callable[[complex, complex], bool],
            Callable[[complex, float], bool],
            Callable[[complex, int], bool],
        ],
        "__gt__": [],
        "__ge__": [],
        "__hash__": [Callable[[complex], int]],
    },

}
