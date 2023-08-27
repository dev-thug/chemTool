
import pandas as pd
import csv

from utill import chemical, medicinal_compound, name_translation


mc = pd.read_excel("data/medicinal_compound.xlsx", engine="openpyxl")
medicine = dict()
chem = chemical()
for row in mc.itertuples():
    if row.ID == 0:
        continue

    medicine[row.COMPOUND] = row.ID


dynamic = pd.read_excel("data/dynamic.xlsx", engine="openpyxl",sheet_name=2)
smiles = dict()
n = len(dynamic)
output = [["smiles", "result"]]
model = "t(1/2)"
for row in dynamic.itertuples():
    if row.측정항목 == model:
        if row.측정결과 == "NA":
            continue
        target = str(row.측정결과).split()[0]
        if target== "nan":
            continue
        if row.측정성분.lower() not in medicine.keys():
            continue
        output.append([chem.smiles_for(medicine[row.측정성분.lower()]), target])


#
# cp = pd.read_excel("data/chemical_property.xlsx", engine="openpyxl")
# smiles = dict()
# n = len(cp)
# for row in cp.itertuples():
#     smiles[row.ID] = row.SMILES
#
# c_protein = pd.read_excel("data/chemical_protein.xlsx", engine="openpyxl")
# protein = dict()
# genes = set()
# for row in c_protein.itertuples():
#     genes.add(row.PREFERRED_NAME)
#     if row.ID in protein.keys():
#         protein[row.ID].add(row.PREFERRED_NAME)
#     else:
#         preferred = set()
#         preferred.add(row.PREFERRED_NAME)
#         protein[row.ID] = preferred
#
# # print(protein)
# # print(genes)
# genes = list(genes)
# genes_dic = {}
# for index, gene in enumerate(genes, 1):
#     genes_dic[gene] = index
#
# col = ["smiles"] + sorted(genes)
# leng = len(col)
# arr = [col]
# # arr.append([0]*leng)
#
# for p in protein:
#     r = [0] * leng
#     r[0]= smiles[p]
#
#     for g_key in list(protein[p]):
#         r[genes_dic[g_key]] = 1
#     arr.append(r)
#
#
name = f"{model}.csv"

with open(name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output)

print("Data saved to data.csv")
