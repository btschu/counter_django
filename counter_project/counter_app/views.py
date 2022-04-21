from django.shortcuts import render, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] = request.session['counter'] + 1
        request.session['actual_count'] = request.session['actual_count'] + 1
    else:
        request.session['counter'] = 0
        request.session['actual_count'] = 0
    return render(request, 'index.html')

def add_two(request):
    request.session['counter'] += 1
    return redirect('/')

def increase_by_amount(request):
    amount = int(request.POST['views'])
    request.session['counter'] += amount - 1
    return redirect('/')

def destroy_session(request):
    del request.session['counter']
    return redirect('/')