from .models import EligibilityConfirmation, InformedConsent
from edc_constants.constants import YES
from faker import Faker
from model_mommy.recipe import Recipe, seq

fake = Faker()

eligibilityconfirmation = Recipe(
    EligibilityConfirmation,
    age_in_years=40)

informedconsent = Recipe(
    InformedConsent,
    first_name=fake.first_name,
    last_name=fake.last_name,
    identity=seq('123427675'),
    confirm_identity=seq('123427675'),
    is_literate=YES,
    consent_reviewed=YES,
    study_questions=YES,
    assessment_score=YES,
    consent_signature=YES,
    consent_copy=YES)
