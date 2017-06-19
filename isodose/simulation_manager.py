import logging
import dose
import os
import sys

from multiprocessing import Process

class SimulationManager:

    simulations = []

    @staticmethod
    def __simulation_woker__(parameters):

        class simulation_functions(dose.dose_functions):

            def organism_movement(self, Populations, pop_name, World): pass

            def organism_location(self, Populations, pop_name, World): pass

            def ecoregulate(self, World): pass

            def update_ecology(self, World, x, y, z): pass

            def update_local(self, World, x, y, z): pass

            def report(self, World): pass

            def fitness(self, Populations, pop_name): pass

            def mutation_scheme(self, organism):
                organism.genome[0].rmutate(parameters["mutation_type"],
                                           parameters["additional_mutation"])

            def prepopulation_control(self, Populations, pop_name): pass

            def mating(self, Populations, pop_name): pass

            def postpopulation_control(self, Populations, pop_name): pass

            def generation_events(self, Populations, pop_name): pass

            def population_report(self, Populations, pop_name):
                sequences = [''.join(org.genome[0].sequence) for org in Populations[pop_name].agents]
                identities = [org.status['identity'] for org in Populations[pop_name].agents]
                locations = [str(org.status['location']) for org in Populations[pop_name].agents]
                demes = [org.status['deme'] for org in Populations[pop_name].agents]
                return '\n'.join(sequences)

            def database_report(self, con, cur, start_time,
                                Populations, World, generation_count):
                try:
                    dose.database_report_populations(con, cur, start_time,
                                                     Populations, generation_count)
                except: pass
                try:
                    dose.database_report_world(con, cur, start_time,
                                               World, generation_count)
                except: pass

            def deployment_scheme(self, Populations, pop_name, World): pass

        sys.stdout = open(str(os.getpid()) + ".out", "w")
        dose.simulate(parameters, simulation_functions)
        return

    @staticmethod
    def run_simulation(parameters):
        simulation = Process(target=SimulationManager.__simulation_woker__, args=(parameters,))
        SimulationManager.simulations.append(simulation)
        simulation.start()
