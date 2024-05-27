# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

days = {
    'saturday': 'this is saturday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary',
}


def days_list(request):

    days_list = list(days.keys())
    list_item = ""
    for day in days_list:
        url_path = reverse('days-of-week', args=[day])
        list_item += f'<li><a href="{url_path}">{day}</a></li>\n'

    content = f" <ul>   {list_item}   </ul>"
    return HttpResponse(content)


def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')

    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(day)


def dynamic_days(request, day):
    day_data = days.get(day)
    if day_data is not None:
        response_data = render_to_string('challenges/challenge.html')
        return HttpResponse(response_data)
    return HttpResponseNotFound('day does not exists')
