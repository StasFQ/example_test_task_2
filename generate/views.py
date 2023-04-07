import csv
from io import StringIO

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import DataSchema
from django.shortcuts import render, redirect
from faker import Faker
from generate.forms import CreateDataSchema


def home(request):
    user = request.user
    schema = DataSchema.objects.filter(user=user)
    return render(request, 'generate/home.html', {'schema': schema})


def create_data_schema(request):
    if request.method == 'POST':
        form = CreateDataSchema(request.POST)
        if form.is_valid():
            data_schema = form.save(commit=False)
            data_schema.user = request.user
            data_schema.save()
            return redirect('home')
    else:
        form = CreateDataSchema()
    return render(request, 'generate/data_schema_create.html', {'form': form})


def generate_data(request, schema_id):
    schema = get_object_or_404(DataSchema, pk=schema_id)

    num_records = int(request.POST.get('num_records', 0))
    if num_records <= 0:
        num_records = 10

    csv_file = StringIO()
    writer = csv.writer(csv_file)

    fake = Faker()
    print(schema.columns)
    for i in range(num_records):
        row = []
        for col in schema.columns:
            if col['type'] == 'full_name':
                row.append(fake.name())
            elif col['type'] == 'job':
                row.append(fake.job())
            elif col['type'] == 'email':
                row.append(fake.email())
            elif col['type'] == 'domain_name':
                row.append(fake.domain_name())
            elif col['type'] == 'phone_number':
                row.append(fake.phone_number())
            elif col['type'] == 'company_name':
                row.append(fake.company())
            elif col['type'] == 'text':
                row.append(fake.text(max_nb_chars=col['max_nb_chars']))
            elif col['type'] == 'integer':
                row.append(fake.random_int())
            elif col['type'] == 'address':
                row.append(fake.address())
            elif col['type'] == 'date':
                row.append(fake.date_between(start_date='-1y', end_date='today'))
        writer.writerow(row)

    response = HttpResponse(csv_file.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{schema.name}.csv"'
    return response
