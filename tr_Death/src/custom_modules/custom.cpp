/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./custom.h"

// declare cell definitions here 

Cell_Definition apoptotic_cell;
Cell_Definition necrotic_cell;
 

void create_cell_types( void )
{
	// use the same random seed so that future experiments have the 
	// same initial histogram of oncoprotein, even if threading means 
	// that future division and other events are still not identical 
	// for all runs 
	
	SeedRandom( parameters.ints("random_seed") ); // or specify a seed here 
	
	// housekeeping 
	
	initialize_default_cell_definition();
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment ); 
	
	// Name the default cell type 
	
	cell_defaults.type = 0; 
	cell_defaults.name = "default cell"; 
	
	// set default cell cycle model 

	cell_defaults.functions.cycle_model = live; 
	
	// set default_cell_functions; 
	
	cell_defaults.functions.update_phenotype = NULL; 
	
	// needed for a 2-D simulation: 
	
	/* grab code from heterogeneity */ 
	
	cell_defaults.functions.set_orientation = up_orientation; 
	cell_defaults.phenotype.geometry.polarity = 1.0;
	cell_defaults.phenotype.motility.restrict_to_2D = true; 
	
	// make sure the defaults are self-consistent. 
	
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment );
	cell_defaults.phenotype.sync_to_functions( cell_defaults.functions ); 

	// set the rate terms in the default phenotype 

	// first find index for a few key variables. 
	int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
	int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Necrosis" );
	int oxygen_substrate_index = microenvironment.find_density_index( "oxygen" ); 

	int start_index = live.find_phase_index( PhysiCell_constants::live );
	int end_index = live.find_phase_index( PhysiCell_constants::live );

	// initially no necrosis and apoptosis
	cell_defaults.phenotype.death.rates[necrosis_model_index] = 0.0; 
	cell_defaults.phenotype.death.rates[apoptosis_model_index] = 0.0; 

	// set oxygen uptake / secretion parameters for the default cell type 
	cell_defaults.phenotype.secretion.uptake_rates[oxygen_substrate_index] = 0; 
	cell_defaults.phenotype.secretion.secretion_rates[oxygen_substrate_index] = 0; 
	cell_defaults.phenotype.secretion.saturation_densities[oxygen_substrate_index] = 0; 
	cell_defaults.phenotype.volume.rupture_volume=parameters.doubles( "rupture_volume" );
	
	
	// add custom data here, if any 

	// Now, let's define another cell type. 
	// It's best to just copy the default and modify it. 
	
	// make this cell type randomly motile, less adhesive, greater survival, 
	// and less proliferative 
	
	apoptotic_cell = cell_defaults; 
	apoptotic_cell.type = 1; 
	apoptotic_cell.name = "apoptotic cell"; 
	
	// make sure the new cell type has its own reference phenotype
	apoptotic_cell.parameters.pReference_live_phenotype = &( apoptotic_cell.phenotype ); 
	
	// enable random motility 
	apoptotic_cell.phenotype.motility.is_motile = false; 
	
	// Set cell-cell adhesion to 5% of other cells 
	apoptotic_cell.phenotype.mechanics.cell_cell_adhesion_strength *= parameters.doubles( "cell_relative_adhesion" ); // 0.05; 
	
	// Set apoptosis to user paramter
	apoptotic_cell.phenotype.death.rates[apoptosis_model_index] = parameters.doubles( "apoptosis_rate" );
	apoptotic_cell.phenotype.death.current_parameters().unlysed_fluid_change_rate = parameters.doubles("unlysed_fluid_change_rate"); // apoptosis 
	apoptotic_cell.phenotype.death.current_parameters().cytoplasmic_biomass_change_rate = parameters.doubles("cytoplasmic_biomass_change_rate"); // apoptosis 
	apoptotic_cell.phenotype.death.current_parameters().nuclear_biomass_change_rate = parameters.doubles("nuclear_biomass_change_rate"); // apoptosis 
	apoptotic_cell.phenotype.death.current_parameters().lysed_fluid_change_rate = parameters.doubles("lysed_fluid_change_rate"); // lysed necrotic cell
	apoptotic_cell.phenotype.cycle.data.transition_rate(start_index,end_index) *= 0.0;
	
	
	// necrotic cell definitions
	necrotic_cell = cell_defaults;
	necrotic_cell.type = 2;
	necrotic_cell.name = "necrotic cell";
	necrotic_cell.parameters.pReference_live_phenotype = &( necrotic_cell.phenotype ); 
	necrotic_cell.phenotype.motility.is_motile = false;	
	// Set apoptosis to zero 
	necrotic_cell.phenotype.death.rates[apoptosis_model_index] = 0.0;
	necrotic_cell.phenotype.cycle.data.transition_rate(start_index,end_index) *= 0.0;
	necrotic_cell.functions.update_phenotype = update_cell_and_death_parameters_O2_based; 
	necrotic_cell.parameters.max_necrosis_rate = parameters.doubles( "necrosis_rate" );


	necrotic_cell.phenotype.death.current_parameters().unlysed_fluid_change_rate = parameters.doubles("unlysed_fluid_change_rate"); // apoptosis 
	necrotic_cell.phenotype.death.current_parameters().cytoplasmic_biomass_change_rate = parameters.doubles("cytoplasmic_biomass_change_rate"); // apoptosis 
	necrotic_cell.phenotype.death.current_parameters().nuclear_biomass_change_rate = parameters.doubles("nuclear_biomass_change_rate"); // apoptosis 
	necrotic_cell.phenotype.death.current_parameters().lysed_fluid_change_rate = parameters.doubles("lysed_fluid_change_rate"); // lysed necrotic cell
	necrotic_cell.parameters.o2_necrosis_threshold = parameters.doubles("o2_necrosis_threshold");
	necrotic_cell.parameters.o2_necrosis_max = parameters.doubles("o2_necrosis_max");
    double necrosis_type = parameters.doubles("necrosis_type");
    if  (necrosis_type == 1)
    {
        necrotic_cell.parameters.necrosis_type = PhysiCell_constants::deterministic_necrosis;
    }
    else if ( necrosis_type == 2)
    {
        necrotic_cell.parameters.necrosis_type = PhysiCell_constants::stochastic_necrosis;
    }
    else
	{
        std::cout << "Wrong parameter has been entered for necrosis type! As a default, necrosis is set as stochastic." << std::endl;
        necrotic_cell.parameters.necrosis_type = PhysiCell_constants::stochastic_necrosis;
	}
        necrotic_cell.phenotype.volume.relative_rupture_volume=parameters.doubles( "relative_rupture_volume");
	return; 
}

