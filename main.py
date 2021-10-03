# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
This implementation does its best to follow the Robert Martin's Clean code  guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2021, FCRLab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = ''
__description__ = ''

import argparse

def main():
	description = ('%s\n%s' % (__author__, __description__))
	epilog = ('%s\n%s' % (__credits__, __copyright__))
	parser = argparse.ArgumentParser(
		description = description,
		epilog = epilog
	)
	
	parser.add_argument('-v', '--verbosity',
						dest='verbosity',
						help='Logging verbosity level',
						action="store_true")
						
	options = parser.parse_args()
	verbosity = options.verbosity
	
if __name__ == "__main__":
	main()