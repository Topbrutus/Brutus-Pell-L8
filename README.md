# Brutus-Pell L8

**Author:** Gabriel Saint-Pierre  
**Public alias:** TopBrutus  
**Version:** 1.0.0  
**Date:** 2026-10-01

This repository isolates the Brutus-Pell **L8 exact-rank relation** and the first recorded explicit computational witness for the target q = 47.

## L8 statement

For the Pell sequence defined by P_0 = 0, P_1 = 1 and P_(n+2) = 2P_(n+1) + P_n, define

Q_q = P_(q^2) / P_q.

If q is an odd prime and r is a prime divisor of Q_q, then the Pell entry rank z_P(r) equals q^2.

## Explicit q = 47 witness

r = 424675575059690484579658261789171649

Independent checks give Q_47 mod r = 0, P_47 mod r != 0, P_2209 mod r = 0, and r is prime. Therefore z_P(r) = 2209 = 47^2.

See `paper/BRUTUS_PELL_L8.md` for the derivation, domain boundaries, computational protocol and evidence limits.

## Reproducibility

- Exact Q_47: `data/q47.txt`
- Machine-readable witness: `data/q47_witness.json`
- Independent checker: `verification/verify_q47.py`
- Python dependency: `requirements.txt`

Run:

```bash
python -m pip install -r requirements.txt
python verification/verify_q47.py
```

Expected core result:

```text
isprime(r) = True
Q47 mod r = 0
P47 mod r != 0
P2209 mod r = 0
exact rank = 2209
```

## Provenance

The result was developed and counter-tested in `Topbrutus/Brutus`, then isolated here as a publication-grade trace. The Brutus counter-test vector reached PASS / PASS / PASS / PASS on 2026-10-01.

## Priority and novelty note

This release establishes a dated public record of the formulation named **L8**, its derivation in this project, and the q = 47 computational witness. It does **not** claim that all underlying Pell/Lucas divisibility facts are new, nor does it make an exhaustive priority claim over the full mathematical literature.
