 
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

        div_row1 = Button(description='---Domain Options---', disabled=True, layout=divider_button_layout)

        param_name1 = Button(description='type_of_death_model', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.type_of_death_model = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='initial_tumor_radius', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.initial_tumor_radius = FloatText(
          value=150,
          step=10,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Apoptosis---', disabled=True, layout=divider_button_layout)

        param_name3 = Button(description='apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.apoptosis_rate = FloatText(
          value=0.0014,
          step=0.0001,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Necrosis---', disabled=True, layout=divider_button_layout)

        param_name4 = Button(description='necrosis_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.necrosis_rate = FloatText(
          value=0.00277777777,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='necrosis_type', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.necrosis_type = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='o2_necrosis_threshold', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.o2_necrosis_threshold = FloatText(
          value=5.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='o2_necrosis_max', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.o2_necrosis_max = FloatText(
          value=2.5,
          step=0.1,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---Fluid change rates---', disabled=True, layout=divider_button_layout)

        param_name8 = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.cytoplasmic_biomass_change_rate = FloatText(
          value=0.01666666,
          step=0.001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.nuclear_biomass_change_rate = FloatText(
          value=0.00583333333,
          step=0.001,
          style=style, layout=widget_layout)

        param_name10 = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.lysed_fluid_change_rate = FloatText(
          value=0.00083333333,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name11 = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.unlysed_fluid_change_rate = FloatText(
          value=0.01666666,
          step=0.001,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='micrometer', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='mmHG', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='mmHG', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'

        desc_button2 = Button(description='1->apoptosis 2->necrosis' , tooltip='1->apoptosis 2->necrosis', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='initial tumor radius' , tooltip='initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button5 = Button(description='mean apoptosis rate' , tooltip='mean apoptosis rate', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='mean necrosis rate' , tooltip='mean necrosis rate', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='1->deterministic 2->stochastic' , tooltip='1->deterministic 2->stochastic', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button10 = Button(description='oxygen threshold level for dying with necrotic death' , tooltip='oxygen threshold level for dying with necrotic death', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='oxygen threshold level for maximum rate of necrotic death' , tooltip='oxygen threshold level for maximum rate of necrotic death', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='rate of degradation for solids in the cytoplasm other than the nucleus' , tooltip='rate of degradation for solids in the cytoplasm other than the nucleus', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='rate of degradation for nucleus solids' , tooltip='rate of degradation for nucleus solids', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='rate of fluid change (cytoplasmic fluid) after cell lysis ' , tooltip='rate of fluid change (cytoplasmic fluid) after cell lysis ', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='rate of fluid change (cytoplasmic fluid) before cell lysis' , tooltip='rate of fluid change (cytoplasmic fluid) before cell lysis', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'

        row2 = [param_name1, self.type_of_death_model, units_button2, desc_button2] 
        row3 = [param_name2, self.initial_tumor_radius, units_button3, desc_button3] 
        row5 = [param_name3, self.apoptosis_rate, units_button5, desc_button5] 
        row6 = [param_name4, self.necrosis_rate, units_button7, desc_button6] 
        row7 = [param_name5, self.necrosis_type, units_button8, desc_button7] 
        row10 = [param_name6, self.o2_necrosis_threshold, units_button9, desc_button10] 
        row11 = [param_name7, self.o2_necrosis_max, units_button10, desc_button11] 
        row12 = [param_name8, self.cytoplasmic_biomass_change_rate, units_button12, desc_button12] 
        row13 = [param_name9, self.nuclear_biomass_change_rate, units_button13, desc_button13] 
        row14 = [param_name10, self.lysed_fluid_change_rate, units_button14, desc_button14] 
        row15 = [param_name11, self.unlysed_fluid_change_rate, units_button15, desc_button15] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)

        self.tab = VBox([
          div_row1,
          box2,
          box3,
          div_row2,
          box5,
          div_row3,
          box6,
          box7,
          box10,
          box11,
          div_row4,
          box12,
          box13,
          box14,
          box15,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.type_of_death_model.value = float(uep.find('.//type_of_death_model').text)
        self.initial_tumor_radius.value = float(uep.find('.//initial_tumor_radius').text)
        self.apoptosis_rate.value = float(uep.find('.//apoptosis_rate').text)
        self.necrosis_rate.value = float(uep.find('.//necrosis_rate').text)
        self.necrosis_type.value = float(uep.find('.//necrosis_type').text)
        self.o2_necrosis_threshold.value = float(uep.find('.//o2_necrosis_threshold').text)
        self.o2_necrosis_max.value = float(uep.find('.//o2_necrosis_max').text)
        self.cytoplasmic_biomass_change_rate.value = float(uep.find('.//cytoplasmic_biomass_change_rate').text)
        self.nuclear_biomass_change_rate.value = float(uep.find('.//nuclear_biomass_change_rate').text)
        self.lysed_fluid_change_rate.value = float(uep.find('.//lysed_fluid_change_rate').text)
        self.unlysed_fluid_change_rate.value = float(uep.find('.//unlysed_fluid_change_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//type_of_death_model').text = str(self.type_of_death_model.value)
        uep.find('.//initial_tumor_radius').text = str(self.initial_tumor_radius.value)
        uep.find('.//apoptosis_rate').text = str(self.apoptosis_rate.value)
        uep.find('.//necrosis_rate').text = str(self.necrosis_rate.value)
        uep.find('.//necrosis_type').text = str(self.necrosis_type.value)
        uep.find('.//o2_necrosis_threshold').text = str(self.o2_necrosis_threshold.value)
        uep.find('.//o2_necrosis_max').text = str(self.o2_necrosis_max.value)
        uep.find('.//cytoplasmic_biomass_change_rate').text = str(self.cytoplasmic_biomass_change_rate.value)
        uep.find('.//nuclear_biomass_change_rate').text = str(self.nuclear_biomass_change_rate.value)
        uep.find('.//lysed_fluid_change_rate').text = str(self.lysed_fluid_change_rate.value)
        uep.find('.//unlysed_fluid_change_rate').text = str(self.unlysed_fluid_change_rate.value)
