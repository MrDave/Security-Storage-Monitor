from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.duration_functions import get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):

    current_visitors = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visitor in current_visitors:
        duration = get_duration(visitor)
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard,
                'entered_at': localtime(visitor.entered_at),
                'duration': format_duration(duration),
                'is_strange': is_visit_long(visitor),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
