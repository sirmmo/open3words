

def load_words():
    with open('data/words.txt', 'rb') as fh:
        return fh.readlines()

words = load_words()
base_len = len(words)
print 'BASE LEN', base_len
import math
grid_len = int(math.floor(math.sqrt(base_len)))
print 'GRID LEN', grid_len
print 'GRID LEN SQUARED', grid_len ** 2



from decimal import Decimal

lat, lon = Decimal('52.516272'), Decimal('13.377722')

print lat, lon

abs_lat = lat + 90
abs_lon = lon + 180

print abs_lat, abs_lon
