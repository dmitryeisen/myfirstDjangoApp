from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import boardmodul, comment
from django.urls import reverse
def index(request):
    latest_boardmodul_list = boardmodul.objects.order_by('-pub_date')[:5]
    return render(request, 'boardmodul/list.html', {'latest_boardmodul_list': latest_boardmodul_list})
def detail(request, boardmodul_id):
    try:
        a = boardmodul.objects.get( id = boardmodul_id )
    except:
        raise Http404("Seite existiert nicht")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'boardmodul/detail.html', {'boardmodul': a, 'latest_comments_list': latest_comments_list})
def leave_comment(request, boardmodul_id):
    try:
        a = boardmodul.objects.get( id = boardmodul_id )
    except:
        raise Http404("Seite existiert nicht")
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('boardmodul:detail', args = (a.id,)) )
