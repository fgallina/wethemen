from django.conf import settings

CONTACT_TEMPLATE = getattr(settings, "CONTACT_TEMPLATE", "contact.html")
CONTACT_THANKS_TEMPLATE = getattr(settings, "CONTACT_THANKS_TEMPLATE", "contact_thanks.html")
CONTACT_EMAIL_SUBJECT_FIELD = getattr(settings, "CONTACT_EMAIL_SUBJECT_FIELD", None)
CONTACT_EMAIL_SUBJECT_DEFAULT = getattr(settings, "CONTACT_EMAIL_SUBJECT_DEFAULT", "Contact from the site.")
CONTACT_SUCCESS_REDIRECT = getattr(settings, "CONTACT_SUCCESS_REDIRECT", "/thanks/")
CONTACT_RECIPIENTS = getattr(settings, "CONTACT_RECIPIENTS", [admin[1] for admin settings.ADMINS])
CONTACT_EMAIL_FIELD = getattr(settings, "CONTACT_EMAIL_FIELD", "email")
CONTACT_CC_MYSELF_FIELD = getattr(settings, "CONTACT_CC_MYSELF_FIELD", "cc_myself")
