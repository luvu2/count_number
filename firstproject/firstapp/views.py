from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    count = 0
    data = request.POST['sentences']

    for i in data:
        count += len(i)
    print(count)
    
    return render(request, 'result.html', {'input_sentences': data, 'count' : count})