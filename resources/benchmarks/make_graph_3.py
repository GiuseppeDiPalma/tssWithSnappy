import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
threshold_w_coefficient1_2 = [2396, 3624, 1058, 1822, 1570, 191, 3837, 71]
threshold_w_coefficient1_3 = [1009, 1727, 679, 903, 858, 75, 1490, 77]
threshold_w_coefficient2_3 = [5066, 7108, 1805, 3579, 2967, 434, 10506, 73]

threshold_constant2 = [783, 1698, 805, 771, 1099, 3, 3577, 71]
threshold_constant4 = [1867, 4464, 1550, 1853, 2358, 7, 7993, 69]
threshold_constant6 = [2859, 6713, 1696, 2739, 3224, 16, 11008, 69]
 
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
plt.title('p_edge_neighborhood_biased_reverse', fontweight ='bold', fontsize = 20)

plt.savefig('p_edge_neighborhood_biased_reverse')
#plt.savefig('primo.eps', format='eps')