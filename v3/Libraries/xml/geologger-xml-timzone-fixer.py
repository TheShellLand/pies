#!/usr/bin/env python
# -*- coding: utf8 -*-

# I went to Japan and the timestamps in the geologging events are all EST
# I need to convert them all to Asia/Tokyo


from xml.etree.ElementTree import iterparse

import xml.etree.ElementTree as ElementTree
import os
import pytz
import datetime
import time
import argparse
import logging

from textwrap import dedent
from pprint import pprint

# TODO: Read file from shell
# TODO: Create a little database of files that have been modified and fixed
# TODO: I'm tempted to create a front end for this lol


# Parse incoming arguments from the shell
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='Geologging file (.gpx)')
parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
parser.add_argument('-d', '--debug', help='Output all debugging logs', action='store_true')
args = parser.parse_args()

# Setup logging
logging.basicConfig(level=logging.DEBUG)

if args.verbose:
    logging.basicConfig(level=logging.INFO)
if args.debug:
    logging.basicConfig(level=logging.DEBUG)

# timezones
utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
japan = pytz.timezone('Asia/Tokyo')

current_time = datetime.datetime.now()
utc_now = datetime.datetime.now(tz=utc)
eastern_now = datetime.datetime.now(tz=eastern)
japan_now = datetime.datetime.now(tz=japan)

logging.debug(dedent(
    '''
    Current time: {}
        UTC time: {}
    Eastern time: {}
      Japan time: {}
    '''.format(
        current_time,
        utc_now,
        eastern_now,
        japan_now
    )
)
)


