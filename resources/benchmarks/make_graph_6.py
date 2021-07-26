import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd

data = {'Before': [198110,93497,14496,118521,24998,333983,214078,16706],
        ## Prendo quelli con Coeff 2|3
        'After': [194414,92954,14382,116590,25830,226422,200380,113]
       }

df = pd.DataFrame(data,columns=['Before','After'], index = ['CA-AstroPh', 'CA-CondMat', 'CA-GrQc', 'CA-HepPh', 'CA-HepTh', 'BlogC-3', 'Brightkite', 'Email'])

df.plot.barh(figsize=(12, 5), fontsize=11, edgecolor='black')

plt.ylabel('Dataset')
plt.xlabel('Edges')

plt.grid(color='b', ls = '-.', lw = 0.25)
plt.title('Num edges before and after | p_edge_neighborhood_biased_reverse', fontweight ='bold', fontsize = 20)

plt.savefig('BA_p_edge_neighborhood_biased_reverse')