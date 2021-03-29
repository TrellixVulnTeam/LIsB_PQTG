import ipaddress

import logging

from spamfilter.EmailEnvelope import EmailEnvelope
from spamfilter.filtering.filters.DBFilter import DBFilter


class SPFFilter(DBFilter):

    def filter(self, envelope: EmailEnvelope) -> bool:
        """
        This filter detected whether the senders IP really belongs to its domain by using the Sender Policy Framework (SPF)

        :param envelope: the email to be filtered
        :return: True, if the sender's IP does not belong to the sender's domain (detected as spam). False, if it does.
        """

        # Get sender domain and check if we have data for it. If we don't then look up the IP ranges and return False.
        # If we do then check the IP.
        domain = envelope.get_sender_domain()
        if domain not in self.data:
            self.data[domain] = envelope.get_all_sender_ip_ranges()
            return False
        else:
            sender_ip = envelope.peer[0]
            for ip_range in self.data[domain]:
                if ipaddress.ip_address(sender_ip) in ipaddress.ip_network(ip_range):
                    return False
            logging.warning(f"[ SPFFilter ] Sender IP '{sender_ip}' does not belong to the sender domain '{domain}'")
            return True
