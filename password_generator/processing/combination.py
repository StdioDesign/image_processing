import random, string

def generator(size, keywords):

    size = 16
     
    keywords = "".join(str(x) for x in keywords)

    keywords = keywords.upper() + keywords.lower()

    chars = keywords + string.digits + '!@#$%&*_'

    rnd = random.SystemRandom()

    return ''.join(rnd.choice(chars) for i in range(size))