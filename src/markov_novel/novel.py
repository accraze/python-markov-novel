from .chapter import Chapter


class Novel(object):
    """
    Writes a bunch of
    Chapters to file
    """

    def __init__(self, markov, chapter_count=1):
        self.chapters = []
        self.markov = markov
        self.chapter_count = chapter_count

    def write(self, novel_title='novel', filetype='txt'):
        """
        Composes chapters
        and writes the novel to a text file
        """
        self._compose_chapters()
        self._write_to_file(novel_title, filetype)

    def _compose_chapters(self):
        """
        Creates a chapters
        and appends them to list
        """
        for count in range(self.chapter_count):
            chapter_num = count + 1
            c = Chapter(self.markov, chapter_num)
            self.chapters.append(c)

    def _write_to_file(self, novel_title, filetype):
        with open('%s.%s' % (novel_title, filetype), 'w') as f:
            for chapter in self.chapters:
                if filetype == 'md':
                    f.write('## ' + chapter.title)
                else:
                    f.write(chapter.title)
                f.write('\n')
                paragraphs = chapter.write_chapter()
                for paragraph in paragraphs:
                    f.write(paragraph)
                    f.write('\n')
