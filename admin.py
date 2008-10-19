"""
Admin for blog_entries.

"""

from django.contrib import admin
from blog_entries.models import Entry

class EntryAdmin(admin.ModelAdmin):
    "Options for the Entry Admin interface."

    change_form_template = 'blog_entries/change_form.html'

    class Media:
        js = (
            'http://yui.yahooapis.com/combo?2.6.0/build/yahoo-dom-event/yahoo-dom-event.js&2.6.0/build/container/container_core-min.js&2.6.0/build/menu/menu-min.js&2.6.0/build/element/element-beta-min.js&2.6.0/build/button/button-min.js&2.6.0/build/editor/editor-min.js',
        )
        css = {
            'all': ('http://yui.yahooapis.com/combo?2.6.0/build/assets/skins/sam/skin.css',)
        }

    prepopulated_fields = {
        'slug':        ('title',),
    }
    date_hierarchy = 'pub_date'
    fieldsets = (
        ('Metadata',
            {'fields': ('title', 'slug', 'pub_date', 'author', 'status', 'featured', 'enable_comments')}),
        ('Entry',
            {'fields': ('excerpt', 'body')}),
        ('Categorization and SEO',
            {'fields': ('tags', 'keywords', 'description')}),
    )
    list_display = ('title', 'pub_date', 'author', 'status', 'enable_comments', '_get_comment_count')
    list_filter = ('status',)
    search_fields = ('excerpt', 'body', 'title')

site = admin.site
site.register(Entry, EntryAdmin)
