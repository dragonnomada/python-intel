# Importación por ALIAS/SOBRENOMBRE `import <libreria> as <alias>`
import numpy as np # import numpy

serie_1 = np.array([1, 2, 3, 4]) # [1. 2. 3. 4.]
serie_2 = np.array([4, 5, 8, 9]) # [4. 5. 8. 9.]

print( serie_1 + serie_2 ) # [5. 7. 11. 13.]
print( serie_1 * serie_2 ) # [4. 10. 24. 36.]
print( serie_1.reshape(2, 2) ) # [[1. 2.] [3. 4.]]
