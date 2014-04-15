Latest Changes
==============
Compiled on: O  apr 15 09:05:29 EEST 2014

    * 3c6eb77 - (HEAD, master) Signal handlers need kwargs even if unused. Bumping to 0.2.1. (2014-04-15 09:04:27 +0300) <Kristaps Karlsons>
    * 04e0f6e - (origin/master, origin/HEAD) Changelog++ (2014-04-14 18:05:39 +0300) <Kristaps Karlsons>
    *   4ecb162 - Merge branch 'feature/denormalization'. (2014-04-14 18:03:29 +0300) <Kristaps Karlsons>
    |\  
    | * 59e212a - (origin/feature/denormalization, feature/denormalization) Removed pdf generation, binary data shouldn't live here. (2014-04-14 18:00:23 +0300) <Kristaps Karlsons>
    | * b76112a - Removed testproject, it's broken. Adjusted requirements. (2014-04-14 17:56:16 +0300) <Kristaps Karlsons>
    | * c9da833 - Removed tests directory, why lie to ourselves, we don't have any tests. Yet. (2014-04-14 17:48:43 +0300) <Kristaps Karlsons>
    | * d87a74d - PEP8zed models. Removed file-related code. (2014-04-14 17:47:11 +0300) <Kristaps Karlsons>
    | * 1ebfb7b - Removed plugin functionality, transformed Section no base upon MPTT, no more Section nodes. Brakes compatibility - changes aren't backwards-compatible, needs data migration. (2014-04-14 17:30:21 +0300) <Kristaps Karlsons>
    * | 5d4222e - Version bump. (2014-04-14 18:03:00 +0300) <Kristaps Karlsons>
    |/  
    * eddc38e - (tag: release/0.1.0) 0.1.0 Changelog and Model chart. (2014-01-31 09:56:34 +0200) <Kristaps Karlsons>
    * d3a1051 - Article has SectionNode binding, not Section. This enables Article to have multiple first-level sections: Article->SectionNode->SectionNodes->Section (2014-01-31 09:52:19 +0200) <Kristaps Karlsons>
    * 7bcbd01 - (tag: release/0.0.4) Blindly forgot to add Article <-> (base) Section relation. (2014-01-22 16:25:01 +0200) <Kristaps Karlsons>
    * 1361728 - (tag: release/0.0.3) Bump to 0.0.3, changed changelog format. (2014-01-22 15:01:48 +0200) <Kristaps Karlsons>
    * 332ae02 - Added SectionNode MPTT model. (2014-01-22 14:20:24 +0200) <Kristaps Karlsons>
    * 789fcee - Addeed Section and SectionRevision stubs (based on Article respective counterparts). Renamed ArticleManager to PermissionManager. (2014-01-22 12:03:56 +0200) <Kristaps Karlsons>
    * fa11087 - Got rid of sekizai dependency, removed plugin views and urls. (2014-01-21 13:43:04 +0200) <Kristaps Karlsons>
    * 4837abc - Added sphinx-apidoc built documentation. (2014-01-21 13:21:32 +0200) <Kristaps Karlsons>
    * d800670 - (origin/cleanup, cleanup) Added `notes` section to documentation (2014-01-21 13:15:41 +0200) <Kristaps Karlsons>
    * 925b82c - Updated documentation, removed test url settings, adjusted Sphinx settings. (2014-01-21 13:05:50 +0200) <Kristaps Karlsons>
    * 18d0577 - Removed views, emptied tests (as they were view-based). Updated documentation to include correct links. Botched CHANGELOG.md while testing pypi upload and build-sdist.sh. Related - uploaded current version 0.0.1 to pypi. (2014-01-21 11:54:08 +0200) <Kristaps Karlsons>
    * 437f852 - Fixed tipo (2014-01-21 10:38:31 +0200) <Kristaps Karlsons>
    * 8dcd4cf - Moved ArticleRevision `deleted` and `locked` flags to Article. (2014-01-21 10:36:26 +0200) <Kristaps Karlsons>
    * 980022b - Removed static files and templates. (2014-01-21 10:13:42 +0200) <Kristaps Karlsons>
    * 0621a6e - Updated docs and settings. (2014-01-21 08:45:28 +0200) <Kristaps Karlsons>
    * 937b39c - Removed django_notify dependency and `notifications` plugin. It'll be possible to hook in to signals. (2014-01-21 08:40:35 +0200) <Kristaps Karlsons>
    * 3001d1d - Updated README.md to reflect django-wiki-base goals (2014-01-20 17:10:27 +0200) <Kristaps Karlsons>
    * 53807f5 - add rtd conf env (2014-01-09 17:14:06 +0100) <benjaoming>
    *   ecd2dec - Merge pull request #227 from spookylukey/easy_branding (2014-01-09 07:57:52 -0800) <benjaoming>
    |\  
    | * 051ca6e - Corrected docs for easy branding method (2014-01-09 14:33:04 +0000) <Luke Plant>
    | * d1ea57b - Added easy way to brand the wiki, avoiding lots of copy and paste. (2014-01-09 14:15:17 +0000) <Luke Plant>
    | * 3b7420e - Beginnings of docs - converted from README (2014-01-09 13:34:47 +0000) <Luke Plant>
    |/  
    * 2eaf23e - (tag: alpha/0.0.23) Bump to 0.0.23 (2014-01-06 23:45:11 +0100) <benjaoming>
    * 57e9bcf - Fix #221 - not correctly inheriting some permissions, save() called on URLPath object instead of Article object! (2014-01-06 23:38:52 +0100) <benjaoming>
    *   489f2c5 - Merge pull request #220 from Russell-Jones/master (2013-12-30 12:45:47 -0800) <benjaoming>
    |\  
    | * d36dbed - Add try catch block to test for and use if available new in 1.6 db transaction API (2013-12-30 17:10:58 +0000) <Russell Jones>
    |/  
    *   9931ffd - Merge pull request #217 from tominardi/master (2013-12-16 05:29:50 -0800) <benjaoming>
    |\  
    | * 59a5614 - Edit french translations (2013-12-16 14:24:46 +0100) <tominardi>
    |/  
    * ec5036c - (tag: alpha/0.0.22) bump version number (2013-11-25 00:20:28 +0100) <benjaoming>
    * 38252b8 - #213 django 1.6 trouble fixed (2013-11-19 15:10:54 +0100) <benjaoming>
    *   5538b39 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-11-19 15:08:55 +0100) <benjaoming>
    |\  
    | * 5cab46e - Change requirements to use Pillow instead of PIL (2013-11-19 11:32:35 +0100) <benjaoming>
    | * 127ada5 - Ah whatever... just delete everything about PIL!! (2013-11-19 11:32:07 +0100) <benjaoming>
    | * 525b1b5 - PIL / Pillow related docs (2013-11-19 11:08:32 +0100) <benjaoming>
    * | 974db28 - Add PyCharm ignores (2013-11-18 23:20:21 +0100) <benjaoming>
    |/  
    * 40c6a4e - make README compatible with the pandoc translation to ReST (2013-11-18 01:51:06 +0100) <benjaoming>
    * ffd2216 - Readme and Changelog update (2013-11-18 01:34:45 +0100) <benjaoming>
    * 2f59ecb - version bump to 0.0.21 (2013-11-18 01:24:58 +0100) <benjaoming>
    * 6e47242 - Fix #191 - introduce DRY in plugins.notifications default_url (2013-11-18 01:20:22 +0100) <benjaoming>
    * 363f50a - Fix #206 by upgrading markitup to newer version (2013-11-18 00:57:41 +0100) <benjaoming>
    * 34ac301 - Fix #207 and upgrade to jquery 1.10.2 (2013-11-18 00:52:04 +0100) <benjaoming>
    * 57a3c97 - Fix #211 by adding a bit more clarity on the context variable handling (2013-11-18 00:43:47 +0100) <benjaoming>
    * e08b54d - Fix bug in decorator causing double reverse lookups (2013-11-17 20:58:06 +0100) <benjaoming>
    * e4d904e - Remove tests from plugins that are just stub implementations and not django 1.6 compat (2013-11-14 12:47:06 +0100) <benjaoming>
    * a71b0ff - README updated (2013-11-14 12:42:49 +0100) <benjaoming>
    * a5395e8 - syntax highlighting for README (2013-11-14 12:40:13 +0100) <benjaoming>
    * 233bcf4 - Writing a few words on usage (2013-11-14 12:37:28 +0100) <benjaoming>
    * 1db4378 - Add a screenshot (2013-11-14 12:21:55 +0100) <benjaoming>
    * ab87c5a - Adding Travis tests for Django 1.6 (2013-11-14 11:55:28 +0100) <benjaoming>
    * f1bad2d - automatically generate docs and CHANGELOG.md (2013-11-14 11:50:36 +0100) <benjaoming>
    * b757c6d - Trying out a markdown formatted auto-gererated for new releases CHANGELOG (2013-11-14 11:47:37 +0100) <benjaoming>
    * 22936c3 - Automating version number for sphinx (2013-11-14 01:56:21 +0100) <benjaoming>
    * f232fd6 - django 1.6 fix for #191 - ArticleRevision.get_latest_by should be single field, not tuple (2013-11-13 17:17:31 +0100) <benjaoming>
    * cc31f07 - django 1.6 and #191 BooleanField now has NULL value (2013-11-13 17:14:34 +0100) <benjaoming>
    *   d0ea990 - Merge pull request #208 from stratatech/master (2013-10-28 03:54:16 -0700) <benjaoming>
    |\  
    | * d8e872f - Russian translations fixes (2013-10-28 10:59:30 +0400) <sminozhenko>
    | * 13c3e06 - Remove unnecessary lamba function (2013-10-28 10:55:56 +0400) <sminozhenko>
    | * 164b416 - Russion translations + some missing label added + problem with transaltions in django_notify.settings.py (2013-10-25 16:11:27 +0400) <sminozhenko>
    |/  
    *   b4d3be8 - Merge pull request #202 from rgcarrasqueira/master (2013-10-24 11:12:29 -0700) <benjaoming>
    |\  
    | * 8ede8b8 - Bugfix request method is not found Django 1.4.7 (2013-10-22 22:44:02 -0200) <Rogério Carrasqueira>
    | * 02f4bbe - Changing mptt to 0.5.3 (2013-10-22 22:19:52 -0200) <Rogério Carrasqueira>
    | * e146a5d - Become compatible with django-cms 2.4.2 due django-sekizai (2013-10-22 00:17:22 -0200) <Rogério Carrasqueira>
    * |   08758a6 - Merge pull request #203 from TomLottermann/master (2013-10-22 03:11:45 -0700) <benjaoming>
    |\ \  
    | |/  
    |/|   
    | * ef4cccf - Updated translation. Fixed some minor issues. (2013-10-22 09:05:51 +0200) <Thomas Lottermann>
    |/  
    * af767e3 - Instruction text for direct pip installation from git (2013-10-02 13:02:48 +0200) <benjaoming>
    *   6104404 - Merge pull request #199 from TomLottermann/master (2013-09-30 15:11:19 -0700) <benjaoming>
    |\  
    | * 29a03a3 - indentation fixed (2013-10-01 00:04:13 +0200) <Thomas Lottermann>
    | * d3b52cf - pagination broke with bootstrap 3. It now works again! (2013-10-01 00:00:15 +0200) <Thomas Lottermann>
    |/  
    *   db32a3e - Merge pull request #198 from TomLottermann/master (2013-09-27 17:15:25 -0700) <benjaoming>
    |\  
    | *   be3b35d - Merge remote-tracking branch 'upstream/master' (2013-09-28 01:03:23 +0200) <Thomas Lottermann>
    | |\  
    | |/  
    |/|   
    * | d07ba79 - fix #193 - only add style to input type=text/password (2013-09-28 00:49:28 +0200) <benjaoming>
    * | c8d9307 - Fix [TOC] compatibility with custom ids and add support for [[WikiLink]] #179 (2013-09-28 00:41:38 +0200) <benjaoming>
    * | c73d331 - remove bogus highlight plugin (2013-09-27 23:19:13 +0200) <benjaoming>
    * |   809a12f - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-09-27 23:16:06 +0200) <benjaoming>
    |\ \  
    | * \   d956400 - Merge pull request #190 from yedpodtrzitko/master (2013-09-27 13:35:02 -0700) <benjaoming>
    | |\ \  
    | | * | 085d4aa - bump translations (2013-08-17 21:45:05 +0200) <yed_>
    | | * | e4e655e - show info about missing root instead of redirect to login (fix #174) (2013-08-17 21:44:52 +0200) <yed_>
    * | | | 92cddce - add codehilite to default markdown extensions and close #134 (2013-09-27 23:15:56 +0200) <benjaoming>
    |/ / /  
    * | |   e5cbdf4 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-09-27 22:27:25 +0200) <benjaoming>
    |\ \ \  
    * | | | aca44f0 - fix #197 - use twitter typeahead (2013-09-27 22:27:04 +0200) <benjaoming>
    * | | | 9716942 - ignore haystack test indexes (2013-09-27 22:26:15 +0200) <benjaoming>
    | | | * b7c24ed - Group and owner can be null. The index must support this! (2013-09-28 01:02:03 +0200) <Thomas Lottermann>
    | | |/  
    | |/|   
    | * |   51019fc - Merge pull request #192 from jbazik/master (2013-08-22 16:50:59 -0700) <benjaoming>
    | |\ \  
    | | * | f1560a3 - Use a private instance of sorl.thumbnails. (2013-08-22 18:37:05 -0400) <John Bazik>
    | |/ /  
    | * |   2314aa0 - Merge pull request #189 from yedpodtrzitko/master (2013-08-15 11:24:40 -0700) <benjaoming>
    | |\ \  
    | | |/  
    | | *   05a5f53 - Merge remote-tracking branch 'orig/master' (2013-08-15 17:25:18 +0200) <yed_>
    | | |\  
    | | |/  
    | |/|   
    | * |   0cb2ca2 - Merge pull request #188 from yedpodtrzitko/master (2013-08-15 06:43:58 -0700) <benjaoming>
    | |\ \  
    |/ / /  
    | | * 30c45e2 - _change revision_ as a class-based view (2013-08-15 17:21:49 +0200) <yed_>
    | |/  
    | * 10a4457 - create root as a class-based view (2013-08-15 15:07:10 +0200) <yed_>
    |/  
    *   9528bf7 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-08-12 17:22:51 +0200) <benjaoming>
    |\  
    | * 04ce91f - Update local.py (2013-08-12 00:52:14 +0200) <benjaoming>
    * | 2c35ea7 - urlize also on last-of-line urls + fix icon (2013-08-12 17:22:17 +0200) <benjaoming>
    |/  
    * 8fd557c - Fix #186 -- add empty local.py file (2013-08-12 00:44:13 +0200) <benjaoming>
    *   8af2a61 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-08-12 00:41:32 +0200) <benjaoming>
    |\  
    | * 8ffd8f0 - Fix #178 - improve urlize regex to accept everything after a domain, except spaces, [, and ( (2013-08-12 00:39:43 +0200) <benjaoming>
    * | 05ecdbb - Fix #178 - improve urlize regex to accept everything after a domain, except spaces, [, and ( (2013-08-12 00:41:20 +0200) <benjaoming>
    |/  
    * 2108a32 - grid layout on all form-action occurences (2013-08-10 00:17:55 +0200) <benjaoming>
    * 5a90cfe - more issues in bootstrap 3 form widgets (2013-08-10 00:12:27 +0200) <benjaoming>
    * bb89355 - textarea height and edit page button layout (2013-08-10 00:01:06 +0200) <benjaoming>
    * 4aef17a - Fix #181 and #183 -- responsive modals, prepend for form inputs, form controls fixed for horizontal and vertical layouts (2013-08-09 23:53:19 +0200) <benjaoming>
    * eb21b9d - bootstrap 3 compat on attachments plugin (2013-08-09 23:23:35 +0200) <benjaoming>
    * 826b082 - fix 404 on respond.js (2013-08-09 22:53:11 +0200) <benjaoming>
    *   3253098 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-08-08 01:57:47 +0200) <benjaoming>
    |\  
    | *   5b34a24 - Merge pull request #185 from vezjakv/master (2013-08-06 06:13:35 -0700) <benjaoming>
    | |\  
    | | * cbb815a - Init std.out stream handler compatable with Python 2.6 (2013-08-02 14:44:43 +0200) <vezjakv>
    | |/  
    | * 27cc33c - Update README.md (2013-08-01 01:49:02 +0200) <benjaoming>
    | * d059edb - SHA digest should display as link (2013-08-01 01:47:05 +0200) <benjaoming>
    | * 515a1b7 - News update (2013-08-01 01:45:45 +0200) <benjaoming>
    | * a594811 - Github Markdown broken on multiple comments in one line (2013-08-01 01:35:09 +0200) <benjaoming>
    * | 8e77f06 - add codehilite note in README and a testproject settings module (2013-08-08 01:57:33 +0200) <benjaoming>
    * | 06aa0e2 - add codehilite CSS to enable syntax highlighting for the codehilite Markdown extension (2013-08-08 01:54:07 +0200) <benjaoming>
    * | e4382c8 - strip tags from Haystack searches (2013-08-07 14:04:50 +0200) <benjaoming>
    * | 0cf10f5 - fix some more btn-default (2013-08-07 01:41:03 +0200) <benjaoming>
    * | 47dee16 - fix btn-default in some other cases (2013-08-07 01:38:13 +0200) <benjaoming>
    * | 9ccb216 - fix bootstrap btn-default class (2013-08-07 01:26:59 +0200) <benjaoming>
    |/  
    * d8149a6 - fix #182 - bootstrap problem, not html (2013-07-31 22:18:48 +0200) <benjaoming>
    * be42a26 - include font files in MANIFEST (2013-07-31 21:33:29 +0200) <benjaoming>
    * d077af2 - responsive search form (2013-07-27 20:50:40 +0200) <benjaoming>
    * fbccb07 - Fix search form on chromium (2013-07-27 20:31:07 +0200) <benjaoming>
    * 657b8f9 - remove old bootstrap files (2013-07-27 20:30:51 +0200) <benjaoming>
    * 34b9117 - refactor bootstrap grid layout (2013-07-27 20:28:56 +0200) <benjaoming>
    * b919d54 - Upgrade to Bootstrap 3 RC1, add font-awesome, lots of refactoring (2013-07-27 17:06:49 +0200) <benjaoming>
    * 204cc43 - make __init__.py always try to import settings.local (2013-07-26 00:43:15 +0200) <benjaoming>
    * 91064d6 - Add SECRET_KEY to standard settings so testproject runs out of the box (2013-07-25 03:05:20 +0200) <benjaoming>
    * e624b61 - Remove old settings_local.py (2013-07-25 02:34:51 +0200) <benjaoming>
    * 04f131c - Add #django-wiki IRC channel - yay :) (2013-07-24 18:49:00 +0200) <benjaoming>
    * 0f3bf03 - add setting WIKI_ACCOUNT_SIGNUP_ALLOWED (2013-07-23 19:58:14 +0200) <benjaoming>
    * ebe1503 - Don't be verbose while scanning for plugins (2013-07-23 19:57:03 +0200) <benjaoming>
    * 384fb62 - Fix #23 - move model registration from taking place within wiki.models to wiki.urls -- after all apps and models have been loaded (2013-07-17 02:06:01 +0200) <benjaoming>
    * fcce3ce - cleanup (2013-07-16 23:26:32 +0200) <benjaoming>
    * 5ff6fac - Fix #160 by allowing django-sendfile to be plugged in through settings.USE_SENDFILE (2013-07-16 23:25:27 +0200) <benjaoming>
    * 0418642 - Fix #162 -- add filter_exclude to notify() (2013-07-16 22:57:56 +0200) <benjaoming>
    * 02cb4d2 - Fix #164 by always setting a timeout for notification updates (2013-07-16 22:33:01 +0200) <benjaoming>
    *   0bc8e32 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-07-16 22:27:58 +0200) <benjaoming>
    |\  
    | * 0c148d3 - make possible for moderators to replace attachments (2013-07-16 22:25:52 +0200) <benjaoming>
    * | 7846c81 - make possible for moderators to replace attachments, also fix #170, and remove catching all exceptions (2013-07-16 22:27:48 +0200) <benjaoming>
    |/  
    * 8f65dd2 - Travis settings for test project (2013-07-16 22:00:08 +0200) <benjaoming>
    *   3f3c903 - Fix #173 by letting articles refer to other article's attachments while checking the permissions of the original article owner (2013-07-16 21:35:48 +0200) <benjaoming>
    |\  
    | * b9981cf - Updating travis test to use new settings layout (2013-07-16 21:12:05 +0200) <benjaoming>
    * | 0090335 - Trying a new travis configuration since the PYTHON_PATH does not understand testproject.settings (2013-07-16 21:33:38 +0200) <benjaoming>
    |/  
    * 112bba7 - cleanup (2013-07-16 20:47:01 +0200) <benjaoming>
    * 88030a1 - Add Haystack search plugin (NB! Whoosh backend is broken upstream) (2013-07-16 20:46:11 +0200) <benjaoming>
    * e21da47 - script to migrate south migrations to a custom auth user model (has already been run on wiki.migrations) (2013-07-16 19:07:59 +0200) <benjaoming>
    * 58a46b8 - Refactore testproject.settings to accommodate more scenarios (2013-07-16 19:04:08 +0200) <benjaoming>
    * a4e3ebf - make SEARCH_VIEW configurable from conf.settings (2013-07-16 19:00:42 +0200) <benjaoming>
    * 24271db - cleanup unnecessary file (2013-07-16 16:19:58 +0200) <benjaoming>
    * 810bd00 - Automatically generate README.rst for PyPi (2013-07-16 15:51:59 +0200) <benjaoming>
    *   0c49222 - Merge branches 'master' and 'haystack' of github.com:benjaoming/django-wiki into haystack (2013-07-16 12:49:27 +0200) <benjaoming>
    |\  
    | *   b9d969d - Merge pull request #172 from holdenweb/patch-1 (2013-06-30 14:16:05 -0700) <benjaoming>
    | |\  
    | | * bcb47c9 - Update README.md (2013-06-30 06:12:29 -0700) <Steve Holden>
    | |/  
    | *   3a06ff1 - Merge pull request #168 from TomLottermann/master (2013-06-20 11:08:53 -0700) <benjaoming>
    | |\  
    | | *   a448f74 - Merge remote-tracking branch 'upstream/master' (2013-06-20 10:23:26 +0200) <Thomas Lottermann>
    | | |\  
    | | |/  
    | |/|   
    | * | 39ecbdf - Cleanup 'admin' slug error message (2013-06-17 18:29:20 +0300) <benjaoming>
    | * |   d9b2a5b - Merge pull request #166 from BenMarchant/patch-2 (2013-06-17 08:19:36 -0700) <benjaoming>
    | |\ \  
    | | * | 0449a29 - Visitor cannot use admin as a slug (just in case !) (2013-06-17 10:35:37 -0300) <BenMarchant>
    | |/ /  
    | * |   3d573b0 - Merge pull request #165 from BenMarchant/patch-1 (2013-06-17 06:34:41 -0700) <benjaoming>
    | |\ \  
    | | * | be728b0 - Fixed: "wiki_footer_prepend block" (2013-06-17 10:27:11 -0300) <BenMarchant>
    | |/ /  
    | | * 7b40385 - fixed non-found absolute wiki urls (2013-06-20 10:15:35 +0200) <Thomas Lottermann>
    * | | 2c1e7c1 - Fix Django 1.4 incompatibility (2013-07-16 12:47:23 +0200) <benjaoming>
    * | |   9c31dc3 - Merge branch 'haystack-search' of git://github.com/jdcaballero/django-wiki into jdcaballero-haystack-search (2013-06-12 01:33:51 +0200) <benjaoming>
    |\ \ \  
    | |/ /  
    |/| |   
    | * |   784f8d6 - Merge pull request #1 from TomLottermann/haystack-search (2013-06-11 11:23:59 -0700) <jdcaballero>
    | |\ \  
    | | * | 6108d30 - Minor fix (2013-06-10 12:55:18 +0200) <Thomas Lottermann>
    | | * | e10d573 - Haystack 2.0 broke some stuff (site did not exist). This is fixed now. Furthermore we can use the highlighter by haystack. It does some stuff nicer than django-wikis (2013-06-10 12:36:29 +0200) <Thomas Lottermann>
    | | * | e68272c - Some minor cleanup and same redirect behaviour on anonymous access (2013-06-09 19:10:33 +0200) <Thomas Lottermann>
    | | * |   a1a25c2 - Merge remote-tracking branch 'jdcaballero/haystack-search' into haystack-search (2013-06-09 18:58:36 +0200) <Thomas Lottermann>
    | | |\ \  
    | | |/ /  
    | |/| /   
    | | |/    
    | * | 4035783 - Permissions bare implementation (2013-03-28 10:32:06 +0100) <Juan Diego Caballero>
    | * | ba667f1 - Paginator used to show the number of results (2013-02-27 10:12:49 +0100) <Juan Diego Caballero>
    | * | 54c14bb - Initial Implementation of Search using Haystack (2013-02-26 17:46:19 +0100) <Juan Diego Caballero>
    * | | dfe7be5 - hand empty notifications settings (2013-06-10 00:41:48 +0200) <benjaoming>
    * | | d7df0af - pep8 cleanup (2013-06-10 00:41:12 +0200) <benjaoming>
    * | | ed9d853 - Add notification interval to Article Settings page + New Notifications Settings page (2013-06-10 00:35:50 +0200) <benjaoming>
    * | | 1d4faa9 - get_absolute_path added to Article model (2013-06-10 00:33:18 +0200) <benjaoming>
    * | | 0a946c5 - Bootstrap 2.3.2 added and compatibility changes for dropdown menu (2013-06-10 00:29:22 +0200) <benjaoming>
    * | | c24c882 - cleanup bootstrap (2013-06-09 23:32:54 +0200) <benjaoming>
    | |/  
    |/|   
    * | c259b31 - Alter plugin API: BasePlugin.urlpatterns is now a dictionary (2013-06-09 18:43:02 +0200) <benjaoming>
    * | ca59f20 - undo, only bad inheritance results in need of self.request set here (2013-06-09 18:13:52 +0200) <benjaoming>
    * | 8bab47d - self.request on ArticleMixin view to allow for parent dispatch methods assuming its existence (2013-06-09 17:45:57 +0200) <benjaoming>
    * | 0b9c2c5 - shorten database settings (2013-06-09 17:44:52 +0200) <benjaoming>
    * | ac04cb6 - fix missing refactoring on renamed template block wiki_pagetitle (2013-06-09 17:44:03 +0200) <benjaoming>
    * |   dfb9456 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-06-09 15:50:30 +0200) <benjaoming>
    |\ \  
    | * | 00e4713 - Update README.md (2013-06-07 02:08:15 +0300) <benjaoming>
    * | | 0d13578 - Fix #161 (mark accumulated notifications is_emailed=False) + clean up code + make notification email nicer (2013-06-09 15:50:14 +0200) <benjaoming>
    |/ /  
    * |   a84eb16 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-06-07 00:57:25 +0200) <benjaoming>
    |\ \  
    | * | b78edee - Update README.md (2013-06-07 01:55:11 +0300) <benjaoming>
    * | | 00cf45b - (tag: alpha/0.0.20) Bump to 0.0.20 (2013-06-07 00:38:39 +0200) <benjaoming>
    |/ /  
    * |   cc537a5 - Merge pull request #159 from TomLottermann/master (2013-06-06 14:16:19 -0700) <benjaoming>
    |\ \  
    | * | 1bc5e48 - The management command now loads the language see https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ for more details (2013-06-06 20:40:21 +0200) <Thomas Lottermann>
    | * | 5c53280 - adding missing manifest information. language files were not included in the build. (2013-06-06 19:47:51 +0200) <Thomas Lottermann>
    |/ /  
    * |   10c6444 - Merge pull request #157 from crazyzubr/master (2013-05-29 12:08:48 -0700) <benjaoming>
    |\ \  
    | * | 6575a4a - simplify notify_settings (2013-05-26 20:39:19 +0800) <crazyzubr>
    | * | dca3618 - fix notify_settings confuse (2013-05-26 18:25:13 +0800) <crazyzubr>
    | * | f00af80 - filehandler django_notify in daemon mode (2013-05-26 17:56:12 +0800) <crazyzubr>
    * | |   eabe615 - Merge pull request #156 from crazyzubr/master (2013-05-25 10:49:04 -0700) <benjaoming>
    |\ \ \  
    | |/ /  
    | * | 3f08aec - fix (2013-05-25 23:57:58 +0800) <crazyzubr>
    | * | 1006454 - add russian translation from django-notify (2013-05-25 23:55:26 +0800) <crazyzubr>
    * | |   4fe5e47 - Merge pull request #155 from crazyzubr/master (2013-05-25 06:03:37 -0700) <benjaoming>
    |\ \ \  
    | |/ /  
    | * | 90dde5a - fix errata (locale ru) (2013-05-25 20:38:22 +0800) <crazyzubr>
    | * | 2d4eae2 - update locale ru (.po and .mo) (2013-05-25 20:11:49 +0800) <crazyzubr>
    | * | fe8c7bd - Create django.po (2013-05-25 18:33:47 +0800) <crazyzubr>
    |/ /  
    * |   69d209d - Merge pull request #153 from TomLottermann/master (2013-05-20 11:38:34 -0700) <benjaoming>
    |\ \  
    | * | fd0ef6a - Updated german translations (2013-05-20 19:10:23 +0200) <TomLottermann>
    |/ /  
    * |   1b7c241 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-05-20 13:46:47 +0200) <benjaoming>
    |\ \  
    | * | 8b93d34 - Update TEMPLATE_CONTEXT_PROCESSORS instructions (2013-05-19 14:37:31 +0200) <benjaoming>
    * | | 71880a2 - #145 do not break when AUTH_USER_MODEL is set on django<1.5 project (2013-05-19 22:02:50 +0200) <benjaoming>
    * | | ad7b664 - Respect custom models (NB! current django 1.5.1 breaks wiki.views.accounts) #145 (2013-05-19 21:47:02 +0200) <benjaoming>
    * | | 68e3478 - Remove spaces (2013-05-19 21:45:15 +0200) <benjaoming>
    * | | 4e32ab6 - Add test suite that supports settings.AUTH_USER_MODEL and testing of South migrations #145 (2013-05-19 18:43:31 +0200) <benjaoming>
    * | | 670c4d2 - #145 - add compatibility layer for importing users (2013-05-19 18:43:15 +0200) <benjaoming>
    |/ /  
    * | 60c24e6 - Remove revisions to shrink prepopulated test db (2013-05-18 20:39:45 +0200) <benjaoming>
    * | 03f0cc5 - vacuum sqlite test database and add new migrations (2013-05-18 20:36:16 +0200) <benjaoming>
    * | e2d188b - Remember to call parent UserCreationForm.clean - fix username not tested for uniqueness in account handling (2013-05-18 20:15:29 +0200) <benjaoming>
    * | 5d4c545 - BaseRevisionMixin.previous_revision: Allow deletion of Revisions by setting back-referenced revisions to NULL such that future revisions are not cascade deleted. (2013-05-18 20:13:00 +0200) <benjaoming>
    * | e506c09 - Issue #145 - Add support for settings.AUTH_USER_MODEL both in model ForeignKey fields and South migrations. Backwards-compatible. (2013-05-18 20:10:53 +0200) <benjaoming>
    * | 84c07e8 - #151 - missing translation calls (2013-05-17 13:05:06 +0200) <benjaoming>
    * |   ec82837 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-05-17 12:40:20 +0200) <benjaoming>
    |\ \  
    | * \   7a2103d - Merge pull request #150 from xiaclo/patch-1 (2013-05-13 01:39:53 -0700) <benjaoming>
    | |\ \  
    | | * | ee85908 - Remove space from urlify.js path (2013-05-12 15:50:11 +1000) <xiaclo>
    | |/ /  
    | * |   7e0f0a3 - Merge pull request #149 from TomLottermann/master (2013-05-04 05:13:21 -0700) <benjaoming>
    | |\ \  
    | | * | 8782c84 - Slug stays fixed if the article already has a initial slug (2013-05-04 14:03:41 +0200) <TomLottermann>
    | * | |   b5acff0 - Merge pull request #147 from TomLottermann/master (2013-04-28 10:26:01 -0700) <benjaoming>
    | |\ \ \  
    | | |/ /  
    | | * |   6a69d88 - Merge remote-tracking branch 'upstream/master' (2013-04-28 18:27:44 +0200) <TomLottermann>
    | | |\ \  
    | | |/ /  
    | |/| |   
    | * | | 7f172fb - Update README.md (2013-04-23 19:51:21 +0300) <benjaoming>
    | | * | 493305b - Added wrapSelection to editor.js (2013-04-28 18:23:37 +0200) <TomLottermann>
    * | | | 5b6c496 - (tag: alpha/0.0.19) Version bump (2013-04-23 18:26:26 +0200) <benjaoming>
    |/ / /  
    * | | 61b3c61 - Make the urlize parser more strict (2013-04-23 18:19:13 +0200) <benjaoming>
    * | | 36f3640 - add back anon read access to test main article (2013-04-16 18:42:42 +0200) <benjaoming>
    * | | 31e2e60 - font size in blockquotes (2013-04-16 17:46:36 +0200) <benjaoming>
    * | | 83c72bf - lock main article in the test project (2013-04-16 17:46:14 +0200) <benjaoming>
    * | | dec9335 - Add attr_list to allow e.g. custom Header ids for custom references to header sections (2013-04-14 17:49:41 +0200) <benjaoming>
    * | | 1a896ed - Markdown needs to be >2.2.0 due to 2.1.1 headerid extension tested broken with newer ElemenTree versions (2013-04-14 17:40:06 +0200) <benjaoming>
    * | | 09e8af9 - less blahblah on the contribution stuff (2013-04-11 01:21:38 +0200) <benjaoming>
    * | | 78bf232 - remove pip --use-mirrors (2013-04-11 01:14:56 +0200) <benjaoming>
    * | |   6a1217c - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-04-09 22:47:59 +0200) <benjaoming>
    |\ \ \  
    | * \ \   60bcbbd - Merge pull request #143 from TomLottermann/master (2013-04-07 13:07:03 -0700) <benjaoming>
    | |\ \ \  
    | | |/ /  
    | | * |   9ca5afb - Merge branch 'master' of github.com:TomLottermann/django-wiki (2013-04-07 18:50:48 +0200) <TomLottermann>
    | | |\ \  
    | | | * | d4ce6ca - Fixed wrong icon when deleting article (2013-04-07 18:46:42 +0200) <TomLottermann>
    | | * | | 06dc3ed - Fixed wrong icon when deleting article (2013-04-07 18:49:22 +0200) <TomLottermann>
    | | |/ /  
    | * | |   d280dd4 - Merge pull request #142 from TomLottermann/master (2013-04-07 07:28:43 -0700) <benjaoming>
    | |\ \ \  
    | | |/ /  
    | | * | a705f64 - version fix (2013-04-07 16:06:29 +0200) <TomLottermann>
    | | * | 4cbc633 - version fix (2013-04-07 16:02:59 +0200) <TomLottermann>
    | | * | 7188641 - Added translations for django_notify (2013-04-07 16:02:49 +0200) <TomLottermann>
    | | * | acba7f7 - Respected changes, reformatted the lines (2013-04-07 15:34:13 +0200) <TomLottermann>
    | |/ /  
    * | | c2f450b - fix SimplePlugin constructor - pull #144 (2013-04-09 22:47:21 +0200) <benjaoming>
    |/ /  
    * |   ca5e28a - pull #141 - remove old test mechanism, try adding Warning failure (2013-04-07 01:17:10 +0200) <benjaoming>
    |\ \  
    | * | 16f8e0b - pull #141 - add manage.py test + Django 1.5 to Travis config (2013-04-07 00:27:01 +0200) <benjaoming>
    * | | e36f597 - pull #141 - remove old test mechanism, try adding Warning failure (2013-04-07 01:16:13 +0200) <benjaoming>
    |/ /  
    * |   177bf3c - Merge pull request #141 from hynekcer/master (2013-04-06 15:14:29 -0700) <benjaoming>
    |\ \  
    | * | eecd8a5 - Fixed on_article_delete_clear_cache. Some articles in the cache were not cleared and tests failed. (2013-04-06 23:31:28 +0200) <Hynek Cernoch>
    | * | 2ad0694 - Added tests for clearing cache and for updating article_list (2013-04-06 22:33:13 +0200) <Hynek Cernoch>
    | * | effc58a - Fixed on_article_delete if the article has children. (2013-04-06 19:28:13 +0200) <Hynek Cernoch>
    | * | 44e4d7a - Added more tests and refactored the the first one. (2013-04-06 19:13:57 +0200) <Hynek Cernoch>
    | * | 6dc14a1 - Fixed RuntimeWarning by replacing naive datetime by utc (2013-04-06 19:07:35 +0200) <Hynek Cernoch>
    * | | d746543 - #140 - Markdown 2.2/2.3 API change - do not rely on markdown.extensions.headerid.unique (2013-04-06 16:25:10 +0200) <benjaoming>
    |/ /  
    * | f6eb8be - French translation - changed msg id (att. pull #138) (2013-04-05 17:13:18 +0200) <benjaoming>
    * | 8332ab6 - pull #139 - form data from args or kwargs (2013-04-04 21:11:25 +0200) <benjaoming>
    * |   1aa8eb2 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-04-04 21:11:14 +0200) <benjaoming>
    |\ \  
    | * | 4f0ef1a - pull #139 - form data from args or kwargs (2013-04-04 21:08:08 +0200) <benjaoming>
    * | | 09f91ea - pull #139 - form data from args or kwargs (2013-04-04 21:10:18 +0200) <benjaoming>
    |/ /  
    * |   159025b - Merge pull request #139 from hynekcer/master (2013-04-04 11:50:39 -0700) <benjaoming>
    |\ \  
    | * | 634c3c0 - Revert "Fixed posting data to views.article.Preview" (2013-04-04 18:20:18 +0200) <Hynek Cernoch>
    | * | 1bba4ec - Added recursion test for the current bug in preview. (2013-04-04 18:19:31 +0200) <Hynek Cernoch>
    |/ /  
    * |   c3bbc37 - Do not use kwargs for permission methods (2013-04-04 14:36:23 +0200) <benjaoming>
    |\ \  
    | * | 2d7957a - Do not use kwargs for permission methods (2013-04-04 14:34:24 +0200) <benjaoming>
    * | | 37d9939 - Do not use kwargs for permission methods (2013-04-04 14:35:15 +0200) <benjaoming>
    |/ /  
    * | d37e09c - #137 place permission logic ONLY in core.permissions and make article.can_read and article.can_write configurable (2013-04-04 14:23:17 +0200) <benjaoming>
    * |   fdd36cd - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-04-04 14:22:36 +0200) <benjaoming>
    |\ \  
    | * \   de55506 - Merge pull request #138 from jdcaballero/master (2013-04-02 11:08:56 -0700) <benjaoming>
    | |\ \  
    | | * \   054b3af - Merge remote-tracking branch 'origin/master' (2013-04-02 18:32:50 +0200) <Juan Diego Caballero>
    | | |\ \  
    | | |/ /  
    | |/| |   
    | * | | 84dc39f - More clear PIL instructions. (2013-04-02 17:46:06 +0300) <benjaoming>
    | | * | 5468b9a - Spanish translations added. (2013-04-02 16:27:39 +0200) <Juan Diego Caballero>
    | | * | b74303e - Do not use HttpResponseRedirectBase anyways, just check status_code (2013-04-02 16:21:25 +0200) <benjaoming>
    | | * | 43dbdd9 - fix imporerror for HttpResponseRedirectBase (2013-04-02 16:21:25 +0200) <benjaoming>
    | | * | bc0eff8 - JSON view can return HttpResponseRedirect (2013-04-02 16:21:24 +0200) <benjaoming>
    | | * | 71a6457 - changing apt-get to use python-imaging (2013-04-02 16:21:24 +0200) <Dennis Coldwell>
    | | * | f76bc85 - adding PIL pre-req documentation (2013-04-02 16:21:24 +0200) <Dennis Coldwell>
    * | | | 71c59d6 - fix wrong form target on clicking 'Switch to selected version' + modal window height (2013-04-04 14:20:47 +0200) <benjaoming>
    |/ / /  
    * | | beb7571 - Do not use HttpResponseRedirectBase anyways, just check status_code (2013-03-29 23:19:58 +0100) <benjaoming>
    * | | 6da0fd9 - fix imporerror for HttpResponseRedirectBase (2013-03-29 23:16:44 +0100) <benjaoming>
    * | | 3f1ac96 - JSON view can return HttpResponseRedirect (2013-03-29 23:13:53 +0100) <benjaoming>
    * | |   6a9539d - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-03-29 17:57:39 +0100) <benjaoming>
    |\ \ \  
    | |/ /  
    |/| |   
    | * |   f4f3a1d - Merge pull request #135 from coldwd/patch-1 (2013-03-27 10:55:43 -0700) <benjaoming>
    | |\ \  
    | | * | ef83744 - changing apt-get to use python-imaging (2013-03-27 10:45:41 -0700) <Dennis Coldwell>
    | | * | 4cf921f - adding PIL pre-req documentation (2013-03-26 20:39:53 -0700) <Dennis Coldwell>
    | |/ /  
    * | | 0ff3fd4 - Fix #136 (2013-03-29 17:57:08 +0100) <benjaoming>
    |/ /  
    * | e9bd946 - add clearfix for article tocs and indexes (2013-03-26 20:12:43 +0100) <benjaoming>
    * | 5fdb93d - fix #130 - display disabled dropdown when no assignment permission (2013-03-26 20:12:20 +0100) <benjaoming>
    * | 45cd25e - clean up block tags to be prefixed 'wiki_*' (2013-03-26 20:11:42 +0100) <benjaoming>
    * |   0911c58 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-03-26 18:52:31 +0100) <benjaoming>
    |\ \  
    | * \   914ecf5 - Merge pull request #132 from hynekcer/master (2013-03-26 10:15:52 -0700) <benjaoming>
    | |\ \  
    | | * | 8f60a11 - Fixed typo in admin - Article revision list columns (2013-03-26 17:38:41 +0100) <Hynek Cernoch>
    | |/ /  
    | * | a908af4 - Update README.md (2013-03-26 11:22:36 +0100) <benjaoming>
    * | | 0344928 - Update to Bootstrap 2.3.1 and simplify LESS import statements (2013-03-26 18:52:02 +0100) <benjaoming>
    |/ /  
    * | 428d236 - (tag: alpha/0.0.18) Bump to 0.0.18 (2013-03-26 11:08:09 +0100) <benjaoming>
    * | 85602fe - Fix #125 - missing redirect call (2013-03-26 11:06:41 +0100) <benjaoming>
    * |   807611b - Merge pull request #131 from daltonmatos/translation/pt_BR (2013-03-26 02:46:40 -0700) <benjaoming>
    |\ \  
    | * | 5779039 - Adding translation for pt_BR (2013-03-26 00:03:18 -0300) <Dalton Barreto>
    |/ /  
    * |   2cd0dbe - Merge pull request #129 from TomLottermann/master (2013-03-19 07:18:05 -0700) <benjaoming>
    |\ \  
    | * | dc6a2aa - reset readme and removed mo ignorance from gitignore, since it is needed (2013-03-19 09:07:27 +0100) <TomLottermann>
    | * | 548cc81 - complete set of languages (2013-03-18 21:33:15 +0100) <TomLottermann>
    | * | 62b37b3 - compiled recent version (2013-03-17 20:53:47 +0100) <TomLottermann>
    | * | 757f24a - Plugins are a WIP (2013-03-17 20:53:14 +0100) <TomLottermann>
    | * | b694a89 - right names (2013-03-17 15:44:00 +0100) <TomLottermann>
    | * | 3339ae4 - fixes to the manifest (2013-03-17 15:25:30 +0100) <TomLottermann>
    | * | 69a4b2d - german locale (2013-03-17 14:58:43 +0100) <TomLottermann>
    | * | 9da762d - Compilation of german locale (2013-03-17 14:57:11 +0100) <TomLottermann>
    | * | d9b997b - initial translation done (without the plugins) (2013-03-17 14:54:02 +0100) <TomLottermann>
    | * | a6182dd - start of translations (2013-03-16 20:19:40 +0100) <TomLottermann>
    | * | 59b6558 - start of translations (2013-03-16 20:19:01 +0100) <TomLottermann>
    | * | 8efc4bd - readme changed (2013-03-16 17:49:34 +0100) <TomLottermann>
    |/ /  
    * |   75a0581 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-03-08 13:33:21 +0100) <benjaoming>
    |\ \  
    | * | 2b28521 - Update README.md (2013-03-06 18:27:09 +0100) <benjaoming>
    | * |   17b15d9 - Merge pull request #124 from SacNaturalFoods/master (2013-02-27 08:11:16 -0800) <benjaoming>
    | |\ \  
    | | * | 3add05a - fixed _clear_ancestor_cache call (2013-02-27 08:08:30 -0800) <tschmidt>
    | * | |   bc57765 - Merge pull request #122 from SacNaturalFoods/master (2013-02-26 15:49:21 -0800) <benjaoming>
    | |\ \ \  
    | | |/ /  
    | | * | 088e2de - moved article save and delete clear cache signal handlers to Article model (2013-02-25 17:21:39 -0800) <tschmidt-dev>
    | | * | 217fea9 - refactored urlpath._clear_ancenstor_cache to use article.ancenstor_objects generator (2013-02-25 15:47:12 -0800) <tschmidt-dev>
    | | * |   7a2985c - merge (2013-02-25 15:10:42 -0800) <tschmidt-dev>
    | | |\ \  
    | | * | | e20b2d6 - clear ancestor cache on save and delete article so that things like article_lists are refreshed (2013-02-25 11:22:37 -0800) <tschmidt>
    | | | |/  
    | | |/|   
    * | | | 6641ed1 - use self.stdout in django_notify management script logging (see django docs: https://docs.djangoproject.com/en/dev/howto/custom-management-commands/) (2013-03-08 13:32:59 +0100) <benjaoming>
    |/ / /  
    * | | df27e51 - Fixed posting data to views.article.Preview (2013-02-26 21:46:49 +0100) <benjaoming>
    | |/  
    |/|   
    * | c775a18 - #111 Add ancestor generator to Article (2013-02-26 00:18:37 +0100) <benjaoming>
    |/  
    * 9ca892d - Do not use URLField, it does not allow relative paths (2013-02-23 19:07:00 +0100) <benjaoming>
    * 7ec137f - Redirect from sign up and login pages for logged in users. Use wiki:root url for root article. (2013-02-23 18:28:20 +0100) <benjaoming>
    * 0af4af2 - #119 restore if image deleted and uploading new image file (2013-02-23 18:20:05 +0100) <benjaoming>
    * b73278c - remove initial blank attachments and images (2013-02-23 18:18:14 +0100) <benjaoming>
    * 7f6acb7 - #119 do not fail when deleting blank image and attachment fields (2013-02-23 18:17:36 +0100) <benjaoming>
    * 51497ca - page title for signup page (2013-02-23 17:56:36 +0100) <benjaoming>
    *   c06108c - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-23 17:54:27 +0100) <benjaoming>
    |\  
    | *   c8eeab5 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-23 17:54:00 +0100) <benjaoming>
    | |\  
    * | \   6e9f4f5 - Add a simple honeypot for signups #116 (2013-02-23 17:54:18 +0100) <benjaoming>
    |\ \ \  
    | |/ /  
    |/| /   
    | |/    
    | * a570d0a - Add a simple honeypot for signups (2013-02-23 17:52:39 +0100) <benjaoming>
    * | acd9636 - Add a simple honeypot for signups #117 (2013-02-23 17:53:49 +0100) <benjaoming>
    |/  
    *   2173d4b - Merge pull request #117 from jdcaballero/master (2013-02-23 08:08:31 -0800) <benjaoming>
    |\  
    | * c96d656 - User creation form extendedto include email as a required field (2013-02-23 09:21:14 +0100) <Juan Diego Caballero>
    | *   3932d27 - Merge branch 'master' of https://github.com/benjaoming/django-wiki (2013-02-22 14:07:28 +0100) <Juan Diego Caballero>
    | |\  
    | * | f0b25a5 - UserCreateForm subclassed to include the email as a required parameter in the signup. (2013-02-22 12:19:37 +0100) <Juan Diego Caballero>
    * | | 80790d5 - #118 django 1.5 (2013-02-23 17:04:54 +0100) <benjaoming>
    * | | 3950de5 - Fix #118 Avoid deprecation warning in Django 1.5 (2013-02-23 01:08:30 +0100) <benjaoming>
    * | |   e091f01 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-23 01:07:44 +0100) <benjaoming>
    |\ \ \  
    | * | | c6f9ee5 - Fix #118 Avoid deprecation warning in Django 1.5 (2013-02-23 00:57:27 +0100) <benjaoming>
    * | | | 6367157 - Fix #118 (forgot django_notify) Avoid deprecation warning in Django 1.5 (2013-02-23 01:07:18 +0100) <benjaoming>
    |/ / /  
    * | | 098faa1 - Add note in pluginbase about use of Meta.app_label (2013-02-22 23:41:01 +0100) <benjaoming>
    * | | b20094c - Inherit from EmptyQuerySet (2013-02-22 16:56:04 +0100) <benjaoming>
    | |/  
    |/|   
    * | a4f9d3b - Few more readme changes (2013-02-22 12:42:29 +0100) <benjaoming>
    * | ead17b0 - Todo and readme updates (2013-02-22 12:39:47 +0100) <benjaoming>
    * |   65c882b - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-22 11:55:47 +0100) <benjaoming>
    |\ \  
    | |/  
    | * efb617e - Update to 0.0.17 (2013-02-22 02:13:22 +0100) <benjaoming>
    * | a7254ab - (tag: alpha/0.0.17) bump to 0.0.17 (2013-02-22 02:00:50 +0100) <benjaoming>
    |/  
    * bfec4e8 - rename command, cleanup code, add logging (2013-02-22 02:00:05 +0100) <benjaoming>
    * 15b02ae - ignore settings_local (2013-02-22 00:46:48 +0100) <benjaoming>
    * 1e9d5b5 - remove print stm (2013-02-22 00:46:14 +0100) <benjaoming>
    * bcddb0b - Support and contributions (2013-02-22 00:11:39 +0100) <benjaoming>
    * d913907 - Support and contributions (2013-02-22 00:11:24 +0100) <benjaoming>
    *   088c0fe - Merge pull request #115 from jdcaballero/master (2013-02-21 14:56:36 -0800) <benjaoming>
    |\  
    | * fbd75ae - Subject changed to a translated string, notification email changed to @example.com (2013-02-21 16:36:02 +0100) <Juan Diego Caballero>
    | * c13d97d -  Notifications Implementation: (2013-02-21 14:37:02 +0100) <Juan Diego Caballero>
    | * a47c6da - Revert "Email Notifications Implementation" (2013-02-21 14:33:32 +0100) <Juan Diego Caballero>
    | * 700bb6e - Email Notifications Implementation (2013-02-21 14:22:21 +0100) <Juan Diego Caballero>
    |/  
    * e448e2b - Replace Markdown toc extension and add improved version to macro package. (2013-02-18 12:17:22 +0100) <benjaoming>
    * 9655067 - bootstrap typography (2013-02-15 16:38:11 +0100) <benjaoming>
    * ea70181 - bootstrap typography and remove extra <li>s on article_list (2013-02-15 16:35:45 +0100) <benjaoming>
    * 61131d8 - (tag: alpha/0.0.16) bump to 0.0.16 (2013-02-15 02:30:48 +0100) <benjaoming>
    * d66234e - cache key should be from current revision (2013-02-14 23:43:43 +0100) <benjaoming>
    * 089dd2f - restore lost-and-found auto collection if subtrees are disconnected (2013-02-14 23:40:37 +0100) <benjaoming>
    * fa3c916 - soft linebreak after images to conserve preceeding headline elements (2013-02-14 23:40:05 +0100) <benjaoming>
    * db07ac2 - invalidate article cache when plugins are updated (2013-02-14 23:39:16 +0100) <benjaoming>
    * 1dd4788 - thumbnail styles (2013-02-14 23:37:56 +0100) <benjaoming>
    * db73b51 - redirect for delete view to parent (2013-02-14 20:52:49 +0100) <benjaoming>
    * dcf7e72 - fix article purging (2013-02-14 20:45:34 +0100) <benjaoming>
    * c57656a - only show active children in article_list (2013-02-14 20:42:21 +0100) <benjaoming>
    * 701e34b - show article titles instead of slugs in index view (2013-02-14 20:37:13 +0100) <benjaoming>
    * ea1b3ad - allow inline attachment tag (2013-02-14 20:14:59 +0100) <benjaoming>
    * fc94f67 - do not show deleted files in list, add separate restore menu item (2013-02-14 20:07:47 +0100) <benjaoming>
    * fc9efa6 - non-zip files fix for moderators and clean up a bit (2013-02-14 19:52:59 +0100) <benjaoming>
    * e85cbc6 - title for TOCs (2013-02-14 19:33:54 +0100) <benjaoming>
    * b0a6d6e - bootstrap styling (2013-02-14 19:17:43 +0100) <benjaoming>
    * dfb5693 - python 2.5 compatibility for zip archives (2013-02-14 17:30:17 +0100) <benjaoming>
    * 1b5b583 - zip file uploading and extracting for moderators (2013-02-14 16:47:57 +0100) <benjaoming>
    * 4f019e7 - raise 404 if plugin is missing (2013-02-14 16:47:38 +0100) <benjaoming>
    * 0cabdfb - refactor article view to use view.html template (2013-02-14 14:13:40 +0100) <benjaoming>
    * 0579521 - fix spam protection wrongly targetting moderators (2013-02-14 13:20:03 +0100) <benjaoming>
    * 44b1e2f - Make cache timeout configurable and remove erred block tags from render.html (2013-02-14 13:05:27 +0100) <benjaoming>
    * 0d092fa - improve resizable to properly fit nested iframes etc (2013-02-13 01:42:07 +0100) <benjaoming>
    * ecaccbd - add request context processor and check that config is OK (2013-02-13 01:24:54 +0100) <benjaoming>
    * 6a3c777 - resizable modals (2013-02-13 01:21:08 +0100) <benjaoming>
    * e4d0669 - add template assignment tag login_url (2013-02-13 00:27:27 +0100) <benjaoming>
    * 73af524 - broken boostrap-responsive build (2013-02-12 22:28:25 +0100) <benjaoming>
    * be19fdb - do not show deleted articles in article_list macro (2013-02-11 17:37:22 +0100) <benjaoming>
    *   6be1a3d - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-09 16:06:11 +0100) <benjaoming>
    |\  
    | * eb3bd0b - Update README.md (2013-02-08 12:48:34 +0100) <benjaoming>
    * | e6e0a84 - Add better info about licensing (2013-02-09 14:20:11 +0100) <benjaoming>
    |/  
    * d25da1c - (tag: alpha/0.0.15) Bump to 0.0.15 (2013-02-08 12:28:21 +0100) <benjaoming>
    * 51daba0 - add model chart in pdf to the build-sdist process (2013-02-08 12:23:59 +0100) <benjaoming>
    * e7c70fd - typo (2013-02-08 12:20:55 +0100) <benjaoming>
    * 89b64aa - modify build to clean up old egg dir and add back the MANIFEST.in symlink (2013-02-08 12:18:45 +0100) <benjaoming>
    * d568683 - python 2.5 support (2013-02-07 18:05:23 +0100) <benjaoming>
    * 2c39d15 - do not fail when removing images located in non-existing dirs (2013-02-07 17:54:57 +0100) <benjaoming>
    * 628b59c - image plugin thumbnail css (2013-02-07 17:45:25 +0100) <benjaoming>
    * 948580c - image plugin thumbnail css (2013-02-07 17:35:11 +0100) <benjaoming>
    * da15d5d - use LESS for stylesheets by extending twitter-bootstrap (2013-02-07 17:26:56 +0100) <benjaoming>
    * 76a3532 - rm dupe lines (2013-02-07 16:23:00 +0100) <benjaoming>
    * f0c3458 - footer clearfix (2013-02-07 16:22:33 +0100) <benjaoming>
    *   ece1239 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-07 15:28:59 +0100) <benjaoming>
    |\  
    | *   94e6035 - Merge pull request #108 from SacNaturalFoods/master (2013-02-04 16:58:52 -0800) <benjaoming>
    | |\  
    | | * 26c922b - removed overlooked debug print statements (2013-02-04 15:09:24 -0800) <tschmidt-dev>
    | | * 4d34e70 - fixed macro arg regex for args longer than 1 character (2013-02-04 09:36:01 -0800) <tschmidt-dev>
    | |/  
    * | abe7282 - unfinished generic markdown extension (2013-02-07 15:28:54 +0100) <benjaoming>
    * | 53205ac - fix setting article fk on reusable plugins for identifying permissions (2013-02-07 15:27:20 +0100) <benjaoming>
    |/  
    * 7e6da88 - (tag: alpha/0.0.14) Bump to 0.0.14 (2013-02-03 19:53:09 +0100) <benjaoming>
    * 67d8cf3 - Security fix, do not call eval on input (2013-02-03 19:52:33 +0100) <benjaoming>
    * d9d19f0 - fix python 2.5 unknown elementree method (2013-02-03 17:42:18 +0100) <benjaoming>
    * f9a46f1 - (tag: alpha/0.0.13) Note on python 2.5 and improve article list (2013-02-03 17:31:54 +0100) <benjaoming>
    * c4e855d - Update README.md (2013-02-03 17:22:31 +0100) <benjaoming>
    * 076ad8e - Python 2.5 support note (2013-02-03 17:21:15 +0100) <benjaoming>
    * 0106b6f - python 2.5 support (2013-02-03 16:15:21 +0100) <benjaoming>
    * b86be8c - (tag: alpha/0.0.12) version bump to 0.0.12 (2013-02-03 15:58:27 +0100) <benjaoming>
    * d5f8352 - Fix #100 add print CSS and remove inline <style> (2013-02-03 15:55:37 +0100) <benjaoming>
    * 9070358 - Fix error in macros removing unknown tags from stack and prettify styling (2013-02-03 15:08:25 +0100) <benjaoming>
    * ff9ad26 - add a few more default markdown plugins (2013-02-03 15:07:43 +0100) <benjaoming>
    * 2ed231a - Apply user info on the creater of the first revision of the root article (2013-02-03 14:31:08 +0100) <benjaoming>
    * c50e05f - Display a helping exception message when MPTT is failing (2013-02-03 14:30:30 +0100) <benjaoming>
    * e25b3a4 - logo block for footer (2013-02-03 14:28:23 +0100) <benjaoming>
    * 1b06fb0 - Fix example code (2013-02-03 14:27:45 +0100) <benjaoming>
    * 2aabc2d - move macros configuration and do not include django_notify twice in the urlconf (2013-02-03 14:27:27 +0100) <benjaoming>
    * affa159 - Make django notify admin configurable so it can be excluded (2013-02-03 14:10:46 +0100) <benjaoming>
    *   d004700 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-02-03 14:09:11 +0100) <benjaoming>
    |\  
    | *   365793d - Merge pull request #107 from SacNaturalFoods/master (2013-02-01 18:40:49 -0800) <benjaoming>
    | |\  
    | | * 22486f5 - added kwargs logic to macros plugin and depth kwarg to article_list macro (2013-02-01 15:28:05 -0800) <tschmidt-dev>
    | |/  
    * | b336586 - Add help sidebar for macros and make allowed methods configurable (2013-02-03 14:08:57 +0100) <benjaoming>
    |/  
    * 0751cc8 - using wrong class for widget when in readonly mode on some settings form fields (2013-02-01 18:38:22 +0100) <benjaoming>
    * 86ee414 - receive post_save signal only using kwargs (2013-02-01 14:09:00 +0100) <benjaoming>
    * 91076f2 - security fix for macro plugin, add plugins.acros to testproject (2013-02-01 14:08:16 +0100) <benjaoming>
    *   933ac19 - Merge pull request #105 from SacNaturalFoods/master (2013-02-01 04:04:43 -0800) <benjaoming>
    |\  
    | * d6f3724 - restructured url resolver in article_list macro (2013-01-31 13:58:07 -0800) <tschmidt-dev>
    | * c0d5f25 - fixed article_list macro sublist markup (2013-01-30 09:20:31 -0800) <tschmidt-dev>
    | * a7bbf18 - added Django 1.5 url syntax to macros plugin; added condition to avoid generating empty lists for each child in article_list macro (2013-01-30 09:13:30 -0800) <tschmidt-dev>
    | * 5eda878 - added wiki-article-sublist class to article_list macro template (2013-01-29 15:59:55 -0800) <tschmidt-dev>
    | * 3493af1 - added wiki-article-list class to article_list macro template (2013-01-29 15:54:30 -0800) <tschmidt-dev>
    | * 5a3c029 - added core macros plugin with initial article_list macro (2013-01-29 10:24:21 -0800) <tschmidt-dev>
    * |   919d45e - Merge pull request #104 from SacNaturalFoods/master (2013-01-28 17:11:29 -0800) <benjaoming>
    |\ \  
    | |/  
    | * f14ecef - collapsed MARKDOWN_EXTENSIONS and MARKDOWN_SAFE_MODE settings into MARKDOWN_KWARGS (2013-01-28 11:55:17 -0800) <tschmidt-dev>
    * | f58974d - Update README.md (2013-01-27 19:50:47 +0100) <benjaoming>
    * | 4bf8769 - Update README.md (2013-01-27 19:49:52 +0100) <benjaoming>
    * |   61e5952 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-01-27 03:30:18 +0100) <benjaoming>
    |\ \  
    | * | 603898f - Update README.md (2013-01-27 03:18:52 +0100) <benjaoming>
    | * | 3167e4b - Update README.md (2013-01-27 03:04:06 +0100) <benjaoming>
    | * | 281e276 - Update README.md (2013-01-27 02:24:58 +0100) <benjaoming>
    * | | c93f3c5 - add debug_toolbar if installed (2013-01-27 03:27:54 +0100) <benjaoming>
    |/ /  
    * |   27f5b44 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-01-27 02:21:35 +0100) <benjaoming>
    |\ \  
    | * \   23f48b3 - Merge pull request #102 from SacNaturalFoods/master (2013-01-26 16:34:39 -0800) <benjaoming>
    | |\ \  
    | | |/  
    | | * 0f02092 - added MARKDOWN_SAFE_MODE setting (2013-01-24 15:35:03 -0800) <tschmidt-dev>
    | | * 8ac9814 - fixed help plugin TOC syntax and added Tables section (2013-01-24 10:07:18 -0800) <tschmidt-dev>
    | * |   31562fd - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-01-20 19:32:49 +0100) <benjaoming>
    | |\ \  
    * | | | 68fc90c - Add settings for inheriting owner and group permissions and fix #99 (2013-01-27 02:21:12 +0100) <benjaoming>
    * | | |   b1b3aea - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-01-20 19:33:44 +0100) <benjaoming>
    |\ \ \ \  
    | |/ / /  
    |/| / /   
    | |/ /    
    | * | c21775d - Use Form Media for SelectWidgetBootstrap and update wiki_form templatetag (2013-01-20 19:31:53 +0100) <benjaoming>
    | |/  
    * | 9c5f46d - Use Form Media for SelectWidgetBootstrap and update wiki_form templatetag Fix #95 (2013-01-20 19:32:27 +0100) <benjaoming>
    |/  
    * efd8db8 - WARNING! May break your config: Clean up settings variale names in images and attachments plugins and use unified defaults. Issue #91. (2013-01-16 10:22:51 +0100) <benjaoming>
    *   6b9f346 - Merge pull request #92 from gluwa/master (2013-01-16 01:06:26 -0800) <benjaoming>
    |\  
    | * 55a4a5b - in attachments plugin, append '.upload' to uploaded files only when settings.APPEND_EXTENSION is True. (2013-01-16 17:25:54 +0900) <Tae-lim Oh>
    | * 15a33ea - adding custom storage backend option to images plugin (2013-01-16 17:25:03 +0900) <Tae-lim Oh>
    |/  
    *   64a22a8 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-01-10 16:45:51 +0100) <benjaoming>
    |\  
    | * 5f90b18 - Update README.md (2013-01-09 21:03:45 +0100) <benjaoming>
    * | 453131e - add testproject template dir (2013-01-10 16:45:25 +0100) <benjaoming>
    * | 59567e3 - Error pages for test project (2013-01-10 16:44:05 +0100) <benjaoming>
    |/  
    * 9664ce1 - Add PIL to requirements.txt and remove Python 2.5 from travis (2013-01-09 21:01:56 +0100) <benjaoming>
    * 3607ea8 - test with manage.py (2013-01-09 20:18:00 +0100) <benjaoming>
    * 659d145 - fix double requirement (2013-01-09 19:12:29 +0100) <benjaoming>
    *   6c7f905 - Merge branch 'master' of github.com:benjaoming/django-wiki (2013-01-09 18:37:21 +0100) <benjaoming>
    |\  
    | * 62d2c4f - Update README.md (2013-01-09 18:11:47 +0100) <benjaoming>
    * | 558d88c - fix pip argument for travis (2013-01-09 18:37:03 +0100) <benjaoming>
    |/  
    * 3b2aceb - travis config added (2013-01-09 18:07:14 +0100) <benjaoming>
    * 09cab11 - missing template load stm (2013-01-09 14:39:30 +0100) <benjaoming>
    * c14ee73 - Use JS to save article form data on all sidebar plugin forms (2013-01-09 01:33:47 +0100) <benjaoming>
    * 2e36575 - Scroll if there are many images, only warn about unsaved changes if there are in fact such (2013-01-09 01:30:31 +0100) <benjaoming>
    * fb40d08 - Avoid losing user data when a sidebar form is called and article contents have been modified #33 (2013-01-09 01:26:12 +0100) <benjaoming>
    * b9e95ef - Support for I10N - use timezone.now (2013-01-09 00:29:48 +0100) <benjaoming>
    * ab45a20 - Cleanup nicely when an image or attachment is deleted - remove the file and any empty directories #25 (2013-01-09 00:21:22 +0100) <benjaoming>
    * 36eb1f8 - Do not allow merging with a deleted revision #27 (2013-01-08 23:43:05 +0100) <benjaoming>
    * 652433f - Remove unused setting (2013-01-08 23:12:40 +0100) <benjaoming>
    * 8a010d8 - apply migrations to prepopulated test database (2013-01-08 22:19:10 +0100) <benjaoming>
    * 6eb99d2 - Account handling system should pass all django.contrib.auth test cases #86 (2013-01-08 22:10:32 +0100) <benjaoming>
    * ea2cd01 - Account handling system should pass all django.contrib.auth test cases #86 (2013-01-08 22:08:49 +0100) <benjaoming>
    * df59145 - Redirect for the built-in account handling when login is required + better err page. (2013-01-08 21:03:40 +0100) <benjaoming>
    * c805fee - Add link to forum/mailing list (2012-12-30 14:48:02 +0100) <benjaoming>
    * ac826e3 - sorl.thumbnail in INSTALLED_APPS + copy-paste friendly (2012-12-30 14:24:14 +0100) <benjaoming>
    * e8dcb97 - Update README.md (2012-12-30 13:49:54 +0100) <benjaoming>
    * bde97a5 - Update README.md (2012-12-30 13:48:23 +0100) <benjaoming>
    * 97734d0 - Update README.md (2012-12-30 13:44:58 +0100) <benjaoming>
    * f482b0c - Bumping to version 0.0.9 for new PyPi release (2012-12-30 13:42:09 +0100) <benjaoming>
    * 3add660 - Remove 'center' from javascript prompt help text (#88) (2012-11-25 23:51:52 +0100) <benjaoming>
    * 2c0b35a - Add local settings to testproject (2012-11-16 22:49:44 +0100) <benjaoming>
    * 82b4e32 - #71 and #87 - put the 'get' by path pattern at the very end of all patterns (2012-11-16 22:34:07 +0100) <benjaoming>
    * 9604209 - #71 - missing pattern 'get' in new class based urls (2012-11-16 22:07:18 +0100) <benjaoming>
    *   a106977 - Merge pull request #85 from shaunc/master (2012-11-15 03:03:40 -0800) <benjaoming>
    |\  
    | * f0592f5 - fixes merge (2012-11-14 21:50:53 -0500) <Shaun Cutts>
    | *   9a38e27 - merges recent changes w/ classurl branch (2012-11-14 21:46:54 -0500) <Shaun Cutts>
    | |\  
    |/ /  
    | * f8900d0 - adds class for url configuration (2012-11-14 20:41:50 -0500) <Shaun Cutts>
    | * 5e812ac - updates {% url %} use in notifications menubaritem template to confrom to django 1.5 (2012-11-14 20:40:02 -0500) <Shaun Cutts>
    * | c93b318 - Be explicit about application order (#84) (2012-11-08 00:10:56 +0100) <benjaoming>
    * |   ceb705b - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-11-08 00:05:36 +0100) <benjaoming>
    |\ \  
    | * | 6704790 - Retry: Fix settings.py link (#81) (2012-11-03 20:41:37 +0100) <benjaoming>
    | * | f84a092 - Fix settings.py link (#81) (2012-11-03 20:40:00 +0100) <benjaoming>
    | * | d586040 - Fix settings.py link (2012-11-03 18:55:31 +0100) <benjaoming>
    * | | 32591c2 - Regression from adding spam protection, missing argument in when view class Preview initialized EditForm (#83) (2012-11-08 00:04:27 +0100) <benjaoming>
    |/ /  
    * | 2cb3950 - Move all javascript to load at the bottom of the page and ensure only to add javascript inside Sekizai addtoblock tag. (#54) (2012-10-31 01:30:22 +0100) <benjaoming>
    * | 109421e - Fix markdown extension for images to allow no align:xx specified and use bootstrap pull-left and pull-right. Don't allow center alignment. (#65) (2012-10-31 00:57:36 +0100) <benjaoming>
    * | 1834071 - Add spam/bot protection by verifying user session and ip_address and check the number of recent revisions (#72) Add global setting to disable anonymous article creation (#72) (2012-10-31 00:36:46 +0100) <benjaoming>
    * | ecbacc8 - Count number of occurences of the same message and display "x times" in the notification list instead of duplicate messages. (2012-10-30 23:57:59 +0100) <benjaoming>
    * | ea71c5c - Add warning on Edit page if user is not logged in w/ link to login page and redirect back to edit page (#55) (2012-10-30 14:27:24 +0100) <benjaoming>
    * | 58cb725 - eh..remove alert() (2012-10-30 13:45:39 +0100) <benjaoming>
    * | ce1ff2e - Setting Colorbox.js width and height (#69) and adding captions. (2012-10-30 13:44:41 +0100) <benjaoming>
    * |   2458217 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-10-30 13:30:09 +0100) <benjaoming>
    |\ \  
    | * | cb3d251 - Ensure that CreateForm fails when slug field is longer than the maximum allowed slug length (#54). (2012-10-30 13:27:24 +0100) <benjaoming>
    * | | 1dbd51f - Ensure that CreateForm fails when slug field is longer than the maximum allowed slug length (#57) (2012-10-30 13:29:53 +0100) <benjaoming>
    |/ /  
    * | 393aa34 - Adding check on article locked for attachments. (#74) - Also cleaning up attachment list and removing forms when article is locked. Adding template filter is_locked (2012-10-30 13:12:37 +0100) <benjaoming>
    * | 9d801fb - Adding Bootstrap 2.2.0 (2012-10-30 13:12:09 +0100) <benjaoming>
    * |   e948b73 - Merge pull request #79 from avtobiff/update-readme-dependencies (2012-10-29 09:15:17 -0700) <benjaoming>
    |\ \  
    | * | f31b6d4 - Correct django dependency invariant (2012-10-29 17:08:10 +0100) <Per Andersson>
    | * | 78fa3a8 - Increase django-mptt dependency version (2012-10-29 17:07:47 +0100) <Per Andersson>
    |/ /  
    * |   f3f667e - Merge pull request #75 from jdcaballero/master (2012-10-25 08:48:46 -0700) <benjaoming>
    |\ \  
    | * | 0f422c0 - Update wiki/plugins/notifications/forms.py (2012-10-25 17:48:58 +0300) <jdcaballero>
    |/ /  
    * | e7d64e1 - Never return a proxy object from __unicode__ ! (#73) (2012-10-23 14:39:20 +0200) <benjaoming>
    * |   46fc152 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-10-23 14:37:57 +0200) <benjaoming>
    |\ \  
    | |/  
    | *   2288efd - Merge pull request #64 from webdevelop/master (2012-10-17 05:47:59 -0700) <benjaoming>
    | |\  
    | | * d77930c - Greedy regex algorithm (2012-10-13 00:36:23 +0300) <Vladyslav>
    * | | a479748 - Never return a proxy object from __unicode__ ! (#73) (2012-10-23 14:37:16 +0200) <benjaoming>
    |/ /  
    * | 0c8a554 - Issue #68 - Add sorl-thumbnail to dependencies. Furthermore, add >=0.5.3 to django-mptt which has caused some reports. Read requirements.txt into setup.py to avoid hard coding and mismatches. Create 0.0.2 release which is not broken because README.md was missing from distribution file. (2012-10-17 14:13:10 +0200) <benjaoming>
    * | 5db399c - Issue #67 - left joins caused by m2m fields sometimes result in duplicate rows, applying distinct() (2012-10-16 18:03:57 +0200) <benjaoming>
    * | 0850915 - Fix Issue #66 (2012-10-16 16:34:53 +0200) <benjaoming>
    * | d08301f - Fix transaction support for uploading attachments (2012-10-05 17:53:30 +0200) <benjaoming>
    * | ee08a7f - Fix #60 - do not allow empty image form fields even though the model should handle it. (2012-10-05 17:45:17 +0200) <benjaoming>
    * | 520e123 - Fixing long titles in notifications and display total count of notifications instead of just a truncated number. (2012-10-05 17:42:32 +0200) <benjaoming>
    * | a886040 - Cosmetic changes to fix #38 - but otherwise there is no rules for URL lengths other than IE setting the lower limit at 2048 characters which should hardly annoy anyone. (2012-10-05 17:25:35 +0200) <benjaoming>
    * | 8884709 - Remove redundant table (2012-10-05 17:25:07 +0200) <benjaoming>
    * | bbd4234 - Issue#50 - make using send_file configurable to allow for remote storage backends such as S3. (2012-10-05 17:07:45 +0200) <benjaoming>
    * |   1082aef - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-10-05 16:55:26 +0200) <benjaoming>
    |\ \  
    | * | 0bc5611 - Update README.md (2012-10-02 02:47:34 +0300) <benjaoming>
    | * |   4e2ced2 - Merge pull request #62 from webdevelop/master (2012-09-24 03:32:58 -0700) <benjaoming>
    | |\ \  
    | | |/  
    | | * e0a3b99 - Uncode filename in US-ASCII format, needable for russian and other language (2012-09-19 19:15:52 +0300) <Vladyslav>
    | | * f723c60 - Change max_length of file to 255 for handling files with big name (2012-09-19 17:58:09 +0300) <Vladyslav>
    | * | 9e3a9d0 - Adding news section about RC1. (2012-09-20 15:08:16 +0300) <benjaoming>
    | |/  
    | *   4f750cd - Merge pull request #52 from pypetey/master (2012-09-10 05:46:26 -0700) <benjaoming>
    | |\  
    | | * 0fd815b - small fix for extra hash (2012-09-10 13:18:31 +0200) <pypetey>
    | | * 3183706 - Fix for line 561 error: 'msgid' format string with unnamed arguments cannot be properly localized: The translator cannot reorder the arguments. Please consider using a format string with named arguments, and a mapping instead of a tuple for the arguments. (2012-09-10 11:10:44 +0200) <pypetey>
    | |/  
    * | 2a9167a - Add support for counting duplicate notifications instead of repeating the same. (2012-10-05 16:54:40 +0200) <benjaoming>
    |/  
    * 0fa8bad - Use safe preprocessors for attachments and images plugin. Fix Issue #39. Also use a template to render attachments html. (2012-09-06 23:03:40 +0200) <benjaoming>
    * 8d1dd37 - Updating model chart to reflect current project status (2012-09-06 22:39:53 +0200) <benjaoming>
    * 9503fac - Issue #50 do not use full paths because remote storage does not implement this. (2012-09-06 22:09:54 +0200) <benjaoming>
    * 8f64202 - Issue #48: Searches should be case insensitive (2012-09-06 15:31:58 +0200) <benjaoming>
    * b68f0b5 - More modifications for pypi, first 0.0.1 released - pip install wiki (2012-09-05 16:00:39 +0200) <benjaoming>
    * 996800c - Adding a MANIFEST for pypi distribution (2012-09-05 15:48:12 +0200) <benjaoming>
    * da4e421 - Fixing issues with PYPI compatibility (2012-09-05 02:09:43 +0200) <benjaoming>
    *   8a589bb - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-09-04 17:27:26 +0200) <benjaoming>
    |\  
    | *   c7aa2e1 - Merge pull request #40 from uAnywhere/master (2012-08-30 02:11:22 -0700) <benjaoming>
    | |\  
    | | * 4e6cdda - Minor optimisation to ACLs (use .exists() instead of bool() because it's faster), fix an issue on Django 1.5 where EmptyQuerySet has no method select_related_common() (2012-08-30 10:54:09 +0930) <Michael Farrell>
    | |/  
    * | 3a31f2c - Do not conditionally include login, logout and signup URLs in urlpatterns. Handle WIKI_ACCOUNT_HANDLING inside views. Issue #43. (2012-09-04 17:26:54 +0200) <benjaoming>
    |/  
    *   76b0698 - Merge branch 'edx_release' (2012-08-27 17:01:16 +0200) <benjaoming>
    |\  
    | * 7fad1ac - (origin/edx_release) Removing settings from links plugin (2012-08-27 14:57:42 +0200) <benjaoming>
    | * d489d13 - Merging with edx branch, fixing link plugin to not use live_lookups (it's meaningless because whole articles are normally cached and therefore, links are not resolved at every article view). Also, settings for the links plugin were wrongly placed in the main settings file. (2012-08-27 14:54:52 +0200) <benjaoming>
    | *   72faa3b - Merge pull request #31 from rocha/edx_release (2012-08-23 13:06:02 -0700) <benjaoming>
    | |\  
    | | * cd1c23e - Fixed WikiPath regexp. It was incorrectly matching [Title](Link) on the same line. (2012-08-23 13:12:52 -0400) <Carlos Andrés Rocha>
    | |/  
    | * 7e42bce - Changed behavior of wikilinks extension to optionally disable database and prefer to stay at a certain level. (2012-08-23 09:55:42 -0400) <Bridger Maxwell>
    | * f00b7d3 - Fixed bug where non-found wiki links ignored base url. (2012-08-23 08:45:49 -0400) <Bridger Maxwell>
    | * 533c7fc - Dir links are now prominently view links with arrows for viewing children. (2012-08-22 21:03:55 -0400) <Bridger Maxwell>
    | * d1b97e2 - Fixed bug for calling .active() on empty query sets. (2012-08-22 20:15:21 -0400) <Bridger Maxwell>
    | * 50c08a3 - Added setting for disabling SelectWidgetBootstrap. (2012-08-22 20:02:36 -0400) <Bridger Maxwell>
    | * 3576a2d - Allowing periods in slug for wikilinks. (2012-08-22 15:54:44 -0400) <Bridger Maxwell>
    * |   81bf613 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-25 11:18:02 +0200) <benjaoming>
    |\ \  
    | * | 7aab68a - Adding ideas section. (2012-08-25 00:43:28 +0300) <benjaoming>
    * | | bb87802 - unchanged, git detects change but shows no diff (2012-08-25 11:17:37 +0200) <benjaoming>
    * | | 0fc9b2d - Important fix! Remove HTML tags from Markdown code. (2012-08-25 11:16:15 +0200) <benjaoming>
    * | | 4a58ac1 - Adding clearfix (2012-08-25 00:29:58 +0200) <benjaoming>
    |/ /  
    * | 98aaee3 - Issue #32, yes, clearly a typo here. Don't know why it was working, but replaced with super(RevisionForm.. and tested. (2012-08-24 23:24:56 +0200) <benjaoming>
    * |   7435980 - Merge pull request #35 from rfurman/master (2012-08-24 14:14:47 -0700) <benjaoming>
    |\ \  
    | * | 60142fa - Fixed image captions by resetting caption_lines for each new image.  Before, the n-th image would have the first n captions concatenated together. (2012-08-23 19:40:43 -0700) <Ralph Furmaniak>
    |/ /  
    * |   60c83ee - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-22 15:49:42 -0400) <Bridger Maxwell>
    |\ \  
    | * | d9518ea - Only mark shown notifications as read -- never the ones that haven't been display because only 10 notifications are display at the same time... (2012-08-22 20:28:23 +0200) <benjaoming>
    | * | ebfaff4 - order notifications (2012-08-22 20:16:01 +0200) <benjaoming>
    | * | e229819 - Notify dropdown should look at the latest id of a notification and not retrieve any older notifications on updating from JSON. (2012-08-22 20:13:42 +0200) <benjaoming>
    | * | 288e25a - Merge user menu and notifications menu (2012-08-22 19:53:52 +0200) <benjaoming>
    | * | 3c9c2f1 - more search layout (2012-08-22 19:37:55 +0200) <benjaoming>
    | * |   6d20678 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-22 19:33:53 +0200) <benjaoming>
    | |\ \  
    | * | | f8a6e1c - Search "optimization".... layout-wise :) (2012-08-22 19:33:16 +0200) <benjaoming>
    * | | | a558ea6 - Allowing periods in slug for wikilinks. (2012-08-22 15:49:32 -0400) <Bridger Maxwell>
    | |/ /  
    |/| |   
    * | | 7f820b6 - user.is_superuser is not a function. (2012-08-22 13:19:28 -0400) <Bridger Maxwell>
    |/ /  
    * |   0012481 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-22 19:12:05 +0200) <benjaoming>
    |\ \  
    | |/  
    | * 63003aa - Removed print statement accidentally left in. (2012-08-22 13:08:44 -0400) <Bridger Maxwell>
    | * afdd97d - Made a workaround for django bug 15040, which made permissions forms have all checked boxes. (2012-08-22 12:40:34 -0400) <Bridger Maxwell>
    | * 6ccd08e - Moved subtree delete to a model method with transactions. (2012-08-22 10:08:26 -0400) <Bridger Maxwell>
    * | c0d7e2a - Search function (2012-08-22 19:11:41 +0200) <benjaoming>
    |/  
    * c2cfcc2 - A few search related things... adding search bar (doesnt work yet) (2012-08-22 15:28:44 +0200) <benjaoming>
    * 56d8e57 - Filtering on Directory listings. Issue #27 - never create a merged revision that inherits the deleted or locked attribute. (2012-08-22 14:41:06 +0200) <benjaoming>
    * 2979c98 - Few things here and there in the README (2012-08-22 14:40:42 +0200) <benjaoming>
    * ff8fd1c - Issue #28 (2012-08-22 14:25:30 +0200) <benjaoming>
    *   bf0d9cd - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-22 12:51:30 +0200) <benjaoming>
    |\  
    | * 9865b5c - Changed preview to show warning when previewing a deleted revision. (2012-08-22 00:03:12 -0400) <Bridger Maxwell>
    | * d2f08a3 - You can now preview deleted revisions (so they work in the history tab). (2012-08-21 23:51:54 -0400) <Bridger Maxwell>
    | * a8dbb5f - Fixed confusing if statement that had the side effect of restoring every deleted article a moderator views. (2012-08-21 23:41:40 -0400) <Bridger Maxwell>
    | *   c432574 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-21 22:56:57 -0400) <Bridger Maxwell>
    | |\  
    | * | 1415c85 - Was accidentally using old permission for showing purge confirm form. (2012-08-21 22:56:48 -0400) <Bridger Maxwell>
    * | | b03a317 - Very small commit before merge... (2012-08-22 12:51:00 +0200) <benjaoming>
    * | | 8e691c1 - Modal should not animate... the bootstrap animation is loo choppy (2012-08-22 12:39:11 +0200) <benjaoming>
    | |/  
    |/|   
    * |   6be6a0c - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-22 04:03:38 +0200) <benjaoming>
    |\ \  
    | |/  
    | *   32416cd - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-21 22:01:44 -0400) <Bridger Maxwell>
    | |\  
    | * | ce4fd7a - Removed the lost and found until it can be debugged. (2012-08-21 22:01:38 -0400) <Bridger Maxwell>
    | * | 4ddc7cb - Properly deletes children when purging articles. (2012-08-21 21:31:48 -0400) <Bridger Maxwell>
    | * |   632bb59 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-21 21:08:10 -0400) <Bridger Maxwell>
    | |\ \  
    | * \ \   096e149 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-21 21:04:49 -0400) <Bridger Maxwell>
    | |\ \ \  
    | * \ \ \   af0b2a6 - Merge branch 'edx_release' (2012-08-21 20:40:02 -0400) <Bridger Maxwell>
    | |\ \ \ \  
    | | * | | | 82806fa - An article is now considered deleted if a parent is instead of explicitly needing to mark all children as deleted. (2012-08-21 20:32:44 -0400) <Bridger Maxwell>
    | | * | | | 02275fb - Fixed import for installation to run without attachments being enabled. (2012-08-21 17:56:46 -0400) <Bridger Maxwell>
    * | | | | | 915260d - oops mess (2012-08-22 04:03:13 +0200) <benjaoming>
    | |_|_|_|/  
    |/| | | |   
    * | | | | 59ecabd - Layout stuff (2012-08-22 04:00:58 +0200) <benjaoming>
    * | | | | 2770ad1 - Fix slug checking: Should respect case sensitivity (if configured) and feedback if its a deleted article (2012-08-22 03:23:06 +0200) <benjaoming>
    | |_|_|/  
    |/| | |   
    * | | | 66f357e - Removing the stupid delete check once and for all (2012-08-22 03:07:41 +0200) <benjaoming>
    | |_|/  
    |/| |   
    * | | d5d90a4 - Removing circular permission check can_write->can_delete->can_write.... (2012-08-22 03:04:04 +0200) <benjaoming>
    * | | a3ee89d - Adding user_can_read as a kwarg on Article.get_children (2012-08-22 02:43:49 +0200) <benjaoming>
    |/ /  
    * | 489dcba - Removing the is_moderator decorator -- it is replaced by can_moderate (2012-08-22 02:26:17 +0200) <benjaoming>
    * | 9a996a7 - Updating todo and comments (2012-08-22 02:23:27 +0200) <benjaoming>
    * |   1e5bb80 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-22 02:19:45 +0200) <benjaoming>
    |\ \  
    | * \   221fca1 - Merge branch 'edx_release' (2012-08-21 15:41:53 -0400) <Bridger Maxwell>
    | |\ \  
    | | |/  
    | | * 876357a - Added an error page (for when even the parent isn't found). (2012-08-21 15:36:31 -0400) <Bridger Maxwell>
    * | | 832d790 - Loads of changes in permission system. Many aspects are now configurable. (2012-08-22 02:18:55 +0200) <benjaoming>
    |/ /  
    * | 495d70e - Adding a couple of new settings that are not fully implemented yet. Do not let MARKDOWN_EXTENSIONS be a callable since the markdown_instance already has an article property accessible to any extension that wants it. (2012-08-21 21:36:49 +0200) <benjaoming>
    * | 9392b2f - Image deletion: Purge function to throw out files and everything! (2012-08-21 20:01:42 +0200) <benjaoming>
    * | 72a2884 - Update TODO. Should allow null values of image width and height since image files disappear sometimes and fields have to be emptied. (2012-08-21 19:24:05 +0200) <benjaoming>
    * | 46c4857 - Image captions should keep line breaks. Missing image files still keep causing problems (2012-08-21 19:19:20 +0200) <benjaoming>
    * | 5b49a60 - Fix whitespaces added from html template (2012-08-21 18:03:45 +0200) <benjaoming>
    * | 5352792 - Locking of articles and source view. (2012-08-21 17:16:51 +0200) <benjaoming>
    * | 8b4f51b - Settings tab should inherit from article.html (2012-08-21 16:08:28 +0200) <benjaoming>
    * | 4d941f6 - View Source is almost finished... (2012-08-21 16:02:22 +0200) <benjaoming>
    * | 4287c93 - Updates relating to new bootstrap version. Removing several js plugins as they are now in the minified bootstrap.js (2012-08-21 16:01:22 +0200) <benjaoming>
    * | 65147c5 - Inherit correct properties from predecessor and be more robust when returning size and filename on images (2012-08-21 15:05:58 +0200) <benjaoming>
    * | 657831f - IOError, not OSError (2012-08-21 14:59:22 +0200) <benjaoming>
    * | fabea44 - Add image.null=True for images field so that files can disappear and not cause unreparable error. (2012-08-21 14:57:38 +0200) <benjaoming>
    * | 471f8eb - Image replacement bug, did not inherit from predecessor (2012-08-21 14:52:59 +0200) <benjaoming>
    * | bff93ef - Updating test database (2012-08-21 14:48:15 +0200) <benjaoming>
    * | b4c18cb - Update to Bootstrap 2.1.0 (2012-08-21 14:47:26 +0200) <benjaoming>
    * | b39f8f1 - Printer friendliness (2012-08-21 03:27:12 +0200) <benjaoming>
    * | f9130a6 - Various small fixes (2012-08-21 03:18:38 +0200) <benjaoming>
    * | 1a4ef5a - Add links plugin to testproject. Do not fail if an attachment file has disappeared. (2012-08-21 03:01:14 +0200) <benjaoming>
    * | 2b8c7f4 - Adding a plugin for handling links and detecting if they are broken (which will show a read link in the article text). Also a sidebar for looking up links with typeahead. (2012-08-21 02:57:38 +0200) <benjaoming>
    |/  
    * e237b2a - Creating a proper WikiSlug javascript generator from the django urlify (2012-08-20 20:19:22 +0200) <benjaoming>
    *   95d8651 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-20 20:07:27 +0200) <benjaoming>
    |\  
    | * a49b4d5 - Patch for django bug where EmptyQuerySet actually needs the model to be set (or it can't raise a DoesNotExist exception). (2012-08-20 12:39:19 -0400) <Bridger Maxwell>
    * | 354c6b2 - Customizable storage backend for attachments. Proper error handling for illegal file types on replace view. (2012-08-20 20:05:56 +0200) <benjaoming>
    |/  
    * 7216584 - Browsing levels and adding articles to either current or parent level so users dont get confused about the hierarchy (2012-08-20 16:25:05 +0200) <benjaoming>
    * c83ad43 - Checking read permissions on page list (2012-08-20 15:00:08 +0200) <benjaoming>
    * b37e140 - Move add_select_related so it isn't a class method but an instance method of the URLPath's querysets. Fix error in permission lookup of users in a group. (2012-08-20 13:45:43 +0200) <benjaoming>
    * 0a273ee - Forgot a file in last commit, list.html (2012-08-19 23:26:35 -0400) <Bridger Maxwell>
    *   92ab132 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-19 23:26:13 -0400) <Bridger Maxwell>
    |\  
    | * 5988130 - Sidebar to handle plugins without a form (2012-08-20 03:49:04 +0200) <benjaoming>
    | * cd60dfd - Removing after refactor (2012-08-20 03:40:27 +0200) <benjaoming>
    | * 8d7f606 - Adding a help plugin and extra markdown extensions (2012-08-20 03:39:03 +0200) <benjaoming>
    | * 1b69061 - Permissions in settings tab can be applied recursively and owner can be changed. (2012-08-20 02:30:27 +0200) <benjaoming>
    | *   85c58dc - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-20 01:31:19 +0200) <benjaoming>
    | |\  
    | * | 3edd286 - Adding possibility for Plugins to add media to rendering pages. Adding advanced markdown extension for images. Adding colorbox for images plugin to enlarge photos. (2012-08-20 01:30:21 +0200) <benjaoming>
    * | | 2edd8d3 - Added simple child list page. Doesn't have any styling yet. (2012-08-19 23:25:51 -0400) <Bridger Maxwell>
    | |/  
    |/|   
    * | 2d7c987 - children_slice is no longer queried when SHOW_MAX_CHILDREN=0 (2012-08-19 17:34:53 -0400) <Bridger Maxwell>
    * | 55469f7 - Further reducing sql queries. (2012-08-19 17:25:12 -0400) <Bridger Maxwell>
    * | 7c6af7b - Added caching of ancestors for urlpath to reduce sql queries. (2012-08-19 16:47:51 -0400) <Bridger Maxwell>
    |/  
    * df4fd06 - Sending request object to sidebar forms (2012-08-19 22:26:03 +0200) <benjaoming>
    * 7c1542c - Adding new image revisions and better looks for history page (2012-08-19 22:22:52 +0200) <benjaoming>
    * fcc466d - Image management, revert, delete and restore (2012-08-19 20:36:20 +0200) <benjaoming>
    * c145596 - Refactoring wiki.core.plugins (2012-08-19 14:34:34 +0200) <benjaoming>
    *   ebe86a4 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-18 17:13:17 +0200) <benjaoming>
    |\  
    | * 97f8413 - Fixed some circular imports that were causing errors. (2012-08-18 00:01:28 -0400) <Bridger Maxwell>
    | * 8e76eae - IMPORTANT: Fix this. I just commented out a line that was causing trouble. (2012-08-18 00:01:09 -0400) <Bridger Maxwell>
    | * 96328e3 - Changed getting of EditorClass and editor to functions (so they don't run so early). (2012-08-17 22:39:02 -0400) <Bridger Maxwell>
    * | 45b67b2 - Adding RevisionPlugin. Images plugin becoming a plugin with its own revision system. Fixing anonymous settings for attachments plugin. (2012-08-18 17:12:28 +0200) <benjaoming>
    |/  
    *   d58dcbc - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-17 16:10:09 -0400) <Bridger Maxwell>
    |\  
    | * 1438944 - Moving sidebar outside of the main edit form so plugins can handle their own form data independently (2012-08-17 21:14:05 +0200) <benjaoming>
    * | 0072871 - Removed debug print. (2012-08-17 16:10:05 -0400) <Bridger Maxwell>
    |/  
    * eea5726 - Changing plugin base models for a more intuitive understanding of what types of models should exist. The image model should maintain revisions of itself to avoid a difficult process when replacing images. (2012-08-17 20:52:05 +0200) <benjaoming>
    * d4de685 - admin.py uses correct import of Editor, EditorClass. (2012-08-17 14:08:12 -0400) <Bridger Maxwell>
    * 12cc515 - Creating editors package with markitup module (2012-08-17 19:37:59 +0200) <benjaoming>
    * 8a7a3e7 - New app label for notifications (2012-08-17 19:30:56 +0200) <benjaoming>
    *   63b6da7 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-17 19:28:51 +0200) <benjaoming>
    |\  
    | * 95dd8fe - Moved MarkItUp editors to plugins also. (2012-08-17 13:26:58 -0400) <Bridger Maxwell>
    * | 8c84848 - comments (2012-08-17 19:28:38 +0200) <benjaoming>
    * | a4ef195 - New tables after altering APP_LABEL on plugins (2012-08-17 18:54:29 +0200) <benjaoming>
    |/  
    * d567a4d - Moving BaseEditor to wiki.plugins to avoid circular imports (2012-08-17 18:30:54 +0200) <benjaoming>
    *   944075a - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-17 18:21:17 +0200) <benjaoming>
    |\  
    | * 48a1377 - Fixed render_to_string parameter (context was being passed in without using 'context_instance' kwarg) (2012-08-17 10:57:11 -0400) <Bridger Maxwell>
    | *   7b6078b - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-17 10:49:18 -0400) <Bridger Maxwell>
    | |\  
    | * | 7ec4943 - Small typo where I used ANONYMOUS instead of ANONYMOUS_WRITE. (2012-08-17 10:49:15 -0400) <Bridger Maxwell>
    * | | 9a04ef4 - Changing app_label for plugin models (2012-08-17 18:20:45 +0200) <benjaoming>
    | |/  
    |/|   
    * | ab7dc9a - Adding migrations for URLPath.article cache field Adding dependency on sorl-thumbnail (2012-08-17 15:03:29 +0200) <benjaoming>
    * |   3e7ddf6 - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-17 12:26:49 +0200) <benjaoming>
    |\ \  
    | |/  
    | * 473fd5e - Added a permission denied page. (2012-08-16 17:29:24 -0400) <Bridger Maxwell>
    | * 3324ab0 - Added a permission denied page. (2012-08-16 17:26:54 -0400) <Bridger Maxwell>
    * | 1d3677b - prefetch and swap lookups such that path is always looked up before article_id (2012-08-17 12:25:54 +0200) <benjaoming>
    * |   6af3dcb - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-16 22:29:29 +0200) <benjaoming>
    |\ \  
    | |/  
    | * 8cd2bb7 - ANONYMOUS and ANONYMOUS_WRITE settings are now respected. (2012-08-16 14:52:08 -0400) <Bridger Maxwell>
    | * 9c83dfb - Fixed issues where 'if user.is_anonymous' was missing () so was always True (2012-08-16 14:23:57 -0400) <Bridger Maxwell>
    | * 484ff1c - Added auto migration. (2012-08-15 23:40:10 -0400) <Bridger Maxwell>
    | * cdb2c3a - Added a bit of caching to retrieving path, so it doesn't make so many sql queries. (2012-08-15 22:35:57 -0400) <Bridger Maxwell>
    | * 6c9e1a0 - Added a hack to the hacky reverse to allow for transforms on reversed url. (2012-08-15 19:36:45 -0400) <Bridger Maxwell>
    * | 5fe706c - Merging with Basecamp feature list (2012-08-16 15:36:48 +0200) <benjaoming>
    |/  
    *   4ab9701 - Merge branch 'master' of git://github.com/benjaoming/django-wiki (2012-08-13 23:42:50 -0400) <Bridger Maxwell>
    |\  
    | * b85791d - Message after uploading image. Do not redirect after plugin form submit as changes to article text and title are lost. (2012-08-14 01:54:47 +0200) <benjaoming>
    | * 0863c41 - Sidebar plugins. First plugin: images. Upload an image directly via a plugin on the edit page. (2012-08-14 01:34:38 +0200) <benjaoming>
    | * 6eae1fc - Instructions about settings and tips (2012-08-13 19:45:39 +0200) <benjaoming>
    | * 3a876d9 - Block anonymous access to upload files (2012-08-13 19:39:56 +0200) <benjaoming>
    * | c053503 - Added login_required to create_root. (2012-08-13 23:42:30 -0400) <Bridger Maxwell>
    * |   d238020 - Merge branch 'master' of git://github.com/benjaoming/django-wiki (2012-08-13 12:33:37 -0400) <Bridger Maxwell>
    |\ \  
    | |/  
    | * d1f50d1 - test db not properly synced (2012-08-13 18:15:22 +0200) <benjaoming>
    | * 19716f7 - Adding South migrations for wiki, django_notify and wiki plugins (2012-08-13 16:04:58 +0200) <benjaoming>
    | * a1d6ebe - Refactor plugins: Put base classes in wiki.plugins (2012-08-13 15:56:15 +0200) <benjaoming>
    | * f7f6527 - Deleted article view with purge and restore options (2012-08-13 14:58:39 +0200) <benjaoming>
    | * 63c7e9f - Correctly inform user that a deletion ALSO deletes children. (2012-08-13 03:02:02 +0200) <benjaoming>
    | * 8ce2236 - Deletion for articles: Soft delete and purge. Also soft deletes or purges children. A soft deletion creates a new revision in which the article is marked as deleted. (2012-08-13 02:57:45 +0200) <benjaoming>
    | * c1514ab - Do not delete old notifications when user unsubscribes + allow notifications to be created without a subscription (to enable notifications for only one specific user) (2012-08-13 02:54:45 +0200) <benjaoming>
    | * 4800d5b - Decorator for muting notifications + Issue #11 fix (2012-08-13 02:31:35 +0200) <benjaoming>
    | * 2eae064 - Correcting errors caused by removal of Article.title field. Almost done with Delete view. (2012-08-13 00:05:14 +0200) <benjaoming>
    * | c10ee82 - Corrected parameters on render_to_response. Also fixed login url resolution when ACCOUNT_HANDLING=False. (2012-08-13 12:32:47 -0400) <Bridger Maxwell>
    * |   9f1b3a9 - Merge branch 'master' of git://github.com/benjaoming/django-wiki (2012-08-12 12:52:42 -0400) <Bridger Maxwell>
    |\ \  
    | |/  
    | * c3303e1 - Example urlpattern Issue #12 (2012-08-12 14:17:59 +0200) <benjaoming>
    | * 84d44da - Updating week and date (2012-08-12 14:05:38 +0200) <benjaoming>
    | * 0303bcd - Headlines (2012-08-12 14:04:42 +0200) <benjaoming>
    | * 0de3382 - Nicer headlines for install instructions (2012-08-12 14:03:20 +0200) <benjaoming>
    | * 5710402 - Small things (2012-08-12 14:01:25 +0200) <benjaoming>
    | * 11b00ec - Adding mptt to requirements Issue #10 (2012-08-12 13:57:36 +0200) <benjaoming>
    | * 869a62e - Better install instructions for Issue #14 and #12 (2012-08-12 13:55:38 +0200) <benjaoming>
    | *   43c32df - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-08-11 20:12:26 +0200) <benjaoming>
    | |\  
    | | *   1888ff6 - Merge pull request #15 from hgdeoro/updates-on-readme (2012-08-11 11:12:12 -0700) <benjaoming>
    | | |\  
    | | | * 212b3a2 - Updated install instructions on README. (2012-08-11 14:03:38 -0300) <Horacio G. de Oro>
    | | * |   f365669 - Merge pull request #10 from hgdeoro/pip-requirements (2012-08-11 11:00:04 -0700) <benjaoming>
    | | |\ \  
    | | | * | 0b054e0 - README: added instructions: how to use requirements.txt to install dependencies. (2012-08-11 12:45:15 -0300) <Horacio G. de Oro>
    | | | * | 5e5640f - Creates a requirements.txt to facilitate installing dependencies. (2012-08-11 12:39:02 -0300) <Horacio G. de Oro>
    | | | |/  
    | * | | 94a3ebf - Remove redundant Article.title field (2012-08-11 19:24:02 +0200) <benjaoming>
    | * | | 4418482 - Making footer prettier, clean up code (2012-08-11 18:37:57 +0200) <benjaoming>
    | |/ /  
    * | |   341db91 - Merge branch 'master' of git://github.com/benjaoming/django-wiki (2012-08-11 13:45:17 -0400) <Bridger Maxwell>
    |\ \ \  
    | |/ /  
    | * | 846a665 - Cleaning up template boiler plate markup (2012-08-11 18:29:16 +0200) <benjaoming>
    | * | 588bcdd - Making notifications update in a smart way. Fixing wrong urls in accounts (2012-08-11 17:51:19 +0200) <benjaoming>
    | * | bf09bf4 - Changing the urlpatterns to always prioritize paths over IDs if a path string is supplied -- even an empty one for the root article. Also modifying models in pluginbase to not be abstract such that it is possible to generically access all types of plugins. (2012-08-11 17:30:36 +0200) <benjaoming>
    | * | 33186aa - Adding model chart generation of the wiki (2012-08-11 15:00:23 +0200) <benjaoming>
    | |/  
    * |   193d514 - Merge branch 'master' of git://github.com/benjaoming/django-wiki (2012-08-10 11:41:26 -0400) <Bridger Maxwell>
    |\ \  
    | |/  
    | * afce7d8 - msg when child menu is empty (2012-08-10 00:17:36 +0200) <benjaoming>
    | * b3bf535 - msg when child menu is empty (2012-08-10 00:16:35 +0200) <benjaoming>
    | * 1bff649 - insert transaction commits so they cover all cases (2012-08-10 00:05:32 +0200) <benjaoming>
    | * 7091ac9 - Use chained QuerySet objects for can_read and can_write methods and active() to filter out inactive objects. Issue #9 (2012-08-09 23:56:15 +0200) <benjaoming>
    * | a7a5f5e - Added related_name to Article.owner to prevent conflict with existing Simplewiki install. (2012-08-10 11:41:22 -0400) <Bridger Maxwell>
    |/  
    * ea26ab8 - Anonymous users cannot be used in queries! (2012-08-09 21:38:28 +0200) <benjaoming>
    * c619639 - Making more agile url patterns that are agnostic to either receiving a  path or an article_id. The path takes precedence over the article_id, except for the root article which needs to be forced in the template. Prettyfying the article revision list. (2012-08-09 19:34:10 +0200) <benjaoming>
    * 24ea671 - Failed use of select_related -- need some good idea. Better UI with current level's child articles as dropdown menu. (2012-08-09 18:43:03 +0200) <benjaoming>
    * 2864d69 - Avoid duplicate notifications for overlapping subscription types. Make notification list empty when marking all notifications as read. (2012-08-09 16:28:34 +0200) <benjaoming>
    * b676975 - Admin labels (2012-08-09 16:13:50 +0200) <benjaoming>
    * b232ea8 - Notifications for attachments plugin and plugins in general (2012-08-09 15:59:09 +0200) <benjaoming>
    * 276c658 - Prettyfying the attachments page (2012-08-09 14:37:52 +0200) <benjaoming>
    * c385fc6 - Renaming permission - no permissions should overlap in their meaning. Fixing can_read and can_write on Article instances to match new permissions. (2012-08-09 14:07:38 +0200) <benjaoming>
    * efe01f7 - Improving managers. Adding select_related (untested) on get_article decorator. Adding search function for attachments to add other article's attachments. Adding better permission handling through managers. (2012-08-09 14:02:47 +0200) <benjaoming>
    * 6988059 - Fixing preview function to use correct revision id (2012-08-09 02:18:14 +0200) <benjaoming>
    * 299017e - Wrong preview link (2012-08-09 02:12:11 +0200) <benjaoming>
    * 19b191a - Removing files that should not be in testproject (2012-08-09 02:08:50 +0200) <benjaoming>
    * d264f48 - Further frustations perhaps fixed on file upload issues (2012-08-09 02:06:06 +0200) <benjaoming>
    * 751c21a - Better error if permissions are wrong on MEDIA_ROOT (2012-08-09 02:05:01 +0200) <benjaoming>
    * b6e7b94 - Hopefully fixing transaction issue for other systems (2012-08-09 01:59:02 +0200) <benjaoming>
    * 0c57d76 - moving transaction commit (2012-08-09 01:50:04 +0200) <benjaoming>
    * 08bfb16 - More robustness in Attachments plugin. Give a good error message upon non-allowed uploads. Fix JSON decorator error. Ignore media files in test project. (2012-08-09 01:40:31 +0200) <benjaoming>
    * a2ba2c8 - Attachment plugin almost finished. Can delete and restore files and replace. Contains a smart obscurification feature that hides files. This way, files can have reading restrictions imposed. (2012-08-09 00:20:09 +0200) <benjaoming>
    * d96da78 - Better install instructions (2012-08-07 19:21:20 +0200) <benjaoming>
    * 81e8157 - Simple account handling, log in, log out and sign up. (2012-08-07 18:35:06 +0200) <benjaoming>
    * bfef21b - A bit of login toolbar (2012-08-07 15:45:19 +0200) <benjaoming>
    * ebb25ab - Adding notify frontend. (2012-08-07 15:34:44 +0200) <benjaoming>
    * 1a0396d - Adding from old feature list (2012-08-07 02:08:27 +0200) <benjaoming>
    * 5e3b668 - Add GPLv3 license, clean up code (2012-08-07 01:36:28 +0200) <benjaoming>
    * 8408f01 - More class-based views. Mixin class for Article-related views handling permissions etc. More complex plugin structure for easy creation of plugins with very easy integration in the article tab menu etc. (2012-08-07 01:15:53 +0200) <benjaoming>
    * fa4af85 - Error on saving revisions for anonymous users (2012-08-06 01:05:32 +0200) <benjaoming>
    * 64a20e8 - Adding notifications for article edits and creations (2012-08-06 01:00:39 +0200) <benjaoming>
    * 700e466 - Fixing js bug in SelectWidgetBootstrap (2012-08-05 23:34:28 +0200) <benjaoming>
    * 4162909 - Fix Issue #7 (in setup.py) + Add forms in settings tab, save new permissions and notification preferences (2012-08-05 22:35:44 +0200) <benjaoming>
    * 15a363d - Detection of editing conflicts, ie. concurrent article edits. If the revision number has changed while editing, warn the user and merge the user's content with the new revision. (2012-08-05 15:33:17 +0200) <benjaoming>
    * 9d92e96 - Updating the TODO (2012-08-02 23:50:26 +0200) <benjaoming>
    * 68e6c32 - added text editor backup files to gitignore; fix url tags so they are django 1.3-style, so it works properly with django 1.5 (which requires it) (2012-08-02 11:27:20 +0930) <Michael Farrell>
    * 3500999 - django_notify in wiki self-check on INSTALLED_APPS and a better README.md (2012-08-02 01:24:16 +0200) <benjaoming>
    * acff0fe - Update django_notify/README (2012-08-02 02:17:56 +0300) <benjaoming>
    * 083b56d - Update README.md (2012-08-02 02:14:13 +0300) <benjaoming>
    * 9dda155 - Update README.md (2012-08-02 02:12:55 +0300) <benjaoming>
    * 56ef8e6 - Update README.md (2012-08-02 02:12:08 +0300) <benjaoming>
    * 4ede9c8 - Creating new notification application django_notify and adding support for plugin registration and hooking additional forms into the settings page, such as notification settings for articles. (2012-08-01 19:59:26 +0200) <benjaoming>
    * 99041d5 - Redirecting if article does not exist, add user and ip_address to new articles (2012-08-01 02:30:54 +0200) <benjaoming>
    * efd542a - Create function added (2012-08-01 01:53:40 +0200) <benjaoming>
    * b75d893 - Diffs also display log messages and title changes (2012-07-31 23:49:38 +0200) <benjaoming>
    * 37b1cd5 - Pressing the final merge button now works and puts an automatic log entry (2012-07-31 23:31:15 +0200) <benjaoming>
    *   83394ad - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-07-31 23:19:47 +0200) <benjaoming>
    |\  
    | * 9360e1d - Update README.md (2012-07-31 14:29:27 +0300) <benjaoming>
    | * dc3e415 - Update README.md (2012-07-31 14:28:57 +0300) <benjaoming>
    * | e19ec3a - Viewing diffs and merging revisions. (2012-07-31 23:18:41 +0200) <benjaoming>
    |/  
    * 327ff0c - Issue #4 and #2 (2012-07-31 13:09:09 +0200) <benjaoming>
    *   06d06ce - Merge branch 'master' of github.com:benjaoming/django-wiki (2012-07-30 23:12:58 +0200) <benjaoming>
    |\  
    | * b096e34 - Update README.md (2012-07-29 23:07:07 +0300) <benjaoming>
    | * 60bc647 - Adding sekizai dep. (2012-07-29 23:06:38 +0300) <benjaoming>
    * | 750f6b4 - Adding history page, first class-based view, saving pointer to previous revision, better more strict handling of URLS (must always end with a /, except the root which must be "") (2012-07-30 23:10:58 +0200) <benjaoming>
    |/  
    * 8294826 - A few deployment details (2012-07-29 21:55:03 +0200) <benjaoming>
    * 58cf1a3 - Adding edit page, preview function and MORE. South migrations will be added back soon. (2012-07-29 20:56:35 +0200) <benjaoming>
    * dba6f82 - Adding template tags, bootstrap front end, creation of first root article, template tags for rendering (2012-07-28 21:01:56 +0200) <benjaoming>
    * 458bbd2 - Initial plugin and editor structure and base classes for extending MarkItUp editor in admin Creating images and attachments as plugins (2012-07-27 21:09:11 +0200) <benjaoming>
    * 2940142 - More work on models. Add Attachment model, and let attachments pass through a revision system. (2012-07-27 03:04:27 +0200) <benjaoming>
    * 322b5a6 - Finalizing URLPath as an MPTT model and generic relations on Articles (2012-07-26 01:08:48 +0200) <benjaoming>
    * 83fe3d4 - More on models. Not done yet. (2012-07-25 05:21:40 +0200) <benjaoming>
    * 30fb1ec - Begging to implement models (2012-07-23 20:50:56 +0200) <benjaoming>
    * 330c772 - Django south administration and URL patterns with default namespace (2012-07-23 18:33:16 +0200) <benjaoming>
    * ef2b1ec - Documentation with sphinx (2012-07-23 16:19:44 +0200) <benjaoming>
    * 357d9fa - Adding install instructions and setup.py (2012-07-23 16:06:31 +0200) <benjaoming>
    * 692aeae - Prepopulated test project. (2012-07-23 15:35:43 +0200) <benjaoming>
    * a3fe227 - typos (2012-07-23 13:25:36 +0200) <benjaoming>
    * 0e24a0b - typos (2012-07-23 13:24:29 +0200) <benjaoming>
    * de6c30b - Project skeleton, README with explanation of project (2012-07-23 13:22:18 +0200) <benjaoming>
    * aac85a2 - Update master (2012-07-17 21:47:01 +0300) <benjaoming>
    * ad97277 - Initial commit (2012-07-17 11:46:10 -0700) <benjaoming>