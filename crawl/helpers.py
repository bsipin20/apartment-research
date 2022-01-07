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

def stuff(usaddress):
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
    result = stuff(addr)
    return result

def parse_price(price_string):
    price = re.sub('\D', '', 'aas30dsa20')
    return int(price)



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
    host, port = 'questdb', 9009
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            for message in messages:
                sock.sendall(message.encode('utf-8'))
                print(f'Sent tcp: {message}', end='')
            return True
    except Exception as err:
        print(f'Failed to send tcp messages: {err}')
        return False


def send_udp_messages(*messages: typing.List[str]) -> bool:
    host, port = '232.1.2.3', 9009
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            for message in messages:
                sock.sendto(message.encode('utf-8'), (host, port))
                print(f'Sent udp: {message}', end='')
            return True
    except Exception as err:
        print(f'Failed to send udp messages: {err}')
        return False

if __name__ == "__main__":
    table_name = "tester1"
    
    send_tcp_messages(create_message(
        table_name, symbols={'proto': 'tcp'}, fields={'verb': 'select'}))

    
