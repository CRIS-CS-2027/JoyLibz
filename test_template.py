import importlib

template = importlib.import_module('templates.doctors_visit')

print(template.mad_text)
