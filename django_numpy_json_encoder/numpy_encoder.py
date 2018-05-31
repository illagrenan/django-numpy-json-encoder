# -*- encoding: utf-8 -*-
# ! python3

import numpy as np
from django.core.serializers.json import DjangoJSONEncoder

__all__ = ['NumpyJSONEncoder', 'NumpyEncoder']


class NumpyJSONEncoder(DjangoJSONEncoder):
    """
    Subclass of :class:`~DjangoJSONEncoder` [1] that can encode `np.ndarray` as standard list.


    Ref:

        [1] https://docs.djangoproject.com/en/2.0/topics/serialization/#djangojsonencoder

    Credits:

        - https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
        - https://github.com/mpld3/mpld3/issues/434#issuecomment-340255689
    """

    def default(self, o):
        if isinstance(o, (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64)):
            return int(o)
        elif isinstance(o, (np.float_, np.float16, np.float32, np.float64)):
            return float(o)
        # noinspection PyUnresolvedReferences
        elif isinstance(o, np.ndarray):
            return o.tolist()

        return super().default(o)


NumpyEncoder = NumpyJSONEncoder
