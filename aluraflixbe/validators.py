import re

def cor_valida(codigo_cor):    
    return re.search(r'^#[0-9a-fA-F]{6}$', codigo_cor)