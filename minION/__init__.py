###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

__title__ = 'minION'
__description__ = 'MinION evseq caller'
__url__ = 'https://github.com/fhalab/MinION/'
__version__ = '0.1.0'
__author__ = 'Yueming Long, Emreay Gursoy'
__author_email__ = 'ylong@caltech.edu'
__license__ = 'GPL3'

from minION.globals import *
from minION.IO_processor import *
from minION.parser import *
from minION.variantcaller import *
from minION.visualization import *
from minION.interface import *
from minION.cmd import *
from minION.basecaller import *