from math import *

def print_volume_diagram(container):
    
    gas = sum(row.count('.') for row in container)
    liquid = sum(row.count('~') for row in container)

    a = container.split('\n')
    total_volume = (len(a)-2) * (len(a[0])-2)
    

    r = []
    r += [(len(a))*'#']
    
    c1, c2 = 0, 0 
    
    for i in range(round(gas / (len(a)-2))):
        r += ['#' + (len(a)-2)*'.' + '#']
        c1 += 1
    volume_gas = c1 * (len(a)-2)
        
    for j in range(round(liquid // (len(a)-2))):
        r += ['#' + (len(a)-2)*'~' + '#']
        c2 += 1
    volume_liquid = c2 * (len(a)-2)
        
    r += [(len(a))*'#']
    print('\n'.join(r))

    if volume_gas >= volume_liquid:
        gas, liquid = 20, round(20*volume_liquid/volume_gas)
        s1 = str(volume_gas) + '/' + str(total_volume)
        ind1, ind2 = 1, 20 - len(s1)
    else:
        gas, liquid = round(20*volume_gas/volume_liquid), 20
        s2 = str(volume_liquid) + '/' + str(total_volume)
        ind1, ind2 = 20 - len(s2), 1

    print('.' * gas + ' ' + f"{str(volume_gas) + '/' + str(total_volume):>{ind1}}")
    print('~' * liquid + ' ' + f"{str(volume_liquid) + '/' + str(total_volume):>{ind2}}")

container = '''########
#......#
#~~~~~~#
#~~~~~~#
########'''
    
#container = input()

print_volume_diagram(container)


