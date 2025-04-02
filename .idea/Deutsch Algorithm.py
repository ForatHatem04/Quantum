from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import Oracle
import matplotlib.pyplot as plt
import pylatexenc

circuit=QuantumCircuit(2,1)
circuit.x(1)
circuit.h(1)
circuit.h(0)
circuit.compose(Oracle.oracle(), inplace=True)
circuit.h(0)
circuit.measure(0,0)
circuit.draw(output='mpl')
plt.show()

job = AerSimulator().run(circuit,shots=10000)
counts = job.result().get_counts()
print(counts)
