class AutentiqueMethod():
    def autentique_key(self, key):
        return False
    
class AutentiqueMethod2():
    def autentique_key(self, key):
        if key == "abc":
            return True
        return False


class Autentique():
    mecanismos=[AutentiqueMethod, AutentiqueMethod2]

    def autentique(self, key):
        isauth =False
        for mec in self.mecanismos:
            if mec.autentique_key(key):
                isauth = True
                break
        return isauth