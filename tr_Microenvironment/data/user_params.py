 
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
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='make_Dirichlet_node', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.make_Dirichlet_node = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name2 = Button(description='Dirichlet_node_position_x', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.Dirichlet_node_position_x = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name3 = Button(description='Dirichlet_node_position_y', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'tan'

        self.Dirichlet_node_position_y = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name4 = Button(description='set_Dirichlet_condition_for_oxygen', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.set_Dirichlet_condition_for_oxygen = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name5 = Button(description='Concentration_of_oxygen', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.Concentration_of_oxygen = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name6 = Button(description='set_Dirichlet_condition_for_Chemical_A', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.set_Dirichlet_condition_for_Chemical_A = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name7 = Button(description='Concentration_of_Chemical_A', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.Concentration_of_Chemical_A = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'tan'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'

        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='value on x-axis for dirichlet node; make sure it is within domain size' , tooltip='value on x-axis for dirichlet node; make sure it is within domain size', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='value on y-axis for dirichlet node; make sure it is within domain size' , tooltip='value on y-axis for dirichlet node; make sure it is within domain size', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='concentration of oxygen at this specific Dirichlet node' , tooltip='concentration of oxygen at this specific Dirichlet node', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='concentration of Chemical_A at this specific Dirichlet node' , tooltip='concentration of Chemical_A at this specific Dirichlet node', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'

        row2 = [param_name1, self.make_Dirichlet_node, units_button1, desc_button2] 
        row3 = [param_name2, self.Dirichlet_node_position_x, units_button2, desc_button3] 
        row4 = [param_name3, self.Dirichlet_node_position_y, units_button3, desc_button4] 
        row5 = [param_name4, self.set_Dirichlet_condition_for_oxygen, units_button4, desc_button5] 
        row6 = [param_name5, self.Concentration_of_oxygen, units_button5, desc_button6] 
        row7 = [param_name6, self.set_Dirichlet_condition_for_Chemical_A, units_button6, desc_button7] 
        row8 = [param_name7, self.Concentration_of_Chemical_A, units_button7, desc_button8] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)

        self.tab = VBox([
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.make_Dirichlet_node.value = ('true' == (uep.find('.//make_Dirichlet_node').text.lower()) )
        self.Dirichlet_node_position_x.value = float(uep.find('.//Dirichlet_node_position_x').text)
        self.Dirichlet_node_position_y.value = float(uep.find('.//Dirichlet_node_position_y').text)
        self.set_Dirichlet_condition_for_oxygen.value = ('true' == (uep.find('.//set_Dirichlet_condition_for_oxygen').text.lower()) )
        self.Concentration_of_oxygen.value = float(uep.find('.//Concentration_of_oxygen').text)
        self.set_Dirichlet_condition_for_Chemical_A.value = ('true' == (uep.find('.//set_Dirichlet_condition_for_Chemical_A').text.lower()) )
        self.Concentration_of_Chemical_A.value = float(uep.find('.//Concentration_of_Chemical_A').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//make_Dirichlet_node').text = str(self.make_Dirichlet_node.value)
        uep.find('.//Dirichlet_node_position_x').text = str(self.Dirichlet_node_position_x.value)
        uep.find('.//Dirichlet_node_position_y').text = str(self.Dirichlet_node_position_y.value)
        uep.find('.//set_Dirichlet_condition_for_oxygen').text = str(self.set_Dirichlet_condition_for_oxygen.value)
        uep.find('.//Concentration_of_oxygen').text = str(self.Concentration_of_oxygen.value)
        uep.find('.//set_Dirichlet_condition_for_Chemical_A').text = str(self.set_Dirichlet_condition_for_Chemical_A.value)
        uep.find('.//Concentration_of_Chemical_A').text = str(self.Concentration_of_Chemical_A.value)
