import unittest
from app import CalculaGanador

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.calculador = CalculaGanador()

    def calcular_votos(self, data):
        # Método auxiliar para contar los votos válidos por candidato
        votosxcandidato = {}
        for fila in data:
            candidato = fila[4]  # El nombre del candidato está en la columna 4
            if fila[5] == '1': 
                if candidato not in votosxcandidato:
                    votosxcandidato[candidato] = 0
                votosxcandidato[candidato] += 1
        return votosxcandidato

    def test_un_ganador_mayoria(self):
        # Caso de prueba: Un candidato tiene mayoría absoluta de votos válidos
        print("test_un_ganador_mayoria")
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1']
        ]
        votos = self.calcular_votos(data)
        ganador = max(votos, key=votos.get) if max(votos.values()) > sum(votos.values()) / 2 else None
        self.assertEqual(self.calculador.calcularganador(data), [ganador])

    def test_dos_ganadores_segunda_vuelta(self):
        # Caso de prueba: Dos candidatos pasan a segunda vuelta
        print("test_dos_ganadores_segunda_vuelta")
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        votos = self.calcular_votos(data)
        total_votos_validos = sum(votos.values())
        ganador = [candidato for candidato, votos_validos in votos.items() if votos_validos > total_votos_validos / 2]
        if not ganador:
            ordenado = sorted(votos.items(), key=lambda item: item[1], reverse=True)
            ganador = [ordenado[0][0], ordenado[1][0]]
        self.assertEqual(self.calculador.calcularganador(data), ganador)

    def test_empate(self):
        # Caso de prueba: Empate entre dos candidatos
        print("test_empate")
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        votos = self.calcular_votos(data)
        total_votos_validos = sum(votos.values())
        ganador = [candidato for candidato, votos_validos in votos.items() if votos_validos > total_votos_validos / 2]
        if not ganador:
            ordenado = sorted(votos.items(), key=lambda item: item[1], reverse=True)
            ganador = [ordenado[0][0], ordenado[1][0]]
        self.assertEqual(self.calculador.calcularganador(data), ganador)

    def test_dni_no_valido(self):
        # Caso de prueba: Hay un DNI no válido en los datos
        print("test_dni_no_valido")
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '4081062', 'Eddie Hinesley', '1'],  # DNI no válido
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        # Filtrar los votos con DNI válidos
        votos = self.calcular_votos([fila for fila in data if len(fila[3]) == 8])
        total_votos_validos = sum(votos.values())
        ganador = [candidato for candidato, votos_validos in votos.items() if votos_validos > total_votos_validos / 2]
        if not ganador:
            ordenado = sorted(votos.items(), key=lambda item: item[1], reverse=True)
            ganador = [ordenado[0][0], ordenado[1][0]]
        self.assertEqual(self.calculador.calcularganador(data), ganador)

if __name__ == '__main__':
    unittest.main()
