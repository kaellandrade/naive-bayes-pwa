from flask import Flask, jsonify, request

from main import DataBaseQuerys



from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


class ProxyPetIndica:

  def __init__(self,data_clients: dict,  name_table: str) -> None:
    self._name_table = name_table
    self.data_clients = data_clients


  @property
  def name_table(self)-> str:
    return self._name_table
  
  @property
  def profiles(self) -> list:

    data = self.data_clients
    key = 'profiles'

    if data.get(key):
      return self.data_clients[key]
    return []
  

  def get_response(self, resData: list) -> dict:
    if len(resData):
      return self.__get_responseDTO(resData, 'Operação realizada com sucesso.')
    
    return self.__get_responseDTO(resData, 'Nenhum dado foi encontrado.')
       
  
  def __get_responseDTO(resData: list, msg: str):
    return {
        'result': {
          'Message: ': msg,
          'dados': resData
        }
    }


  def not_is_None(self) -> bool:
    """
    Este metodo verifica se todos os valores de um dicionario 
    sao diferentes de none
    """
    return all(val is not None for val in self.profiles)
  


class DBQuerys:

  def __init__(self, profiles: list) -> None:
    self.profiles = profiles
    self.bd = DataBaseQuerys

  def queryColaborativeFilteringDuplicate(self):
    """
    Este metodo eh uma consulta que retorna uma lista de produtos
    sua categoria, a quantidade de venda e o percentual que vendeu 

    PRECISO REMOVER ESSA REPETICAO DE DADOS
    """
    return '''
        SELECT
        p.CODCLI,
        p.PRODUTO,
        p.DEPARTAMENTO,
        p.QT_VENDA,
        p.QT_VENDA * 100.0 / s.TOTAL AS PERCENTUAL
      FROM
        petIndica.allData p
      JOIN
        (
          SELECT CODCLI, SUM(QT_VENDA) AS TOTAL
          FROM petIndica.allData
          GROUP BY CODCLI
        ) s
      ON
        p.CODCLI = s.CODCLI
      WHERE
        p.CODCLI IN ({});
    '''.format(self.codes_profiles)
  

  def queryColaborativeFiltering(self):
    """

    ESSA EH A CONSULTA ORIGINAL ACHO QUE TA FUNCIONANDO CORRETAMENTE
    """
    return '''
        SELECT
          CODCLI,
          PRODUTO,
          DEPARTAMENTO,
          SUM(QT_VENDA) AS TOTAL_VENDIDO,
          COUNT(*) AS NUM_VENDAS,
          100 * SUM(QT_VENDA) / (SELECT SUM(QT_VENDA) FROM petIndica.allData) AS PERCENT_VENDIDO
        FROM
          petIndica.allData p
        WHERE
          CODCLI IN ({})
        GROUP BY
          CODCLI,
          PRODUTO,
          DEPARTAMENTO
        ORDER BY
          CODCLI
    '''.format(self.codes_profiles)
  
  @property
  def codes_profiles(self):
    return ','.join(str(cod) for cod in self.profiles)


class CommendProducts:

  @staticmethod
  @app.route('/', methods=['POST'])
  def get_Products():
    proxy = ProxyPetIndica(request.json, 'petIndica.allData')
    profiles = proxy.profiles

    if len(profiles):
      query = "SELECT * FROM products WHERE code IN %s"

   
    return jsonify(proxy.get_response([])), 200




if __name__ == '__main__':

  teste = CommendProducts()
  host = '0.0.0.0'
  port = 5000
  app.run(port=port)




"""
SELECT
  p.CODCLI,
  p.PRODUTO,
  p.DEPARTAMENTO,
  p.QT_VENDA * 100.0 / s.TOTAL AS PERCENTUAL
FROM
  petIndica.allData p
JOIN
  (
    SELECT CODCLI, SUM(QT_VENDA) AS TOTAL
    FROM petIndica.allData
    GROUP BY CODCLI
  ) s
ON
  p.CODCLI = s.CODCLI
WHERE
  p.CODCLI IN (302501, 30491);
  
  
  
SELECT
  CODCLI,
  PRODUTO,
  DEPARTAMENTO,
  SUM(QT_VENDA) AS TOTAL_VENDIDO,
  COUNT(*) AS NUM_VENDAS,
  100 * SUM(QT_VENDA) / (SELECT SUM(QT_VENDA) FROM petIndica.allData) AS PERCENT_VENDIDO
FROM
  petIndica.allData p
WHERE
  CODCLI IN (302501, 30491)
GROUP BY
  CODCLI,
  PRODUTO,
  DEPARTAMENTO
ORDER BY
  CODCLI
  
"""