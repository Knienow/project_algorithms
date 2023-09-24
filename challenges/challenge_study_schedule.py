#boas práticas para legibilidade:
#Entre cada função temos um espaço de 2 linhas;
#As funções são declaradas com nomes em letras minúsculas;
#O import é utilizado para termos todas as funções do módulo disponíveis em outro arquivo;
#https://www.w3schools.com/python/python_try_except.asp
    #O try permite testar um bloco de código em busca de erros.
    #O except permite lidar com o erro.

def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for start, end in permanence_period: # vamos iterar a lista completa
            if start <= target_time <= end: # se encontrar o elemento alvo, retorne a posição
                counter += 1
        return counter
    except TypeError:
        return None
