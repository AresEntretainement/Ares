INSTALL_PACKAGE_INFOS = ['Proprieties','DefaultValues','Field','Questions','Buttons']
class Pao:

    def __init__(self,GeneralLib):
        self.Doc = GeneralLib
        for key in self.Doc.keys():
            if (key == 'Field'):
                for newKey in self.Doc['Field']:
                    Query = "self." + newKey + " = " + str(self.Doc['Field'][newKey]) 
                    exec(Query)
                    for insideKey in self.Doc['Field'][newKey].keys():
                        if (isinstance(self.Doc['Field'][newKey][insideKey], dict)):
                            Queryed = "self." + insideKey + " = " + str(self.Doc['Field'][newKey][insideKey])
                        elif(self.Doc['Field'][newKey][insideKey].isdigit()):
                            Queryed = "self." + insideKey + " = " + str(self.Doc['Field'][newKey][insideKey])
                        else:
                            Queryed = "self." + insideKey + " = '" + str(self.Doc['Field'][newKey][insideKey] + "'")
                        exec(Queryed)
            else:
                Query = "self." + key + " = " + str(self.Doc[key]) 
                exec(Query)
                for insideKey in self.Doc[key].keys():
                    if(self.Doc[key][insideKey].isdigit()):
                        Queryed = "self." + insideKey + " = " + str(self.Doc[key][insideKey])
                    else:
                        Queryed = "self." + insideKey + " = '" + str(self.Doc[key][insideKey] + "'")
                    exec(Queryed)
                    
    def affichage(self):
        print(self.Title)
        print(self.Prefix)