import datetime
import gzip
import time
import socket
import argparse
import pytz

parser = argparse.ArgumentParser(
    description='Stream a nycTaxi dataset to a socket')
parser.add_argument('hostname', type=str,
                    help='The hostname on which to open the socket')
parser.add_argument('port', type=int,
                    help='The port on which to open the socket')
parser.add_argument('dataset', type=str, choices=['fares', 'rides'],
                    help='The dataset to stream ("fares" or "rides")')
parser.add_argument('-t', '--timezone', type=str, default='UTC',
                    help='The port on which to open the socket')

args = parser.parse_args()

USE_TIMEZONE = pytz.timezone(args.timezone)
CSV_START_TIME = datetime.datetime(2013, 1, 1, tzinfo=pytz.utc)
STREAM_START_TIME = datetime.datetime.now(USE_TIMEZONE)
DATE_OFFSET = STREAM_START_TIME - CSV_START_TIME \
    + STREAM_START_TIME.utcoffset()

TIME_FORMAT = r'%Y-%m-%d %H:%M:%S'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream_socket:
    stream_socket.bind((args.hostname, args.port))
    stream_socket.listen()
    print('Waiting for connection on port %d' % args.port)
    conn, addr = stream_socket.accept()

    with gzip.open('data/nycTaxi%s.gz'
                   % args.dataset.capitalize()) as csv_file:
        line = csv_file.readline().decode('utf-8')

        while line:
            record = line[:-1].split(',')

            if args.dataset == 'fares':
                record_time = datetime.datetime.strptime(record[3],
                                                         TIME_FORMAT)
                stream_time = record_time + DATE_OFFSET

                record[3] = stream_time.strftime(TIME_FORMAT)
            elif args.dataset == 'rides':
                time1 = datetime.datetime.strptime(record[2], TIME_FORMAT)
                time2 = datetime.datetime.strptime(record[3], TIME_FORMAT)

                if time2 == datetime.datetime(1970, 1, 1):
                    stream_time = time1 + DATE_OFFSET
                    record[2] = stream_time.strftime(TIME_FORMAT)
                else:
                    stream_time = time2 + DATE_OFFSET
                    record[3] = stream_time.strftime(TIME_FORMAT)
                    record[2] = (
                        time1 + DATE_OFFSET).strftime(TIME_FORMAT)

            while stream_time > datetime.datetime.now():
                time.sleep(0.01)

            print(','.join(record))
            conn.sendall(bytes((','.join(record) + '\n').encode('utf-8')))

            line = csv_file.readline().decode('utf-8')
