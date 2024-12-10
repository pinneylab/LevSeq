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


def check_config():

    assert config['front_window_size'] > 0 and isinstance(config['front_window_size'], int), 'front_window_size must be an integer greater than 0.'
    assert config['rear_window_size'] > 0 and isinstance(config['rear_window_size'], int), 'rear_window_size must be an integer greater than 0.'

    assert config['min_read_length'] > 0 and isinstance(config['min_read_length'], int), 'min_read_length must be an integer greater than 0.'
    assert config['max_read_length'] > 0 and isinstance(config['max_read_length'], int), 'max_read_length must be an integer greater than 0.'
    assert config['min_read_length'] < config['max_read_length'], 'min_read_length cannot be greater than max_read_length'

    assert config['alignment_score_threshold'] <= 100 and config['alignment_score_threshold'] >= 0, 'alignment_score_threshold must be a number between 0 and 100.'
    assert config['edit_distance_threshold'] > 0 and isinstance(config['edit_distance_threshold'], int), 'edit_distance_threshold must be an integer greater than 0.'

    assert isinstance(config['position_offset'], int), 'position_offset must be an integer.'
    assert config['calling_threshold'] >= 0 and config['calling_threshold'] <= 1, 'calling_threshold must be a number between 0 and 1.'
    assert config['n_threads'] >= 0 and isinstance(config['n_threads'], int), 'n_threads must be an integer greater than or equal to 0.'

    assert isinstance(config['skip_demultiplexing'], bool), 'skip_demultiplexing must be a boolean.'
    assert isinstance(config['skip_variantcalling'], bool), 'skip_variantcalling must be a boolean.'
    assert isinstance(config['show_msa'], bool), 'show_msa must be a boolean.'


# Execute LevSeq
def execute_LevSeq():
    # Build parser
    parser = build_cli_parser()
    args = vars(parser.parse_args())

    with open(args['config'], 'r') as f:
        config = yaml.safe_load(f)
    check_config(config)
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
