from django.db import models
from django.contrib.auth.models import User

DATA_TYPE_FULL_NAME = 'full_name'
DATA_TYPE_JOB = 'job'
DATA_TYPE_EMAIL = 'email'
DATA_TYPE_DOMAIN_NAME = 'domain_name'
DATA_TYPE_PHONE_NUMBER = 'phone_number'
DATA_TYPE_COMPANY_NAME = 'company_name'
DATA_TYPE_TEXT = 'text'
DATA_TYPE_INTEGER = 'integer'
DATA_TYPE_ADDRESS = 'address'
DATA_TYPE_DATE = 'date'
DATA_TYPES = (
    (DATA_TYPE_FULL_NAME, 'Full name'),
    (DATA_TYPE_JOB, 'Job'),
    (DATA_TYPE_EMAIL, 'Email'),
    (DATA_TYPE_DOMAIN_NAME, 'Domain name'),
    (DATA_TYPE_PHONE_NUMBER, 'Phone number'),
    (DATA_TYPE_COMPANY_NAME, 'Company name'),
    (DATA_TYPE_TEXT, 'Text'),
    (DATA_TYPE_INTEGER, 'Integer'),
    (DATA_TYPE_ADDRESS, 'Address'),
    (DATA_TYPE_DATE, 'Date'),
)

DATASET_STATUS_PROCESSING = 'processing'
DATASET_STATUS_READY = 'ready'
DATASET_STATUSES = (
    (DATASET_STATUS_PROCESSING, 'Processing'),
    (DATASET_STATUS_READY, 'Ready'),
)


class DataSchema(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    columns = models.JSONField()



