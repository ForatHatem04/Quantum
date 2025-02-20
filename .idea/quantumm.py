# hello.py
import cirq
from random import choices

#declare qubits
qubits = cirq.NamedQubit.range(4, prefix= 'q')
print(qubits)

#declare circuit
circuit = cirq.Circuit()

#declare the gates in a list
my_gates = [cirq.X, cirq.Z, cirq.H, cirq.H]

#for loop to add gates
for i in range(4):
    gates = my_gates[i]
    circuit.append(gates(qubits[i]))

#ket notation
vec=cirq.final_state_vector(circuit)
ket = cirq.dirac_notation(vec)
print(ket)

#measurement
circuit.append(cirq.measure(qubits))

#circuit
print(circuit)

#simulation
sim = cirq.Simulator()
result = sim.run(circuit)
print(result)





