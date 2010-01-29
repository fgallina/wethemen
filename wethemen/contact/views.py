from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import Context, loader
from forms import ContactForm
from defaults import *

def contact(request):
    """Processes the contact form.

    Your template defined in CONTACT_TEMPLATE should define the form
    like this:

    <form class="contact" action="{{ request.get_full_path }}" method="post">
    {% for field in form %}
    <p>
        {{ field.label_tag }} {{ field }}
    </p>
    {{ field.errors }}
    {% endfor %}
    <p>
        <input type="submit" value="{% trans "Send" %}" name="submit"/>
    </p>
    </form>
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context = Context({form.cleaned_data})
            template = loader.get_template('contact_email.html')
            subject = ""
            if CONTACT_EMAIL_SUBJECT_FIELD:
                try:
                    subject = getattr(form.cleaner_data[CONTACT_EMAIL_SUBJECT_FIELD)
                except IndexError:
                    subject = CONTACT_EMAIL_SUBJECT_DEFAULT
            else:
                subject = CONTACT_EMAIL_SUBJECT_DEFAULT
            recipients = CONTACT_RECIPIENTS                
            if CONTACT_CC_MYSELF_FIELD:
                cc = False
                try:
                    cc = form_cleaner_data[CONTACT_CC_MYSELF_FIELD]
                except IndexError:
                    pass
                if cc:
                    try:
                        recipients.append(form_cleaner_data[CONTACT_EMAIL_FIELD])
                    except IndexError:
                        pass
            send_mail(subject,
                      template.render(context),
                      email,
                      recipients)
            return HttpResponseRedirect(CONTACT_SUCCESS_REDIRECT)
    else:
        form = ContactForm()
    return render_to_response(CONTACT_TEMPLATE)

def thanks(request, lang):
    """Displays the thanks message to the user once the contact form
    has been sent.
    """
    return render_to_response(CONTACT_THANKS_TEMPLATE)