void setup_microenvironment( void )
{
	// set domain parameters 
	
/* now this is in XML 
	default_microenvironment_options.X_range = {-1000, 1000}; 
	default_microenvironment_options.Y_range = {-1000, 1000}; 
	default_microenvironment_options.simulate_2D = true; 
*/
	
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}
	
/* now this is in XML 	
	// no gradients need for this example 

	default_microenvironment_options.calculate_gradients = false; 
	
	// set Dirichlet conditions 

	default_microenvironment_options.outer_Dirichlet_conditions = true;
	
	// if there are more substrates, resize accordingly 
	std::vector<double> bc_vector( 1 , 38.0 ); // 5% o2
	default_microenvironment_options.Dirichlet_condition_vector = bc_vector;
	
	// set initial conditions 
	default_microenvironment_options.initial_condition_vector = { 38.0 }; 
*/
	
	// put any custom code to set non-homogeneous initial conditions or 
	// extra Dirichlet nodes here. 
	
	// initialize BioFVM 
	
	initialize_microenvironment(); 	
	
	return; 
}


void setup_tissue( void )
{
	// create some cells near the origin
	
	Cell* pCell;
	
	double cell_radius = cell_defaults.phenotype.geometry.radius; 
	double cell_spacing = 0.8 * 2.0 * cell_radius; 
	double initial_tumor_radius =  parameters.doubles("initial_tumor_radius");
	double type_of_death_model = parameters.doubles("type_of_death_model");
	
	std::vector<std::vector<double>> positions = create_cell_circle_positions(cell_radius,initial_tumor_radius);
	

	
	if (type_of_death_model == 1)
	{
		std::cout << "Creating apoptotic cells" << std::endl;
		for( int i=0; i < positions.size(); i++ )
		{
			pCell = create_cell(apoptotic_cell);
			pCell->assign_position( positions[i] );
		}
	}
	else if ( type_of_death_model == 2)
	{
		std::cout << "Creating necrotic cells" << std::endl;
		for( int i=0; i < positions.size(); i++ )
		{
			pCell = create_cell(necrotic_cell);
			pCell->assign_position( positions[i] );
            //std::cout << pCell->parameters.necrosis_type << std::endl;
		}
	}
	else
	{
		std::cout << "Wrong parameter has been entered for type of death model! As a default, apoptotic cells are seeded." << std::endl;
		std::cout << "Creating apoptotic cells" << std::endl;
		for( int i=0; i < positions.size(); i++ )
		{
			pCell = create_cell(apoptotic_cell);
			pCell->assign_position( positions[i] );
		}
	}
	
	return; 
}

