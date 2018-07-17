import json

notebook1 = open('Untitled1.ipynb')
notebook1_str = notebook1.read()
notebook1_json = json.loads(notebook1_str)

cells1 = notebook1_json['cells']
notebook2 = open('Untitled2.ipynb')
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

cells2 = notebook2_json['cells']
target_cells = cells1 + cells2


target_json = json.dumps(target_cells)

target = open('target_notebook.ipynb','w')
target.write(target_json)