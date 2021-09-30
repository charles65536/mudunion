question_id = int(input())
import math

def nest(f, x, n):
    for i in range(n):
        x = f(x)
    return x


output = [
    0,
    'I love Luogu!',
    '%d %d' % (2+4, 10-2-4),
    '%d\n%d\n%d' % (14//4, 14//4*4, 14 % 4),
    '%.3lf' % 500/3,
    (260+220)//(12+20),
    '%.4lf' % math.sqrt(6**2+9**2),
    '%d\n%d\n%d' % (100+10, 100+10-20, 0),
    '31.4159\n78.5398\n523.599',
    nest(lambda x: 2*(x+1), 1, 3),

][question_id]