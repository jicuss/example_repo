__version__ = '5.1.11rc0'

import argparse, os


from analyst_layer import TestEmptyBatch
from etl_logger.logger import EstablishLogger

def run_empty_batches():
    parser = argparse.ArgumentParser(description='Analyst Run Empty Batches Arguments')

    parser.add_argument('-d', '--logFolder', default='/tmp', help='Location of the log folder.  Default is /tmp')
    parser.add_argument('-l', '--logLevel', default='INFO', choices=["DEBUG", "INFO", "ERROR", "CRITICAL"],
                        help='This is the logging level used by the logging module, the default is INFO.')
    parser.add_argument('-f', '--logFile', default='model.log',
                        help='Name of the log file to use.  Default is model.log')
    parser.add_argument('-r', '--runnerPath',
                        default=os.path.join(os.path.dirname(__file__), 'bin', 'sql_runner_new.sh'),
                        help='Absolute path to sql_runner_new.sh')
    parser.add_argument('-t', '--sqllogRoot', default='/data/runtime/logs/scripts/analyst_layer',
                        help='Absolute path of the log folder for sqlrunner')
    parser.add_argument('-s', '--sqlRoot', default=os.path.join(os.path.dirname(__file__), 'sql'),
                        help='Absolute path of the log folder for sqlrunner')
    parser.add_argument('-o', '--outputPath', default=os.path.join(os.path.dirname(__file__), 'results'),
                        help='Absolute path of the output result folder')
    args = parser.parse_args()


    log_file, logger = EstablishLogger(log_folder=args.logFolder,
                                       log_file=args.logFile,
                                       pipeline_name='analyst_layer',
                                       tool_name='etl_model',
                                       normalize_status_messages=False,
                                       normalize_message_spacing=False,
                                       log_level=args.logLevel
                                       )

    it = TestEmptyBatch(args.runnerPath, args.sqllogRoot, args.sqlRoot, args.outputPath)

    if not it.run():
        exit(1)
