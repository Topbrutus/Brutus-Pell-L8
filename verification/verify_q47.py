from hashlib import sha256
from pathlib import Path

from sympy import isprime

ROOT = Path(__file__).resolve().parents[1]
Q_TEXT = (ROOT / "data" / "q47.txt").read_text().strip()

Q = int(Q_TEXT)
q = 47
q2 = q * q
r = 424675575059690484579658261789171649

def pell_mod(n: int, modulus: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b % modulus, (2 * b + a) % modulus
    return a

assert len(Q_TEXT) == 828
assert sha256(Q_TEXT.encode()).hexdigest() == "59ce8bd15e4bbfbec0403b55231ee2919425739d929a32787aa3135f9891d634"
assert Q % r == 0

p1 = pell_mod(1, r)
p47 = pell_mod(q, r)
p2209 = pell_mod(q2, r)

assert isprime(r)
assert p1 != 0
assert p47 != 0
assert p2209 == 0

cofactor = Q // r
cofactor_text = str(cofactor)

assert len(cofactor_text) == 792
assert sha256(cofactor_text.encode()).hexdigest() == "978b7253d1665b4c59168fed591b9844db1faf9020b675776ef6a274ba36f570"
assert r * cofactor == Q

print("isprime(r) =", isprime(r))
print("Q47 mod r =", Q % r)
print("P1 mod r =", p1)
print("P47 mod r =", p47)
print("P2209 mod r =", p2209)
print("exact rank =", q2)
print("cofactor digits =", len(cofactor_text))
print("verification = PASS")
