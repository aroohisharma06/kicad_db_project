# core/parser.py

import os
import re
import hashlib

def parse_symbol(file_path):
    """
    Parse a KiCad symbol file (.kicad_sym)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    symbol_name_match = re.search(r'\(symbol\s+"([^"]+)"', content)
    description_match = re.search(r'\(description\s+"([^"]+)"', content)
    pin_count = len(re.findall(r'\(pin ', content))

    symbol_name = symbol_name_match.group(1) if symbol_name_match else ''
    description = description_match.group(1) if description_match else ''
    file_size = os.path.getsize(file_path)
    checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
    library_name = os.path.splitext(os.path.basename(file_path))[0]
    category = 'logic'  # default
    license = 'MIT'

    return {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'file_size': file_size,
        'library_name': library_name,
        'category': category,
        'symbol_name': symbol_name,
        'description': description,
        'pin_count': pin_count,
        'checksum': checksum,
        'license': license
    }


def parse_footprint(file_path):
    """
    Parse a KiCad footprint file (.kicad_mod)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    footprint_name_match = re.search(r'\(module\s+"([^"]+)"', content)
    description_match = re.search(r'\(description\s+"([^"]+)"', content)
    pad_count = len(re.findall(r'\(pad ', content))

    footprint_name = footprint_name_match.group(1) if footprint_name_match else ''
    description = description_match.group(1) if description_match else ''
    file_size = os.path.getsize(file_path)
    checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
    library_name = os.path.splitext(os.path.basename(file_path))[0]
    category = 'footprint'
    license = 'MIT'

    return {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'file_size': file_size,
        'library_name': library_name,
        'category': category,
        'symbol_name': footprint_name,
        'description': description,
        'pin_count': pad_count,
        'checksum': checksum,
        'license': license
    }


def parse_schematic(file_path):
    """
    Parse a KiCad schematic file (.kicad_sch)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract sheet name and description if possible
    sheet_name_match = re.search(r'\(sheet\s+"([^"]+)"', content)
    description_match = re.search(r'\(description\s+"([^"]+)"', content)
    component_count = len(re.findall(r'\(symbol ', content))

    sheet_name = sheet_name_match.group(1) if sheet_name_match else ''
    description = description_match.group(1) if description_match else ''
    file_size = os.path.getsize(file_path)
    checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
    library_name = os.path.splitext(os.path.basename(file_path))[0]
    category = 'schematic'
    license = 'MIT'

    return {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'file_size': file_size,
        'library_name': library_name,
        'category': category,
        'symbol_name': sheet_name,
        'description': description,
        'pin_count': component_count,
        'checksum': checksum,
        'license': license
    }


def parse_pcb(file_path):
    """
    Parse a KiCad PCB file (.kicad_pcb)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pcb_name_match = re.search(r'\(module\s+"([^"]+)"', content)  # modules in PCB
    description_match = re.search(r'\(description\s+"([^"]+)"', content)
    pad_count = len(re.findall(r'\(pad ', content))

    pcb_name = pcb_name_match.group(1) if pcb_name_match else ''
    description = description_match.group(1) if description_match else ''
    file_size = os.path.getsize(file_path)
    checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
    library_name = os.path.splitext(os.path.basename(file_path))[0]
    category = 'pcb'
    license = 'MIT'

    return {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'file_size': file_size,
        'library_name': library_name,
        'category': category,
        'symbol_name': pcb_name,
        'description': description,
        'pin_count': pad_count,
        'checksum': checksum,
        'license': license
    }
