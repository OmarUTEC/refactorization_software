import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leerdatos(self, filename='0204.csv'):
        data = []
        with open(filename, 'r') as csvfile:
            next(csvfile)  # Saltar la fila del encabezado
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def calcularganador(self, data):
        votosxcandidato = {}
        total_votos_validos = 0
        
        # Contar votos válidos por candidato y el total de votos válidos
        for fila in data:
            region, provincia, distrito, dni, candidato, esvalido = fila
            if len(dni) == 8 and dni.isdigit() and esvalido == '1':
                if candidato not in votosxcandidato:
                    votosxcandidato[candidato] = [candidato, 0]
                votosxcandidato[candidato][1] += 1
                total_votos_validos += 1

        # Calcular el porcentaje de votos de cada candidato
        porcentajes = {candidato: (votos[1] / total_votos_validos) * 100 for candidato, votos in votosxcandidato.items()}

        # Ordenar candidatos por número de votos y preservar el orden de aparición
        ordenado = sorted(votosxcandidato.items(), key=lambda item: (-item[1][1], data.index(next(filter(lambda x: x[4] == item[0], data)))))

        # Imprimir los resultados de los votos
        for candidato in votosxcandidato:
            print(f'candidato: {candidato} votos validos: {votosxcandidato[candidato]}')

        # Verificar si algún candidato tiene más del 50% de los votos
        for candidato, votos in ordenado:
            if porcentajes[candidato] > 50:
                return [candidato]

        # Si no hay un candidato con más del 50%, retornar los dos primeros
        if len(ordenado) >= 2:
            return [ordenado[0][0], ordenado[1][0]]
        elif len(ordenado) == 1:
            return [ordenado[0][0]]
        else:
            return []

# Crear una instancia de la clase y llamar a los métodos necesarios
c = CalculaGanador()
print(c.calcularganador(c.leerdatos()))  # Leer datos del archivo CSV

# Prueba con datos proporcionados
datatest = [
    ['Ancash', 'Asunción', 'Chacas', '81122156', 'Eddie Hinesley', '1'],
    ['Ancash', 'Asunción', 'Chacas', '20398144', 'Paula Daigle', '1'],
    ['Ancash', 'Asunción', 'Chacas', '33656332', 'Aundrea Grace', '0'],
    ['Ancash', 'Asunción', 'Chacas', '46615862', 'Robert Redmond', '0'],
    ['Ancash', 'Asunción', 'Chacas', '62329211', 'Aundrea Grace', '0'],
    ['Ancash', 'Asunción', 'Chacas', '86085915', 'Jamie Mitchell', '1'],
    ['Ancash', 'Asunción', 'Chacas', '83514019', 'Theresa Waterer', '1'],
    ['Ancash', 'Asunción', 'Chacas', '53247316', 'Paula Daigle', '1'],
    ['Ancash', 'Asunción', 'Chacas', '13185070', 'Paula Daigle', '0'],
    ['Ancash', 'Asunción', 'Chacas', '25303653', 'Theresa Waterer', '1']
]
print(c.calcularganador(datatest))  # Prueba con datos de ejemplo
