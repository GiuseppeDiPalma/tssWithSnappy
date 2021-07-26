import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
threshold_w_coefficient1_2 = [1880, 2699, 809, 1398, 1251, 273, 4197, 77]
threshold_w_coefficient1_3 = [761, 1340, 555, 676, 829, 110, 2306, 28]
threshold_w_coefficient2_3 = [4293, 5672, 1409, 2924, 2474, 620, 9762, 189]

threshold_constant2 = [890, 2294, 874, 995, 1358, 3, 4617, 4]
threshold_constant4 = [2238, 5243, 1424, 2160, 2516, 28, 8750, 11]
threshold_constant6 = [3824, 7018, 1607, 2792, 2995, 91, 11035, 32]
 
# Set position of bar on X axis
br1 = np.arange(len(threshold_w_coefficient1_2))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
br5 = [x + barWidth for x in br4]
br6 = [x + barWidth for x in br5]
 
# Make the plot
plt.bar(br1, threshold_w_coefficient1_2, color ='red', width = barWidth,
        edgecolor ='black', label ='Threshold Coefficients 1|2')
plt.bar(br2, threshold_w_coefficient1_3, color ='gold', width = barWidth,
        edgecolor ='black', label ='Threshold Coefficients 1|3')
plt.bar(br3, threshold_w_coefficient2_3, color ='lime', width = barWidth,
        edgecolor ='black', label ='Threshold Coefficients 2|3')
plt.bar(br4, threshold_constant2, color ='cyan', width = barWidth,
        edgecolor ='black', label ='Threshold constant 2')
plt.bar(br5, threshold_constant4, color ='blue', width = barWidth,
        edgecolor ='black', label ='Threshold constant 4')
plt.bar(br6, threshold_constant6, color ='purple', width = barWidth,
        edgecolor ='black', label ='Threshold constant 6')
 
# Adding Xticks
plt.xlabel('Dataset name', fontweight ='bold', fontsize = 20)
plt.ylabel('TSS Size', fontweight ='bold', fontsize = 20)
plt.xticks([r + barWidth for r in range(len(threshold_constant6))],
        ['CA-AstroPh', 'CA-CondMat', 'CA-GrQc', 'CA-HepPh', 'CA-HepTh', 'BlogC-3', 'Brightkite', 'Email'])
 
plt.legend()
plt.show()
plt.axis
plt.grid(color='b', ls = '-.', lw = 0.25)
plt.title('p_edge_uniform', fontweight ='bold', fontsize = 20)

plt.savefig('p_edge_uniform')
#plt.savefig('primo.eps', format='eps')