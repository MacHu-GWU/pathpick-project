# -*- coding: utf-8 -*-

from pathpick.impl import PathPick


class TestPathPick:
    def test_include_exclude_interaction(self):
        # Case 1: Empty include, empty exclude (matches everything)
        pick = PathPick.new(include=[], exclude=[])
        assert pick.is_match("file.txt") is True
        assert pick.is_match("folder/file.py") is True

        # Case 2: Empty include, with exclude (matches everything except excluded)
        pick = PathPick.new(include=[], exclude=["*.txt"])
        assert pick.is_match("file.txt") is False
        assert pick.is_match("file.py") is True

        # Case 3: With include, empty exclude (matches only included)
        pick = PathPick.new(include=["*.py"], exclude=[])
        assert pick.is_match("file.txt") is False
        assert pick.is_match("file.py") is True

        # Case 4: With include, with exclude (exclude takes precedence)
        pick = PathPick.new(include=["*.py"], exclude=["test_*.py"])
        assert pick.is_match("file.py") is True
        assert pick.is_match("test_file.py") is False

        # Case 5: With include, with overlapping exclude (exclude takes precedence)
        pick = PathPick.new(include=["**/*.py"], exclude=["folder/*.py"])
        assert pick.is_match("file.py") is True
        assert pick.is_match("folder/file.py") is False
        assert pick.is_match("other/file.py") is True

        # Case 6: Multiple includes, multiple excludes
        pick = PathPick.new(
            include=["**/*.py", "**/*.md"], exclude=["**/test_*.py", "**/temp/*"]
        )
        assert pick.is_match("file.py") is True
        assert pick.is_match("docs/file.md") is True
        assert pick.is_match("test_file.py") is False
        assert pick.is_match("temp/file.py") is False
        assert pick.is_match("folder/temp/file.md") is False


if __name__ == "__main__":
    from pathpick.tests import run_cov_test

    run_cov_test(
        __file__,
        "pathpick.impl",
        preview=False,
    )
