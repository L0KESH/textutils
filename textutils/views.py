# I created this file

from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
# return HttpResponse(
#     '<a href = "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiJ0O-6wurmAhXTR30KHcnJA2EQPAgH">'
#     'google </a><br>\n '
#     '    <a href = "https://www.facebook.com/"> Facebook</a><br>'
#     '<a href = "http://127.0.0.1:8000/file"> file</a>')


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    djtext = request.POST.get('text', 'default')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed = ""
        puncs = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in puncs:
                analyzed = analyzed + char


        params = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed}
        # # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index , char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed ExtraSpace', 'analyzed_text': analyzed}
        # # Analyze the text
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)





def file(request):
    f = open("C:/Users/lkpal/PycharmProjects/firstsite/textutils/textutils/new.txt", 'r+')

    return HttpResponse(f.read() + '<br><a href = "/"> back </a>')
    # return HttpResponse('<a href = "/"> back </a>')    >>>> only one httpresponse work in a function
