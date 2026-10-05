import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

st.title("Quantum OTP Generator - Quantum Superposition")
st.write(" First Own Quantum App - Generate OTP using Quantum Superposition!")

def generate_quantum_otp(num_digits=6):
    simulator = AerSimulator()
    otp = ""
    for _ in range(num_digits):
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
        # Get 4 bits for one digit (0-15 -> 0-9)
        digit_bits = ""
        for _ in range(4):
            result = simulator.run(qc, shots=1).result()
            bit = list(result.get_counts().keys())[0]
            digit_bits += bit
        digit = int(digit_bits, 2) % 10
        otp += str(digit)
    return otp

if st.button("Generate Quantum OTP!"):
    otp_code = generate_quantum_otp(6)
    st.success(f"Your Quantum OTP: {otp_code}")
    st.balloons()
    st.write("6 digits - True Quantum Random - Superposition used!")

st.write("---")
st.write("Circuit:")
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
st.write(qc.draw())