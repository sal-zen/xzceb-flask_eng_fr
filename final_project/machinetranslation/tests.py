import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """
    This class is aimed at testing the functions of the translator module.

    Attributes:
    None

    Methods:
    test_english_to_french(): Test the englishToFrench function of the translator module.
    test_french_to_english(): Test the frenchToEnglish function of the translator module
    """

    def test_english_to_french(self):
        """
        Test function for English to French translation.

        This function tests the translation from English to French using the `englishToFrench` method
        of the translator object.
        It covers different scenarios and expected outcomes to ensure the accuracy and reliability of the translation.

        Parameters:
        self: The instance of the testing class.

        Returns:
        The outcomes of the test functions of the module unittest.TestCase.
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Today I feel awesome!"), "Aujourd'hui il pleut!")

    def test_french_to_english(self):
        """
        Test function for French to English translation.

        This function tests the translation from French to English using the `frenchToEnglish` method
        of the translator object.
        It covers different scenarios and expected outcomes to ensure the accuracy and reliability of the translation.

        Parameters:
        self: The instance of the testing class.

        Returns:
        The outcomes of the test functions of the module unittest.TestCase.
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Je suis heureux"), "I am jacked!")


unittest.main()
