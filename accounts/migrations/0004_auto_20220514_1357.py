from django.db import migrations

def populate_languages(apps, schemaeditor):
    languages =[
            {
                "key": "EN",
                "name": "English"
            },
            {
                "key": "ES",
                "name": "Espanol"
            },
            {
                "key": "DE",
                "name": "Deutsch"
            },
            {
                "key": "PT",
                "name": "Portugues"
            }
        ]
    Language = apps.get_model('accounts', 'Language')
    for language in languages:
        lang_obj = Language(
            key=Language.get('key'),
            name=language.get('name')
        )
    lang_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_language_customuser_preferred_language'),
    ]

    operations = [
        migrations.RunPython(populate_languages),
    ]
