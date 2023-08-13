from django.utils.timezone import localtime


def get_duration(visitor):
    entering_time = localtime(visitor.entered_at)
    leaving_time = localtime(visitor.leaved_at)
    duration = leaving_time - entering_time
    return duration


def format_duration(duration):
    visit_duration = duration.total_seconds()
    hours = int(visit_duration // 3600)
    minutes = int((visit_duration % 3600) // 60)
    seconds = int((visit_duration % 3600) % 60)
    formatted_duration = f"{hours}:{minutes}:{seconds}"
    return formatted_duration


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes*60
