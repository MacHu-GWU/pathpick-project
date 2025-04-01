# -*- coding: utf-8 -*-

from pathpick import api


def test():
    _ = api

    _ = api.PathPick


if __name__ == "__main__":
    from pathpick.tests import run_cov_test

    run_cov_test(
        __file__,
        "pathpick.api",
        preview=False,
    )
