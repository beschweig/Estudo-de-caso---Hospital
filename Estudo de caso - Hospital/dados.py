from functions import Paciente
from functions import Medico
from functions import Ficha

paciente1 = Paciente('1', 'Juliana', '49281225506', '04-OCT-62', 'F', 'jupires@email.com')
paciente2 = Paciente('2', 'Maria Souza', '49638826479', '16-NOV-52', 'F', 'maria@email.com')
paciente3 = Paciente('3', 'Jaques Lutti', '37843461388', '09-AUG-70', 'M', 'jaques@email.com')
paciente4 = Paciente('4', 'Carla do Santos', '70719177871', '13-SEP-84', 'F', 'csantos@email.com')
paciente5 = Paciente('5', 'Raquel Gomes', '25513392275', '21-JAN-37', 'F', 'raqgomes@email.com')

medico1 = Medico('38222', 'Dra. Dora Lima', '7')
medico2 = Medico('29299', 'Dr. Pedro Cunha', '7')
medico3 = Medico('38393', 'Dr. Juliano Costa', '7')
medico4 = Medico('08841', 'Dr. Mario Rui', '4')
medico5 = Medico('39698', 'Dra. Sara Lee', '4')
medico6 = Medico('10853', 'Dra. Jurema Pimentel', '4')
medico7 = Medico('41685', 'Dr. Roger Dutra', '6')
medico8 = Medico('39741', 'Dra. Paulo Lima', '6')
medico9 = Medico('38477', 'Dra. Samanta Apple', '9')


ficha1 = Ficha('1', '10-SEP-21', paciente1, medico1)

print(paciente1)
print(medico1)
print(ficha1)