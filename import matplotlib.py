import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from scipy.stats import norm
# Example data
physical_data= np.array([1.166666667,0.666666667,1.666666667,0.333333333,1.666666667,0.333333333,
                        0.666666667,0.666666667,0.666666667,0.833333333,0.833333333,0.666666667,
                        2.166666667,1.333333333,1.333333333,1.5,1.833333333,1.333333333,2.166666667,1.333333333,1.166666667,1.5])
online_data= np.array([0.333333333,0,1,0,0,0,0.166666667,0.166666667,0.833333333,0.666666667,0.166666667,0,0.5,0.166666667,1.166666667])


# Example data for two independent groups
# group1 = [23, 27, 28, 29, 30, 31, 33, 35, 37, 40]
# group2 = [18, 20, 22, 25, 27, 28, 29, 30, 32, 35]

# Perform Mann-Whitney U test
statistic, p_value = scipy.stats.mannwhitneyu(physical_data, online_data, alternative='two-sided')

# Print results
print(f"Mann-Whitney U Statistic: {statistic}")
print(f"P-value: {p_value}")

# Interpret the results
if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")



# Example: Critical value for Mann-Whitney U test with sample sizes 20 and 25 at alpha = 0.05
sample_size1 = 22
sample_size2 = 15
# norm.ppf(0.025, loc=20*25/2, scale=(20*25*(20+25+1)/12)**0.5)
print(norm.ppf(0.025, loc=sample_size1*sample_size2/2, scale=(sample_size1*sample_size2*(sample_size1+sample_size2+1)/12)**0.5))

