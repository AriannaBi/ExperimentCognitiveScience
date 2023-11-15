import numpy as np 
import matplotlib.pyplot as plt


values_physical = np.array([0.909,0.727,1.000,1.000,0.545,1.000])
# values_online = np.array([0.727,0.636,0.636,0.364,0.545,0.455])
values_online = np.array([0.600,0.200,0.600,0.000,0.300,0.200])
question = np.array([1,2,3,4,5,6])



fig, ax = plt.subplots(figsize=(8, 6))

# plt.axhline(y=0, color='r', linestyle='-')
plt.plot(question, values_physical,'-o', color='blue', label='Physical questionnaire',linestyle='dashed')
plt.plot(question, values_online,'-o', color='red', label='Online questionnaire',linestyle='dashed')



ax.set_ylim(0, 2.5) 


plt.xlabel('Question')
plt.ylabel('Changed in opinion: \n AVG (before - after values)')
plt.title('Change in opinion for physical and online questionnaire')
plt.legend()
plt.grid(True)


plt.plot()



plt.savefig('change_in_opinion.png')
plt.show()
