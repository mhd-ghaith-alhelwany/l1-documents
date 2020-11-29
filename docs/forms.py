from django import forms
from upload_validator import FileTypeValidator
import re
from django.core.exceptions import ValidationError
from .services.documentService import DocumentTableValidator


def starts_with_table(title):
    return re.match(r"Table([0-9]+)$", title)


def document_tables_validator(file):
    validator = DocumentTableValidator(file).validate()
    if not validator['is_valid']:
        raise ValidationError(
            validator['errors'],
        )


class DocumentForm(forms.Form):
    file = forms.FileField(
        label="File",
        widget=forms.FileInput(
            attrs={"class": 'form-control'},
        ),
        help_text="Only documents are accepted.",
        validators=[
            FileTypeValidator(
                allowed_types=["application/*"],
                allowed_extensions=['.doc', '.docx']
            ),
            document_tables_validator
        ],
    )
