import os
import sys
from re import X
import ipywidgets as widgets
from IPython.display import clear_output


%cd /content/
!rm -rf /content/module_import/
!git clone https://github.com/hut5269/Civil3D_to_ICPR4.git
sys.path.insert(0,'/content/module_import')

def checkbox_change_event(change):
    if dropdown.disabled:
        dropdown.disabled = False
    else:
        dropdown.disabled = True

option_1 = "Create Simulation Files"
option_2 = "Correct Pipe Flow Direction"
option_3 = "Create Boundary Files"
option_4 = "Create Basin File"
unit_hydrographs = [['UH256', '256'], ['UH323', '323'], ['UH484', '484']]
drop_options     = []

for unit_hydrograph in unit_hydrographs:
    drop_options.append(unit_hydrograph[1])

checkbox_1 = widgets.Checkbox(value=False, description=option_1)
checkbox_2 = widgets.Checkbox(value=False, description=option_2)
checkbox_3 = widgets.Checkbox(value=False, description=option_3)
checkbox_4 = widgets.Checkbox(value=False, description=option_4)
dropdown   = widgets.Dropdown(
                options=drop_options,
                value=drop_options[1],
                description='Peaking Factor',
                disabled=True,)

checkboxes = [checkbox_1, checkbox_2, checkbox_3, checkbox_4]

clear_output()
print("Select script(s) to run")
checkbox_4.observe(checkbox_change_event, names='value')
display(checkbox_1, checkbox_2, checkbox_3, checkbox_4, dropdown)