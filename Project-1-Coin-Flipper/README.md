# Quantum Projects

I am a student exploring quantum computing out of curiosity. I am building these projects in pure Python
because I want to understand the math and logic from scratch before moving to real quantum hardware.

## Project 1: Quantum Coin Flipper

### What This Project Does
This project simulates the difference between a classical coin flip and a quantum coin flip using pure Python. 
No quantum computer was used.This is a mathematical simulation that follows the same rules a real quantum computer follows.

### Why No Quantum Computer?
A real quantum computer uses physical qubits — electrons or photons in a lab. 
We do not have access to that hardware. But the math is exactly the same. 
Just like a flight simulator teaches a pilot before a real plane.This simulator teaches quantum concepts before real hardware.

### Concepts I Learned

**Qubit**
A qubit is represented as a list of two numbers — [alpha, beta]. 
These are called amplitudes. They are not probabilities directly.

**Born Rule**
To get probability from amplitude — square it.
- P(0) = alpha²
- P(1) = beta²
- alpha² + beta² must always equal 1.0

**Superposition**
When both alpha and beta are non-zero — the qubit has no definite value. 
Both 0 and 1 exist as possibilities at the same time.
Example: [0.707, 0.707] means 50% chance of 0 and 50% chance of 1.

**State Collapse**
The moment we measure a qubit — it picks one value permanently.
If 0 comes, qubit becomes [1.0, 0.0]  now 100% chance of 0 forever.
This is called collapse. Classical randomness does not behave this way.

**Classical vs Quantum**
A classical coin flip is hidden randomness, the value existed, we just did not know it. 
A quantum measurement creates the value, it did not exist before we measured.

### Code Explanation

**`make_qubit(alpha, beta)`**
Takes two amplitude values, checks if they form a valid qubit using assert, and returns them as a list [alpha, beta].

**Why assert and not ==?**
Decimal numbers in computers are never perfectly exact.
0.1 + 0.2 gives 0.30000000000000004 in Python.
So we check if the difference from 1.0 is less than 0.000000001, not exactly equal to 1.0.

**`hadamard_state()`**
Returns a 50/50 qubit. Uses 1/√2 = 0.707 because:
0.707² + 0.707² = 0.5 + 0.5 = 1.0

**`measure(qubit)`**
- Unpacks [alpha, beta] from the qubit list
- Uses random.choices with weights=[alpha², beta²] to pick 0 or 1
- This weighted random choice is the Born Rule in code
- After result,qubit collapses to [1.0, 0.0] or [0.0, 1.0]
- Returns the result

### How to Run
```bash
python quantum_coin.py
```
### What the Output Means

Classical (1000 flips):
Heads: 505 Tails: 495 ← random, changes every run

Quantum (1000 measurements):
|0>: 504 |1>: 496 ← also ~50/50, looks same

Collapse demo:
First measurement: 0
Second measurement: 0 ← always (same state collapsed)

Both look 50/50 on surface — but the mechanism is completely different.

### My Learnings
- A qubit is just two numbers in a list
- Squaring amplitudes gives probabilities (Born Rule)
- Measuring a qubit destroys its superposition permanently
- Computers cannot compare decimals with == reliably
- assert is a guard — it stops the program if something is wrong
- Simulation follows the same math as real quantum hardware