from comics.settings.testing import *

# Test runner with code coverage
TEST_RUNNER = 'comics.utils.test_runner.test_runner_with_coverage'
COVERAGE_MODULES = (
    'comics.aggregator.command',
    'comics.aggregator.crawler',
    'comics.aggregator.downloader',
    'comics.aggregator.exceptions',
    'comics.aggregator.lxmlparser',
    'comics.aggregator.management.commands.getcomics',
    'comics.comics',
    'comics.core.context_processors',
    'comics.core.exceptions',
    'comics.core.feeds',
    'comics.core.managers',
    'comics.core.models',
    'comics.core.templatetags.versioned_media',
    'comics.core.utils.comic_releases',
    'comics.core.utils.navigation',
    'comics.core.utils.time_frames',
    'comics.core.views',
    'comics.feedback.forms',
    'comics.feedback.views',
    'comics.meta.base',
    'comics.meta.command',
    'comics.meta.management.commands.loadmeta',
    'comics.sets.feeds',
    'comics.sets.forms',
    'comics.sets.middleware',
    'comics.sets.models',
    'comics.sets.views',
    'comics.utils.commands',
)
