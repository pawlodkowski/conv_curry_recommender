"""
Module itself also gets a docstring.
"""

import random
from conv_curry_recommender.config import MOVIES


class Recommender:

    """
    Nice little docstring for my class.
    Class -> a paragraph for all my complete sentences
    """

    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f"<Recommender> object for {len(self.items)} items."

    def simple_recommender(self, num: int) -> list:

        """
        Nice little docstring.
        Function -> like the complete sentence!
        """

        result = [i.lower() for i in self.items]
        result = random.choices(result, k=num)
        return result

    def nmf_recommender(self):
        """Not built yet. Please be patient. Coming in Version 2.0, which won't be free. 💰"""
        pass

    def cosim_recommender(self):
        """Not built yet. Please be patient. Coming in Version 2.0, which won't be free. 💰"""
        pass

    def pca_recommender(self):
        """Not built yet. Please be patient. Coming in Version 2.0, which won't be free. 💰"""
        pass


if __name__ == "__main__":
    # run this code below ONLY IF we explicitly call this file, i.e. `python recommender_module.py`
    # DO NOT run this code below, if we are simply importing.

    rec = Recommender(MOVIES)
    result = rec.simple_recommender(4)
    print(result)