import sys
import time


# # Print iterations progress
# def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iteration   - Required  : current iteration (Int)
#         total       - Required  : total iterations (Int)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#     """
#     percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
#     filledLength = int(length * iteration // total)
#     bar = fill * filledLength + '-' * (length - filledLength)
#     print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
#     # Print New Line on Complete
#     if iteration == total:
#         print()
#
#
# #
# # Sample Usage
# #
#
# from time import sleep
#
# # A List of Items
# items = list(range(0, 57))
# l = len(items)
#
# # Initial call to print 0% progress
# printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
# for i, item in enumerate(items):
#     # Do stuff...
#     sleep(0.1)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)
#
#
# # progres characters
# def animation(counter, length):
#     stage = counter % (length * 2 + 2)
#     if stage < length + 1:
#         left_spaces = stage
#     else:
#         left_spaces = length * 2 - 1 - stage
#     return '[' + ' ' * left_spaces + '=' + ' ' * (length - left_spaces) + ']'
#
#
# for i in range(100):
#     sys.stdout.write('\b\b\b')
#     sys.stdout.write(animation(i, 6))
#     sys.stdout.flush()
#     time.sleep(0.2)
#
# import sys
# import time
#
#
# # spinner
# def spinning_cursor():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor
#
#
# spinner = spinning_cursor()
# for _ in range(50):
#     sys.stdout.write(next(spinner))
#     sys.stdout.flush()
#     time.sleep(0.1)
#     sys.stdout.write('\b')
