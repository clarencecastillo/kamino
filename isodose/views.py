from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from simulation_manager import SimulationManager

@api_view(['GET'])
def start_simulation(request):
    """
    Starts a simulation.
    """

    parameters = {
      "simulation_name": "kamino_sim",
      "population_names": ['pop_01'],
      "population_locations": [[(0,0,0)]],
      "deployment_code": 1,
      "chromosome_bases": ['0','1'],
      "background_mutation": 0.1,
      "additional_mutation": 0,
      "mutation_type": 'point',
      "chromosome_size": 30,
      "genome_size": 1,
      "max_tape_length": 50,
      "clean_cell": True,
      "interpret_chromosome": True,
      "max_codon": 2000,
      "population_size": 100,
      "eco_cell_capacity": 100,
      "world_x": 5,
      "world_y": 5,
      "world_z": 5,
      "goal": 0,
      "maximum_generations": 100,
      "fossilized_ratio": 0.01,
      "fossilized_frequency": 20,
      "print_frequency": 10,
      "ragaraja_version": 0,
      "ragaraja_instructions": ['000', '001', '010',
                                '011', '100', '101'],
      "eco_buried_frequency": 100,
      "database_file": "simulation.db",
      "database_logging_frequency": 1
     }

    SimulationManager.run_simulation(parameters)
    return Response('started simulation!', status=status.HTTP_200_OK)
