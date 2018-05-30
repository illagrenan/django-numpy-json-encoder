# -*- encoding: utf-8 -*-
# ! python3

import json

import numpy as np
from django.test import SimpleTestCase

from django_numpy_json_encoder.numpy_encoder import NumpyJSONEncoder


class TodoTestCase(SimpleTestCase):
    def test_numpy_array_is_be_encoded_as_json(self):
        numpy_array = np.array([1, 2, 3])
        json_output = json.dumps(numpy_array, cls=NumpyJSONEncoder)

        self.assertIsInstance(json_output, str)
        self.assertEqual('[1, 2, 3]', json_output)

    def test_complex_structure_is_encoded_as_json(self):
        numpy_array = np.array([1, 2, 3])
        json_output = json.dumps({
            'a': [2, (2, 3, 4), numpy_array],
            'b': [2]
        }, cls=NumpyJSONEncoder)

        self.assertIsInstance(json_output, str)
