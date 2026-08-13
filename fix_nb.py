import json, io

path = 'Data_Analysis_Projects/HR_Employee_Attrition_ml_6.ipynb'
with io.open(path, encoding='utf-8') as f:
    nb = json.load(f)

# Inspect cells to find the model building cell
for i, c in enumerate(nb['cells']):
    if 'roc_auc_score' in ''.join(c['source']):
        print('CELL INDEX:', i)
        print('TYPE:', c['cell_type'])
        print('---SOURCE WITH REPR---')
        print(repr(''.join(c['source'])))

