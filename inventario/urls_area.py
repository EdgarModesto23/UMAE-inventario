from django.urls import path, re_path
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('', views.AreaViewSet, basename= 'Area')


cama_router = routers.NestedDefaultRouter(router, '', lookup='id')
cama_router.register('camas', views.CamaViewSet, basename='cama-area')

area_router = routers.NestedDefaultRouter(router, '', lookup='id')
area_router.register('equipos_area', views.AreaEquipoViewSet, basename='area-equipo')

checklist_router = routers.NestedDefaultRouter(area_router, 'equipos_area', lookup = 'area_equipo')
checklist_router.register('checklist', views.CheckListCrearViewSet, basename='checklist_area')

# URLConf
urlpatterns = router.urls + cama_router.urls + area_router.urls + checklist_router.urls