import re

def senha_valida(senha):
    # verificar se a senha tem pelo menos 1 letra maiúscula
    tem_maiuscula = any(c.isupper() for c in senha)
    
    # verificar se a senha tem pelo menos 1 caractere numérico
    tem_numero = any(c.isdigit() for c in senha)
    
    # verificar se a senha tem pelo menos 1 símbolo especial (*, !, $, #)
    tem_simbolo_especial = any(c in '*!$#' for c in senha)
    
    # a senha é válida se atender a todos os critérios
    if tem_maiuscula and tem_numero and tem_simbolo_especial:
        return True
    else:
        return False

# exemplos de uso
senha1 = "Senha@123"
senha2 = "senha123!"
senha3 = "Senh@123"

print(f"A senha '{senha1}' é válida? {senha_valida(senha1)}")
print(f"A senha '{senha2}' é válida? {senha_valida(senha2)}")
print(f"A senha '{senha3}' é válida? {senha_valida(senha3)}")