from django.shortcuts import render
from django.utils.translation import ugettext as _


def index(request):

    first_message = _('I borrow {amount} from {name}').format(
        amount=100,
        name='TP'
    )

    return render(request, 'index.html', {
        'message': first_message
    })
