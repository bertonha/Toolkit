from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from sqlhelper.forms import InsertForm


def insert(request):
    if request.POST:
        form = InsertForm(request.POST, request.FILES)
        if form.is_valid():
            sql = generate_insert(form.cleaned_data['table'], request.FILES['cvs'])
            return HttpResponse(sql, mimetype='text/x-sql')
    else:
        form = InsertForm()

    return render(request, 'form.html', {
        'form': form,
        'action': reverse('insert_sql'),
        'title': _('Insert Generator'),
    })
