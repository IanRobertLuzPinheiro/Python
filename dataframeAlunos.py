import pandas as pd
from faker import Faker
import random
import numpy as np

# Inicializa o Faker
fake = Faker('pt_BR')

# Lista para armazenar os dados
alunos = []

# Gera 1000 registros de alunos
for _ in range(1000):
    cpf = fake.cpf()
    tres_primeiros_digitos = cpf[:3]
    sexo = random.choice(['Masculino', 'Feminino'])
    nome = fake.name_male() if sexo == 'Masculino' else fake.name_female()
    idade = np.random.randint(18, 29) 
    email = f"{nome.lower().replace(' ', '_')}_{tres_primeiros_digitos}@cepedi.com"
    nota_enem = np.round(np.random.uniform(640, 800)).astype(int)
    abandonou = random.choice(['Sim', 'Não'])
    semestre_abandono = fake.random_int(min=1, max=8) if abandonou == 'Sim' else None

    if semestre_abandono and semestre_abandono <= 2:
        cra_segundo_semestre = None
        cra_quarto_semestre = None
        cra_sexto_semestre = None

    elif semestre_abandono and semestre_abandono <= 4:
        cra_segundo_semestre = fake.random.uniform(5.0, 10.0)
        cra_quarto_semestre = None
        cra_sexto_semestre = None

    elif semestre_abandono and semestre_abandono <= 6:
        cra_segundo_semestre = fake.random.uniform(5.0, 10.0)
        cra_quarto_semestre = fake.random.uniform(5.0, 10.0)
        cra_sexto_semestre = None
    else:
        cra_segundo_semestre = fake.random.uniform(5.0, 10.0)
        cra_quarto_semestre = fake.random.uniform(5.0, 10.0)
        cra_sexto_semestre = fake.random.uniform(5.0, 10.0)

    alunos.append({
        'CPF': cpf,
        'Nome': nome,
        'Idade': idade,
        'Sexo': sexo,
        'Email': email,
        'Nota_ENEM': nota_enem,
        'CRE_2o_Semestre': cra_segundo_semestre,
        'CRA_4o_Semestre': cra_quarto_semestre,
        'CRA_6o_Semestre': cra_sexto_semestre,
        'Abandonou': abandonou,
        'Semestre_Abandono': semestre_abandono
    })


df_alunos = pd.DataFrame(alunos)

pd.set_option('display.max_columns', None)

print(df_alunos)
df_alunos.to_csv('alunos.csv', index=False)

