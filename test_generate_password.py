from app2 import generate_password

def test_generate_password(mocker):
    mock_choice = mocker.patch("app2.random.choice", side_effect=["a", "a", "a", "a", "b", "b", "b", "b"])
    password = generate_password(8)
    mock_choice.assert_called_with("abc123")

    assert mock_choice.call_count == 8
    assert password == "aaaabbbb"