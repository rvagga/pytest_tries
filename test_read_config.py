from app1 import read_config

def test_read_config(mocker):
    mocked_open = mocker.patch("builtins.open", mocker.mock_open(read_data="host=localhost"))

    result = read_config("config.txt")

    mocked_open.assert_called_once_with("config.txt", "r")
    assert result == "host=localhost"