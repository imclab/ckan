try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from ckan import __version__, __description__, __long_description__, __license__

setup(
    name='ckan',
    version=__version__,
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    license=__license__,
    url='http://ckan.org/',
    description=__description__,
    keywords='data packaging component tool server',
    long_description =__long_description__,
    install_requires=[
    ],
    extras_require = {
    },
    zip_safe=False,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ckanext', 'ckanext.stats'],
    include_package_data=True,
    package_data={'ckan': [
        'i18n/*/LC_MESSAGES/*.mo',
        'migration/migrate.cfg',
        'migration/README',
        'migration/tests/test_dumps/*',
        'migration/versions/*',
    ]},
    message_extractors = {
        'ckan': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('templates/importer/**', 'ignore', None),
            ('templates/**.html', 'ckan', None),
            ('templates_legacy/**.html', 'ckan', None),
            ('ckan/templates/home/language.js', 'genshi', {
                'template_class': 'genshi.template:TextTemplate'
            }),
            ('templates/**.txt', 'genshi', {
                'template_class': 'genshi.template:TextTemplate'
            }),
            ('templates_legacy/**.txt', 'genshi', {
                'template_class': 'genshi.template:TextTemplate'
            }),
            ('public/**', 'ignore', None),
        ],
        'ckanext': [
            ('**.py', 'python', None),
            ('**.html', 'ckan', None),
            ('multilingual/solr/*.txt', 'ignore', None),
            ('**.txt', 'genshi', {
                'template_class': 'genshi.template:TextTemplate'
            }),
        ]
    },
    entry_points="""
    [nose.plugins.0.10]
    main = ckan.ckan_nose_plugin:CkanNose

    [paste.app_factory]
    main = ckan.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [paste.paster_command]
    db = ckan.lib.cli:ManageDb
    create-test-data = ckan.lib.cli:CreateTestDataCommand
    sysadmin = ckan.lib.cli:Sysadmin
    user = ckan.lib.cli:UserCmd
    dataset = ckan.lib.cli:DatasetCmd
    search-index = ckan.lib.cli:SearchIndexCommand
    ratings = ckan.lib.cli:Ratings
    notify = ckan.lib.cli:Notification
    celeryd = ckan.lib.cli:Celery
    rdf-export = ckan.lib.cli:RDFExport
    tracking = ckan.lib.cli:Tracking
    plugin-info = ckan.lib.cli:PluginInfo
    profile = ckan.lib.cli:Profile
    color = ckan.lib.cli:CreateColorSchemeCommand
    check-po-files = ckan.i18n.check_po_files:CheckPoFiles
    trans = ckan.lib.cli:TranslationsCommand
    minify = ckan.lib.cli:MinifyCommand
    less = ckan.lib.cli:LessCommand
    datastore = ckanext.datastore.commands:SetupDatastoreCommand
    front-end-build = ckan.lib.cli:FrontEndBuildCommand


    [console_scripts]
    ckan-admin = bin.ckan_admin:Command

    [paste.paster_create_template]
    ckanext=ckan.pastertemplates:CkanextTemplate

    [ckan.forms]
    standard = ckan.forms.package:get_standard_fieldset
    package = ckan.forms.package:get_standard_fieldset
    group = ckan.forms.group:get_group_fieldset
    package_group = ckan.forms.group:get_package_group_fieldset

    [ckan.search]
    sql = ckan.lib.search.sql:SqlSearchBackend
    solr = ckan.lib.search.solr_backend:SolrSearchBackend

    [ckan.plugins]
    synchronous_search = ckan.lib.search:SynchronousSearchPlugin
    stats=ckanext.stats.plugin:StatsPlugin
    publisher_form=ckanext.publisher_form.forms:PublisherForm
    publisher_dataset_form=ckanext.publisher_form.forms:PublisherDatasetForm
    multilingual_dataset=ckanext.multilingual.plugin:MultilingualDataset
    multilingual_group=ckanext.multilingual.plugin:MultilingualGroup
    multilingual_tag=ckanext.multilingual.plugin:MultilingualTag
    organizations=ckanext.organizations.forms:OrganizationForm
    organizations_dataset=ckanext.organizations.forms:OrganizationDatasetForm
    datastore=ckanext.datastore.plugin:DatastorePlugin
    test_tag_vocab_plugin=ckanext.test_tag_vocab_plugin:MockVocabTagsPlugin
    resource_proxy=ckanext.resourceproxy.plugin:ResourceProxy
    json_preview=ckanext.jsonpreview.plugin:JsonPreview
    pdf_preview=ckanext.pdfpreview.plugin:PdfPreview
    recline_preview=ckanext.reclinepreview.plugin:ReclinePreview
    example_itemplatehelpers=ckanext.example_itemplatehelpers.plugin:ExampleITemplateHelpersPlugin

    [ckan.system_plugins]
    domain_object_mods = ckan.model.modification:DomainObjectModificationExtension

    [babel.extractors]
	    ckan = ckan.lib.extract:extract_ckan
    """,
    # setup.py test command needs a TestSuite so does not work with py.test
    # test_suite = 'nose.collector',
    # tests_require=[ 'py >= 0.8.0-alpha2' ]
)
