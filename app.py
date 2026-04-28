import math
import streamlit as st


# Formula used in the scenario approach:
# N = ceil((2 / epsilon) * (ln(1 / beta) + d))
# where d is the number of decision variables,
# epsilon is the allowed violation probability,
# and beta is the confidence parameter.
def calculate_required_samples(d: int, epsilon: float, beta: float) -> int:
    return math.ceil((2.0 / epsilon) * (math.log(1.0 / beta) + d))


st.set_page_config(page_title="Required Sample Size Calculator", page_icon="📊", layout="centered")

st.title("Required Sample Size Calculator")
st.write(
    "Use the scenario approach formula to compute the required sample size N: "
    "N = ceil((2 / epsilon) * (ln(1 / beta) + d))."
)

# Inputs are text fields so we can provide clear validation messages.
d_input = st.text_input("d (number of decision variables)", value="10")
epsilon_input = st.text_input("epsilon (allowed violation probability)", value="0.1")
beta_input = st.text_input("beta (confidence parameter)", value="1e-6")

if st.button("Calculate N"):
    errors = []

    # Validate d: must be an integer >= 1
    try:
        d = int(d_input.strip())
        if d < 1:
            errors.append("d must be an integer greater than or equal to 1.")
    except ValueError:
        errors.append("d must be a valid integer.")

    # Validate epsilon: must be in (0, 1)
    try:
        epsilon = float(epsilon_input.strip())
        if not (0.0 < epsilon < 1.0):
            errors.append("epsilon must be greater than 0 and less than 1.")
    except ValueError:
        errors.append("epsilon must be a valid number.")

    # Validate beta: must be in (0, 1)
    try:
        beta = float(beta_input.strip())
        if not (0.0 < beta < 1.0):
            errors.append("beta must be greater than 0 and less than 1.")
    except ValueError:
        errors.append("beta must be a valid number.")

    if errors:
        for message in errors:
            st.error(message)
    else:
        n_value = calculate_required_samples(d, epsilon, beta)
        st.success(f"Required number of samples: N = {n_value}")

st.caption(
    "N is the required number of samples to guarantee violation probability at most epsilon "
    "with confidence 1 - beta."
)
