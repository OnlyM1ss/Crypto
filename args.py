import argparse

parser = argparse.ArgumentParser(description='Decoder')
parser.add_argument('word', type = str,help='слово которое нужно закодировать')
parser.add_argument('shift',type = str,help='шаг')
parser.add_argument('dec16',type = str,help='кодировка 16')
parser.add_argument('dec32',type = str,help='кодировка 32')
parser.add_argument('dec64',type = str,help='кодировка 64')
