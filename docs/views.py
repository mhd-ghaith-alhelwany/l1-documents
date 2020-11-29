from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Document, Table
from .forms import DocumentForm
from .services.documentService import DocumentConverter
from ast import literal_eval
import json
import os

def index(request):
    documents = Document.objects.all()
    context = {
        "name": "Docs",
        "documents": documents,
    }
    return render(request, 'docs/index.html', context)


def show(request, id, table_id=None):
    document = Document.objects.get(id=id)
    tables = Table.objects.filter(document_id=document).values()
    context = {
        "document": document,
        "tables": tables,
    }
    if table_id:
        selected_table = Table.objects.filter(id=table_id, document_id=document).get()
        context["selected_table_id"] = table_id
        context["selected_table_array"] = literal_eval(selected_table.json)
    return render(request, 'docs/show.html', context)


def download_table_json(request, id):
    table = Table.objects.filter(id=id).get()
    json_table = DocumentConverter.table_to_json(table)
    json_table = json.dumps(json_table)

    response = HttpResponse(json_table, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="json.txt"'
    return response


def download_table_xml(request, id):
    table = Table.objects.filter(id=id).get()
    xml_table = DocumentConverter.table_to_xml(table)

    response = HttpResponse(xml_table, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="xml.xml"'
    return response


def download_document(request, id):
    document = Document.objects.filter(id=id).get()
    document_file_path = DocumentConverter.from_document_model(document).to_document_file()
    with open(document_file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(document_file_path)
    os.remove(document_file_path)
    return response


def add(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            return save_object(request)
    else:
        form = DocumentForm()
    context = {
        'form': form
    }
    return render(request, "docs/add.html", context)


def save_object(request):
    document_tables = DocumentConverter.from_file(request.FILES['file'])
    document = Document.objects.create(
        file_name=document_tables.title,
    )
    for table in document_tables.tables:
        Table.objects.create(
            title=table['title'],
            json=table['rows'],
            document_id=document
        )
    return redirect(show, id=document.id)
