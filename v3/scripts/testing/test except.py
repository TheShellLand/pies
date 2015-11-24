

try:
    import platform_specific_module
except Exception as exc:
    print(exc)
    #raise exc
    #raise


try:
    raise Exception('spam', 'eggs', 'toast')
except Exception as inst:
    print(inst.args)
    x, y, z = inst.args
    print(x, y, z)
