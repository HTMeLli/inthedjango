from django.contrib import admin
from .models import Ingredient, Vendor, Supplement, Form, Unit, ActiveIngredient, Content, Shop, ShoppingItem, Connection, Trace, SpecialLabel, Discount, Price, Alias

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
admin.site.register(ActiveIngredient)
admin.site.register(Content)
admin.site.register(Shop)
admin.site.register(ShoppingItem)
admin.site.register(Ingredient)
admin.site.register(Connection)
admin.site.register(Trace)
admin.site.register(SpecialLabel)
admin.site.register(Discount)
admin.site.register(Price)
admin.site.register(Alias)
