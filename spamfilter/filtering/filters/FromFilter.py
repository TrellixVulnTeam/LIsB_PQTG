from spamfilter.EmailEnvelope import EmailEnvelope
from spamfilter.filtering.filters.Filter import Filter


class FromFilter(Filter):

    def filter(self, envelope: EmailEnvelope) -> bool:
        """
        This filter checks whether the envelope originator is the same as the email message originator.
        If not, this indicates that the email may be spam.

        :param envelope: The message to be filtered
        :return: False if the originators are the same, True if else (Spam)
        """

        parsed_msg_from = envelope.get_parsed_from()

        if envelope.mail_from != parsed_msg_from:
            print(f"[ FromFilter ] Senders differ: '{envelope.mail_from}' in envelope VS. '{parsed_msg_from}' in message")
            return True

        return False
