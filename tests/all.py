# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from pathpick.tests import run_cov_test

    run_cov_test(
        __file__,
        "pathpick",
        is_folder=True,
        preview=False,
    )
