from django.contrib import admin
from django.http import HttpResponse
from .models import Informer,Subscriber,Siting,Message

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=elehphant_sightings.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Reported At"),
        smart_str(u"Latitude"),
        smart_str(u"Longitude"),
        smart_str(u"Message"),
        smart_str(u"Informer"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(str(obj.created_at)),
            smart_str(obj.location),
            smart_str(obj.message),
            smart_str(obj.informer.name),
        ])
    return response
export_csv.short_description = u"Export CSV"

class SitingAdmin(admin.ModelAdmin):
    actions = [export_csv]

# Register your models here.

admin.site.register(Siting,SitingAdmin)
admin.site.register(Informer)
admin.site.register(Subscriber)
admin.site.register(Message)


