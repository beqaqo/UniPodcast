
from src.admin_views import SecureModelView

class CategoryView(SecureModelView):
   
    can_edit = True
    can_delete = False
    can_create = False
  
