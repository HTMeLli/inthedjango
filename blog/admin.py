from django.contrib import admin
from .models import Post, Vendor, Supplement, Form, Unit, Active, Content, Shop, ShoppingItem

admin.site.register(Post)
admin.site.register(Vendor)


class ContentInline(admin.TabularInline):
    model = Content
    extra = 0


@admin.register(Supplement)
class SupplementAdmin(admin.ModelAdmin):
    inlines = (ContentInline, )
    list_display = ("name", "pk", "amount", "vendor", "customBla", )
    search_fields = ("name", )

    def customBla(self, supplement):
        return f"FormName: {supplement.form.name}"


admin.site.register(Form)
admin.site.register(Unit)
admin.site.register(Active)
admin.site.register(Content)
admin.site.register(Shop)
admin.site.register(ShoppingItem)
