import copy

def tick(matrix):

    if not matrix: return []
    
    filas = len(matrix)
    cols = len(matrix[0])
    

    nueva_matrix = copy.deepcopy(matrix)
    
    direcciones = [(-1, -1), (-1, 0), (-1, 1), 
                   (0, -1),           (0, 1), 
                   (1, -1),  (1, 0),  (1, 1)]

    for f in range(filas):
        for c in range(cols):
            vecinos_vivos = 0
            

            for df, dc in direcciones:
                nf, nc = f + df, c + dc
                if 0 <= nf < filas and 0 <= nc < cols:
                    if matrix[nf][nc] == 1:
                        vecinos_vivos += 1
            

            
            celula_actual = matrix[f][c]
            
            if celula_actual == 1:
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nueva_matrix[f][c] = 0
            else: 
                if vecinos_vivos == 3:
                    nueva_matrix[f][c] = 1
                    
    return nueva_matrix