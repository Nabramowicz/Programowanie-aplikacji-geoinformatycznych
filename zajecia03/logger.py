import logging


logging.basicConfig(filename='myapp.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#loger konsoli
logging.StreamHandler().setLevel(logging.INFO)
