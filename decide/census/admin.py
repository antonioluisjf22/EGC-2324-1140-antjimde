from django.contrib import admin

from .models import Census


class CensusAdmin(admin.ModelAdmin):
    list_display = ('voting_id_2', 'voter_id')
    list_filter = ('voting_id_2', )

    search_fields = ('voter_id', )


admin.site.register(Census, CensusAdmin)
