from django.core.validators import ValidationError

def file_size(value):
    if value.size > 10000000:
        raise ValidationError('File too large')
