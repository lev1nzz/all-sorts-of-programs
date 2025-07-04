def count_diam(d_rull: float, col_vo_vit: float, chirina: float):
    no_toch = 0.36 
    no_toch2 = 2
    
    
    f1 = d_rull + no_toch
    f2 = f1 / no_toch2
    f3 = f2 * col_vo_vit
    f4 = round(f3 * chirina, 2)
    print('Col-co pogon/metr = ', f3)
    print('KVmetr = ', f4)
    return f3, f4
    
d1_rull = float(input('Enter diametr: '))
col1_vo_vit = float(input('Enter colvo vitkov: '))
chir = float(input('Enter chirina: '))
count_diam(d_rull=d1_rull, col_vo_vit=col1_vo_vit, chirina=chir)