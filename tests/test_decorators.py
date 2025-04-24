import pytest


def test_log_without_args(capsys):
    def say_one():
        print("one")

    say_one()
    result = capsys.readouterr()

    assert result.out == "one\n"




