import random
import math

# Classical
def classical_flip():
    return "H" if random.random() < 0.5 else "T"

# Quantum
def make_qubit(alpha,beta):
    # Normalize so squared(alpha) + squared beta =1
    assert abs(pow(alpha,2) + pow(beta,2)-1.0) < 1e-9 , "Must be normalized" # pythonic  way: alpha**2
    return [alpha,beta]
def hadamard_state():
    return make_qubit(1/math.sqrt(2) , 1/math.sqrt(2))
def measure(qubit):
    alpha,beta = qubit
    result = random.choices([0,1],weights=[pow(alpha,2),pow(beta,2)]) [0]

    # Collapse state is now definite
    qubit[0], qubit[1] = (1.0 , 0.0) if result == 0 else (0.0 , 1.0)
    return result


#-----Run Experiment-----
print("=== Classical vs Quantum Coin Flipper ===\n")
print("Classical (1000 flip):")
results = [classical_flip() for _ in range(1000)]
print(f" Heads :{results.count("H")}  Tails :{results.count("T")}\n")

print("Quantum (1000 measurements):")
results = [measure(hadamard_state()) for _ in range(1000)]
print(f" |0> : {results.count(0)} |1> : {results.count(1)}\n")

print("Collapse demo - measure same qubit twice:")
q = hadamard_state()
print(f" First measurement: {measure(q)}")
print(f" Second measurement: {measure(q)} <- always same!")
