
def load_words():
    with open('data/words.txt', 'rb') as fh:
        return fh.readlines()

import math
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile, zoom)

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/c2w')
def c2w():
  w = load_words()
  lon = float(request.args.get("lon"))
  lat = float(request.args.get("lat"))

  (x,y,z) = deg2num(lon,lat, 20)
  return "%s.%s.%s" % (w[x], w[y], w[z])

def w2c():
  w = load_words()
  words = request.args.get("w").split(".")
  x = w.index(words[0])
  y = w.index(words[1])
  z = w.index(words[2])
  lat,lon = num2deg(x,y,z)
  return "%s, %s" % (lat, lon)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
