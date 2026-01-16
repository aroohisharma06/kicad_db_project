import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Database path
DB_PATH = os.path.join(BASE_DIR, 'db', 'kicad.db')

# Folders for KiCad files
SYMBOLS_FOLDER      = os.path.join(BASE_DIR, 'data', 'symbols')
FOOTPRINTS_FOLDER   = os.path.join(BASE_DIR, 'data', 'footprints')
SCH_FILES_FOLDER    = os.path.join(BASE_DIR, 'data', 'schematics')
PCB_FILES_FOLDER    = os.path.join(BASE_DIR, 'data', 'pcbs')

# Table names
SYMBOLS_TABLE       = 'symbols'
FOOTPRINTS_TABLE    = 'footprints'
SCH_FILES_TABLE     = 'schematics'
PCB_FILES_TABLE     = 'pcbs'
