from random import randint

import markovify
from .paragraph import Paragraph


class Chapter(object):
    """
    A chapter
    that contains paragraphs
    written by markov models.
    """

    def __init__(self, model, title):
        if not isinstance(model, markovify.Text):
            raise Exception('model must be a markov model')
        self.model = model
        self.title = 'Chapter %d' % title

    def write_chapter(self):
        """
        Create a chapter
        that contains a random number
        of paragraphs
        """
        self.paragraphs = []
        self.paragraphs.append('\n')
        for x in range(randint(0, 50)):
            p = Paragraph(self.model)
            self.paragraphs.append(p.get_paragraph())
            self.paragraphs.append('\n')
        return self.paragraphs
