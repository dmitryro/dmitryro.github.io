def test(*args, **kwargs):
   foo = args[0]
   bar = kwargs['bar']
   print(f"FOO {foo} BAR {bar}")



test('oh', bar='ah')

