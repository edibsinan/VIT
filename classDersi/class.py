class Ucus():
    havayolu="THY"
    def __init__ (self,kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

print(Ucus.havayolu)
ucus2=Ucus('th123','ist','ank',60,300,50)
kalkis=ucus2.kalkis
varis=ucus2.varis
print(varis)
print(kalkis)
