from typing import List
import cirq
from random import choices

#gates based on bits
encode_gates = {0:cirq.I, 1:cirq.X}
#gates based on basis
basis_gates = {'Z':cirq.I, 'X':cirq.H}
#vector
print("input number of bits")
num_bits = int(input())
qubits = cirq.NamedQubit.range(num_bits, prefix ='q')

#ALICE
#generate key
alice_key = choices([0,1], k = num_bits)
print("alice key" , alice_key)

#picking bases
alice_bases = choices(['Z', 'X'], k= num_bits)
#circuit
alice_circuit = cirq.Circuit()

for bit in range(num_bits):
    encode_value = alice_key[bit]
    encode_gate  = encode_gates[encode_value]
    basis_value  = alice_bases[bit]
    basis_gate   = basis_gates[basis_value]
    qubit        = qubits[bit]
    alice_circuit.append(encode_gate(qubit))
    alice_circuit.append(basis_gate(qubit))


#BOB
#generate key
bob_key = choices([0,1], k = num_bits)
print("bob key", bob_key)

#picking bases
bob_basis: list[str] = choices(['Z', 'X'], k=num_bits)
#circuit
bob_circuit = cirq.Circuit()

for bit in range (num_bits):
    basis_value = bob_basis[bit]
    basis_gate = basis_gates[basis_value]
    qubit = qubits[bit]
    bob_circuit.append(basis_gate(qubit))

#measure
bob_circuit.append(cirq.measure(qubits, key = 'bob key'))
#create the big circuit
bb84_circuit = alice_circuit + bob_circuit
#simulation
sim = cirq.Simulator()
result = sim.run(bb84_circuit)
#create bob key
bob_key = result.measurements['bob key'][0]
#compare keys
final_alice_key = []
final_bob_key = []
#create the loop for compatible keys
for bit in range(num_bits):

    if alice_bases[bit] == bob_basis[bit]:
      final_alice_key.append(alice_key[bit])
      final_bob_key.append(bob_key[bit])

print("Final Alice Key:", final_alice_key)
print("Final Bob Key:", final_bob_key)

