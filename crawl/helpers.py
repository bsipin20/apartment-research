import usaddress
import socket
import typing
import re

US_ADDR = { 'AddressNumber': 'number',
            'StreetName' : 'street',
            'PlaceName': 'place',
            'StateName': 'state',
            'ZipCode': 'zip_code',
            'StreetNamePostType': 'street_type'}

HOST = 'questdb'
PORT = 9009

def clear(usaddress):
    results = {}
    number = None
    street = None
    place = None
    state = None
    zip_code = None
    for i in usaddress:
        if i[1] in US_ADDR:
            key = US_ADDR[i[1]]
            results[key] = i[0]
    return results
            
def parse_address(addr):
    addr = usaddress.parse(addr)
    result = clear(addr)
    return result

def parse_price(price_string):
    price = re.sub('\D', '', 'aas30dsa20')
    return int(price)

def parse_where(where):
    if 'bay ridge' in where:
        return 'bay ridge'
    elif 'gowanus' in where:
        return 'gowanus'
    elif 'windsor' in where:
        return 'windsor terrace'
    elif 'flatbush' in where:
        return 'flatbush'
    elif 'boreum' in where:
        return 'boreum hill'
    elif 'lefferts' in where:
        return 'prospect lefferts gardens'
    elif 'prospect heights' in where:
        return 'prospect heights'
    elif 'prospect park' in where:
        return 'prospect park'
    elif 'park slope' in where:
        return 'park slope'
    elif 'south slope' in where:
        return 'south slope'
    elif 'bedford' in where:
        return 'bedford-stuyvesant'
    elif 'greenpoint' in where:
        return 'greenpoint'
    elif 'williamsburg' in where:
        return 'williamsburg'
    elif 'dumbo' in where:
        return 'dumbo'
    elif 'yonkers' in where:
        return 'yonkers'
    elif 'weeksvile' in where:
        return 'weeksville'
    elif 'woodside' in where:
        return 'woodside'
    elif 'woodlawn' in where:
        return 'woodlawn'
    elif 'yellowstone' in where:
        return 'yellowstone'
    elif 'yorktown' in where:
        return 'yorktown'
    elif 'staten' in where:
        return 'staten island'
    elif 'borough park' in where:
        return 'borough park'
    elif 'corona' in where:
        return 'corona'
    elif 'queens' in where:
        return 'queens'
    else:
        return 'notparsed'

def parse_location(result):
    try:
        lat = float(result[0])
        lon = float(result[1])
    except:
        lat = 0.0
        lon = 0.0
    return lat, lon

def create_message(table_name: str,
                   symbols: typing.Dict[str, typing.Any] = None,
                   fields: typing.Dict[str, typing.Any] = None,
                   ts: int = -1) -> str:
    message = [table_name]
    if symbols:
        for (name, value) in symbols.items():
            message.extend((',', name, '=', value))
    if fields:
        message.append(' ')
        for idx, (name, value) in enumerate(fields.items()):
            if isinstance(value, str):
                value = f'"{value}"'
            elif isinstance(value, int):
                value = f'{value}i'
            else:
                value = str(value)
            if idx == 0:
                message.extend((name, '=', value))
            else:
                message.extend((',', name, '=', value))
    if ts > -1:
        message.extend((' ', str(ts)))
    message.append('\n')
    return ''.join(message)


def send_tcp_messages(*messages: typing.List[str]) -> bool:
    host, port = HOST, PORT
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            for message in messages:
                sock.sendall(message.encode('utf-8'))
                print(f'Sent tcp: {message}', end='')
            return True
    except Exception as err:
        print(f'Failed to send tcp messages: {err}')
        print(messages)
        return False
