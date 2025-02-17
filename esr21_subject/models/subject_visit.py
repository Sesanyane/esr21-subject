from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager as BaseCurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin

from ..choices import VISIT_INFO_SOURCE, VISIT_REASON
from edc_appointment.models import Appointment


class CurrentSiteManager(VisitModelManager, BaseCurrentSiteManager):
    pass


class SubjectVisit(
        VisitModelMixin, CreatesMetadataModelMixin,
        ReferenceModelMixin, RequiresConsentFieldsModelMixin,
        SiteModelMixin, BaseUuidModel):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """
    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason = models.CharField(
        verbose_name='What is the reason for this visit report?',
        max_length=25,
        choices=VISIT_REASON)

    reason_missed = models.CharField(
        verbose_name='If \'Did not attend scheduled visit\' is detailed above,'
                     ' reason visit was not attended.',
        blank=True,
        null=True,
        max_length=250)

    reason_unscheduled = models.CharField(
        verbose_name='If \'Unscheduled\' above, provide reason for the '
                     'unscheduled visit',
        blank=True,
        null=True,
        max_length=25,)

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=40,
        choices=VISIT_INFO_SOURCE)

    on_site = CurrentSiteManager()

    objects = VisitModelManager()

    history = HistoricalRecords()

    class Meta(VisitModelMixin.Meta):
        pass
