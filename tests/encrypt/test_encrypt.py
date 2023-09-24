import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError,  match="tipo inválido para message"):
        encrypt_message(1, 2)

    with pytest.raises(TypeError,  match="tipo inválido para key"):
        encrypt_message("Katia", "a")

    assert_invalid_index = encrypt_message("Katia", 9)
    assert assert_invalid_index == "aitaK"

    assert_odd_key = encrypt_message("Katia", 3)
    assert assert_odd_key == "taK_ai"

    assert_pair_key = encrypt_message("Katia", 2)
    assert assert_pair_key == "ait_aK"
