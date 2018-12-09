from dynamic_preferences.types import BooleanPreference, StringPreference, IntegerPreference, ChoicePreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.users.registries import user_preferences_registry

from YtManagerApp.models import VIDEO_ORDER_CHOICES

# we create some section objects to link related preferences together

hidden = Section('hidden')
general = Section('general')
scheduler = Section('scheduler')
manager = Section('manager')
downloader = Section('downloader')


# Hidden settings
@global_preferences_registry.register
class Initialized(BooleanPreference):
    section = hidden
    name = 'initialized'
    default = False


# General settings
@global_preferences_registry.register
class YouTubeAPIKey(StringPreference):
    section = general
    name = 'youtube_api_key'
    default = 'AIzaSyBabzE4Bup77WexdLMa9rN9z-wJidEfNX8'
    required = True


@global_preferences_registry.register
class AllowCDN(BooleanPreference):
    section = general
    name = 'allow_cdn'
    default = True
    required = True


@global_preferences_registry.register
class AllowRegistrations(BooleanPreference):
    section = general
    name = 'allow_registrations'
    default = True
    required = True


@global_preferences_registry.register
class SyncSchedule(StringPreference):
    section = scheduler
    name = 'synchronization_schedule'
    default = '5 * * * *'  # hourly
    required = True


@global_preferences_registry.register
class SchedulerConcurrency(IntegerPreference):
    section = scheduler
    name = 'concurrency'
    default = 2
    required = True


# User settings
@user_preferences_registry.register
class MarkDeletedAsWatched(BooleanPreference):
    section = manager
    name = 'mark_deleted_as_watched'
    default = True
    required = True


@user_preferences_registry.register
class AutoDeleteWatched(BooleanPreference):
    section = manager
    name = 'auto_delete_watched'
    default = True
    required = True


@user_preferences_registry.register
class AutoDownloadEnabled(BooleanPreference):
    section = downloader
    name = 'download_enabled'
    default = True
    required = True


@user_preferences_registry.register
class DownloadGlobalLimit(IntegerPreference):
    section = downloader
    name = 'download_global_limit'
    default = None
    required = False


@user_preferences_registry.register
class DownloadGlobalSizeLimit(IntegerPreference):
    section = downloader
    name = 'global_size_limit_mb'
    default = None
    required = False


@user_preferences_registry.register
class DownloadSubscriptionLimit(IntegerPreference):
    section = downloader
    name = 'download_limit_per_subscription'
    default = 5
    required = False


@user_preferences_registry.register
class DownloadMaxAttempts(IntegerPreference):
    section = downloader
    name = 'download_max_attempts'
    default = 3
    required = True


@user_preferences_registry.register
class DownloadOrder(ChoicePreference):
    section = downloader
    name = 'download_order'
    choices = VIDEO_ORDER_CHOICES
    default = 'playlist'
    required = True


@user_preferences_registry.register
class DownloadPath(StringPreference):
    section = downloader
    name = 'download_path'
    default = None
    required = False


@user_preferences_registry.register
class DownloadFilePattern(StringPreference):
    section = downloader
    name = 'download_file_pattern'
    default = '${channel}/${playlist}/S01E${playlist_index} - ${title} [${id}]'
    required = True


@user_preferences_registry.register
class DownloadFormat(StringPreference):
    section = downloader
    name = 'download_format'
    default = 'bestvideo+bestaudio'
    required = True


@user_preferences_registry.register
class DownloadSubtitles(BooleanPreference):
    section = downloader
    name = 'subtitles_enabled'
    default = True
    required = True


@user_preferences_registry.register
class DownloadAutogeneratedSubtitles(BooleanPreference):
    section = downloader
    name = 'autogenerated_subtitles'
    default = False
    required = True


@user_preferences_registry.register
class DownloadAllSubtitles(BooleanPreference):
    section = downloader
    name = 'all_subtitles'
    default = False
    required = False


@user_preferences_registry.register
class DownloadSubtitlesLangs(StringPreference):
    section = downloader
    name = 'subtitles_langs'
    default = 'en,ro'
    required = False


@user_preferences_registry.register
class DownloadSubtitlesFormat(StringPreference):
    section = downloader
    name = 'subtitles_format'
    default = False
    required = False
