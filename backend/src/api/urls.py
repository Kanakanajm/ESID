from rest_framework.routers import SimpleRouter

from src.api import views

api_router = SimpleRouter()

api_router.register(r'restrictions', views.RestrictionsViewSet, basename='restriction')
api_router.register(r'scenarios', views.ScenarioViewSet, basename='scenario')
api_router.register(r'simulationmodels', views.SimulationModelViewSet, basename='simulationmodel')
api_router.register(r'nodes', views.NodesViewSet, basename="node")
