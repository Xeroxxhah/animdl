"""
Fun helpers for the cli.

Credits for the functions:
    create_random_titles: (https://www.ruggenberg.nl/titels.html)
"""

import logging
import re
from random import choice

from ...__version__ import __core__

package_banner = """\
░█████╗░███╗░░██╗██╗███╗░░░███╗██████╗░██╗░░░░░
██╔══██╗████╗░██║██║████╗░████║██╔══██╗██║░░░░░
███████║██╔██╗██║██║██╔████╔██║██║░░██║██║░░░░░
██╔══██║██║╚████║██║██║╚██╔╝██║██║░░██║██║░░░░░
██║░░██║██║░╚███║██║██║░╚═╝░██║██████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝v{}
A highly efficient anime downloader and streamer
""".format(__core__)

URL_REGEX = re.compile(r"(?:https?://)?(?P<base>(?:\S+\.)+[^/]+)/(?:(?:[^/])+/)*(?P<url_end>[^?/]+)")

LANGUAGE = {
    'adjective': ['third', 'obsessed', 'seventh', 'silent', 'blue', 'purple', 'sacred', 'hot', 'lovely', 'captured', 'trembling', 'burning', 'professional', 'first', 'luscious', 'black', 'diamond', 'misty', 'next', 'willing', 'all', 'lonely', 'swollen', 'forgotten', 'no', 'elemental', 'what', 'silver', 'red', 'living', 'last', 'sleeping', 'bloody', 'lost', 'invisible', 'whispering', 'dark', 'white', 'naked', 'which', 'bare', 'hidden', 'fallen', 'dangerous', 'sucking', 'wild', 'ragged', 'licking', 'devoted', 'kissing', 'grey', 'prized', 'green', 'missing', 'silky', 'growing', 'darkest', 'wet', 'rough', 'cracked', 'bold', 'bound', 'slithering', 'unwilling', 'vacant', 'delicious', 'dying', 'only', 'erect', 'some', 'smooth', 'absent', 'eager', 'playful', 'silken', 'falling', 'laughing', 'broken', 'entwined', 'rising', 'hard', 'sharp', 'dwindling', 'each', 'splintered', 'silvery', 'stolen', 'wanton', 'final', 'twinkling', 'cold', 'weeping', 'stripped', 'magnificent', 'ravaged', 'deep', 'frozen', 'shadowy', 'emerald', 'azure', 'every'],
    'noun': ['dream', 'dreamer', 'dreams', 'waves', 'sword', 'kiss', 'sex', 'lover', 'slave', 'slaves', 'pleasure', 'servant', 'servants', 'snake', 'soul', 'touch', 'men', 'women', 'gift', 'scent', 'ice', 'snow', 'night', 'silk', 'secret', 'secrets', 'game', 'fire', 'flame', 'flames', 'husband', 'wife', 'man', 'woman', 'boy', 'girl', 'truth', 'edge', 'boyfriend', 'girlfriend', 'body', 'captive', 'male', 'wave', 'predator', 'female', 'healer', 'trainer', 'teacher', 'hunter', 'obsession', 'hustler', 'consort', 'dream', 'dreamer', 'dreams', 'rainbow', 'dreaming', 'flight', 'flying', 'soaring', 'wings', 'mist', 'sky', 'wind', 'winter', 'misty', 'river', 'door', 'gate', 'cloud', 'fairy', 'dragon', 'end', 'blade', 'beginning', 'tale', 'tales', 'emperor', 'prince', 'princess', 'willow', 'birch', 'petals', 'destiny', 'theft', 'thief', 'legend', 'prophecy', 'spark', 'sparks', 'stream', 'streams', 'waves', 'sword', 'darkness', 'swords', 'silence', 'kiss', 'butterfly', 'shadow', 'ring', 'rings', 'emerald', 'storm', 'storms', 'mists', 'world', 'worlds', 'alien', 'lord', 'lords', 'ship', 'ships', 'star', 'stars', 'force', 'visions', 'vision', 'magic', 'wizards', 'wizard', 'heart', 'heat', 'twins', 'twilight', 'moon', 'moons', 'planet', 'shores', 'pirates', 'courage', 'time', 'academy', 'school', 'rose', 'roses', 'stone', 'stones', 'sorcerer', 'shard', 'shards', 'slave', 'slaves', 'servant', 'servants', 'serpent', 'serpents', 'snake', 'soul', 'souls', 'savior', 'spirit', 'spirits', 'voyage', 'voyages', 'voyager', 'voyagers', 'return', 'legacy', 'birth', 'healer', 'healing', 'year', 'years', 'death', 'dying', 'luck', 'elves', 'tears', 'touch', 'son', 'sons', 'child', 'children', 'illusion', 'sliver', 'destruction', 'crying', 'weeping', 'gift', 'word', 'words', 'thought', 'thoughts', 'scent', 'ice', 'snow', 'night', 'silk', 'guardian', 'angel', 'angels', 'secret', 'secrets', 'search', 'eye', 'eyes', 'danger', 'game', 'fire', 'flame', 'flames', 'bride', 'husband', 'wife', 'time', 'flower', 'flowers', 'light', 'lights', 'door', 'doors', 'window', 'windows', 'bridge', 'bridges', 'ashes', 'memory', 'thorn', 'thorns', 'name', 'names', 'future', 'past', 'history', 'something', 'nothing', 'someone', 'nobody', 'person', 'man', 'woman', 'boy', 'girl', 'way', 'mage', 'witch', 'witches', 'lover', 'tower', 'valley', 'abyss', 'hunter', 'truth', 'edge'],
}

LABELS = {
    'storage.googleapis.com': "Google API Storage",
}


def create_random_titles():
    
    adjs = LANGUAGE.get('adjective')
    noun = LANGUAGE.get('noun')
    
    return [
        "%s-%s" % (choice(adjs), choice(noun)),
        "the-%s-%s" % (choice(adjs), choice(noun)),
        "%s-%s" % (choice(noun), choice(noun)),
        "the-%s's-%s" % (choice(noun), choice(noun)),
        "the-%s-of-the-%s" % (choice(noun), choice(noun)),
        "%s-in-the-%s" % (choice(noun), choice(noun)),
    ]

def to_stdout(message, caller='animdl', *, color_index=36):
    if caller:
        message = "[\x1b[{}m{}\x1b[39m] ".format(color_index, caller) + message
    return print(message)

def stream_judiciary(url):
    """
    A fun regex to judge urls.
    """
    match = URL_REGEX.search(url)
    if not match:
        return "Unknown"
    
    base, url_end = match.group('base', 'url_end')
    return "'%s' from %s" % (url_end, LABELS.get(base, base))

def bannerify(f):
    def internal(*args, **kwargs):
        quiet_state = kwargs.get('log_level')
        if quiet_state is not None:
            if quiet_state <= 20:
                print("\x1b[35m{}\x1b[39m".format(package_banner))
            logging.basicConfig(level=quiet_state)
        return f(*args, **kwargs)
    return internal
