# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from core.models import TradeInfo
from django.contrib.auth import get_user_model


def index(request):
    # template = loader.get_template('tradeinfo/index.html')
    user_id = 2
    cur_user = get_user_model().objects.filter(id=user_id).values()
    tradeinfo_2 = TradeInfo.objects.filter(user_id=user_id).values()

    d = []
    for _ in range(len(tradeinfo_2)):
        d.append(tradeinfo_2[_]['profit'])

    print(tradeinfo_2)
    context = {'data': d, 'user': cur_user[0], 'len': len(d)}
    return render(request, 'tradeinfo/index.html', context)


def detail(request, tradeinfo_id):
    context = {}
    return render(request, "You're looking at tradeinfo %s." % tradeinfo_id, context)
