import pandas as pd


class chemical:
    def __init__(self, file = "data/chemical_property.xlsx"):
        cp = pd.read_excel(file, engine="openpyxl")
        self.smiles = dict()
        n = len(cp)
        for row in cp.itertuples():
            self.smiles[row.ID] = row.SMILES

    def smiles_for(self,id):
        return self.smiles[id]

class medicinal_compound:
    def __init__(self, file = "data/medicinal_compound.xlsx"):
        mc = pd.read_excel(file, engine="openpyxl")
        self.medicine = dict()
        for row in mc.itertuples():
            if row.ID == 0:
                continue
            if row.LATIN in self.medicine.keys():
                self.medicine[row.LATIN].add(row.ID)
            else:
                ids = set()
                ids.add(row.ID)
                self.medicine[row.LATIN] =ids

    def ids_of(self, name):
        return self.medicine[name]

    def names(self):
        return self.medicine.keys()

class name_translation:
    def __init__(self, file = "data/medicinal_material.xlsx"):
        names_df = pd.read_excel(file, engine="openpyxl")
        self.names = dict()
        for row in names_df.itertuples():
            self.names[str(row.LATIN).strip()] = str(row.KOREAN).strip()

    def korean_of(self, latin):
        return self.names[latin]
