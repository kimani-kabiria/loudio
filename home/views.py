from django.shortcuts import render_to_response


def index_view(request):
    context = {'index': 'home'}
    return render_to_response('home/index.html', context)