class GeoLogger:
    """Convert Android PhotoMap Gallery geologging XML timestamps
    to the correct timezone


    App Store: https://play.google.com/store/apps/details?id=eu.bischofs.photomap
    """

    def __init__(self, file):

        self.file = open(file, 'rt')
        self.fileSize = os.path.getsize(file)

        self.ElementTree = self._parse_xml()
        self.root = self.ElementTree.getroot()
        # alias for ElementTree object
        self.xml = self.ElementTree

        # Start parsing
        self._parse_geolog()

    def _event_template(self, eventID, coord, timestamp, elevation):

        event_template = {
            "eventID": eventID,
            "coordinates": coord,
            "timestamp": timestamp,
            "elevation": elevation
        }

        return event_template

    def _read_file(self):

        self.file.seek(0)

        return self.file

    def _close_file(self, file):

        self.file.close()

    def _parse_xml(self):
        return ElementTree.parse(self._read_file())

    def _parse_geolog(self):
        """Parse out tracks

        The tags are weird, it's like `{http://www.topografix.com/GPX/1/1}gpx`.
        I don't know where the `{http://www.topografix.com/GPX/1/1}` part is
        coming from.


        Data structure:
        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <?xml-stylesheet type="text/xsl" href="details.xsl"?>
        <gpx>
            <trk>
                <trkseg>
                    <trkpt>
                        <time></time>
                        <ele></ele>
                    </trkpt>
                    <trkpt>
                        <time></time>
                        <ele></ele>
                    </trkpt>
                </trkseg>
            </trk>
        </gpx>


        Data structure explained:
        <xml>:          XML metadata
        <gpx>:          gpx metadata
        <trk>:          tracks container
        ..<trkseg>:     track segment
        ....<trkpt>:    track point
        ......<time>:   timestamp
        ......<ele>:    elevation


        Example actual file:

        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <?xml-stylesheet type="text/xsl" href="details.xsl"?>
        <gpx
         version="1.1"
         creator="PhotoMap for Android"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns="http://www.topografix.com/GPX/1/1"
         xmlns:topografix="http://www.topografix.com/GPX/Private/TopoGrafix/0/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.topografix.com/GPX/Private/TopoGrafix/0/1 http://www.topografix.com/GPX/Private/TopoGrafix/0/1/topografix.xsd">
            <trk>
                <trkseg>
                    <trkpt lat="35.706629" lon="139.798964"><time>2018-04-27T03:08:56+0000</time><ele>41</ele></trkpt>
                    <trkpt lat="39.077291" lon="-77.141583"><time>2018-04-21T19:55:06+0000</time><ele>88.849731</ele></trkpt>
                </trkseg>
            </trk>
        </gpx>


        :return:
        """

        filter = '{http://www.topografix.com/GPX/1/1}time'
        filter = self.root.iter(filter)

        # TODO: finish getting the timestamp from the XML
        def get_timestamp(timestamp):
            pass

        for time in filter:

            template = dedent(
            """\
            tag: {tag}
            attrib: {attrib}
            text: {text}\
            """)

            template = template.format(
                tag=time.tag,
                attrib=time.attrib,
                text=time.text
            )

            print(template)

            # TODO: need to update the timestamp right here
            # TODO: convert timestamp from Japan to Eastern?
            # if it was set to Eastern, while in Japan, the hours should be Japan time

            # tag: {http://www.topografix.com/GPX/1/1}time
            # attrib: {}
            # text: 2018-04-21T19:22:08+0000





        def get_children(root):

            children = []

            template = {
                'root': root,
                'child': None
            }

            if root.getchildren():
                for child in root.getchildren():
                    template['child'] = child
                    children.append(template)
                    get_children(child)
            else:
                children.append(root)

            return children

        c = get_children(self.root)




        return




    def shift_timezone(self, old_timezone, new_timezone):
        """Shift the timezone to the new timezone

        Optionally: give the old timezone to verify.
        Although, all the timestamps are `2018-04-25T05:01:35+0000`
        so, the timezone data is all `+0000`, which is saying it's UTC,
        but it really isn't. It's the timezone set in the app, default
        timezone is US/Eastern

        :param old_timezone:
        :param new_timezone:
        :return:
        """


        return

    def list_timestamps(self):
        return self.timestamps

    def show_xml_events(self):

        depth = 0
        prefix_width = 8
        prefix_dots = '.' * prefix_width
        line_template = ''.join([
            '{prefix:<0.{prefix_len}}',
            '{event:<8}',
            '{suffix:<{suffix_len}} ',
            '{node.tag:<12} ',
            '\t\t',
            '{node_id}',
        ])

        EVENT_NAMES = ['start', 'end', 'start-ns', 'end-ns']

        for (event, node) in iterparse(self._read_file(), EVENT_NAMES):
            if event == 'end':
                depth -= 1

            prefix_len = depth * 2

            errors = []

            try:
                print(line_template.format(
                    prefix=prefix_dots,
                    prefix_len=prefix_len,
                    suffix='',
                    suffix_len=(prefix_width - prefix_len),
                    node=node,
                    node_id=id(node),
                    event=event,
                ))
            except:
                errors.append('Error on event: ' + event)

            if event == 'start':
                depth += 1

        print('List of errors:')
        [print(error) for error in errors]

    def write_xml(self, output_file=None):
        """Write XML to file

        :param xml: an ElementTree object
        :param output_file: the path to the file to write out to
        :return:
        """

        if not output_file:
            timestamp = int(time.time())
            output_file = r'/tmp/{}.xml'.format(timestamp)

        with open(output_file, 'w') as f:
            self.ElementTree.write(f, encoding="unicode")

        print('XML saved to:', output_file)
        print('  bytes written: {}'.format(os.path.getsize(output_file)))


def main():
    # tree = ET.parse(filename)
    # root = tree.getroot()
    # pprint(root.tag)
    # pprint(root.attrib)
    # pprint(root.findtext('.'))

    new_log = GeoLogger(r'/turtle/_data/home/eric/tmp/dump/Camera/untagged/2018-03-26 Japan/geologging/2018-04-27.gpx')
    # new_log.show_xml_events()
    new_log.write_xml()


if __name__ == "__main__":
    main()
