from django.apps import apps as django_apps
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_constants.constants import YES
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .covid19_symptomatic_infections import Covid19SymptomaticInfections
from .informed_consent import InformedConsent
from .onschedule import OnSchedule


@receiver(post_save, weak=False, sender=InformedConsent,
          dispatch_uid='informed_consent_on_post_save')
def informed_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """ Put participant on schedule post consent """
    if not raw:
        if created:
            instance.registration_update_or_create()

        if is_subcohort_full():
            cohort = 'esr21'
        else:
            cohort = 'esr21_sub'

            onschedule_model = 'esr21_subject.onschedule'
            put_on_schedule(f'{cohort}_enrol_schedule', instance=instance,
                            onschedule_model=onschedule_model)

            put_on_schedule(f'{cohort}_fu_schedule', instance=instance,
                            onschedule_model=onschedule_model)


@receiver(post_save, weak=False, sender=Covid19SymptomaticInfections,
          dispatch_uid='informed_consent_on_post_save')
def covid19_symptomatic_infections_on_post_save(sender, instance, raw, created, **kwargs):

    if not raw and instance.symptomatic_infections == YES:
        onschedule_model = 'esr21_subject.onscheduleill'
        offschedule_model = 'esr21_subject.offschedule'

        illness_count = None

        latest_onschedule = onschedule_model.objects.all().latest('onschedule_datetime')
        if latest_onschedule:
            try:
                offschedule_model.objects.get(schedule_name=latest_onschedule.schedule_name)
            except offschedule_model.DoesNotExist:
                pass
            else:
                illness_count = 1 + onschedule_model.objects.all().count()

        put_on_schedule(f'esr21_illness{illness_count}_schedule', instance=instance,
                        onschedule_model=onschedule_model)


def put_on_schedule(schedule_name, onschedule_model, instance=None):

    if instance:

        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model=onschedule_model, name=schedule_name)

        onschedule_model_cls = django_apps.get_model(onschedule_model)

        try:
            onschedule_model_cls.objects.get(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)
        except onschedule_model_cls.DoesNotExist:
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.consent_datetime,
                schedule_name=schedule_name)
        else:
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)


def is_subcohort_full():
        onschedule_subcohort = OnSchedule.objects.filter(
            schedule_name='esr21_sub_enrol_schedule')

        return onschedule_subcohort.count() == 3000
