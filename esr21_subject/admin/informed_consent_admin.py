from collections import OrderedDict
from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from edc_consent.actions import (flag_as_verified_against_paper,
                                 unflag_as_verified_against_paper)
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    audit_fieldset_tuple, audit_fields, ModelAdminNextUrlRedirectMixin,
    ModelAdminNextUrlRedirectError, ModelAdminReplaceLabelTextMixin,
    ModelAdminFormInstructionsMixin)
from edc_model_admin import ModelAdminBasicMixin, ModelAdminReadOnlyMixin
from simple_history.admin import SimpleHistoryAdmin

from .exportaction_mixin import ExportActionMixin
from ..forms import InformedConsentForm
from ..models import InformedConsent
from .modeladmin_mixins import VersionControlMixin
from ..admin_site import esr21_subject_admin


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin, ModelAdminReadOnlyMixin,
                      VersionControlMixin, ModelAdminFormInstructionsMixin,
                      ExportActionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    enable_nav_sidebar = False

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['form_version'] = self.get_form_version(request)

        return super().add_view(
            request, form_url=form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):

        extra_context = extra_context or {}

        extra_context['form_version'] = self.get_form_version(request)

        return super().change_view(
            request, object_id, form_url=form_url, extra_context=extra_context)


@admin.register(InformedConsent, site=esr21_subject_admin)
class InformedConsentAdmin(ModelAdminBasicMixin, ModelAdminMixin,
                           SimpleHistoryAdmin, admin.ModelAdmin):

    form = InformedConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'consent_datetime',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'gender',
                'gender_other',
                'dob',
                'is_dob_estimated',
                'identity',
                'identity_type',
                'confirm_identity',
                'hiv_testing_consent',
                'consent_to_participate',
                'optional_sample_collection',
            ),
        }),
        audit_fieldset_tuple
    )

    radio_fields = {
        'language': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'identity_type': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'hiv_testing_consent': admin.VERTICAL,
        'optional_sample_collection': admin.VERTICAL,
        'consent_to_participate': admin.VERTICAL,
    }

    list_display = ('subject_identifier',
                    'verified_by',
                    'is_verified',
                    'is_verified_datetime',
                    'first_name',
                    'initials',
                    'gender',
                    'dob',
                    'consent_datetime',
                    'created',
                    'modified',
                    'user_created',
                    'user_modified')

    search_fields = ('subject_identifier', 'dob',)

    def get_actions(self, request):

        super_actions = super().get_actions(request)

        if ('esr21_subject.change_informedconsent'
                in request.user.get_group_permissions()):

            consent_actions = [
                flag_as_verified_against_paper,
                unflag_as_verified_against_paper]

            # Add actions from this ModelAdmin.
            actions = (self.get_action(action) for action in consent_actions)
            # get_action might have returned None, so filter any of those out.
            actions = filter(None, actions)

            actions = self._filter_actions_by_permissions(request, actions)
            # Convert the actions into an OrderedDict keyed by name.
            actions = OrderedDict(
                (name, (func, name, desc))
                for func, name, desc in actions
            )

            super_actions.update(actions)

        return super_actions

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj=obj) + audit_fields
