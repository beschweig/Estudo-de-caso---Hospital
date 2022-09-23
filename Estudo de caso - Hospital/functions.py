
class Paciente():
    def __init__(self, cod, nome_p, cpf, data_nasc, sexo, email):
        self.cod = cod
        self.nome_p = nome_p
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.email = email
    
    def __str__(self):
        return 'PACIENTE: ' + str(self.cod) + ',' + self.nome_p + ', ' + str(self.cpf) + ', ' + str(self.data_nasc) + ', ' + self.sexo + ', ' + self.email

    


class Medico():
    def __init__(self, crm, nome_m, especialidade):
        self.crm = crm
        self.nome_m = nome_m
        self.especialidade = especialidade

    def __str__(self):
        return 'MÉDICO: ' + str(self.crm) + ', ' + self.nome_m + ', '+  str(self.especialidade)


class Ficha():
    def __init__(self, nro_ficha, data_exame, paciente, medico):
        self.nro_ficha = nro_ficha
        self.data_exame = data_exame
        self.paciente = paciente
        self.medico = medico
        
        
    def __str__(self):
        return 'FICHA: ' + str(self.nro_ficha) + ', '  + self.data_exame +  ', ' + str(self.paciente) + ', ' + str(self.medico)