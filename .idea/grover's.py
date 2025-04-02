import numpy as np
import math
import scipy
import cirq
import random
import matplotlib.pyplot as plt
import warnings

number_choices = 4
correct_choices = 2
nqubits = math.sqrt(number_choices)

#create the binary generation function
def generate_Binary_Strings(number_choices):
    n = int(math.log(number_choices,2))  #Each binary string represents a possible solution to the search problem.
    binary_strings =[]
    for i in range(2**n): #creates the list
        binary_string =bin(i)[2:].zfill(n)   #bin(i) converts the integer i to its binary representation.
        binary_strings.append(binary_string)  #zfill(n) pads the binary string with leading zeros to ensure a consistent length of n.
    return binary_strings

#create the oracle function
def oracle(qubits, ancilla, marked_bitstring ):
    for(q, bit) in zip(qubits, marked_bitstring): #relates the two iterations, the qubit and its binary
        if not bit:                   #if 0 state (rules of the CNOT gate)
            yield (cirq.X(q))         #apply the x circuit to make it a 1 state

        controls = len(qubits) #equals the length of the qubits' list
        mcx_gate = controlled_x_gate(qubits) #applies a CNOT gate through an x gate
        yield(mcx_gate(*qubits, ancilla))  #The controlled-X gate flips the state of the ancilla qubit if all the qubits in the qubits list are in the state |1|.

    for (q, bit) in zip(qubits, marked_bitstring):
      if not bit:
        yield cirq.X(q)     #ensures the negation

# trying to create a CNOT gate
def controlled_x_gate(qubits):
    controls = len(qubits) - 1
    return cirq.ControlledGate(sub_gate=cirq.X, num_controls=controls)

#create the grover algorithm
def grover_iteration(qubits, ancilla, marked_bitstring, reps=1):
    circuit = cirq.Circuit
    circuit.append(cirq.H.on_each(*qubits))    # Create an equal superposition over input qubits.
    circuit.append((cirq.X(ancilla)), (cirq.H(ancilla)))  # - state ( 0--> 1 then 1 --> -)
    for r in range(reps):
        circuit.append(make_oracle(qubits, ancilla))
        circuit.append(cirq.H.on_each(*qubits))
        circuit.append(cirq.X.on_each(*qubits))
        mcx_gate = controlled_x_gate(qubits)
        mcx_op = mcx_gate(*qubits, ancilla)
        circuit.append(mcx_op)
        circuit.append(cirq.X.on_each(*qubits))
        circuit.append(cirq.H.on_each(*qubits))
        circuit.append(cirq.measure(*qubits, key="result"))

        return circuit
def get_marked_bitstring(correct_choice, nqubits):
    binary_representation = list(bin(correct_choice)[2:])# Convert the correct choice to its binary representation as a string
    marked_bitstring = [eval(i) for i in binary_representation] #converts into integer
    desired_length = nqubits
marked_bitstring = [0] * (desired_length - len(marked_bitstring)) + marked_bitstring










