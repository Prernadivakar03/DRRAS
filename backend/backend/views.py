from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to DRRAS API! Use /api/ to access endpoints.<br>"
                        "Use /api/cluster  to access cluster  endpoint<br>"
                        "Use /api/allocate-resources  to access usersInput resources allocation endpoint<br>"
                        "Use /api/run-optimization  to access historic data allocation  endpoint<br>")
