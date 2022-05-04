    if 'red' in line:
        current_color = 'red'
    if 'blue' in line:
        current_color = 'blue'
    if 'yellow' in line:
        current_color = 'yellow'
    if 'green' in line:
        current_color = 'green'
    if 'white' in line:
        current_color = 'white'
        
    if  'XStart' in line:
        if current_color == 'red':
            red_x_start.append((float)(rx.sub('',line)))
        if current_color == 'blue':
            blue_x_start.append((float)(rx.sub('',line)))
        if current_color == 'yellow':
           yellow_x_start.append((float)(rx.sub('',line))) 
        if current_color == 'green':
            green_x_start.append((float)(rx.sub('',line)))
        if current_color == 'white':
            white_x_start.append((float)(rx.sub('',line)))
            
    if  'YStart' in line:
        if current_color == 'red':
            red_y_start.append((float)(rx.sub('',line)))
        if current_color == 'blue':
            blue_y_start.append((float)(rx.sub('',line)))
        if current_color == 'yellow':
           yellow_y_start.append((float)(rx.sub('',line))) 
        if current_color == 'green':
            green_y_start.append((float)(rx.sub('',line)))    
        if current_color == 'white':
            white_y_start.append((float)(rx.sub('',line)))
            
    if  'XEnd' in line:
        if current_color == 'red':
            red_x_end.append((float)(rx.sub('',line)))
        if current_color == 'blue':
            blue_x_end.append((float)(rx.sub('',line)))
        if current_color == 'yellow':
           yellow_x_end.append((float)(rx.sub('',line))) 
        if current_color == 'green':
            green_x_end.append((float)(rx.sub('',line)))
        if current_color == 'white':
            white_x_end.append((float)(rx.sub('',line)))
            
    if  'YEnd' in line:
        if current_color == 'red':
            red_y_end.append((float)(rx.sub('',line)))
        if current_color == 'blue':
            blue_y_end.append((float)(rx.sub('',line)))
        if current_color == 'yellow':
           yellow_y_end.append((float)(rx.sub('',line))) 
        if current_color == 'green':
            green_y_end.append((float)(rx.sub('',line)))
        if current_color == 'white':
            white_y_end.append((float)(rx.sub('',line)))
