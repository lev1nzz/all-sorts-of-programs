def count_diam(d_rull: float, col_vo_vit: float, chirina: float):
    no_toch = 0.36 
    no_toch2 = 2
    
    
    f1 = d_rull + no_toch
    f2 = f1 / no_toch2
    f3 = f2 * col_vo_vit
    f4 = round(f3 * chirina, 2)
    return f3, f4
    