from django.shortcuts import render


def tests(request):
    return render(request, "tests/testing_list.html")
