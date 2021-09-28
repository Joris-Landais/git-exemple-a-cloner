#!/usr/bin/python
# -*- coding: utf-8 -*-

#%%
import numpy as np

#%% [markdown]
# ## le damier
# 
# Écrivez une fonction *checkers*, qui prend en argument la taille *n* du damier, 
# et un paramètre optionnel qui indique la valeur de la case (0, 0), et qui crée 
# un tableau `numpy` carré de coté $n$, et le remplit avec des 0 et 1 comme un damier 
# (0 pour les cases noires et 1 pour les cases blanches).

#%%
def checkers(n, premiere_case=0):
    """
    Génère un tableau numpy en "damier" de taille (n, n).
    """
    return np.array([n,n])

print(checkers(2))


# %%
