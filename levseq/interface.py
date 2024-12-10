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
"""
Contain argument parsers used for command line interface and web interface
"""
# Import packages
import os
import tqdm
import yaml
import argparse
# Import local packages
from levseq.run_levseq import run_LevSeq

# Get the working directory
CWD = os.getcwd()


# Build the CLI argparser
def build_cli_parser():
    parser = argparse.ArgumentParser()
    required_args_group = parser.add_argument_group("Required Arguments", "Arguments required for each run")
    required_args_group.add_argument('config',
            help = 'Path to config.yml file containing run parameters.')             
    return parser


# Execute LevSeq
def execute_LevSeq():
    # Build parser
    parser = build_cli_parser()
    args = vars(parser.parse_args())

    with open(args['config'], 'r') as f:
        config = yaml.safe_load(f)

    # Parse the arguments
    # Set up progres bar
    tqdm_fn = tqdm.tqdm

    print(config, type(config))
    # Run LevSeq
    try:
        run_LevSeq(config, tqdm_fn)
    except Exception as e:
        print(e)
    print("Run Complete, add log info")
