from django.utils.translation import ugettext_lazy as _

from edc_constants.constants import (OTHER, NOT_APPLICABLE, UNKNOWN, POS, NEG,
                                     IND, MALE, FEMALE, YES, NO)
from edc_lab.constants import TUBE
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
from edc_visit_tracking.constants import MISSED_VISIT, COMPLETED_PROTOCOL_VISIT

from .constants import NATIONAL_ID, NATIONAL_ID_RECEIPT

ACTION_TAKEN = (
    ('dose_not_changed', 'Dose not changed'),
    ('drug_withdrawal', 'Drug withdrawal'),
    (NOT_APPLICABLE, NOT_APPLICABLE),
    (UNKNOWN, UNKNOWN),
)

ALCOHOL_STATUS_CHOICES = (
    ('never_drunk_alcohol', 'Never drunk alcohol'),
    ('previously_drunk_alcohol', 'Previously drunk alcohol'),
    ('occasionally_drinks_alcohol', 'Occasionally drinks alcohol'),
    ('currently_drinks_alcohol', 'Currently drinks alcohol'),

)

AE_GRADE = (
    ('mild', 'Mild (Grade 1)'),
    ('moderate', 'Moderate (Grade 2)'),
    ('severe', 'Severe (Grade 3)'),
    ('life_threatening', 'Life-threatening (Grade 4)'),
    ('fatal', 'Fatal (Grade 5)'),
)

AE_NUMBER = (
    ('ae_log_line_number1', 'AE log line number1'),
    ('ae_log_line_number1', 'AE log line number2'),
)

AESI_CATEGORY = (
    ('generalized_convulsion', 'Generalized convulsion'),
    ('guillain_barre_syndrome', 'Guillain-Barre syndrome'),
    ('acute_disseminated', 'Acute disseminated encephalomyelitis'),
    ('other_neuro_events', 'Other neurologic events'),
    ('thrombotic', 'Thrombotic or thromboembolic or neurovascular events'),
    ('Thrombocytopenia', 'Thrombocytopenia'),
    ('vasculitides', 'Vasculitides'),
    ('anaphylaxis', 'Anaphylaxis'),
    ('vaccine_assoc_resp_disease',
     'Vaccine-associated enhanced respiratory disease'),
    ('immune_mediated_cond', 'Potential immune-mediated conditions'),
)

AGREE_DISAGREE = (
    ('strongly_disagree', 'Strongly disagree'),
    ('undecided', 'Undecided'),
    ('strongly_agree', 'Strongly agree'),
)

CONCOMITANT_ROUTE = (
    ('auricular_otic', 'Auricular(otic)'),
    ('buccal', 'Buccal'),
    ('endotracheal', 'Endotracheal'),
    ('epidural', 'Epidural'),
    ('intra-articular', 'Intra-articular'),
    ('intracardiac', 'Intracardiac'),
    ('intradermal', 'Intradermal'),
    ('intralesional', 'Intralesional'),
    ('intramuscular', 'Intramuscular'),
    ('intraocular', 'Intraocular'),
    ('intraperitoneal', 'Intraperitoneal'),
    ('intrathecal', 'Intrathecal'),
    ('intratumor', 'Intratumor'),
    ('intravenous', 'Intravenous'),
    ('intravenous_bolus', 'Intravenous Bolus'),
    ('intravenous_drip', 'Intravenous Drip'),
    ('irrigation', 'Irrigation'),
    ('microdialysis', 'Microdialysis'),
    ('nasal', 'Nasal'),
    ('ophthalmic', 'Ophthalmic'),
    ('oral', 'Oral'),
    ('parenteral', 'Parenteral'),
    ('percutaneous', 'Percutaneous'),
    ('rectal', 'Rectal'),
    ('respiratory_inhalation', 'Respiratory Inhalation'),
    ('subcutaneous', 'Subcutaneous'),
    ('sublingual', 'Sublingual'),
    ('topical', 'Topical'),
    ('transdermal', 'Transdermal'),
    ('vaginal', 'Vaginal'),
    (UNKNOWN, 'Unknown'),
    (OTHER, 'Other'),
)

EMPLOYMENT_STATUS = (
    ('formal-wage_employment_part_time', 'Formal wage employment (Part-time)'),
    ('formal_wage_employment-full_time)',
        'Formal wage employment (full-time)'),
    ('self_employed_full_time)', 'Self-employed (full time)'),
    ('self_employed_part_time)', 'Self-employed (part time)'),
    ('adhoc_work', 'Ad-hoc work'),
    ('Seasonal_employment', 'Seasonal employment'),
    (OTHER, 'Other (specify)'),)

