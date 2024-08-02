import unittest
import os
from src import app
import psycopg2
from dotenv import load_dotenv

class TestRoutes(unittest.TestCase):

    def test_route_main(self):
        testapp = app.test_client()
        response = testapp.get('/')
        self.assertEqual(200,response.status_code)

    '''def test_env(self):

        load_dotenv()

        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        pwd = os.getenv("DB_PWD")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_DATABASE")

        self.assertEqual(host,"#")
        self.assertEqual(user,"#")
        self.assertEqual(pwd,"#")
        self.assertEqual(database,"#")
        self.assertEqual(port,"#")'''

    def test_connection(self):
        
        load_dotenv()
        
        db_config = {
            'host': os.getenv("DB_HOST"),
            'user':  os.getenv("DB_USER"),
            'password': os.getenv("DB_PWD"),
            'dbname': os.getenv("DB_DATABASE")
        }

        try:
            conn = psycopg2.connect(**db_config)
            self.assertTrue(conn.closed == 0)
        except psycopg2.Error as e:
            self.fail(f"Erro ao conectar ao banco de dados: {e}")




if __name__ == '__main__':
    unittest.main()
