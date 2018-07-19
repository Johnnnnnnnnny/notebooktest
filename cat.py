import json
# 接受参数
import sys


# handle argument exceptions
if len(sys.argv)<3:
    raise Exception('老铁 参数数量必须大于2 ！')














#accept argument list
notebook_path1_lst = sys.argv[1:]


cells_lst = []

for path in notebook_path1_lst:
    # with相当于open和close
    with open(path) as notebook:
    
    
      notebook_str = notebook.read()
    
      notebook_json = json.loads(notebook_str) 
      cells = notebook_json['cells']
      cells_lst += cells
   

# 写类
class Notebook:
    def __init__(self,cell):
        self.cell = cell
    
    
    
    def __getitem__(self,index):
        return self[index]
    
note = Notebook(cells_lst)













   
target_notebook = {}
target_notebook['cells'] = cells_lst

'''
notebook1 = open(notebook_path1)
notebook1_str = notebook1.read()
notebook1_json = json.loads(notebook1_str)

cells1 = notebook1_json['cells']
notebook2 = open(notebook_path2)
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

cells2 = notebook2_json['cells']
target_cells = cells1 + cells2

del notebook1_json['cells']
target_notebook = {}
target_notebook['cells'] = cells_lst
target_notebook.update(notebook1_json)

'''
notebook_1 = json.loads(open(sys.argv[1]).read())
del notebook_1['cells']
target_notebook = {}
target_notebook['cells'] = cells_lst
target_notebook.update(notebook_1)


target_json = json.dumps(target_notebook)

# target = open('target_notebook.ipynb','w')
with open('target_notebook.ipynb','w') as endnotebook:
   endnotebook.write(target_json)