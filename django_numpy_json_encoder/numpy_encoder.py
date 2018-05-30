# -*- encoding: utf-8 -*-
# ! python3

import numpy as np
from django.core.serializers.json import DjangoJSONEncoder


class NumpyJSONEncoder(DjangoJSONEncoder):
    """
    Subclass of :class:`~DjangoJSONEncoder` [1] that can encode `np.ndarray` as standard list.


    Ref:

        [1] https://docs.djangoproject.com/en/2.0/topics/serialization/#djangojsonencoder

    Credits:

        https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    """

    def default(self, o):
        # noinspection PyUnresolvedReferences
        if isinstance(o, np.ndarray):
            return o.tolist()

        return super().default(o)


NumpyEncoder = NumpyJSONEncoder
