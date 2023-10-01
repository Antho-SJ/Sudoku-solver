# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:44:07 2023

@author: St-Jean
"""
import os

# Chargement du fichier
fichier_adresses = "sudoku.txt"


# Lecture du fichier et extraction des adresses
with open(fichier_adresses, "r") as file:
    lignes = file.readlines()

def string_to_list(string):
    return[int(char) if char.isdigit() else 0 if char=='_' else None for char in string] 
    
def suppr_return_line(T):
    for i in range(len(T)-1):
        L=T[i]
        L.remove(None)
    return(T)    
        
# Créer le tableau
tableau = [string_to_list(file) for file in lignes]

#normaliser le tableau(enlever les retours à la ligne)
tableau_final = suppr_return_line(tableau)


def absentSurLigneColonneBloc(k, grille, i, j):
    # Vérifiez la ligne
    for col in range(9):
        if grille[i][col] == k:
            return 0
    
    # Vérifiez la colonne
    for row in range(9):
        if grille[row][j] == k:
            return 0
    
    # Vérifiez le bloc 3x3
    xi = i - (i % 3)
    xj = j - (j % 3)
    for row in range(xi, xi + 3):
        for col in range(xj, xj + 3):
            if grille[row][col] == k:
                return 0
    
    return 1


def estValide (grille, position):

  os.system("cls")
  

  # SORTIE DU TABLEAU
  if position == 9*9:
      return 1

  # COORDONNEES
  i = int(position/9)
  j = position%9

  # CHANGE DE CASE
  if grille[i][j] != 0:
      return estValide(grille, position+1)

  # BACKTRACKING
  for k in range(1,10): # correction
      test = absentSurLigneColonneBloc(k, grille, i, j)
      if test == 1:
          grille[i][j] = k
          if estValide(grille, position+1) == 1:
              return 1
  grille[i][j] = 0
  return 0



def main ():
  grille = tableau_final
  estValide(grille,0)

main()






