from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

days = {
    'saturday' : 'this is saturday in disctionary',
    'sunday'   : 'this is sunday in disctionary',
    'monday'   : 'this is monday in disctionary',
    'tuesday'  : 'this is tuesday in disctionary',
    'wednesday': 'this is wednesday in disctionary',
    'thursday': 'this is thursday in disctionary',
    'friday'   : 'this is friday in disctionary',
}

def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')

    redirect_day = days_names[day - 1]
    return HttpResponseRedirect(f'/days/{redirect_day}')
    # return HttpResponse(day)
def dynamic_days(request, day):
    day_data = days.get(day)
    if day_data is not None:
        return HttpResponse(f'day is : {day} and data is {day_data}')

    return HttpResponseNotFound('day does not exists')

