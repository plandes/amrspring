from pathlib import Path
from zensols.pybuild import SetupUtil

su = SetupUtil(
    setup_path=Path(__file__).parent.absolute(),
    name="zensols.amrspring",
    package_names=['zensols', 'resources'],
    # package_data={'': ['*.html', '*.js', '*.css', '*.map', '*.svg']},
    package_data={'': ['*.conf', '*.json', '*.yml']},
    description='A client and server that generates AMR graphs from natural language sentences.',
    user='plandes',
    project='amrspring',
    keywords=['tooling'],
    # has_entry_points=False,
).setup()
