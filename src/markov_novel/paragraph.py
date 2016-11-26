from random import randint

import markovify


class Paragraph(object):
    """
    Object to hold
    multiple setences created by
    a Markov Model
    """

    def __init__(self, model):
        if not isinstance(model, markovify.Text):
            raise Exception('model must be a markov model')
        self.model = model

    def get_paragraph(self):
        """
        Write a paragraph
        of 5 sentences.
        """
        self.text = ''
        for x in range(randint(5, 12)):
            sentence = self._write_sentence()
            self.text = self.text + sentence
        return self.text

    def _write_sentence(self):
        sentence = None
        while sentence is None:
            sentence = self.model.make_sentence()
        return sentence + ' '
