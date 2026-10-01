# Brutus-Pell L8 Exact-Rank Relation and an Explicit q=47 Witness

**Gabriel Saint-Pierre**  
TopBrutus  
Version 1.0.0 - 2026-10-01

## Abstract

Let (P_n) be the Pell sequence defined by P_0 = 0, P_1 = 1 and P_(n+2) = 2P_(n+1) + P_n. For an odd prime q, define Q_q = P_(q^2) / P_q. This note records the project formulation called **L8**:

> If q is an odd prime and r is a prime divisor of Q_q, then the Pell entry rank z_P(r) is exactly q^2.

A short derivation is given from standard Pell divisibility and rank-of-appearance facts together with a quotient congruence. The note also records an explicit q = 47 computational witness. Native GMP-ECM found the 36-digit prime factor

424675575059690484579658261789171649

of the exact 828-digit Q_47. Independent checks verify divisibility, primality, and the exact rank z_P(r) = 2209 = 47^2.

This release is a dated trace of the L8 formulation and witness. It does not claim that the underlying classical Pell/Lucas facts are new, and it does not make an exhaustive priority claim over the literature.

## 1. Definitions

The Pell sequence is

P_0 = 0, P_1 = 1, P_(n+2) = 2P_(n+1) + P_n.

For an integer m > 1, define the Pell entry rank, or order of appearance,

z_P(m) = min{ n >= 1 : m divides P_n },

whenever such an index exists.

For an odd prime q, define the integer quotient

Q_q = P_(q^2) / P_q.

The divisibility P_q | P_(q^2) follows from the strong divisibility property of Pell numbers.

## 2. L8 statement

**L8.** Let q be an odd prime. If r is a prime divisor of Q_q, then

z_P(r) = q^2.

The odd-prime hypothesis on q is essential to this formulation.

## 3. Standard facts used

The derivation uses the following standard properties of Pell sequences.

1. gcd(P_m, P_n) = P_gcd(m,n).
2. For a prime r dividing a Pell number, r divides P_n if and only if z_P(r) divides n.
3. For an odd prime r, z_P(r) divides r - (2/r), where (2/r) is the Legendre symbol.

These facts are standard in the arithmetic of Pell/Lucas sequences and are explicitly available in Faye and Luca (2017), including the strong divisibility and order-of-appearance discussion.

## 4. Quotient congruence

For odd q,

Q_q is congruent to (-1)^((q-1)/2) q modulo P_q.

A convenient derivation uses the Binet representation. Let alpha = 1 + sqrt(2) and beta = 1 - sqrt(2), so alpha beta = -1 and

P_n = (alpha^n - beta^n) / (alpha - beta).

Put x = alpha^q and y = beta^q. Then

Q_q = (x^q - y^q) / (x - y)
    = sum from j=0 to q-1 of x^(q-1-j) y^j.

Modulo P_q in Z[sqrt(2)], x and y are congruent because x - y = (alpha - beta) P_q. Therefore every term in the sum has the same residue and

Q_q is congruent to q y^(q-1).

Since q - 1 is even and x is congruent to y,

y^(q-1) is congruent to (xy)^((q-1)/2).

But xy = (alpha beta)^q = (-1)^q = -1 because q is odd. Hence

Q_q is congruent to (-1)^((q-1)/2) q modulo P_q.

## 5. Coprimality

Suppose q divided P_q. Then z_P(q) would divide q.

For odd prime q, the standard rank bound also gives z_P(q) | q - (2/q), which is q - 1 or q + 1. Thus z_P(q) would divide gcd(q, q +/- 1) = 1, impossible because P_1 = 1.

Therefore q does not divide P_q.

From the quotient congruence,

gcd(P_q, Q_q) = gcd(P_q, q) = 1.

## 6. Exact-rank conclusion

Let r be a prime divisor of Q_q.

Then r divides P_(q^2). Therefore z_P(r) divides q^2.

Because gcd(P_q, Q_q) = 1, r does not divide P_q. Hence z_P(r) does not divide q.

The positive divisors of q^2 are 1, q and q^2. The rank cannot be 1 because P_1 = 1. It cannot be q because r does not divide P_q.

Therefore the only remaining possibility is

z_P(r) = q^2.

