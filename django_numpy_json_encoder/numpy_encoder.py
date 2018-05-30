# -*- encoding: utf-8 -*-
# ! python3

import numpy as np
from django.core.serializers.json import DjangoJSONEncoder


class NumpyEncoder(DjangoJSONEncoder):
    """
    Credits: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    """

    def default(self, o):
        if isinstance(o, np.ndarray):
            return o.tolist()

        return super().default(o)
