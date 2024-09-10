def verificar_paridade_soma_cpf(cpf):
    
    cpf = cpf.replace('.', '').replace('-', '')
    
    
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido. Certifique-se de que o CPF possui 11 dígitos numéricos.")
    
    
    soma = sum(int(digito) for digito in cpf)
    
    
    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'
    
    return resultado


cpf_usuario = input("Digite o CPF (no formato 999.999.999-99): ")

try:
    resultado = verificar_paridade_soma_cpf(cpf_usuario)
    print(f"A soma dos dígitos do CPF é {resultado}.")
except ValueError as e:
    print(e)
