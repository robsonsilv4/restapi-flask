from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 1,
        'nome': 'Hotel 1',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Fortaleza'
    },
    {
        'hotel_id': 2,
        'nome': 'Hotel 2',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Pacoti'
    },
    {
        'hotel_id': 3,
        'nome': 'Hotel 3',
        'estrelas': 4.3,
        'diaria': 320.20,
        'cidade': 'Quixadá'
    },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel

        return {'message': 'Hotel não encontrado.'}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade'],
        }

        hoteis.append(novo_hotel)

        return novo_hotel, 200

    def put(self):
        pass

    def delete(self):
        pass
