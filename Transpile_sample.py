# Build Circuit
from qiskit.circuit.library import QuantumVolume

#Transpile circuit
from qiskit import transpile

circuit = QuantumVolume(5)

transpiled_circuit = transpile(circuit, basis_gates=['sx', 'rz', 'cx'])
transpiled_circuit.draw()

from qiskit.primitives import Sampler
sampler = Sampler()
# Build circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])

# Run the circuit and get result distribution
job = sampler.run(circuit)
quasi_dist = job.result().quasi_dists[0]
print(quasi_dist)

from qiskit.primitives import Estimator
estimator = Estimator()
# Express hydrogen molecule Hamiltonian as an operator
from qiskit.quantum_info import SparsePauliOp
H2_operator = SparsePauliOp.from_list([
    ("II", -1.052373245772859),
    ("IZ", 0.39793742484318045),
    ("ZI", -0.39793742484318045),
    ("ZZ", -0.01128010425623538),
    ("XX", 0.18093119978423156)
])
# Calculate ground state energy using VQE
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import SLSQP
from qiskit.algorithms.minimum_eigensolvers import VQE
ansatz = TwoLocal(num_qubits=2, rotation_blocks="ry", entanglement_blocks="cz")
optimizer = SLSQP(maxiter=100)
vqe = VQE(estimator, ansatz, optimizer)
result = vqe.compute_minimum_eigenvalue(operator=H2_operator)
print(result.eigenvalue)