from django.http import HttpResponse
from nodeconf.models import Nodes
from django.template import loader

# Create your views here.
def index(request):
    node_list = Nodes.objects
    template = loader.get_template('nodes/index.html')
    context = {
        'node_list': node_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, node_id):
    node = Nodes.objects(id=node_id).first()
    template = loader.get_template('nodes/details.html')
    context = {
        'node': node.node,
        'classes': node.classes,
    }
    return HttpResponse(template.render(context, request))
