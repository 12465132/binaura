 
import numpy as np
# initialise array
gfg = np.arange(1, 49)
print('initialised array')
print(gfg)

gfg.resize((6, 8))
print('')
print(gfg)
print(gfg.shape)

gfg = np.ascontiguousarray(np.flip(gfg, axis=0))
print('')
print(gfg)
print(gfg.shape)


gfg.resize((8, 8))
print('')
print(gfg)
print(gfg.shape)

gfg = gfg[2:8,:]
print('')
print(gfg)
print(gfg.shape)

gfg = np.ascontiguousarray(np.flip(gfg, axis=0))
print('')
print(gfg)
print(gfg.shape)
