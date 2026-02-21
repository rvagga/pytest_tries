from app import process_files

def test_process_files(mocker):
    mock_sleep = mocker.patch("app.time.sleep")

    result = process_files()

    mock_sleep.assert_called_once_with(3)
    assert result == "processed"

