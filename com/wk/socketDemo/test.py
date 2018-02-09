#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
from urllib import request


# http://101.200.47.50/solo?nsukey=NZ%2FGSsdPuu%2BYCsqpjQMG%2FJidrX9jI5Q8tWKofAXGfxRcyOODQYeSzVUmN3E9e6RfPHCscfByWQKCr5DY6zbltaplAmZ5mRqpgnbhmuyzNCRpnWbsRNfX6BwR0QH6dtCFwkI1EG9O89LN4p8kcfqfgcDoH9eGaEE%2Byg6SwHvwZXC0r4F7y%2FBkqk3N72nvzyODWFsnuHapOgdPXh0n1gxd%2Bg%3D%3D
# url = 'http://101.200.47.50/solo'
# requests.get(url= url, )


for i in range(1, 5000) :
    with request.urlopen(
            'http://101.200.47.50/solo?nsukey=NZ%2FGSsdPuu%2BYCsqpjQMG%2FJidrX9jI5Q8tWKofAXGfxRcyOODQYeSzVUmN3E9e6RfPHCscfByWQKCr5DY6zbltaplAmZ5mRqpgnbhmuyzNCRpnWbsRNfX6BwR0QH6dtCFwkI1EG9O89LN4p8kcfqfgcDoH9eGaEE%2Byg6SwHvwZXC0r4F7y%2FBkqk3N72nvzyODWFsnuHapOgdPXh0n1gxd%2Bg%3D%3D') as f:
        data = f.read()
        print('status:', f.status, f.reason)
        print(i)


