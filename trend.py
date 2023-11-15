import numpy as np 
import matplotlib.pyplot as plt


values_physical = np.array([0.909,0.727,1.000,1.000,0.545,1.000])
values_online = np.array([0.600,0.200,0.600,0.000,0.300,0.200])
question = np.array([1,2,3,4,5,6])

substraction_of_the_two = abs(values_physical - values_online)
print(substraction_of_the_two)


fig, ax = plt.subplots(figsize=(8, 6))

plt.plot(question, substraction_of_the_two,'-o', color='green', label='Change in opinion',linestyle='dashed')
# plt.plot(participants, values_online,'-o', color='red', label='Changed in in online questionnaire',linestyle='dashed')
ax.set_ylim(0, 1.5) 
# plt.plot(participants, values, color='blue', marker='o')
# m, b = np.polyfit( participants, values_physical, 1)
# m1, b1 = np.polyfit( participants, values_online, 1)
m2, b2 = np.polyfit( question, substraction_of_the_two, 1)
# print(m, m1, b, b1)
plt.xlabel('Question')
plt.ylabel('Change in opinion: \n difference physical - online questionnaire')
plt.legend()
plt.title("Change in opinion")
plt.grid(True)

# plt.plot(participants, m * participants + b)
# plt.plot(participants, m1 * participants + b1)
plt.plot(question, m2 * question + b2)
plt.plot()



plt.savefig('change_in_opinion.png')
plt.show()
