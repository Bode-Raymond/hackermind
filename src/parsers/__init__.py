from typing import Dict, Any

from parsers.exploitnotes import Parser as EN_Parser
from parsers.hacktricks import Parser as HT_Parser
from parsers.parser import Parser


parsers: Dict[str, Any] = {'base_parser': Parser(), 'exploit_notes': EN_Parser(), 'hacktricks': HT_Parser()}
