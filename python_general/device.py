class Router:
    '''Router class'''
    def __init__(self, model, version, ip_add):
        '''initialize values'''
        self.model = model
        self.version = version
        self.ip_add  = ip_add
    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f' Router model                 :{self.model}\n'\
                   f' Software version             :{self.version}\n'\
                   f' Router management if         :{self.ip_add}'     
        return desc

class Switch(Router):
    '''Switch class'''
    def getdesc(self):
        '''return a formatted description of the switch'''
        desc = f' Switch model                 :{self.model}\n'\
                    f' Software version             :{self.version}\n'\
                   f' Switch management if         :{self.ip_add}'     
        return desc