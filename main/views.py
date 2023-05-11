from django.shortcuts import render

import io
import sys

out = io.StringIO()
sys.stdout = out


def index(request):
    code = None
    context = {}
    if request.method == 'POST':
        code = request.POST.get('code')
        context['code'] = code
        try:

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') 
            #execute code
            exec(code)  
            sys.stdout.close()
            sys.stdout = original_stdout 
            output = open('file.txt', 'r').read()

        except Exception as e:

            sys.stdout = original_stdout
            output = e

        context['result'] = output
    return render(request,'index.html',context)
