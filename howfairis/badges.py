from typing import Optional


class Badges:
    """Container for the BADGES of a repository

    Args:
        text: A json blob containing the badges

    Attributes:
        text (str, None): json blob with all badges
    """

    def __init__(self, text: Optional[str] = None):

        self.text = text

    def __eq__(self, other):
        return \
            self.text == other.text
