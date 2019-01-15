from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from isodose.models import Simulation
from serializers import SimulationSerializer
from simulation_manager import SimulationManager

class SimulationViewSet(ModelViewSet):

    serializer_class = SimulationSerializer
    queryset = Simulation.objects.all()

    # # List simulations
    # def get(self, request, format=None):
    #     simulations = Simulation.objects.all()
    #     serializer = SimulationSerializer(simulations, many=True)
    #     return Response(serializer.data)
    #
    # # Create new simulation
    # def post(self, request, format=None):
    #     serializer = SimulationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def run(self, request, pk=None):
        simulation = Simulation.objects.get(pk=pk)
        SimulationManager.run_simulation(simulation)
        return Response('started!')