FREQUENCY = (('BID', 'BID'),
             ('TID', 'TID',),
             ('QID', 'QID'),
             ('QOD', 'QOD'),
             ('PRN', 'PRD'),
             ('Once', 'Once'),
             ('one_time_per_week', 'One Time Per Week'),
             ('every_month', 'Every Month'),
             ('QH', 'QH'),
             ('Q2H', 'Q2H'),
             ('Q3H', 'Q3H'),
             ('Q4H', 'Q4H'),
             ('Q6H', 'Q6H'),
             ('Q8H', 'Q8H'),
             ('Q12H', 'Q12H'),
             (UNKNOWN, 'Unknown'),
             (OTHER, 'Other'))

GENDER_OTHER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, _('Other')),
)

GENERAL_APPEARANCE = (
    ('normal', 'Normal'),
    ('abnormal', 'Abnormal'),
)

HOSPITALISATION_OUTCOME = (
    ('expired', 'Expired'),
    ('hospice_care', 'Home: Hospice Care'),
    ('self_care', 'Home: Self Care'),
    ('hospice_medical_facility', 'Hospice Medical Facility'),
    ('inpatient_rehabilitation', 'Inpatient Rehabilitation'),
    ('intermediate_care_facility', 'Intermediate Care Facility'),
    ('medical_advice', 'Left Against Medical Advice'),
    ('long_term_care_hospital', 'Long Term Care Hospital'),
    ('nursing_facility', 'Nursing Facility'),
    ('unit_ward_change', 'Unit/Ward Change'),
)

HOSPITALISATION_REASON = (
    ('covid19_related_symptoms', 'COVID-19 related symptoms'),
    (OTHER, 'Other'),
)

HOSPITALISATION_STATUS = (
    ('er', 'ER'),
    ('regular_ward', 'Regular Ward'),
    ('icu_hdu', 'ICU/HDU'),
)
INFECTION_STATUS = (
    ('seronegative', 'Seronegative'),
    ('seropositive', 'Seropositive'),)

IDENTITY_TYPE = (
    (NATIONAL_ID, 'National Identity Card'),
    (NATIONAL_ID_RECEIPT, 'National Identity Card Receipt'),
    ('passport', 'Passport'),
    (OTHER, 'Other'),
)

ITEM_TYPE = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TUBE, 'Tube'),
    ('swab', 'Swab'),
    (OTHER, 'Other'),
)

LANGUAGE = (
    ('setswana', 'Setswana'),
    ('setswana', 'English'),
)

LEFT_RIGHT = (
    ('left_deltoid', 'Left deltoid'),
    ('right_arm', 'Right deltoid'),
    (OTHER, 'Other (specify)')
)

MARITAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Cohabiting', 'Cohabiting'),
    ('Widowed', 'Widowed'),
    ('Divorced', 'Divorced'),
    (OTHER, 'Other, specify'))

MODE_TRANSPORT = (
    ('public_transport', 'Public Transport'),
    ('private_transport', 'Private Transport'))

MED_HISTORY_NO = (
    ('mh_log_line_number1', 'MH log line number1'),
    ('mh_log_line_number2', 'MH log line number2'),
)

OUTCOME = (
    ('not_resolved', 'Not recovered/ not resolved'),
    ('resolved', 'Recovered / resolved'),
    ('resolved_with_sequelae', 'Recovered / resolved with sequelae'),
    ('resolving', 'Recovering / resolving'),
    ('fatal', 'Fatal / Death'),
    (UNKNOWN, UNKNOWN),
)

POS_NEG_IND = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate')
)

PREGNANCY_TEST_TYPE = (
    ('urine_serum', 'Urine/Serum'),
    ('hgg', 'HCG'),)

REASON = (
    ('not_collected', 'Not collected'),
    ('not_required', 'Not required at this visit'),
    ('measurement_skipped', 'Measurement skipped at this visit'),
    ('subject_refused', 'Subject refused'),
    ('equipment_malfunction', 'Equipment malfunction'),
    ('staff_unavailable', 'Staff unavailable'),
    ('no_information', 'No further information'),
    (NOT_APPLICABLE, 'Not applicable'),
)

REASON_NOT_DRAWN = (
    ('not_collected', 'Not collected'),
    ('not_required', 'Not required at this visit'),
    ('measurement_skipped', 'Measurement skipped at this visit'),
    ('subject_refused', 'Subject refused'),
    ('equipment_malfunction', 'Equipment malfunction'),
    ('staff_unavailable', 'Staff unavailable'),
    ('no_further_information', 'No further information'),
    (NOT_APPLICABLE, 'Not applicable'),
)

ROUTE = (
    ('intramuscular', 'Intramuscular'),
    ('oral', 'Oral'),
)

SETTLEMENT_TYPE = (
    ('urban', 'Urban'),
    ('rural', 'Rural'),
)

SMOKED_STATUS_CHOICES = (
    ('never_smoked', 'Never Smoked'),
    ('previous_smoker', 'Previous Smoker'),
    ('occasional_smoker', 'Occasional Smoker'),
    ('current_smoking', 'Current Smoker'),
)

