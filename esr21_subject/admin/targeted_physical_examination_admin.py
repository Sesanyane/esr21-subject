from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import TargetedPhysicalExaminationForm
from ..models import TargetedPhysicalExamination
from ..admin_site import esr21_subject_admin


@admin.register(TargetedPhysicalExamination, site=esr21_subject_admin)
class TargetedPhysicalExaminationAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = TargetedPhysicalExaminationForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'physical_exam_performed',
                'reason_not_done',
                'area_performed',
                'exam_date',
                'abnormalities',
                'if_abnormalities',
            ),
        }),
        audit_fieldset_tuple)

    radio_fields = {'physical_exam_performed': admin.VERTICAL,
                    'reason_not_done': admin.VERTICAL,
                    'abnormalities': admin.VERTICAL,
                    'if_abnormalities': admin.VERTICAL,
                    }
