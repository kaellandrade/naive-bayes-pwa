from flask import Flask, jsonify, request



from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# @app.route('/')
# def hello_world():
#   name = request.args.get('name')

#   print(name)
#   data = {'message': 'Hello, world!'}
#   return jsonify(data)

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

    if data.get('key'):
      return self.data_clients[key]
    return []
    


  def not_is_None(self) -> bool:
    """
    Este metodo verifica se todos os valores de um dicionario 
    sao diferentes de none
    """
    return all(val is not None for val in self.profiles)
  



class CommendProducts:

  @staticmethod
  @app.route('/', methods=['POST'])
  def get_Products():
    proxy = ProxyPetIndica(request.json, 'petIndica.allData')
    profiles = proxy.profiles

    if len(profiles):
      query = "SELECT * FROM products WHERE code IN %s"

    return 'aqu1'


  

    




# all_values_not_none = all(val is not None for val in my_dict.values())


if __name__ == '__main__':

  teste = CommendProducts()
  host = '0.0.0.0'
  port = 5000
  app.run(port=port)