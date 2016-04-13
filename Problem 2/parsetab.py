
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '93BC1B8494082B2F4E676322B17A35C0'
    
_lr_action_items = {'HEADER':([0,],[1,]),'$end':([1,2,5,10,12,],[-1,0,-2,-5,-3,]),'.':([6,],[9,]),'/':([4,11,],[8,13,]),'INTEGER':([0,3,7,8,9,12,13,14,],[4,6,6,11,12,-3,14,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'date':([0,],[3,]),'start':([0,],[2,]),'float':([3,7,],[7,10,]),'data':([0,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> HEADER','start',1,'p_start','plyProject5.py',38),
  ('start -> data','start',1,'p_start','plyProject5.py',39),
  ('float -> INTEGER . INTEGER','float',3,'p_float','plyProject5.py',45),
  ('date -> INTEGER / INTEGER / INTEGER','date',5,'p_date','plyProject5.py',49),
  ('data -> date float float','data',3,'p_data','plyProject5.py',53),
]