import re
from functools import reduce
from collections import OrderedDict


def splitlines(s):
    s = re.sub(' ', '', s)
    return re.split('[\r\n]+', s)


def find_all_subexpr(stmt):
    assert isinstance(stmt, str)
    pattern = '[-+]?[0-9]*\([^\(\)]+\)\w?'
    return re.findall(pattern, stmt)


def parse_atom(atom):
    var_lst = sorted(list(set(re.findall('[a-z]{1}', atom))))
    coefs = OrderedDict()
    terms = re.split(
        '[\n]+',
        re.sub('[\(\)]?', '', atom).replace('+', '\n+').replace('-', '\n-')
    )
    print('terms: ', terms)
    for v in var_lst:
        tmp = reduce(
            lambda x, y: x + re.findall(r'[-+]?[0-9]*{v}$'.format(v=v), y),
            [[]] + terms)
        coefs[v] = sum(
            list(map(lambda x: int(x[:-1]) if x[:-1] not in ['-', '+'] else int(
                x[:-1] + '1'), tmp))
        )
    # key 'ZZ' coresponds to constant terms
    tmp = coefs.get('ZZ', []) + \
          reduce(lambda x, y: x + re.findall(r'[-+]?[0-9]+$', y), [[]] + terms)
    coefs['ZZ'] = sum(
        list(
            map(lambda x: int(x) if x not in ['-', '+'] else int(x + '1'), tmp))
    )

    for k in list(coefs.keys()):
        if coefs[k] == 0:
            coefs.pop(k)
    return coefs


def parse_subexpr(subexpr):
    m_l = re.findall('[-+]*[0-9]*\(', subexpr)[0][:-1]
    multiplier_l = int(m_l + '1') if m_l in ['', '+', '-'] else int(m_l)
    m_r = re.findall('\)\w*', subexpr)[0][1:]
    multiplier_r = None if m_r in [''] else m_r
    atom = re.findall('\([^\(\)]+\)', subexpr)[0][1:-1]
    coefs = parse_atom(atom)
    return coefs, multiplier_l, multiplier_r


def simplify_subexpression(subexpr):
    coefs, multiplier_l, multiplier_r = parse_subexpr(subexpr)
    print('coefs: ', coefs)
    for k in coefs.keys():
        coefs[k] = coefs[k] * multiplier_l
    polynomial = ''
    for k in coefs.keys():
        polynomial = polynomial + ('+' if coefs[k] >= 0 else '-') + str(
            abs(coefs[k])) + k
        if multiplier_r:
            polynomial = polynomial + multiplier_r
    polynomial = re.sub('ZZ', '', polynomial)
    print('polinimial: ', polynomial)
    return polynomial


def simplify(stmt):
    stmt = '(' + stmt + ')'
    subexpr_lst = find_all_subexpr(stmt)
    while len(subexpr_lst) > 0:
        for sub in subexpr_lst:
            stmt = stmt.replace(sub, simplify_subexpression(sub))
        subexpr_lst = find_all_subexpr(stmt)
        print('stmt: ', stmt)
    return stmt


def main():
    msg = '1c-4-((2-(1a-3a+3x-(4a-2z+3-1c)-3c)-4+2a-4)+(((1-1d)+1b+1-(2-3x-1+2-3))-2)-2-3c+3d)'
    ans = ''
    for s in splitlines(msg):
        ans = ans + simplify(s) + '\n'
    print('ans: ', ans)


if __name__ == '__main__':
    main()
