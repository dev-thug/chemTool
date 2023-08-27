from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import AllChem

from utill import chemical, medicinal_compound, name_translation

if __name__ == '__main__':
    cm = chemical()
    mc = medicinal_compound()
    name_trans = name_translation()
    drug = dict()
    drug["Mesalamine"] = "C1=CC(=C(C=C1N)C(=O)O)O"
    drug["Sulfasalazine"] = "C1=CC=NC(=C1)NS(=O)(=O)C2=CC=C(C=C2)N=NC3=CC(=C(C=C3)O)C(=O)O"
    drug["Azathioprine"] = "CN1C=NC(=C1SC2=NC=NC3=C2NC=N3)[N+](=O)[O-]"
    drug["Mercaptopurine"] = "C1=NC2=C(N1)C(=S)N=CN2"

    # drug["Metformin"] = "CN(C)C(=N)N=C(N)N"
    # drug["Alpha glucosidase inhibitor"] = "CC1=CC(=O)C2=C(O1)C=C(C(=C2O)C3C(C(C(C(O3)CO)O)O)O)O"
    # drug["DPP-4"] = "CC(C)(C)OCC1C(=O)NCCN1C(=O)CC(CC2=CC(=C(C=C2F)F)F)N"


    crohn = ["Mercaptopurine"]
    # "Mesalamine", "Sulfasalazine", "Azathioprine","Mercaptopurine"
    fpgen = AllChem.GetRDKitFPGenerator()

    result = {}
    errors_num = []

    for molecular in crohn:
        base_molecular = fpgen.GetFingerprint(Chem.MolFromSmiles(drug[molecular]))
        for name in mc.names():
            sigma = []
            for num in mc.ids_of(name):

                if Chem.MolFromSmiles(cm.smiles_for(num)):
                    comparative_molecular = fpgen.GetFingerprint(Chem.MolFromSmiles(cm.smiles_for(num)))
                    similarity = DataStructs.TanimotoSimilarity(base_molecular, comparative_molecular)
                    sigma.append(similarity)
                else:
                    errors_num.append(num)
            result[name] = sum(sigma) / len(sigma)
    sorted_data_descending = sorted(result.items(), key=lambda x: x[1], reverse=True)
    sorted_dict_descending = dict(sorted_data_descending[:5])
    print(sorted_dict_descending)

    nt = name_translation()
    for i in sorted_dict_descending:
        print(nt.korean_of(i), sorted_dict_descending[i])
    print("errors ", len(errors_num))
    print("errors ",errors_num)

