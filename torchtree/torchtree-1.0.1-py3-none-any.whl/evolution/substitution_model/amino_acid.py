import torch

from ...typing import ID
from .general import EmpiricalSubstitutionModel


class LG(EmpiricalSubstitutionModel):
    def __init__(self, id_: ID):
        # fmt: off
        frequencies = torch.tensor(
            [0.079066, 0.012937, 0.053052, 0.071586, 0.042302, 0.057337, 0.022355,
             0.062157, 0.064600, 0.099081, 0.022951, 0.041977, 0.044040, 0.040767,
             0.055941, 0.061197, 0.053287, 0.069147, 0.012066, 0.034155, ])
        rates = torch.tensor(
            [2.489084, 0.395144, 1.038545, 0.253701, 2.066040, 0.358858, 0.149830,
             0.536518, 0.395337, 1.124035, 0.276818, 1.177651, 0.969894, 0.425093,
             4.727182, 2.139501, 2.547870, 0.180717, 0.218959, 0.062556, 0.003499,
             1.105251, 0.569265, 0.640543, 0.320627, 0.013266, 0.594007, 0.893680,
             0.528768, 0.075382, 0.084808, 0.534551, 2.784478, 1.143480, 1.959291,
             0.670128, 1.165532, 5.243870, 0.017416, 0.844926, 0.927114, 0.010690,
             0.282959, 0.015076, 0.025548, 5.076149, 0.394456, 0.523386, 0.123954,
             1.240275, 0.425860, 0.037967, 0.029890, 0.135107, 0.018811, 0.348847,
             0.423881, 0.044265, 1.807177, 0.069673, 0.173735, 0.541712, 0.419409,
             4.128591, 0.363970, 0.611973, 0.604545, 0.245034, 0.077852, 0.120037,
             0.089586, 0.682139, 1.112727, 0.023918, 2.592692, 1.798853, 0.089525,
             0.094464, 0.035855, 0.052722, 0.361819, 0.165001, 0.654683, 2.457121,
             7.803902, 0.311484, 0.008705, 0.296636, 0.044261, 0.139538, 1.437645,
             0.196961, 0.267959, 0.390192, 1.739990, 0.129836, 0.076701, 0.268491,
             0.054679, 0.108882, 0.697264, 0.366317, 0.442472, 4.509238, 0.508851,
             4.813505, 2.426601, 0.990012, 0.584262, 0.119013, 0.597054, 5.306834,
             0.159069, 4.145067, 4.273607, 0.191503, 0.078281, 0.072854, 0.126991,
             0.064105, 1.033739, 10.649107, 0.111660, 0.232523, 0.137500, 0.656604,
             2.145078, 0.390322, 3.234294, 6.326067, 0.748683, 1.136863, 0.185202,
             0.049906, 0.131932, 6.312358, 0.068427, 0.249060, 0.582457, 0.301848,
             0.182287, 0.302936, 1.702745, 0.619632, 0.299648, 0.371004, 0.099849,
             1.672569, 0.484133, 0.346960, 2.020366, 1.898718, 0.696175, 0.481306,
             0.161787, 1.695752, 0.751878, 4.008358, 2.000679, 0.083688, 0.045376,
             0.612025, 0.624294, 0.332533, 1.338132, 0.571468, 0.296501, 0.095131,
             0.089613, 2.807908, 1.223828, 1.080136, 0.210332, 0.236199, 0.257336,
             0.858151, 0.578987, 0.170887, 0.593607, 0.314440, 6.472279, 0.098369,
             0.248862, 0.400547, 2.188158, 0.140825, 0.245841, 0.189510, 0.249313,
             3.151815, ])
        # fmt: on
        super().__init__(id_, rates, frequencies)

    @classmethod
    def from_json(cls, data, dic):
        return cls(data['id'])


class WAG(EmpiricalSubstitutionModel):
    def __init__(self, id_: ID):
        # fmt: off
        frequencies = torch.tensor(
            [0.0866, 0.0193, 0.0570, 0.0581, 0.0384, 0.0833, 0.0244, 0.0485, 0.0620,
             0.0862, 0.0195, 0.0391, 0.0458, 0.0367, 0.0440, 0.0695, 0.0610, 0.0709,
             0.0144, 0.0353, ])
        rates = torch.tensor(
            [1.141050, 0.821500, 1.756410, 0.233492, 1.572160, 0.354813, 0.219023,
             1.005440, 0.443935, 0.989475, 0.569079, 1.594890, 1.011980, 0.610810,
             3.733380, 2.349220, 2.221870, 0.125227, 0.268987, 0.033379, 0.023920,
             0.441300, 0.341086, 0.275403, 0.189890, 0.083649, 0.428414, 0.437393,
             0.296524, 0.122303, 0.109261, 0.585809, 1.560590, 0.570186, 1.114570,
             0.795736, 0.604634, 6.833400, 0.052004, 0.961142, 1.032910, 0.043523,
             0.533362, 0.093930, 0.116813, 6.013660, 0.472601, 0.691268, 0.165074,
             1.192810, 0.417372, 0.169417, 0.146348, 0.363243, 0.092310, 0.630832,
             0.635025, 0.141320, 2.867580, 0.172579, 0.353912, 1.056790, 0.755791,
             6.048790, 0.488649, 0.782467, 0.914814, 0.655045, 0.172682, 0.217549,
             0.055288, 0.756080, 1.177640, 0.098843, 2.348200, 1.320870, 0.110793,
             0.179896, 0.110744, 0.116821, 0.606814, 0.191467, 0.725096, 1.699780,
             7.154480, 0.276379, 0.034151, 0.415992, 0.068651, 0.194220, 1.253910,
             0.273149, 0.366510, 0.650469, 1.486700, 0.251477, 0.209108, 0.374321,
             0.114187, 0.152215, 0.992083, 0.555096, 0.450867, 4.378930, 0.771387,
             4.749460, 2.362040, 0.822459, 0.525511, 0.131869, 0.289998, 4.290350,
             0.360574, 3.517820, 4.714220, 0.615636, 0.111502, 0.131046, 0.206722,
             0.353443, 1.615050, 8.659740, 0.234326, 0.468951, 0.287583, 1.032220,
             3.334390, 0.619503, 4.308310, 5.925170, 1.073780, 1.537920, 0.342012,
             0.152232, 0.147411, 5.375250, 0.147156, 0.462018, 0.964886, 0.551450,
             0.382421, 0.364222, 1.997370, 0.740259, 0.443205, 0.224747, 0.194864,
             1.705070, 0.758446, 0.556353, 1.681970, 2.282020, 0.570369, 0.473810,
             0.217538, 1.716740, 0.711690, 4.394450, 2.257930, 0.221176, 0.078463,
             1.208560, 1.036370, 0.753467, 1.786490, 0.885349, 0.351250, 0.156619,
             0.239607, 3.360330, 1.141210, 0.954144, 0.333890, 0.243615, 0.252457,
             1.357640, 0.613776, 0.280336, 1.294610, 0.423612, 4.847130, 0.258861,
             0.578784, 0.872519, 1.547670, 0.126678, 0.325490, 0.409817, 0.347826,
             2.763540, ])
        # fmt: on
        super().__init__(id_, rates, frequencies)

    @classmethod
    def from_json(cls, data, dic):
        return cls(data['id'])
