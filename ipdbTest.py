import ipdb
ipdb.set_trace()
ipdb.set_trace(context=5)   # 이곳에서 프로그램을 중단.
                            # 이하 5줄을 보여준다. 
ipdb.pm() #debug
ipdb.run('x[0] = 3')
result = ipdb.runcall(function, arg0, arg1, kwarg='foo')
result = ipdb.runeval('f(1,2) - 3')

print(result)

