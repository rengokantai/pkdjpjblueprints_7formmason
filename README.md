####pkdjpjblueprints_7formmason

```
python manage.py shell
from main.models import FormSchema
fs = FormSchema()
fs.title='test'
fs.schema = {"name":"string","age":"number","city":"string","country":"string","time_lived_in_current_city":"string"}
fs.save()
FormSchema.objects.get(pk=1).schema
```
######showing the responses
An error occurs, object_list issue