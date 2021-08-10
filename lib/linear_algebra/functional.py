from .tensor import Tensor


def get_codirectional(x: Tensor, y: Tensor):
    if Tensor.are_collinear(x, y):
        c = x[0] / y[0]
        return (-x, -y) if c < 0 else (x, y)
    return x, y
