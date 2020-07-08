from django.shortcuts import render


def tests(request):
    return render(request, "tests/testing_list.html")


def questions(request):
    return render(request, "tests/questions/questions_list_1.html")