STATUS = (
    ('resolved', 'Resolved'),
    ('ongoing', 'Ongoing'),
    ('death', 'Death'),
)

TEMP_UNITS = (
    ('celcius', 'Celcius (ºC)'),
    ('fahrenheit', 'Fahrenheit (ºF)'),
    (NOT_APPLICABLE, 'Not Applicable')
)

TREATMENT_RELATIONSHIP = (
    ('related', 'Related'),
    ('not_related', 'Not Related'),
)

UNIT_OPTIONS = (
    ('ampule', 'Ampule'),
    ('bag', 'Bag'),
    ('bar', 'Bar'),
    ('bolus', 'Bolus'),
    ('bottle', 'Bottle'),
    ('box', 'Box'),
    ('can', 'Can'),
    ('capsule', 'Capsule'),
    ('cartridge', 'Cartridge'),
    ('coat', 'Coat'),
    ('container', 'Container'),
    ('cylinder', 'Cylinder'),
    ('disk', 'Disk'),
    ('drum', 'Drum'),
    ('grain', 'Grain'),
    ('homeopathic_dilution', 'Homeopathic dilution'),
    ('implant', 'Implant'),
    ('inch', 'Inch'),
    ('inhalation', 'Inhalation'),
    ('jar', 'Jar'),
    ('kallikrein_inhibitor_unit', 'Kallikrein inhibitor unit'),
    ('kit', 'Kit'),
    ('L', 'L'),
    ('MCi', 'MCi'),
    ('mEq', 'mEq'),
    ('mmol', 'mmol'),
    ('ng', 'ng'),
    ('nmol', 'nmol'),
    ('ounce', 'Ounce'),
    ('uCi', 'uCi'),
    ('um', 'um'),
    ('umol', 'umol'),
    ('gram', 'gram'),
    ('mg', 'mg'),
    ('mg/dL', 'mg/dL'),
    ('puff', 'Puff'),
    ('Tbsp', 'Tbsp'),
    ('Tsp', 'tsp'),
    ('cup', 'cup'),
    ('drop', 'Drop'),
    ('iu_l', 'IU / L'),
    ('mg_m2', 'mg / m2'),
    ('ug', 'Ug'),
    ('patch_dosing_unit', 'Patch Dosing Unit'),
    ('pellet_dosing_unit', 'Pellet Dosing Unit'),
    ('%', '%'),
    ('%_v_v)', '% (v / v)'),
    ('%_w_v)', '% (w / v)'),
    ('%_w_w)', '% (w / w)'),
    ('spray', 'Spray'),
    ('tablet', 'Tablet'),
    ('ug_l', 'ug / L'),
    ('iu_ml', 'IU / mL'),
    (OTHER, 'Other'),
    ('gtt', 'gtt'),
    ('iu_kg', 'IU / kg'),
    ('kiu', 'kIU'),
    ('mbq', 'MBq'),
    ('mg_kg', 'mg / kg'),
    ('ug_kg', 'ug / kg'),
    ('ug_m2', 'ug / m2'),
    ('iu', 'IU'),
    ('suppository', 'Suppository'),)

TEST_TYPE = (
    ('pcr_test', 'PCR Test'),
    ('nasal_Swab', 'Nasal Swab'),
    (OTHER, 'Other, specify'),
)

VACCINATION_LOCATION = (
    ('left_deltoid', 'Left deltoid'),
    ('right_deltoid', 'Right deltoid'),
    (OTHER, 'Other, specify'),
    (NOT_APPLICABLE, 'Not applicable'),
)

VISIT_INFO_SOURCE = (
    ('clinic_visit_w_subject', 'Clinic visit with participant'),
    ('other_contact_w_subject',
     'Other contact with participant (i.e telephone call)'),
    ('contact_w_health_worker', 'Contact with health care worker'),
    ('Contact_w_family_design',
     'Contact with family or designated person who can provide information'),
    (OTHER, 'Other,specify'),
)

VISIT_REASON = (
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Did not attend scheduled visit'),
    (UNSCHEDULED, 'Unscheduled visit/contact'),
    (LOST_VISIT, 'Use only when withdrawing subject off study'),
    (COMPLETED_PROTOCOL_VISIT, 'Subject has completed the study'),
)

# IDENTITY_TYPE = (
#     ('NATIONAL_IDENTITY_CARD', 'National Identity Card'),
#     ('DRIVERS', 'Driver\'s License'),
#     ('PASSPORT', 'Passport'),
#     ('NATIONAL_IDENTITY_CARD_RECEIPT', 'National Identity Receipt'),
#     (OTHER, 'Other'),
# )

YES_NO_OTHER = (
    (YES, YES),
    (NO, NO),
    (OTHER, 'Other'))

VACCINATION_DOSE = (
    ("first_dose", "First Dose"),
    ("second_dose", "Second Dose"),
    (NOT_APPLICABLE, 'Not applicable')
)
