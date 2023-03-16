from users.choices import *
from users.models import PollingImage
from django.shortcuts import render, redirect

# Create your views here.
def polling_view(request):
    return render(request, 'polling/polling.html')

def result_view(request):
    if request.method == 'POST':
        button_id = request.POST.get('button_id')

        updated_values = {
            'user_vote' : button_id,
            'name_vote' : button_id,
        }

        PollingImage.objects.update_or_create(
            user_id = request.user,
            defaults = updated_values
            )
        
        return redirect('/polling/result')
    
    vdict = {}

    a = []
    b = []
    c = []

    votings = PollingImage.objects.all()
    
    for i in votings:
        if i.user_vote in vdict:
            vdict[i.user_vote] += 1
        else:
            vdict[i.user_vote] = 1

    for j in sorted(vdict.items())[:10]:
        for k in IMAGE_CHOICES:
            if j[0] == k[0]: a.append(k[1])
        for k in NAME_CHOICES:
            if j[0] == k[0]: b.append(k[1])
        c.append(j[1])


    result = [[x, y, z] for x, y, z in zip(a, b, c)]
    context = {
        'data': result
    }
    print(context)
        
    return render(request, 'polling/result.html', context)
