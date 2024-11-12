import pandas as pd
import numpy as np

num_sets = 128
numbers_per_set = 20
number_range = 80

possible_numbers = np.arange(1, number_range + 1) #range

random_data = [np.random.choice(possible_numbers, size=numbers_per_set, replace=False) for _ in range(num_sets)] #numpy.random uses Mersenne Twister 19937 algo. 
#we ensure that duplicates are not allowed through replace=False

#converting the data into .csv ->
df = pd.DataFrame(random_data)

output_path = "RNG_20x128.csv"
df.to_csv(output_path, index=False, header=False) #idx and header is set to false as we just need data for testing purposes 

print(f"128 sets of 20 unique random numbers saved to '{output_path}'")

"""
Based on the small but consistent differences observed, here’s a reasoned guess:

	1.	Test 1 likely originates from a quantum random number generator (QRNG).
	•	Uniformity: Test 1 shows high uniformity across bins and no significant patterns in sequential tests like the runs test, which is characteristic of the inherent randomness and lack of periodic structure in quantum randomness.
	•	Low Sequential Patterns: The lack of periodicity or non-random sequences in Test 1 aligns with the expectation that quantum processes yield values without underlying structure or predictability.
"""



