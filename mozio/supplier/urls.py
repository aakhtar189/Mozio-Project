from django.conf.urls import url
from supplier import views as supplier_views


urlpatterns = [
    url(r'^add-supplier/$', supplier_views.add_supplier, name="add_supplier"),
    url(r'^edit-supplier/(?P<supplier_id>[0-9]+)/$', supplier_views.edit_supplier, name='edit_supplier'),
    url(r'^delete-supplier/(?P<supplier_id>[0-9]+)/$', supplier_views.delete_supplier, name='delete_supplier'),

]