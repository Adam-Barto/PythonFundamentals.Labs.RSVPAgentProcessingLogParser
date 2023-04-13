# The data directory contains a file named rsvp_agent_log.dat. Create a file called log_parser.py.
# The log_parser script should iterate through the file and look for any instances where the log level is WARNING.
# Anytime it encounters a WARNING entry, it should output the following:
# * the date and time of the entry followed by a space, double dashes, and another space
# * the error message. The error message should exclude the colons and everything between them.
#
# Example output:
#
# 03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# WARNINGS:
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# 03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
# ```

import re
file_path = './data/rsvp_agent_log.dat'
file = open(file_path, 'rt')
txt = file.read()
pull = re.findall(r"(\d+\/\d+ )(\d*:\d*:\d+ )(WARNING)(.*:)( .*\n)", txt)

print_out = 'WARNINGS:\n'
for log in pull:
    print_out = print_out + log[0] + log[1] + '--' + log[4]


print(print_out)
file.close()