This proves L8 on its stated domain.

## 7. Domain boundaries

The odd-prime condition is not cosmetic.

- q = 2: Q_2 = 6 and the prime r = 2 has z_P(2) = 2, not 4.
- q = 9 is composite: 53 divides Q_9, but z_P(53) = 27, not 81.

These examples are kept explicitly as boundary checks.

## 8. Explicit q = 47 witness

For q = 47, the exact quotient Q_47 has 828 decimal digits.

SHA-256 of its decimal representation:

59ce8bd15e4bbfbec0403b55231ee2919425739d929a32787aa3135f9891d634

The exact integer is included in `data/q47.txt`.

A native GMP-ECM 7.0.6 campaign was run with stop-on-first-factor mode and the command shape

```text
ecm -one -c 50 3e6
```

The run requested 50 curves with B1 = 3e6 and no explicit B2. Runtime was approximately 3258.22 seconds.

It returned the factor

r = 424675575059690484579658261789171649.

## 9. Independent verification

The ECM output was not treated as sufficient by itself.

A separate Python 3.12.10 / SymPy 1.14.0 check returned

```text
isprime(r) = True
```

Independent exact modular Pell calculations returned

```text
Q_47 mod r   = 0
P_1 mod r    = 1
P_47 mod r   = 345869461223138161
P_2209 mod r = 0
```

Thus r divides Q_47, r does not divide P_47, and r divides P_2209.

Since 2209 = 47^2 has positive divisors exactly 1, 47 and 2209, these checks force

z_P(r) = 2209 = 47^2.

The repository includes `verification/verify_q47.py` so these checks can be reproduced directly.

## 10. Partial factorization boundary

The factorization of Q_47 is not claimed to be complete.

After removing the 36-digit prime factor r, the remaining cofactor has 792 decimal digits.

SHA-256 of the remaining cofactor decimal representation:

978b7253d1665b4c59168fed591b9844db1faf9020b675776ef6a274ba36f570

Exact reconstruction Q_47 = r times cofactor was verified.

The correct status is therefore **PARTIAL FACTORIZATION**, with one independently verified prime factor sufficient for the recorded q = 47 exact-rank witness.

## 11. Interpretation

The general L8 implication is a mathematical derivation from standard Pell-sequence facts plus the quotient congruence established above.

The q = 47 computation is an explicit numerical witness of the derived relation.

The computation is not used as a substitute for the derivation, and the derivation is not used as a substitute for the primality and modular checks.

## 12. Provenance and evidence discipline

This result was developed inside the Brutus counter-test framework and then isolated in this repository.

The final recorded counter-test vector was

- CT-01: PASS - mathematical audit of the L8 implication.
- CT-02: PASS - exact quotient data and partial factorization state preserved.
- CT-03: PASS - explicit prime factor with independently verified exact rank q^2.
- CT-04: PASS - bounded scan reproduced with its stated limits.

The Brutus evidence gate deliberately kept automatic proof promotion disabled. This repository therefore presents the derivation and computational witness directly rather than relying on a software status label.

## 13. Priority note

The label **L8** and this exact publication trace identify the formulation as used in the Brutus project by Gabriel Saint-Pierre.

No claim is made here that classical strong divisibility, rank-of-appearance theory, primitive divisor theory, or related Lucas-sequence results are new.

No exhaustive literature search is claimed. The purpose of this release is to establish a precise, dated, reproducible public record of the formulation and the q = 47 witness.

## Reference

Bernadette Faye and Florian Luca, "Pell Numbers Whose Euler Function Is a Pell Number," *Publications de l'Institut Mathematique*, 101(115) (2017), 231-245. DOI: 10.2298/PIM1715231F.

The reference is used for standard Pell divisibility and order-of-appearance facts. The L8 naming, quotient-focused formulation, Brutus counter-test trace, and q = 47 computational witness are recorded in this release.

## Reproducibility files

- `data/q47.txt` - exact 828-digit Q_47.
- `data/q47_witness.json` - machine-readable witness metadata.
- `verification/verify_q47.py` - independent exact verifier.
- `requirements.txt` - pinned SymPy version used by the verifier.
- `CITATION.cff` - citation metadata.
- `.zenodo.json` - Zenodo-ready metadata.
