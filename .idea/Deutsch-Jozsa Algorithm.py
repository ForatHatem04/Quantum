from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import Oracle
n = int(input("Insert number of qubits"))
circuit = QuantumCircuit(n+1,n)
circuit.x(n)
circuit.h(range(n+1))
circuit.compose(Oracle.oraclej(n), inplace=True)
circuit.h(range(n))
circuit.measure(range(n), range(n))

circuit.draw(output='mpl')
plt.show()

job = AerSimulator().run(circuit,shots=10000)
counts = job.result().get_counts()
print(counts)
