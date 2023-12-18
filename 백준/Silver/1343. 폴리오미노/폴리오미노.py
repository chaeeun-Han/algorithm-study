board = input()

board = board.replace('XXXX', 'AAAA')
result = board.replace('XX', 'BB')

if 'X' in result:
    result = -1

print(result)