from modeltranslation.translator import register, TranslationOptions
from .models import Category, SubCategory, Product, Order, Subscription


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(SubCategory)
class SubCategoryTranslation(TranslationOptions):
    fields = (
            'name',
            'category',
              )


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = (
        'short_description',
        'compound',
        'description',
        'applying',
        'waiting_time',
        'release_form',
        'storage_date',
        'storage_conditions',
        'sub_category',
    )


# @register(Order)
# class OrderTranslation(TranslationOptions):
#     fields = (
#         'name',
#         'phone',
#         'email',
#     )
#
#
# @register(Subscription)
# class SubscriptionTranslation(TranslationOptions):
#     fields = ('email',)
