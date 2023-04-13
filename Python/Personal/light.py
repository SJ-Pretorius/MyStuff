class light:
    def __init__(self,type,watts,lumens, working):
        self.type = type
        self.watts = watts
        self.lumens = lumens
        self.working = working
    
    def on(self):
        if self.working == 1:
            print('Light is on!')
            self.status=1
        else:
            print('The light is blown!')
            pass

    def off(self):
        print('Light is off!')
        self.status=0

oldLight = light('halogen',65,100,0)
newLight = light("led",5,250,1)

print(f'{newLight.lumens} Lumens')
newLight.on()
print(newLight.status)
print()
print(f'{oldLight.lumens} Lumens')
oldLight.on()
print(oldLight.working)
