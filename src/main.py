from config.settings import DEBUG, VERSION
from utils.helpers import greet

def main():
    print(f'Debug: {DEBUG}, Version: {VERSION}')
    print(greet('World'))

if __name__ == '__main__':
    main()