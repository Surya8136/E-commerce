from menu.models import Cuisines

def links(request):
    c=Cuisines.objects.all()
    return {'links':c}
