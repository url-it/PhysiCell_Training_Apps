 
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
        divider_button_layout={'width':'40%'}

        div_row1 = Button(description='---Parameters---', disabled=True, layout=divider_button_layout)

        param_name1 = Button(description='Volume_target_solid_cytoplasmic', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.Volume_target_solid_cytoplasmic = FloatText(
          value=1488.5,
          step=100,
          style=style, layout=widget_layout)

        param_name2 = Button(description='Volume_target_solid_nuclear', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.Volume_target_solid_nuclear = FloatText(
          value=1135.0,
          step=100,
          style=style, layout=widget_layout)

        param_name3 = Button(description='Volume_target_fluid_fraction', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'tan'

        self.Volume_target_fluid_fraction = FloatText(
          value=0.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='Volume_cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.Volume_cytoplasmic_biomass_change_rate = FloatText(
          value=0.0045,
          step=0.001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='Volume_nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.Volume_nuclear_biomass_change_rate = FloatText(
          value=0.0055,
          step=0.001,
          style=style, layout=widget_layout)

        param_name6 = Button(description='Volume_fluid_change_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.Volume_fluid_change_rate = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='Volume_calcification_rate', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.Volume_calcification_rate = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---State Variables---', disabled=True, layout=divider_button_layout)

        param_name8 = Button(description='Volume_Total', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.Volume_Total = FloatText(
          value=2494,
          step=100,
          style=style, layout=widget_layout)

        param_name9 = Button(description='Volume_solid', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.Volume_solid = FloatText(
          value=623.5,
          step=10,
          style=style, layout=widget_layout)

        param_name10 = Button(description='Volume_fluid', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.Volume_fluid = FloatText(
          value=1870.5,
          step=100,
          style=style, layout=widget_layout)

        param_name11 = Button(description='Volume_fluid_fraction', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.Volume_fluid_fraction = FloatText(
          value=0.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='Volume_nuclear', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.Volume_nuclear = FloatText(
          value=540.0,
          step=10,
          style=style, layout=widget_layout)

        param_name13 = Button(description='Volume_nuclear_solid', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.Volume_nuclear_solid = FloatText(
          value=135.0,
          step=10,
          style=style, layout=widget_layout)

        param_name14 = Button(description='Volume_nuclear_fluid', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'lightgreen'

        self.Volume_nuclear_fluid = FloatText(
          value=405.0,
          step=10,
          style=style, layout=widget_layout)

        param_name15 = Button(description='Volume_cytoplasmic', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'tan'

        self.Volume_cytoplasmic = FloatText(
          value=1954.0,
          step=100,
          style=style, layout=widget_layout)

        param_name16 = Button(description='Volume_cytoplasmic_solid', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'lightgreen'

        self.Volume_cytoplasmic_solid = FloatText(
          value=488.5,
          step=10,
          style=style, layout=widget_layout)

        param_name17 = Button(description='Volume_cytoplasmic_fluid', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'tan'

        self.Volume_cytoplasmic_fluid = FloatText(
          value=1465.5,
          step=100,
          style=style, layout=widget_layout)

        param_name18 = Button(description='Volume_clacification_fraction', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'lightgreen'

        self.Volume_clacification_fraction = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='Volume_cytoplasmic_to_nuclear_ratio', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'tan'

        self.Volume_cytoplasmic_to_nuclear_ratio = FloatText(
          value=3.6,
          step=0.1,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Method to change all Volume parameters consistenly ---', disabled=True, layout=divider_button_layout)

        param_name20 = Button(description='use_function_multiply_by_ratio', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'lightgreen'

        self.use_function_multiply_by_ratio = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name21 = Button(description='multiplication_ratio_value', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'tan'

        self.multiplication_ratio_value = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'
        units_button14 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'lightgreen'
        units_button15 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'tan'
        units_button16 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'lightgreen'
        units_button17 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'tan'
        units_button18 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'lightgreen'
        units_button19 = Button(description='cubic_micron', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'tan'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'lightgreen'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'tan'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'

        desc_button2 = Button(description='default=1488.5' , tooltip='default=1488.5', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='default=1135.0' , tooltip='default=1135.0', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='default=0.75' , tooltip='default=0.75', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='default=0.0045' , tooltip='default=0.0045', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='default=0.0055' , tooltip='default=0.0055', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='default=0.05' , tooltip='default=0.05', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='default=0.0' , tooltip='default=0.0', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='default=2494' , tooltip='default=2494', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='default=623.5' , tooltip='default=623.5', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='default=1870.5' , tooltip='default=1870.5', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='default=0.75' , tooltip='default=0.75', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='default=540.0' , tooltip='default=540.0', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='default=135.0' , tooltip='default=135.0', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='default=405.0' , tooltip='default=405.0', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='default=1954.0' , tooltip='default=1954.0', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='default=488.5' , tooltip='default=488.5', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='default=1465.5' , tooltip='default=1465.5', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='default=0.0' , tooltip='default=0.0', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='default=3.6' , tooltip='default=3.6', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button23 = Button(description='recommended method to change volume in your simulation' , tooltip='recommended method to change volume in your simulation', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='multiplies all parameters accordingly to scale current volume' , tooltip='multiplies all parameters accordingly to scale current volume', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'

        row2 = [param_name1, self.Volume_target_solid_cytoplasmic, units_button2, desc_button2] 
        row3 = [param_name2, self.Volume_target_solid_nuclear, units_button3, desc_button3] 
        row4 = [param_name3, self.Volume_target_fluid_fraction, units_button4, desc_button4] 
        row5 = [param_name4, self.Volume_cytoplasmic_biomass_change_rate, units_button5, desc_button5] 
        row6 = [param_name5, self.Volume_nuclear_biomass_change_rate, units_button6, desc_button6] 
        row7 = [param_name6, self.Volume_fluid_change_rate, units_button7, desc_button7] 
        row8 = [param_name7, self.Volume_calcification_rate, units_button8, desc_button8] 
        row9 = [param_name8, self.Volume_Total, units_button10, desc_button9] 
        row10 = [param_name9, self.Volume_solid, units_button11, desc_button10] 
        row11 = [param_name10, self.Volume_fluid, units_button12, desc_button11] 
        row12 = [param_name11, self.Volume_fluid_fraction, units_button13, desc_button12] 
        row13 = [param_name12, self.Volume_nuclear, units_button14, desc_button13] 
        row14 = [param_name13, self.Volume_nuclear_solid, units_button15, desc_button14] 
        row15 = [param_name14, self.Volume_nuclear_fluid, units_button16, desc_button15] 
        row16 = [param_name15, self.Volume_cytoplasmic, units_button17, desc_button16] 
        row17 = [param_name16, self.Volume_cytoplasmic_solid, units_button18, desc_button17] 
        row18 = [param_name17, self.Volume_cytoplasmic_fluid, units_button19, desc_button18] 
        row19 = [param_name18, self.Volume_clacification_fraction, units_button20, desc_button19] 
        row20 = [param_name19, self.Volume_cytoplasmic_to_nuclear_ratio, units_button21, desc_button20] 
        row23 = [param_name20, self.use_function_multiply_by_ratio, units_button23, desc_button23] 
        row24 = [param_name21, self.multiplication_ratio_value, units_button24, desc_button24] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)

        self.tab = VBox([
          div_row1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          div_row2,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          div_row3,
          box23,
          box24,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.Volume_target_solid_cytoplasmic.value = float(uep.find('.//Volume_target_solid_cytoplasmic').text)
        self.Volume_target_solid_nuclear.value = float(uep.find('.//Volume_target_solid_nuclear').text)
        self.Volume_target_fluid_fraction.value = float(uep.find('.//Volume_target_fluid_fraction').text)
        self.Volume_cytoplasmic_biomass_change_rate.value = float(uep.find('.//Volume_cytoplasmic_biomass_change_rate').text)
        self.Volume_nuclear_biomass_change_rate.value = float(uep.find('.//Volume_nuclear_biomass_change_rate').text)
        self.Volume_fluid_change_rate.value = float(uep.find('.//Volume_fluid_change_rate').text)
        self.Volume_calcification_rate.value = float(uep.find('.//Volume_calcification_rate').text)
        self.Volume_Total.value = float(uep.find('.//Volume_Total').text)
        self.Volume_solid.value = float(uep.find('.//Volume_solid').text)
        self.Volume_fluid.value = float(uep.find('.//Volume_fluid').text)
        self.Volume_fluid_fraction.value = float(uep.find('.//Volume_fluid_fraction').text)
        self.Volume_nuclear.value = float(uep.find('.//Volume_nuclear').text)
        self.Volume_nuclear_solid.value = float(uep.find('.//Volume_nuclear_solid').text)
        self.Volume_nuclear_fluid.value = float(uep.find('.//Volume_nuclear_fluid').text)
        self.Volume_cytoplasmic.value = float(uep.find('.//Volume_cytoplasmic').text)
        self.Volume_cytoplasmic_solid.value = float(uep.find('.//Volume_cytoplasmic_solid').text)
        self.Volume_cytoplasmic_fluid.value = float(uep.find('.//Volume_cytoplasmic_fluid').text)
        self.Volume_clacification_fraction.value = float(uep.find('.//Volume_clacification_fraction').text)
        self.Volume_cytoplasmic_to_nuclear_ratio.value = float(uep.find('.//Volume_cytoplasmic_to_nuclear_ratio').text)
        self.use_function_multiply_by_ratio.value = ('true' == (uep.find('.//use_function_multiply_by_ratio').text.lower()) )
        self.multiplication_ratio_value.value = float(uep.find('.//multiplication_ratio_value').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//Volume_target_solid_cytoplasmic').text = str(self.Volume_target_solid_cytoplasmic.value)
        uep.find('.//Volume_target_solid_nuclear').text = str(self.Volume_target_solid_nuclear.value)
        uep.find('.//Volume_target_fluid_fraction').text = str(self.Volume_target_fluid_fraction.value)
        uep.find('.//Volume_cytoplasmic_biomass_change_rate').text = str(self.Volume_cytoplasmic_biomass_change_rate.value)
        uep.find('.//Volume_nuclear_biomass_change_rate').text = str(self.Volume_nuclear_biomass_change_rate.value)
        uep.find('.//Volume_fluid_change_rate').text = str(self.Volume_fluid_change_rate.value)
        uep.find('.//Volume_calcification_rate').text = str(self.Volume_calcification_rate.value)
        uep.find('.//Volume_Total').text = str(self.Volume_Total.value)
        uep.find('.//Volume_solid').text = str(self.Volume_solid.value)
        uep.find('.//Volume_fluid').text = str(self.Volume_fluid.value)
        uep.find('.//Volume_fluid_fraction').text = str(self.Volume_fluid_fraction.value)
        uep.find('.//Volume_nuclear').text = str(self.Volume_nuclear.value)
        uep.find('.//Volume_nuclear_solid').text = str(self.Volume_nuclear_solid.value)
        uep.find('.//Volume_nuclear_fluid').text = str(self.Volume_nuclear_fluid.value)
        uep.find('.//Volume_cytoplasmic').text = str(self.Volume_cytoplasmic.value)
        uep.find('.//Volume_cytoplasmic_solid').text = str(self.Volume_cytoplasmic_solid.value)
        uep.find('.//Volume_cytoplasmic_fluid').text = str(self.Volume_cytoplasmic_fluid.value)
        uep.find('.//Volume_clacification_fraction').text = str(self.Volume_clacification_fraction.value)
        uep.find('.//Volume_cytoplasmic_to_nuclear_ratio').text = str(self.Volume_cytoplasmic_to_nuclear_ratio.value)
        uep.find('.//use_function_multiply_by_ratio').text = str(self.use_function_multiply_by_ratio.value)
        uep.find('.//multiplication_ratio_value').text = str(self.multiplication_ratio_value.value)
