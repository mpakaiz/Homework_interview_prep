from Stack import Stack

obj = '(((([{}]))))'
obj2 = '[([])((([[[]]])))]{()}'
obj3 = '{{[()]}}'
obj4 = '}{}'
obj5 = '{{[(])]}}'
obj6 = '[[{())}]'


def balance(obj):

    not_b = 'Несбалансированно'
    b = 'Сбалансированно'

    l_brackets = {
        '(': 's',
        '[': 'sq',
        '{': 'f'
    }
    r_brackets = {
        ')': 's',
        ']': 'sq',
        '}': 'f'
    }

    res = []
    obj_list = list(obj)
    stack = Stack(res)
    for i in obj_list:
        if i in l_brackets.keys():
            stack.push(i)
        if i in r_brackets.keys():
            if stack.is_empty():
                print('Несбалансированно')
                return not_b
            if l_brackets[res[-1]] == r_brackets[i]:
                stack.pop()
            else:
                print('Несбалансированно')
                return not_b
    if stack.size() != 0:
        print('Несбалансированно')
        return not_b
    print('Сбалансированно')
    return b


if __name__ == "__main__":
    balance(obj)
    balance(obj2)
    balance(obj3)
    balance(obj4)
    balance(obj5)
    balance(obj6)
