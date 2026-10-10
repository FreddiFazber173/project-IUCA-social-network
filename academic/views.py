from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Schedule

@login_required
def schedule_view(request):
    """
    Безопасный просмотр расписания с проверкой привязки пользователя к факультету.
    """
    user = request.user
    
    # Бэкенд-проверка: если у студента не выбран факультет в профиле
    if not user.faculty:
        messages.warning(request, "Для просмотра расписания укажите ваш факультет в профиле.")
        return redirect('profile')  # Перенаправляем на заполнение профиля
    
    # Оптимизированный запрос с select_related для предотвращения N+1 проблемы
    schedules = Schedule.objects.filter(faculty=user.faculty).select_related(
        'faculty', 
        'subject', 
        'teacher__user'
    ).order_by('weekday', 'start_time')

    # Группировка по дням недели
    schedule_by_day = {}
    for day_num, day_name in Schedule.WEEKDAY_CHOICES:
        schedule_by_day[day_name] = [s for s in schedules if s.weekday == day_num]

    return render(request, 'academic/schedule.html', {
        'schedule_by_day': schedule_by_day,
        'faculty': user.faculty
    })