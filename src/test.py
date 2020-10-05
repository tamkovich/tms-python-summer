from src.main import add

assert add(1, 2) == 3, '1 + 2 = 3'
assert add(15, 189) == 204, 'It is stupid test'
assert add(200, 100) == 300
assert add('3', 2) == 'Bad value'
assert add([], 2) == 'Bad value'
assert add({}, 2) == 'Bad value'
assert add(None, 2) == 'Bad value'
assert add(sum, 2) == 'Bad value'

print('All test passed successfully')
