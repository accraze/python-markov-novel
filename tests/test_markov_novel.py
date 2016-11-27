import os
import shutil

import markovify

import markov_novel


def test_main():
    """
    Basic functional test
    """
    assert markov_novel
    path = 'tmp'
    os.makedirs(path)
    os.chdir(path)
    # Get raw text as string.
    from os.path import dirname, abspath
    filename = os.path.join(
        dirname(dirname(abspath(__file__))), 'tests/futuristmanifest.txt')
    with open(filename) as f:
        text = f.read()
    # Build the model.
    text_model = markovify.Text(text)
    novel = markov_novel.Novel(text_model, chapter_count=1)
    novel.write(novel_title='my-novel', filetype='md')
    assert os.path.exists(os.path.join(os.getcwd(), 'my-novel.md'))
    os.chdir(os.pardir)
    shutil.rmtree('tmp', ignore_errors=True)
