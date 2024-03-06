from modeltranslation.translator import register, TranslationOptions
from .models import Events, Public, ExhibitionCalendar, ManualVideo, Questions


@register(Events)
class EventsTranslation(TranslationOptions):
    fields = (
        'title',
        'description',
    )


@register(Public)
class PublicTranslation(TranslationOptions):
    fields = (
        'title',
        'description',
    )


@register(ExhibitionCalendar)
class ExhibitionCalendarTranslation(TranslationOptions):
    fields = (
        'name_exhibition',
        'period',
        'data_of_participation',
        'location',
    )


@register(ManualVideo)
class ManualVideoTranslation(TranslationOptions):
    fields = (
        'name',
        'description',
    )


@register(Questions)
class QuestionsTranslation(TranslationOptions):
    fields = (
        'name',
        'email',
        'phone',
        'questions',
    )