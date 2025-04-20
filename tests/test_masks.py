from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(input_error, correct_form_card_number, card_number_variations):
    assert get_mask_card_number("0000000000000000") == correct_form_card_number

    assert get_mask_card_number("0000 0000 0000 0000") == correct_form_card_number

    assert get_mask_card_number(card_number_variations) == input_error


def test_get_mask_account(input_error, correct_form_account_number, account_number_variations):
    assert get_mask_account("00000000000000000000") == correct_form_account_number

    assert get_mask_account("0000 0000 0000 0000 0000") == correct_form_account_number

    assert get_mask_account(account_number_variations) == input_error
