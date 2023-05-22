def is_post(request):
    return request.method == "POST"


def is_get(request):
    return request.method == "GET"


def get_sidebar_active(l1="", l2="", l3=""):
    d_active = {"is_dashboard": l1, "is_dash_categories": l2, "is_blogs": l3}

    return d_active
