from dataclasses import dataclass


@dataclass
class Stock:
    no: int
    roe: float
    fcf: float
    grade: str


def metric(roe: float, fcf: float):
    if roe >= 15:
        result = 'A' if (fcf > 0) else 'B1'
    elif roe >= 10:
        result = 'B2' if (fcf > 0) else 'C'
    else:
        result = 'NG'
    return result


