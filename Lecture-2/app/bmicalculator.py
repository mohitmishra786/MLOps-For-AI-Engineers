def bmi_calculator(weight, height):
    '''
    Function calculates bmi according to passed arguments
    weight (int or float) = weight of the person; ex: 61 or 61.0 kg
    height (float) = height of the person, in meter; ex: 1.7 m
    '''
    bmi = weight / (height**2)
    
    return bmi