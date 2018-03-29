def str2tuple(s):
    if len(s) > 1:
        if s[0] + s[-1] == '()':
            return eval(s)
        elif s[0] + s[-1] == '(\n':
            return str2tuple(s[:-1])
        else:
            return (s,)
    else:
        return ()
