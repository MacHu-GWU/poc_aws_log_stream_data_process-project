# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import poc_aws_log_stream_data_process
    pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
