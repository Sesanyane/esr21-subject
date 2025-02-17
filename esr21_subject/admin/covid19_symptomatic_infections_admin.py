from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import esr21_subject_admin
from ..forms import Covid19SymptomaticInfectionsForm
from ..models import Covid19SymptomaticInfections
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Covid19SymptomaticInfections, site=esr21_subject_admin)
class Covid19SymptomaticInfectionsAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = Covid19SymptomaticInfectionsForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'symptomatic_experiences',
                'symptomatic_infections',
                'date_of_infection',
                'infection_status',
                'visits',
                'hospitalisation_date',
            )}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'symptomatic_experiences': admin.VERTICAL,
        'infection_status': admin.VERTICAL,
        'visits': admin.VERTICAL, }

    filter_horizontal = ("symptomatic_infections",)