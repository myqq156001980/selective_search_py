#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import features

class TestMergeSize:
    def setup_method(self, method):
        dummy_image = numpy.zeros((10, 10, 3), dtype=numpy.uint8)
        dummy_label = numpy.zeros((10, 10), dtype=int)
        self.f = features.Features(dummy_image, dummy_label, 1)

    def test_merge_size(self):
        self.f.size = {0: 10, 1: 20}
        self.f._Features__merge_size(0, 1, 2)
        assert self.f.size[2] == 30

class TestMergeColor:
    def setup_method(self, method):
        dummy_image = numpy.zeros((10, 10, 3), dtype=numpy.uint8)
        dummy_label = numpy.zeros((10, 10), dtype=int)
        self.f = features.Features(dummy_image, dummy_label, 1)

    def test_merge_color(self):
        self.f.color[0] = numpy.array([1.] * 75)
        self.f.size[0]  = 100
        self.f.color[1] = numpy.array([2.] * 75)
        self.f.size[1]  = 50
        self.f._Features__merge_color(0, 1, 2)

        expected = (100 * 1. + 50 * 2.) / (100 + 50)
        assert numpy.array_equal(self.f.color[2], [expected] * 75)
