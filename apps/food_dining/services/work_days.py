# Python
from datetime import time

# Rest-Framework
from rest_framework.generics import get_object_or_404

# Model
from food_dining.models import WorkingHours


def create_default_working_days(model, obj, field: str):
    """
        default working hours and days for `model`
    """
    holidays = ['saturday', 'sunday']

    for day in WorkingHours.WEEK_DAYS:
        hour = WorkingHours.objects.create(
            week_day=day[0],
            start_time=None if day[0] in holidays else time(hour=9),
            end_time=None if day[0] in holidays else time(hour=17),
            is_holiday=True if day[0] in holidays else False
        )
        data = {field: obj, 'working_hour': hour}
        model.objects.create(**data)


def update_working_days(pk: int, week_day, stat_time, end_time, is_holiday):
    working_hours: WorkingHours = get_object_or_404(WorkingHours, pk=pk)
    working_hours.week_day = week_day
    working_hours.start_time = stat_time
    working_hours.end_time = end_time
    working_hours.is_holiday = is_holiday
    working_hours.save()
