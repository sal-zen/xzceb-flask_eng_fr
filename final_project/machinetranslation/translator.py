from deep_translator import MyMemoryTranslator


# This module provides functions for English to French translation and vice-versa.


def english_to_french(english_text):
    """
    Translate a text in English, given as an input, to French.

    Parameters:
    english_text (str): The text in English to be translated to French.

    Returns:
    str: The text in French that is the translation of the text in English given as an input.
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translate a text in French, given as an input, to English.

    Parameters:
    french_text (str): The text in French to be translated to English.

    Returns:
    str: The text in English that is the translation of the text in French given as an input.
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
