 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='number_of_cells', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.number_of_cells = IntText(
          value=3,
          step=0.1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='is_motile', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.is_motile = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name3 = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.persistence_time = FloatText(
          value=30,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='migration_speed', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.migration_speed = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.migration_bias = FloatText(
          value=0.8,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='bias_migration_angle', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.bias_migration_angle = FloatText(
          value=30,
          step=1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='degree', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'

        desc_button1 = Button(description='number of cell tracks to simulate', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='true if cells are motile', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='mean persistence time', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='migration speed', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='migration bias parameter', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='migration bias angle respect to x-axis', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'

        row1 = [param_name1, self.number_of_cells, units_button1, desc_button1] 
        row2 = [param_name2, self.is_motile, units_button2, desc_button2] 
        row3 = [param_name3, self.persistence_time, units_button3, desc_button3] 
        row4 = [param_name4, self.migration_speed, units_button4, desc_button4] 
        row5 = [param_name5, self.migration_bias, units_button5, desc_button5] 
        row6 = [param_name6, self.bias_migration_angle, units_button6, desc_button6] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.number_of_cells.value = int(uep.find('.//number_of_cells').text)
        self.is_motile.value = ('true' == (uep.find('.//is_motile').text.lower()) )
        self.persistence_time.value = float(uep.find('.//persistence_time').text)
        self.migration_speed.value = float(uep.find('.//migration_speed').text)
        self.migration_bias.value = float(uep.find('.//migration_bias').text)
        self.bias_migration_angle.value = float(uep.find('.//bias_migration_angle').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//number_of_cells').text = str(self.number_of_cells.value)
        uep.find('.//is_motile').text = str(self.is_motile.value)
        uep.find('.//persistence_time').text = str(self.persistence_time.value)
        uep.find('.//migration_speed').text = str(self.migration_speed.value)
        uep.find('.//migration_bias').text = str(self.migration_bias.value)
        uep.find('.//bias_migration_angle').text = str(self.bias_migration_angle.value)
