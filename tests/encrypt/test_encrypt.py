from pytest import raises
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    # Test valid inputs with odd key
    assert encrypt_message("hello world", 5) == "olleh_dlrow "

    # Test valid inputs with even key
    assert encrypt_message("hello world", 6) == "dlrow_ olleh"

    # Test invalid key type
    with raises(TypeError):
        encrypt_message("hello world", "key")

    # Test invalid message type
    with raises(TypeError):
        encrypt_message(1234, 5)

    # Test invalid key value
    assert encrypt_message("hello world", 0) == "dlrow olleh"
    assert encrypt_message("hello world", 100) == "dlrow olleh"