std::vector<std::string> my_coloring_function( Cell* pCell )
{	
	std::vector<std::string> output = false_cell_coloring_cytometry(pCell); 
		
	if( pCell->phenotype.death.dead == false && pCell->type == 1 )
	{
		 output[0] = "lightblue"; 
		 output[2] = "blue"; 
	}
	
	if( pCell->phenotype.death.dead == true && pCell->type == 1 )
	{
		 output[0] = "pink"; 
		 output[2] = "purple"; 
	}
	
	if( pCell->phenotype.death.dead == false && pCell->type == 2 )
	{
		 output[0] = "green"; 
		 output[2] = "darkgreen"; 
	}

/* 	if( pCell->phenotype.death.dead == true && pCell->type == 2 )
	{
		 output[0] = "pink"; 
		 output[2] = "purple"; 
	} */
	
	return output; 
}


std::vector<std::vector<double>> create_cell_circle_positions(double cell_radius, double sphere_radius)
{
	std::vector<std::vector<double>> cells;
	int xc=0,yc=0,zc=0;
	double x_spacing= cell_radius*sqrt(3);
	double y_spacing= cell_radius*sqrt(3);

	std::vector<double> tempPoint(3,0.0);
	// std::vector<double> cylinder_center(3,0.0);
	
	for(double x=-sphere_radius;x<sphere_radius;x+=x_spacing, xc++)
	{
		for(double y=-sphere_radius;y<sphere_radius;y+=y_spacing, yc++)
		{
			tempPoint[1]=y + (xc%2) * cell_radius;
			tempPoint[0]=x;
			tempPoint[2]=0;
			if(sqrt(norm_squared(tempPoint))< sphere_radius)
			{ cells.push_back(tempPoint); }
		}
	}
	return cells;
}


void oxygen_based_necrosis_death( Cell* pCell, Phenotype& phenotype, double dt )
{
	// supported cycle models:
		// advanced_Ki67_cycle_model= 0;
		// basic_Ki67_cycle_model=1
		// live_cells_cycle_model = 5; 
	
	if( phenotype.death.dead == true )
	{ return; }
	
	// set up shortcuts to find the Q and K(1) phases (assuming Ki67 basic or advanced model)
	static bool indices_initiated = false; 
	static int start_phase_index; // Q_phase_index; 
	static int end_phase_index; // K_phase_index;
	static int necrosis_index; 
	
	static int oxygen_substrate_index = pCell->get_microenvironment()->find_density_index( "oxygen" ); 
	double pO2 = (pCell->nearest_density_vector())[oxygen_substrate_index];
    
    double necrosis_type = parameters.doubles( "necrosis_type" );
	if ( necrosis_type == 1)
	{
    if( pO2 < pCell->parameters.o2_proliferation_threshold );
    {
        pCell->phenotype.death.rates[necrosis_index] = pCell->parameters.max_necrosis_rate;
    }
		
	}
	else if ( necrosis_type == 2)
	{
    if( indices_initiated == false )
	{

	
	// this multiplier is for linear interpolation of the oxygen value 
	double multiplier = 1.0;
	if( pO2 < pCell->parameters.o2_proliferation_saturation )
	{
		multiplier = ( pO2 - pCell->parameters.o2_proliferation_threshold ) 
			/ ( pCell->parameters.o2_proliferation_saturation - pCell->parameters.o2_proliferation_threshold );
	}
	if( pO2 < pCell->parameters.o2_proliferation_threshold )
	{ 
		multiplier = 0.0; 
	}
	
	// now, update the appropriate cycle transition rate 
	
	phenotype.cycle.data.transition_rate(start_phase_index,end_phase_index) = multiplier * 
		pCell->parameters.pReference_live_phenotype->cycle.data.transition_rate(start_phase_index,end_phase_index);
	
	// Update necrosis rate
	multiplier = 0.0;
	if( pO2 < pCell->parameters.o2_necrosis_threshold )
	{
		multiplier = ( pCell->parameters.o2_necrosis_threshold - pO2 ) 
			/ ( pCell->parameters.o2_necrosis_threshold - pCell->parameters.o2_necrosis_max );
	}
	if( pO2 < pCell->parameters.o2_necrosis_max )
	{ 
		multiplier = 1.0; 
	}	
	
	// now, update the necrosis rate 
	
	pCell->phenotype.death.rates[necrosis_index] = multiplier * pCell->parameters.max_necrosis_rate; 
	
	}
	else
	{
		std::cout << "Non-sense parameter has been entered! As a default, apoptotic cells are seeded." << std::endl;
		std::cout << "Seeding deterministic necrosis" << std::endl;
		necrotic_cell.parameters.necrosis_type = PhysiCell_constants::deterministic_necrosis;;
	}
    
    
    
    }
    
	
	return; 
}