import random
import secrets

# Define the elliptic curve parameters y^2 = x^3 + ax + b
a = 0
b = 7
p = 2 ** 256 - 2 ** 32 - 977 # Prime number
Gx = 5506626302227734366957871889516853432625060345377759417550018736038911672924053
Gy = int((Gx ** 3 + a * Gx + b) ** 0.5) 

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def add(self, other):
    if self.x == other.x and self.y == other.y:
      return self.double()
    
    slope = (other.y - self.y) * modInverse(other.x - self.x, p)
    x3 = (slope ** 2 - self.x - other.x) % p
    y3 = (slope * (self.x - x3) - self.y) % p
    return Point(x3, y3)

  def double(self):
    slope = (3 * self.x ** 2 + a) * modInverse(2 * self.y, p)
    x3 = (slope ** 2 - 2 * self.x) % p
    y3 = (slope * (self.x - x3) - self.y) % p
    return Point(x3, y3)

  def multiply(self, scalar):
    u = self
    v = Point(0, 1)
    k = scalar
    if k == 0:
      return 0
    elif k == 1:
      return u
    elif k % 2 == 1:
      return v.add(u)
    else:
      return u.double()
    
def modInverse(a, m):
  x, y, u, v = 0, 1, 1, 0
  while a != 0:
    q = m // a
    r = m % a
    newx = u - q * x
    newy = v - q * y
    x, y, u, v = newx, newy, x, y
    a, m = r, a
  inv = x if x >= 0 else x + m
  return inv

def generateRandomBigInt():
  hexString = ''
  for i in range(64):
    hexString += hex(random.randint(0, 15))[2:]
  return int(hexString, 16)

def generateKeyPair():
  privateKey = secrets.randbits(256)
  publicKey = Point(Gx, Gy).multiply(privateKey)
  return {
    "privateKey": privateKey,
    "publicKey": publicKey
  }

def encrypt(publicKey, message):
  k = generateRandomBigInt()
  if k >= p:
    raise Exception("Random number k is out of range")
  
  C1 = Point(Gx, Gy).multiply(k)
  C2 = message ^ publicKey.multiply(k).x
  return {
    "C1": C1,
    "C2": C2
  }

def decrypt(privateKey, ciphertext):
  C1 = ciphertext["C1"]
  C2 = ciphertext["C2"]
  S = C1.multiply(privateKey)
  message = C2 ^ S.x
  return message


# keyPair = generateKeyPair()
# print("Private key:", hex(keyPair["privateKey"]))
# print("Public key x:", hex(keyPair["publicKey"].x))
# print("Public key y:", hex(keyPair["publicKey"].y))

# message = 123456789
# print("Original message:", message)

# ciphertext = encrypt(keyPair["publicKey"], message)
# print("Ciphertext C1 x:", hex(ciphertext["C1"].x))
# print("Ciphertext C1 y:", hex(ciphertext["C1"].y))
# print("Ciphertext C2:", hex(ciphertext["C2"]))

# decryptedMessage = decrypt(keyPair["privateKey"], ciphertext)
# print("Decrypted message:", decryptedMessage)